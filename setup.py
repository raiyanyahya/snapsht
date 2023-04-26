from os.path import abspath, dirname, join
from os import environ
from setuptools import find_packages, setup

this_dir = abspath(dirname(__file__))
with open(join(this_dir, "README.md"), encoding="utf-8") as file:
    long_description = file.read()


setup(
    name="snapsht",
    python_requires=">3.5",
    options={"bdist_wheel": {"universal": "1"}},
    version="1.0.3",
    description="A command line application to capture full-page screenshots with ease, every time.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/raiyanyahya/snapsht",
    author="Raiyan Yahya",
    license="MIT",
    author_email="raiyanyahyadeveloper@gmail.com",
    keywords=[
        "cli",
        "developer tools",
        "productivity",
        "screenshot",
        "python",
        "selenium",
    ],
    packages=find_packages(),
    install_requires=[
        "click==8.1.3",
        "rich==13.3.2",
        "selenium==4.8.3",
        "requests==2.29.0",
    ],
    entry_points={"console_scripts": ["snapsht=snapsht.cli:cli"]},
)
