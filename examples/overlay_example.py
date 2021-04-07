# -*- coding: utf-8 -*-
"""

"""

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

__author__ = "timmyliang"
__email__ = "820472580@qq.com"
__date__ = "2021-04-07 09:36:01"


import os
import sys

MODULE = os.path.abspath(os.path.join(__file__, "..", ".."))
sys.path.insert(0, MODULE) if MODULE not in sys.path else None

from functools import partial

from dayu_widgets.qt import QWidget, QPushButton


class OverlayExample(QWidget):
    def __init__(self, parent=None):
        super(OverlayExample, self).__init__(parent)
        from Qt.QtCompat import load_ui

        self.setWindowTitle("Examples for OverlayWidget")
        DIR, file_name = os.path.split(__file__)
        file_name = os.path.splitext(file_name)[0]
        load_ui(os.path.join(DIR, "%s.ui" % file_name), self)
        for btn in self.findChildren(QPushButton):
            btn.clicked.connect(partial(print, btn.objectName()))


if __name__ == "__main__":
    import sys
    from dayu_widgets import dayu_theme
    from dayu_widgets.qt import QApplication

    app = QApplication(sys.argv)
    test = OverlayExample()
    dayu_theme.apply(test)

    test.show()
    sys.exit(app.exec_())
