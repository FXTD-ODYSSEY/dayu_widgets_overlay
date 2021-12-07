# dayu_widgets_overlay

Python Qt Overlay Widget as a [dayu_widgets](https://github.com/phenom-films/dayu_widgets) plugin

## How it work

![designer](./images/designer.png)

![demo](https://cdn.jsdelivr.net/gh/FXTD-odyssey/FXTD-odyssey.github.io@master/post_img/1ba28015/09.gif)

overlay the widget onto the other widget and resize together
much easy to add and maintain instead of create a New type of widget.

## How to use

```cmd
pip install dayu_widgets_overlay
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
