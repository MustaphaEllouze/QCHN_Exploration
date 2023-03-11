from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QHBoxLayout,
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
    QRect,
    QSize,
)


class ProgressBar(QWidget):

    def __init__(
            self,
            max_value=15,
            rounded_edges=12,
            height=50,
            padding = 5,
            larg_entre_rectangles = 3,
            ecart_texte = 0.17,
            couleur_fond=QColor('black'),
            couleur_rectangle=QColor('red'),
            font='Times',
            *args,
            **kwargs,
    ):
        super(ProgressBar, self).__init__(*args,**kwargs)

        self.rounded_edges = rounded_edges
        self.couleur_fond = couleur_fond
        self._height = height
        self.padding = padding
        self.ler = larg_entre_rectangles
        self.ecart_texte = ecart_texte
        self.max_value = max_value
        self.couleur_rectangle = couleur_rectangle
        self.current_value = self.max_value
        self.setFixedHeight(self._height)
    
    def paintEvent(self,e):
        painter = QPainter(self)
        brush_fond = QBrush()
        brush_fond.setColor(self.couleur_fond)
        brush_fond.setStyle(Qt.SolidPattern)
        painter.setBrush(brush_fond)
        painter.drawRoundedRect(0,
                                0,
                                painter.device().width(),
                                painter.device().height(),
                                self.rounded_edges,
                                self.rounded_edges,
                                )
        
        font = painter.font()
        font.setFamily('Helvetica')
        font.setPointSize(20)
        painter.setFont(font)
        
        # Rectangles
        d_width = painter.device().width()
        long_rect = ((1-self.ecart_texte)*d_width-2*self.padding-(self.max_value-1)*self.ler)/self.max_value
        centres = [self.padding+0.5*long_rect+(k-1)*(long_rect+self.ler) for k in range(1,self.current_value+1)]
        

        for i,c in enumerate(centres) :
            r,g,b,a =self.couleur_rectangle.getRgb()
            r_set = r*(0.2+0.8*(i/(self.max_value-1)))
            g_set = g*(0.2+0.8*(i/(self.max_value-1)))
            b_set = b*(0.2+0.8*(i/(self.max_value-1)))
            brush_rect = QBrush()
            brush_rect.setColor(QColor(r_set,g_set,b_set,a))
            brush_rect.setStyle(Qt.SolidPattern)
            painter.setBrush(brush_rect)
            painter.drawRoundedRect(
                             c-long_rect/2,
                             self.padding,
                             long_rect,
                             painter.device().height()-2*self.padding,
                             self.rounded_edges/2,
                             self.rounded_edges/2,
                             )

        # Texte
        if self.current_value == self.max_value:
            to_print = 'MAX'
        else : 
            to_print = str(self.current_value)
        pen = QPen(self.couleur_rectangle)
        painter.setPen(pen)
        painter.drawText(
                (1-self.ecart_texte)*d_width,
                painter.device().height()/1.4,
                to_print,
            )
        
        painter.end()

    def _trigger_refresh(self):
        self.update()
    
    def consume(self,n):
        self.current_value -= n
        self.current_value = max(self.current_value,0)
        self.update()
    
    def regenerate(self,n):
        self.current_value += n
        self.current_value = min(self.current_value,self.max_value)
        self.update()
    
if __name__ == '__main__':
    import sys
    from PySide6.QtWidgets import QApplication
        
    app = QApplication(sys.argv)
    a = ProgressBar(
        couleur_rectangle=QColor(125,97,255,255),
    )
    a.show()
    app.exec()