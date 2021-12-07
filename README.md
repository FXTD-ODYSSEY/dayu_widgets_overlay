# dayu_widgets_overlay

[![python version](https://img.shields.io/pypi/pyversions/dayu-widgets-overlay)](https://img.shields.io/pypi/pyversions/dayu-widgets-overlay)
[![PyPI version](https://img.shields.io/pypi/v/dayu-widgets-overlay?color=green)](https://badge.fury.io/py/dauy_widgets_overlay)
![Downloads Status](https://img.shields.io/pypi/dw/dayu-widgets-overlay)
![License](https://img.shields.io/pypi/l/dayu-widgets-overlay)
![pypi format](https://img.shields.io/pypi/format/dayu-widgets-overlay)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/loonghao/dauy_widgets_overlay/graphs/commit-activity)


Python Qt Overlay Widget as a [dayu_widgets](https://github.com/phenom-films/dayu_widgets) plugin

## How it work

![designer](https://cdn.jsdelivr.net/gh/FXTD-odyssey/dayu_widgets_overlay@main/images/designer.png)

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
![designer](https://cdn.jsdelivr.net/gh/FXTD-odyssey/dayu_widgets_overlay@main/images/01.png)


## QtDesigner Property

`direction` : `E` `S` `W` `N`

`stretch` (optional - default: Auto) : `NoStretch` `Vertical` `Horizontal` `Center` `Auto`

![designer](https://cdn.jsdelivr.net/gh/FXTD-odyssey/dayu_widgets_overlay@main/images/02.png)

---

See my blog article for more details in chinese

https://blog.l0v0.com/posts/1ba28015.html
