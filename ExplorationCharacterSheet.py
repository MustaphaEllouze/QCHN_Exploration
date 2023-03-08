from PySide6.QtWidgets import (
    QWidget,
    QApplication,
    QVBoxLayout,
    QLabel,
)

from PySide6.QtGui import (
    QPixmap,
)

from ExplorationCharacters import (
    ExplorationCharacter,
)

from PySide6.QtCore import (
    Qt,
)


class ExplorationCharacterSheet(QWidget):

    def __init__(
            self,
            character:ExplorationCharacter,
            image_path:str,
            largeur:int,
            parent=None,
    ):
        super().__init__(parent=parent)
        self.largeur=largeur
        self.character = character
        self._layout = QVBoxLayout()
        self.image = QLabel()
        self.image.setPixmap(QPixmap(image_path).scaled(
            self.largeur, 
            self.largeur, 
            Qt.IgnoreAspectRatio,
            Qt.SmoothTransformation))
        self._layout.addWidget(QLabel(self.character.name))
        self._layout.addWidget(self.image)
        self._layout.addWidget(QLabel(f'Fatigue : {self.character.CUR_FATIGUE}\\{self.character.MAX_FATIGUE}'))
        self._layout.addWidget(QLabel(f'Faim : {self.character.CUR_HUNGER}\\{self.character.MAX_HUNGER}'))
        self._layout.addWidget(QLabel(f'Soif : {self.character.CUR_THIRST}\\{self.character.MAX_THIRST}'))
        self._layout.addWidget(QLabel(f'Froid : {self.character.CUR_FROST}\\{self.character.MAX_FROST}'))
        self._layout.addWidget(QLabel(f'Endurance magique : {self.character.CUR_MAGIC_FATIGUE}\\{self.character.MAX_MAGIC_FATIGUE}'))
        self.setLayout(self._layout)


if __name__ == '__main__':
    import sys
    from Characters_input import (BEDOMAI)
    app = QApplication(sys.argv)
    window = ExplorationCharacterSheet(
                character=BEDOMAI,
                image_path=f'images\\characters\\{BEDOMAI.name}.png',
                largeur=350,
    )
    window.show()
    app.exec()