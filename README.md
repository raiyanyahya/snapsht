[![Actions Status](https://github.com/raiyanyahya/prompt/workflows/Build%20Test/badge.svg)](https://github.com/raiyanyahya/prompt/actions) [![Actions Status](https://github.com/raiyanyahya/prompt/workflows/Package%20Release/badge.svg)](https://github.com/raiyanyahya/prompt/actions) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=raiyanyahya_snapsht&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=raiyanyahya_snapsht) [![Codacy Badge](https://app.codacy.com/project/badge/Grade/069798adf6af4b7e82b6a0a6591a249d)](https://www.codacy.com/gh/raiyanyahya/snapsht/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=raiyanyahya/snapsht&amp;utm_campaign=Badge_Grade) [![](https://img.shields.io/badge/python-3.6+-blue.svg)] [![Linux](https://svgshare.com/i/Zhy.svg)](https://svgshare.com/i/Zhy.svg)[![macOS](https://svgshare.com/i/ZjP.svg)](https://svgshare.com/i/ZjP.svg)
# Snapsht 🦓 - Capture full-page screenshots with ease, every time.

![](https://s2.gifyu.com/images/demo469393e4abff4feb.gif)
`snapsht` is designed to provide users a command-line interface to take full screen scrolling screenshots of webpages.

Snapsht can be helpful for developers and designers who need to take full-page screenshots of websites for testing or design purposes. They can quickly and easily capture screenshots of entire web pages, even those that extend beyond the visible area of the screen.

For developers, `snapsht` can be useful for testing web page layouts and responsiveness across different screen sizes and devices. It can also be helpful for debugging issues that only occur on specific parts of a web page that are not visible on the screen.

`snapsht` can be useful for creating visual mockups or capturing design inspiration from existing websites. It can also be helpful for reviewing and sharing design feedback with clients or team members.

Overall, `snapsht` can save time and effort for developers and designers who need to capture full-page screenshots of websites on a regular basis.

I hope you find it useful.


## Configuration

The application requires you to have the chromium driver available. If you dont have it on the PATH run the `setup` command which will download the correct binary on your system and use it.

## Installation

Install the snapsht python package directly from pypi. 

```console
  pip install snapsht
```
I would recommend using pipx instead of pip to install cli applications on you machine.

## Usage

```console
Usage: snapsht [OPTIONS] COMMAND [ARGS]...

  🦓 Capture full-page screenshots with ease, every time.

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  click       🎴 Take a full page scrolling screenshot and save it to disk.
  setup       ⏬ Download missing chromium driver.
```


Please feel to create issues or request for features. More options and commands will be added to the application in the near future.
