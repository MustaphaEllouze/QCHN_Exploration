from PySide6.QtWidgets import (
    QWidget,
    QApplication,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QLabel,
    QPushButton,
)

from PySide6.QtGui import (
    QPixmap,
    QColor,
    QFont,
)

from functools import partial

from ExplorationCharacters import (
    ExplorationGroup
)

from PySide6.QtCore import (
    Qt,
)

from ProgressBar import (
    ProgressBar,
)
class ExplorationGroupSheet(QWidget):

    def __init__(
            self,
            group:ExplorationGroup,
            police:str='Helvetica',
            taille_police:int=15,
            parent=None,
    ):
        super().__init__(parent=parent)

        self.group = group

        self._font = QFont(police,taille_police)
        self._font_second = QFont(police,int(0.8*taille_police))
        self._font_tert = QFont(police,int(0.6*taille_police))

        self._layout = QVBoxLayout()
        self.setLayout(self._layout)
        
        name_widg = QLabel(self.group.name)
        name_widg.setFont(self._font)
        self._layout.addWidget(name_widg,stretch=1,alignment=Qt.AlignCenter)
        
        self._grid = QGridLayout()
        self._layout.addLayout(self._grid,stretch=20)

        t0 = QLabel('Fatig.')
        t1 = QLabel('Faim')
        t2 = QLabel('Soif')
        t3 = QLabel('Froid')
        t4 = QLabel('End.M.')

        for t in [t0,t1,t2,t3,t4] : t.setFont(self._font_second)

        self._grid.addWidget(t0,0,1,Qt.AlignCenter)
        self._grid.addWidget(t1,0,2,Qt.AlignCenter)
        self._grid.addWidget(t2,0,3,Qt.AlignCenter)
        self._grid.addWidget(t3,0,4,Qt.AlignCenter)
        self._grid.addWidget(t4,0,5,Qt.AlignCenter)

        self._widgets = {}

        for i,character in enumerate(self.group.characters):
            w0 = QLabel(f'{character.name              }'                                )
            w1 = QLabel()
            w2 = QLabel()
            w3 = QLabel()
            w4 = QLabel()
            w5 = QLabel()

            for w in [w0,w1,w2,w3,w4,w5]: w.setFont(self._font_tert)

            self._widgets[character] = [w0,w1,w2,w3,w4,w5]
            
            self._grid.addWidget(w0,i+1,0,Qt.AlignCenter)
            self._grid.addWidget(w1,i+1,1,Qt.AlignCenter)
            self._grid.addWidget(w2,i+1,2,Qt.AlignCenter)
            self._grid.addWidget(w3,i+1,3,Qt.AlignCenter)
            self._grid.addWidget(w4,i+1,4,Qt.AlignCenter)
            self._grid.addWidget(w5,i+1,5,Qt.AlignCenter)
        
        self.update_widgets()
    
    def update_widgets(self):
        for character,list_w in self._widgets.items():
            w1 = list_w[1]
            w2 = list_w[2]
            w3 = list_w[3]
            w4 = list_w[4]
            w5 = list_w[5]

            w1.setText(f'{int(character.CUR_FATIGUE       )} \\ {int(character.MAX_FATIGUE       )}')
            w2.setText(f'{int(character.CUR_HUNGER        )} \\ {int(character.MAX_HUNGER        )}')
            w3.setText(f'{int(character.CUR_THIRST        )} \\ {int(character.MAX_THIRST        )}')
            w4.setText(f'{int(character.CUR_FROST         )} \\ {int(character.MAX_FROST         )}')
            w5.setText(f'{int(character.CUR_MAGIC_FATIGUE )} \\ {int(character.MAX_MAGIC_FATIGUE )}')

            if character.CUR_FATIGUE <= character.MAX_FATIGUE/4                     : w1.setStyleSheet('color:red')
            elif character.CUR_FATIGUE <= character.MAX_FATIGUE/2                   : w1.setStyleSheet('color:yellow')
            else                                                                    : w1.setStyleSheet('')

            if character.CUR_HUNGER <= character.MAX_HUNGER/4                       : w2.setStyleSheet('color:red')
            elif character.CUR_HUNGER <= character.MAX_HUNGER/2                     : w2.setStyleSheet('color:yellow')
            else                                                                    : w2.setStyleSheet('')

            if character.CUR_THIRST <= character.MAX_THIRST/4                       : w3.setStyleSheet('color:red')
            elif character.CUR_THIRST <= character.MAX_THIRST/2                     : w3.setStyleSheet('color:yellow')
            else                                                                    : w3.setStyleSheet('')

            if character.CUR_FROST <= character.MAX_FROST/4                         : w4.setStyleSheet('color:red')
            elif character.CUR_FROST <= character.MAX_FROST/2                       : w4.setStyleSheet('color:yellow')
            else                                                                    : w4.setStyleSheet('')

            if character.CUR_MAGIC_FATIGUE <= character.MAX_MAGIC_FATIGUE/4         : w5.setStyleSheet('color:red')
            elif character.CUR_MAGIC_FATIGUE <= character.MAX_MAGIC_FATIGUE/2       : w4.setStyleSheet('color:yellow')
            else                                                                    : w5.setStyleSheet('')

if __name__ == '__main__':
    import sys
    from Characters_input import (GROUP1)
    app = QApplication(sys.argv)
    window = ExplorationGroupSheet(
        group=GROUP1,
        taille_police=20,
    )
    window.show()
    app.exec()