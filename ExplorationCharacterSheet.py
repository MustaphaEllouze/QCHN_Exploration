from PySide6.QtWidgets import (
    QWidget,
    QApplication,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
)

from PySide6.QtGui import (
    QPixmap,
    QColor,
)

from functools import partial

from ExplorationCharacters import (
    ExplorationCharacter,
)

from PySide6.QtCore import (
    Qt,
)

from ProgressBar import (
    ProgressBar,
)

class ProgressBarExtended(QWidget):

    def __init__(
            self,
            progress_bar:ProgressBar,
            name_cara:str,
            name_affich:str,
            character:ExplorationCharacter,
            *args,
            **kwargs,
    ):  
        super().__init__(*args,**kwargs)

        self.progress_bar = progress_bar

        self.character = character

        self._layout = QVBoxLayout()
        self.setLayout(self._layout)
        self._layout.setContentsMargins(0,0,0,0)
        self._layout.setSpacing(0)

        self._layout_name_and_freeze = QHBoxLayout()
        self._layout.addLayout(self._layout_name_and_freeze,1)
        self._layout_name_and_freeze.addWidget(QLabel(name_affich))

        self.freeze_but = QPushButton('Freeze')
        self.unfreeze_but = QPushButton('Unfreeze')
        self._layout_name_and_freeze.addWidget(self.freeze_but)
        self._layout_name_and_freeze.addWidget(self.unfreeze_but)

        self._layout_no_label = QHBoxLayout()
        self._layout_no_label.setContentsMargins(0,0,0,0)
        self._layout_no_label.setSpacing(0)
        self._layout_no_label_virtual = QWidget() 
        self._layout_no_label_virtual.setLayout(self._layout_no_label)

        self._layout.addWidget(self._layout_no_label_virtual,5)
                
        self._layout_no_label.addWidget(progress_bar,5000)

        self._layout_first_buttons = QVBoxLayout()
        self.widget_first_buttons = QWidget()
        self.widget_first_buttons.setLayout(self._layout_first_buttons)
        self._layout_no_label.addWidget(self.widget_first_buttons,1)

        self.add_car = QPushButton('+1')
        self.sub_car = QPushButton('-1')
        self._layout_first_buttons.addWidget(self.add_car)
        self._layout_first_buttons.addWidget(self.sub_car)

        self._layout_second_buttons = QVBoxLayout()
        self.widget_second_buttons = QWidget()
        self.widget_second_buttons.setLayout(self._layout_second_buttons)
        self._layout_no_label.addWidget(self.widget_second_buttons,1)

        self.add_shield = QPushButton('+1 B.')
        self.sub_shield = QPushButton('-1 B.')
        self._layout_second_buttons.addWidget(self.add_shield)
        self._layout_second_buttons.addWidget(self.sub_shield)

        self.freeze_but.clicked.connect(lambda x : self.freeze_but.setDisabled(True))
        self.freeze_but.clicked.connect(lambda x : self.unfreeze_but.setEnabled(True))
        self.unfreeze_but.clicked.connect(lambda x : self.unfreeze_but.setDisabled(True))
        self.unfreeze_but.clicked.connect(lambda x : self.freeze_but.setEnabled(True))

        self.freeze_but.clicked.connect(partial(character.set_freeze_state_carac,name_cara,True))
        self.unfreeze_but.clicked.connect(partial(character.set_freeze_state_carac,name_cara,False))

        
        self.add_car.clicked.connect(lambda x : self.character.change_carac(1,name_cara))
        self.add_car.clicked.connect(lambda x : self.progress_bar.set_current_value(character.get_value_of_cara(name_cara)))
        self.sub_car.clicked.connect(lambda x : self.character.change_carac(-1,name_cara))
        self.sub_car.clicked.connect(lambda x : self.progress_bar.set_current_value(character.get_value_of_cara(name_cara)))
        self.add_shield.clicked.connect(lambda x : self.character.change_shield(1,name_cara))
        self.add_shield.clicked.connect(lambda x : self.progress_bar.set_shield_value(character.get_value_of_shield(name_cara)))
        self.sub_shield.clicked.connect(lambda x : self.character.change_shield(-1,name_cara))
        self.sub_shield.clicked.connect(lambda x : self.progress_bar.set_shield_value(character.get_value_of_shield(name_cara)))
        self.freeze_but.clicked.connect(partial(self.character.set_freeze_state_carac,name_cara,True))
        self.unfreeze_but.clicked.connect(partial(self.character.set_freeze_state_carac,name_cara,False))

        self.add_car.setFixedWidth(50)
        self.sub_car.setFixedWidth(50)
        self.add_shield.setFixedWidth(50)
        self.sub_shield.setFixedWidth(50)
                


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
        self.image.setAlignment(Qt.AlignCenter)
        self.image.setFixedHeight(self.largeur-40)
        self._layout_name_and_freeze = QHBoxLayout()
        self._layout.addLayout(self._layout_name_and_freeze)
        self._layout_name_and_freeze.addWidget(QLabel(self.character.name))
        
        self.freeze_but = QPushButton('Freeze')
        self.freeze_but.clicked.connect(partial(character.set_freeze_state,True))
        self.unfreeze_but = QPushButton('Unfreeze')
        self.unfreeze_but.clicked.connect(partial(character.set_freeze_state,False))
        
        self.freeze_but.clicked.connect(lambda x : self.freeze_but.setDisabled(True))
        self.freeze_but.clicked.connect(lambda x : self.unfreeze_but.setEnabled(True))
        self.unfreeze_but.clicked.connect(lambda x : self.unfreeze_but.setDisabled(True))
        self.unfreeze_but.clicked.connect(lambda x : self.freeze_but.setEnabled(True))

        self._layout_name_and_freeze.addWidget(self.freeze_but)
        self._layout_name_and_freeze.addWidget(self.unfreeze_but)

        self._layout.addWidget(self.image)

        self.w_fatigue = ProgressBar(
            max_value=self.character.MAX_FATIGUE,
            couleur_fond=couleur_fond,
            couleur_rectangle=QColor(255,127,0,255),
            shield_value=self.character.SHIELD_FATIGUE,
        )
        self.w_hunger = ProgressBar(
            max_value=self.character.MAX_HUNGER,
            couleur_fond=couleur_fond,
            couleur_rectangle=QColor(255,0,0,255),
            shield_value=self.character.SHIELD_HUNGER,
        )
        self.w_thirst = ProgressBar(
            max_value=self.character.MAX_THIRST,
            couleur_fond=couleur_fond,
            couleur_rectangle=QColor(100,100,255,255),
            shield_value=self.character.SHIELD_THIRST,
        )
        self.w_frost = ProgressBar(
            max_value=self.character.MAX_FROST,
            couleur_fond=couleur_fond,
            couleur_rectangle=QColor(200,200,255,255),
            shield_value=self.character.SHIELD_FROST,
        )
        self.w_magic = ProgressBar(
            max_value=self.character.MAX_MAGIC_FATIGUE,
            couleur_fond=couleur_fond,
            couleur_rectangle=QColor(127,175,55,255),
            shield_value=self.character.SHIELD_MAGIC_FATIGUE,
        )

        self.fatigue_widget = ProgressBarExtended(
            progress_bar = self.w_fatigue,
            name_cara='FATIGUE',
            name_affich='Fatigue',
            character=self.character,
        )
        self._layout.addWidget(self.fatigue_widget)

        self.hunger_widget = ProgressBarExtended(
            progress_bar = self.w_hunger,
            name_cara='HUNGER',
            name_affich='Faim',
            character=self.character,
        )
        self._layout.addWidget(self.hunger_widget)

        self.thirst_widget = ProgressBarExtended(
            progress_bar = self.w_thirst,
            name_cara='THIRST',
            name_affich='Soif',
            character=self.character,
        )
        self._layout.addWidget(self.thirst_widget)

        self.frost_widget = ProgressBarExtended(
            progress_bar = self.w_frost,
            name_cara='FROST',
            name_affich='Froid',
            character=self.character,
        )
        self._layout.addWidget(self.frost_widget)

        self.magic_widget = ProgressBarExtended(
            progress_bar = self.w_magic,
            name_cara='MAGIC',
            name_affich='Endurance magique',
            character=self.character,
        )
        self._layout.addWidget(self.magic_widget)

        self.unfreeze_but.setDisabled(True)
        self.fatigue_widget.unfreeze_but.setDisabled(True)
        self.hunger_widget.unfreeze_but.setDisabled(True)
        self.thirst_widget.unfreeze_but.setDisabled(True)
        self.frost_widget.unfreeze_but.setDisabled(True)
        self.magic_widget.unfreeze_but.setDisabled(True)

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