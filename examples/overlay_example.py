# -*- coding: utf-8 -*-
"""

"""

# Import future modules
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


__author__ = "timmyliang"
__email__ = "820472580@qq.com"
__date__ = "2021-04-07 09:36:01"


# Import built-in modules
import os
import signal
import sys


signal.signal(signal.SIGINT, signal.SIG_DFL)

MODULE = os.path.abspath(os.path.join(__file__, "..", ".."))
sys.path.insert(0, MODULE) if MODULE not in sys.path else None

# Import built-in modules
from functools import partial

# Import third-party modules
from Qt import QtWidgets
from Qt.QtCompat import load_ui


class OverlayExample(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(OverlayExample, self).__init__(parent)

        self.setWindowTitle("Examples for OverlayWidget")
        DIR, file_name = os.path.split(__file__)
        file_name = "%s.ui" % os.path.splitext(file_name)[0]
        load_ui(os.path.join(DIR, file_name), self)
        for btn in self.findChildren(QtWidgets.QPushButton):
            btn.clicked.connect(partial(print, btn.objectName()))


if __name__ == "__main__":
    # Import built-in modules
    import sys

    # Import third-party modules
    from dayu_widgets import dayu_theme

    app = QtWidgets.QApplication(sys.argv)
    test = OverlayExample()
    dayu_theme.apply(test)

    test.show()
    sys.exit(app.exec_())
