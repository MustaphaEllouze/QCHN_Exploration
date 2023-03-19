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
        t1 = QLabel('Faim  ')
        t2 = QLabel('Soif  ')
        t3 = QLabel('Froid ')
        t4 = QLabel('End.M.')

        for t in [t0,t1,t2,t3,t4] : t.setFont(self._font_second)

        self._grid.addWidget(t0,0,1)
        self._grid.addWidget(t1,0,2)
        self._grid.addWidget(t2,0,3)
        self._grid.addWidget(t3,0,4)
        self._grid.addWidget(t4,0,5)

        for i,character in enumerate(self.group.characters):
            w0 = QLabel(f'{character.name              }'                                )
            w1 = QLabel(f'{character.CUR_FATIGUE       } \\ {character.MAX_FATIGUE       }')
            w2 = QLabel(f'{character.CUR_HUNGER        } \\ {character.MAX_HUNGER        }')
            w3 = QLabel(f'{character.CUR_THIRST        } \\ {character.MAX_THIRST        }')
            w4 = QLabel(f'{character.CUR_FROST         } \\ {character.MAX_FROST         }')
            w5 = QLabel(f'{character.CUR_MAGIC_FATIGUE } \\ {character.MAX_MAGIC_FATIGUE }')

            for w in [w0,w1,w2,w3,w4,w5]: w.setFont(self._font_tert)
            
            self._grid.addWidget(w0,i+1,0,Qt.AlignCenter)
            self._grid.addWidget(w1,i+1,1,Qt.AlignCenter)
            self._grid.addWidget(w2,i+1,2,Qt.AlignCenter)
            self._grid.addWidget(w3,i+1,3,Qt.AlignCenter)
            self._grid.addWidget(w4,i+1,4,Qt.AlignCenter)
            self._grid.addWidget(w5,i+1,5,Qt.AlignCenter)
        
        


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