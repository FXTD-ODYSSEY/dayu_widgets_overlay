# dayu_widgets_overlay

[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/FXTD-ODYSSEY/dauy_widgets_overlay/master.svg)](https://results.pre-commit.ci/latest/github/FXTD-ODYSSEY/dauy_widgets_overlay/master)
[![python version](https://img.shields.io/pypi/pyversions/dauy_widgets_overlay)](https://img.shields.io/pypi/pyversions/dauy_widgets_overlay)
[![PyPI version](https://img.shields.io/pypi/v/dauy_widgets_overlay?color=green)](https://badge.fury.io/py/dauy_widgets_overlay)
[![Documentation Status](https://readthedocs.org/projects/dauy_widgets_overlay/badge/?version=master)](https://dauy_widgets_overlay.readthedocs.io/en/master/?badge=master)
![Downloads Status](https://img.shields.io/pypi/dw/dauy_widgets_overlay)
![License](https://img.shields.io/pypi/l/dauy_widgets_overlay)
![pypi format](https://img.shields.io/pypi/format/dauy_widgets_overlay)
[![Downloads](https://pepy.tech/badge/dauy_widgets_overlay)](https://pepy.tech/badge/dauy_widgets_overlay)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/loonghao/dauy_widgets_overlay/graphs/commit-activity)


Python Qt Overlay Widget as a [dayu_widgets](https://github.com/phenom-films/dayu_widgets) plugin

## How it work

![designer](./images/designer.png)

![demo](https://cdn.jsdelivr.net/gh/FXTD-odyssey/FXTD-odyssey.github.io@master/post_img/1ba28015/09.gif)

overlay the widget onto the other widget and resize together
much easy to add and maintain instead of create a New type of widget.

## How to use

```cmd
pip install dayu-widgets-overlay
```

```Python
from dayu_widgets_overlay import MOverlay
```

In Qt Designer, you can extend a QWidget into MOverlay
![designer](./images/01.png)


## QtDesigner Property

`direction` : `E` `S` `W` `N`

`stretch` (optional - default: Auto) : `NoStretch` `Vertical` `Horizontal` `Center` `Auto`

![designer](./images/02.png)

---

See my blog article for more details in chinese

https://blog.l0v0.com/posts/1ba28015.html
