# Snapsht 🦓 - Capture full-page screenshots with ease, every time.


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