from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton, QGroupBox, QPushButton, QButtonGroup, QListWidget, QTextEdit, QLineEdit, QInputDialog)
import json

'''notes = {
    'Добро пожаловать':
    {
        'текст' : 'Это самое лучшее приложение для заметок в мире!',
        'теги' : ['умные заметки', 'инструкция']
    }
}

with open('notes.json', 'w', encoding='utf-8') as file:
    json.dump(notes, file)'''

def show_notes():
    name_note = widget1.selectedItems()[0].text()
    field_text.setText(notes[name_note]['текст'])
    widget2.clear()
    widget2.addItems(notes[name_note]['теги'])

def add_note():
    name_note, ok = QInputDialog.getText(main_win, 'Добавить заметку', 'Название заметки')
    notes[name_note] = {'текст' : '', 'теги' : []}
    widget1.addItem(name_note)

def del_note():
    if widget1.selectedItems():
        name_note = widget1.selectedItems()[0].text()
        del notes[name_note]
        with open('notes.json', 'w', encoding='utf-8') as file:
            json.dump(notes, file)
        widget1.clear()
        widget2.clear()
        field_text.clear()
        widget1.addItems(notes)
    print(notes)

def save_note():
    if widget1.selectedItems():
        name_note = widget1.selectedItems()[0].text()
        saved = field_text.toPlainText()
        notes[name_note]['текст'] = saved
        with open('notes.json', 'w', encoding='utf-8') as file:
            json.dump(notes, file)
    print(notes)

def add_tag():
    if widget1.selectedItems():
        name_note = widget1.selectedItems()[0].text()
        saved = field_tag.text()
        if not saved in notes[name_note]['теги']:
            notes[name_note]['теги'].append(saved)
            widget2.addItem(saved)
            field_tag.clear()
            with open('notes.json', 'w', encoding='utf-8') as file:
                json.dump(notes, file)
    print(notes)



def del_tag():
    if widget1.selectedItems():
        name_note = widget1.selectedItems()[0].text()
        if widget2.selectedItems():
            saved = widget2.selectedItems()[0].text()
            notes[name_note]['теги'].remove(saved)
            with open('notes.json', 'w', encoding='utf-8') as file:
                json.dump(notes, file)
            widget2.clear()
            widget2.addItems(notes[name_note]['теги'])
    print(notes)

def search_tag():
    tag = field_tag.text()
    if button6.text() == 'Искать заметки по тегу' and tag:
        notes_filter = {}
        for note in notes:
            if tag in notes[note]['теги']:
                notes_filter[note] = notes[note]
        button6.setText('Сбросить поиск')
        widget1.clear()
        widget2.clear()
        widget1.addItems(notes_filter)
    elif button6.text() == 'Сбросить поиск':
        field_tag.clear()
        widget1.clear()
        widget2.clear()
        widget1.addItems(notes)
        button6.setText('Искать заметки по тегу')



app = QApplication([])
main_win = QWidget()

field_text = QTextEdit()
field_tag = QLineEdit()
widget1 = QListWidget()
widget2 = QListWidget()
inscription1 = QLabel('Список заметок')
inscription2 = QLabel('Список тегов')
button1 = QPushButton('Создать заметку')
button2 = QPushButton('Удалить заметку')
button3 = QPushButton('Сохранить заметку')
button4 = QPushButton('Добавить к заметке')
button5 = QPushButton('Открепить от заметки')
button6 = QPushButton('Искать заметки по тегу')

layout1 = QHBoxLayout()
layout2 = QVBoxLayout()
layout3 = QVBoxLayout()
countur1 = QHBoxLayout()
countur2 = QHBoxLayout()
countur3 = QHBoxLayout()
countur4 = QHBoxLayout()
countur5 = QHBoxLayout()
countur6 = QHBoxLayout()
countur7 = QHBoxLayout()
countur8 = QHBoxLayout()
countur9 = QHBoxLayout()

layout2.addWidget(field_text)
countur1.addWidget(inscription1)
countur2.addWidget(widget1)
countur3.addWidget(button1)
countur3.addWidget(button2)
countur4.addWidget(button3)
countur5.addWidget(inscription2)
countur6.addWidget(widget2)
countur7.addWidget(field_tag)
countur8.addWidget(button4)
countur8.addWidget(button5)
countur9.addWidget(button6)


layout3.addLayout(countur1)
layout3.addLayout(countur2)
layout3.addLayout(countur3)
layout3.addLayout(countur4)
layout3.addLayout(countur5)
layout3.addLayout(countur6)
layout3.addLayout(countur7)
layout3.addLayout(countur8)
layout3.addLayout(countur9)


layout1.addLayout(layout2)
layout1.addLayout(layout3)


with open('notes.json', 'r', encoding='utf-8') as file:
    notes = json.load(file)
widget1.addItems(notes)

main_win.setLayout(layout1)

widget1.itemClicked.connect(show_notes)
button1.clicked.connect(add_note)
button2.clicked.connect(del_note)
button3.clicked.connect(save_note)
button4.clicked.connect(add_tag)
button5.clicked.connect(del_tag)
button6.clicked.connect(search_tag)

main_win.show()
app.exec_()













































#начни тут создавать приложение с умными заметками