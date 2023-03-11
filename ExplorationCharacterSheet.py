from PySide6.QtWidgets import (
    QWidget,
    QApplication,
    QVBoxLayout,
    QLabel,
)

from PySide6.QtGui import (
    QPixmap,
    QColor,
)

from ExplorationCharacters import (
    ExplorationCharacter,
)

from PySide6.QtCore import (
    Qt,
)

from ProgressBar import (
    ProgressBar,
)


class ExplorationCharacterSheet(QWidget):

    def __init__(
            self,
            character:ExplorationCharacter,
            image_path:str,
            largeur:int,
            couleur_fond=QColor(0,0,0,0),
            parent=None,
    ):
        super().__init__(parent=parent)
        self.largeur=largeur
        self.character = character
        self._layout = QVBoxLayout()
        self.image = QLabel()
        self.image.setPixmap(QPixmap(image_path).scaled(
            self.largeur-40, 
            self.largeur-40, 
            Qt.IgnoreAspectRatio,
            Qt.SmoothTransformation))
        self.image.setFixedHeight(self.largeur-40)
        self._layout.addWidget(QLabel(self.character.name))
        self._layout.addWidget(self.image)

        self.w_fatigue = ProgressBar(
            max_value=self.character.MAX_FATIGUE,
            couleur_fond=couleur_fond,
            couleur_rectangle=QColor(255,127,0,255)
        )
        self.w_hunger = ProgressBar(
            max_value=self.character.MAX_HUNGER,
            couleur_fond=couleur_fond,
            couleur_rectangle=QColor(255,0,0,255)
        )
        self.w_thirst = ProgressBar(
            max_value=self.character.MAX_THIRST,
            couleur_fond=couleur_fond,
            couleur_rectangle=QColor(100,100,255,255)
        )
        self.w_frost = ProgressBar(
            max_value=self.character.MAX_FROST,
            couleur_fond=couleur_fond,
            couleur_rectangle=QColor(200,200,255,255)
        )
        self.w_magic = ProgressBar(
            max_value=self.character.MAX_MAGIC_FATIGUE,
            couleur_fond=couleur_fond,
            couleur_rectangle=QColor(127,175,55,255)
        )

        self._layout.addWidget(QLabel('Fatigue'))
        self._layout.addWidget(self.w_fatigue)
        self._layout.addWidget(QLabel('Faim'))
        self._layout.addWidget(self.w_hunger)
        self._layout.addWidget(QLabel('Soif'))
        self._layout.addWidget(self.w_thirst)
        self._layout.addWidget(QLabel('Froid'))
        self._layout.addWidget(self.w_frost)
        self._layout.addWidget(QLabel('Endurance magique'))
        self._layout.addWidget(self.w_magic)
        self.setLayout(self._layout)


if __name__ == '__main__':
    import sys
    from Characters_input import (BLURP)
    app = QApplication(sys.argv)
    window = ExplorationCharacterSheet(
                character=BLURP,
                image_path=f'images\\characters\\{BLURP.name}.png',
                largeur=350,
    )
    window.show()
    app.exec()