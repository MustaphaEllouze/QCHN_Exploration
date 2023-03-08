from PySide6.QtWidgets import (
    QWidget,
    QLabel,
)

from PySide6.QtGui import (
    QColor,
    QPainter,
    QPen,
    QBrush,
    QPixmap,
)

from PySide6.QtCore import (
    Qt,
)

class ProgressBar(QWidget):

    def __init__(self,parent=None,
                 height=100,
                 length=400,):
        super().__init__(parent)
    
        self.fond = QLabel(parent=self)
        self.canevas = QPixmap(length,height)
        self.canevas.fill(QColor('white'))
        self.painter = QPainter(self.canevas)
        self.pen = QPen(QColor('white'))
        self.pen.setWidth(2)
        self.brush = QBrush(Qt.SolidPattern)
        self.painter.setPen(self.pen)
        self.painter.setBrush(self.brush)
        self.painter.drawRoundedRect(0,0,50,50,10,10)
        self.painter.end()
        self.fond.setPixmap(self.canevas)

if __name__ == '__main__':
    import sys
    from PySide6.QtWidgets import QApplication
        
    app = QApplication(sys.argv)
    a = ProgressBar()
    a.show()
    app.exec()