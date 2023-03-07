import click
import os
import platform
import stat
import time
import requests
import zipfile
from io import BytesIO
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from rich.progress import Console
import pkg_resources
import sys

console = Console()
CHROME_DRIVER_URL = "https://chromedriver.chromium.org/downloads"
LATEST_CHROME_DRIVER_VERSION = (
    "https://chromedriver.storage.googleapis.com/LATEST_RELEASE"
)


@click.group()
@click.version_option(version="1.0.2")
def cli():
    """🦓 Capture full-page screenshots with ease, every time."""


@cli.command("click")
@click.argument("url", type=str)
@click.option("--output", "-o", default="screenshot.png", help="Output file name")
def take_screenshot(url, output):
    """🎴 Take a full page scrolling screenshot and save it to disk."""
    # determine the path to the chromedriver binary included in the package
    chromedriver_path = pkg_resources.resource_filename(__name__, "chromedriver")
    if not os.path.isfile(chromedriver_path):
        print("❎ chromedriver not found in package.")
        print('Use the "setup" command to download and install chromedriver.')
        sys.exit(1)
    # set up Selenium webdriver
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--headless")
    options.add_argument("--start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument("--remote-debugging-port=9222")
    with console.status("Taking a snapshot...", spinner="runner"):
        try:
            # chromedriver_path = "./" + chromedriver_path
            service = webdriver.chrome.service.Service(chromedriver_path)
            service.start()
            driver = webdriver.Remote(service.service_url, options=options)
            driver.get(url)
            time.sleep(1)
            driver.execute_script("window.scrollTo(0, 0);")
        except WebDriverException:
            print("❌ Try again with a proper formatted url.")
            driver.stop_client()
            sys.exit(1)
        except Exception:
            print("❌ Failed to get a screenshot of the webpage.")
            driver.stop_client()
            sys.exit(1)
        original_size = driver.get_window_size()
        required_width = driver.execute_script(
            "return document.body.parentNode.scrollWidth"
        )
        required_height = driver.execute_script(
            "return document.body.parentNode.scrollHeight"
        )
        driver.set_window_size(required_width, required_height)

        screenshots = []
        last_height = driver.execute_script("return document.body.scrollHeight")
        
        while True:
            try:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.TAG_NAME, "body"))
                )
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.TAG_NAME, "body"))
                )
                screenshot = driver.get_screenshot_as_png()
                screenshots.append(screenshot)
            except WebDriverException:
                print("❌ Failed to get a screenshot of the webpage.")
                break
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    driver.set_window_size(original_size["width"], original_size["height"])

    screenshot_filename = output
    if len(screenshots) != 0:
        with open(screenshot_filename, "wb") as f:
            f.write(screenshots[0])
    driver.stop_client()


@cli.command("setup")
def setup():
    """⏬ Download missing chromium driver."""
    # determine the path to the chromedriver binary included in the package
    chromedriver_path = pkg_resources.resource_filename(__name__, "chromedriver")
    version_url = LATEST_CHROME_DRIVER_VERSION
    response = requests.get(version_url, timeout=300)
    if response.status_code != 200:
        print(
            "🧟‍ failed to get latest version of chromedriver ({response.status_code})."
        )
        sys.exit(1)
    version = response.text.strip()
    system = platform.system()
    if system == "Windows":
        chromedriver_url = f"https://chromedriver.storage.googleapis.com/{version}/chromedriver_win32.zip"
    elif system == "Darwin":
        chromedriver_url = f"https://chromedriver.storage.googleapis.com/{version}/chromedriver_mac64.zip"
    elif system == "Linux":
        chromedriver_url = f"https://chromedriver.storage.googleapis.com/{version}/chromedriver_linux64.zip"
    else:
        print("🧟‍: unsupported system ({system}).")
        sys.exit(1)
    response = requests.get(chromedriver_url, timeout=300)
    if response.status_code != 200:
        print("🧟‍: failed to download chromedriver ({response.status_code}).")
        sys.exit(1)
    zipfile_data = BytesIO(response.content)
    with zipfile.ZipFile(zipfile_data, "r") as zip_ref:
        zip_ref.extractall(os.path.dirname(chromedriver_path))
    print("🎉 chromedriver downloaded and installed.")
    st = os.stat(chromedriver_path)
    os.chmod(chromedriver_path, st.st_mode | stat.S_IEXEC)
    sys.exit(0)
