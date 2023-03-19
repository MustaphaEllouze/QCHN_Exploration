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
    """Widget pour afficher une barre de progression
    """

    def __init__(
            self,
            max_value=15,
            rounded_edges=12,
            height=30,
            padding = 5,
            larg_entre_rectangles = 3,
            ecart_texte = 0.17,
            couleur_fond=QColor('black'),
            couleur_rectangle=QColor('red'),
            nom_font='Helvetica',
            shield_value=0,
            *args,
            **kwargs,
    ):
        """
        Args:
            max_value (int, optional): _description_. Defaults to 15.
            rounded_edges (int, optional): _description_. Defaults to 12.
            height (int, optional): _description_. Defaults to 50.
            padding (int, optional): _description_. Defaults to 5.
            larg_entre_rectangles (int, optional): _description_. Defaults to 3.
            ecart_texte (float, optional): _description_. Defaults to 0.17.
            couleur_fond (_type_, optional): _description_. Defaults to QColor('black').
            couleur_rectangle (_type_, optional): _description_. Defaults to QColor('red').
            nom_font (str, optional): _description_. Defaults to 'Helvetica'.
            shield_value (int, optional): _description_. Defaults to 0.
        """

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
        self.nom_font=nom_font
        self.shield_value=shield_value
        self.setMinimumHeight(self._height)
    
    def paintEvent(self,e):
        painter = QPainter(self)

        pen_fond = QPen()
        pen_fond.setColor(self.couleur_fond)
        brush_fond = QBrush()
        brush_fond.setColor(self.couleur_fond)
        brush_fond.setStyle(Qt.SolidPattern)
        painter.setPen(pen_fond)
        painter.setBrush(brush_fond)
        painter.drawRoundedRect(0,
                                0,
                                painter.device().width(),
                                painter.device().height(),
                                self.rounded_edges,
                                self.rounded_edges,
                                )
        
        font = painter.font()
        font.setFamily(self.nom_font)
        font.setPointSize(17)
        painter.setFont(font)
        
        # Rectangles
        d_width = painter.device().width()
        long_rect = ((1-self.ecart_texte)*d_width-2*self.padding-(self.max_value-1)*self.ler)/self.max_value
        centres = [self.padding+0.5*long_rect+(k-1)*(long_rect+self.ler) for k in range(1,int(self.max_value+1))]
        

        for i,c in enumerate(centres) :
            if i<self.current_value:
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
                r_set_s = min(255,r*(0.5+0.5*(i/(self.max_value-1)))+20)
                g_set_s = min(255,g*(0.5+0.5*(i/(self.max_value-1)))+20)
                b_set_s = min(255,b*(0.5+0.5*(i/(self.max_value-1)))+20)
                pen_shield = QPen()
                pen_shield.setColor(QColor(r_set_s,g_set_s,b_set_s,a))
                painter.setPen(pen_shield)
                painter.drawRoundedRect(
                                c-long_rect/2,
                                self.padding,
                                long_rect,
                                painter.device().height()-2*self.padding,
                                self.rounded_edges/2,
                                self.rounded_edges/2,
                                )
            if i<self.shield_value:
                painter.setBrush(QBrush(QColor(255,255,255,130),Qt.Dense6Pattern))
                painter.drawRoundedRect(
                                c-long_rect/2,
                                self.padding,
                                long_rect,
                                painter.device().height()-2*self.padding,
                                self.rounded_edges/2,
                                self.rounded_edges/2,
                                )
                
                painter.setBrush(QBrush(QColor(255,255,255,130),Qt.Dense7Pattern))
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
            to_print = f'{int(self.current_value)}/{self.max_value}'
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
    
    def set_current_value(self,n):
        assert 0<=n<=self.max_value
        self.current_value = n
        self.update()
    
    def set_shield_value(self,n):
        assert 0<=n<=self.max_value
        self.shield_value = n
        self.update()
    
if __name__ == '__main__':
    import sys
    from PySide6.QtWidgets import QApplication
        
    app = QApplication(sys.argv)
    a = ProgressBar(
        couleur_rectangle=QColor(125,97,255,255),
    )
    a.set_shield_value(1)
    a.show()
    app.exec()