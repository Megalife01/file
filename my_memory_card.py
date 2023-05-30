#подключение библиотек
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QMessageBox, QGroupBox, QButtonGroup
from random import shuffle, randint
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_asked = []
question_list = []
question_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Русский','Англиский', 'Испанский'))
question_list.append(Question('Какого цвета нет на флаге России', 'Зелёный', 'Синий', 'Красный', 'Белый'))
question_list.append(Question('Как называется национальная хижина якутов', 'Ураса', 'Юрта', 'Иглу', 'Хата')) 
question_list.append(Question('Как звали собаку первую полетевшую в космос', 'Лайка', 'Белка', 'Стрелка', 'Пушок'))
question_list.append(Question('В каком году произошла комунистическая революция', '1917', '1898', '1941', '1923')) 
#создание приложения и главного окна
app = QApplication([])
main_win = QWidget()
#создание виджетов главного окна
main_win.setWindowTitle('Memory Card') 
lb_Question = QLabel('Самый сложный вопрос в мире')
btn_OK = QPushButton('Ответить')
RadioGroup = QButtonGroup()
RadioGroupBox = QGroupBox('Варианты ответов')
btn_answer1 = QRadioButton('вариант 1')
btn_answer2 = QRadioButton('вариант 2')
btn_answer3 = QRadioButton('вариант 3')
btn_answer4 = QRadioButton('вариант 4')

RadioGroup.addButton(btn_answer1)
RadioGroup.addButton(btn_answer2)
RadioGroup.addButton(btn_answer3)
RadioGroup.addButton(btn_answer4)

layout_ans_hor = QHBoxLayout()
layout_ans_ver1 = QVBoxLayout()
layout_ans_ver2 = QVBoxLayout()
layout_ans_ver1.addWidget(btn_answer1)
layout_ans_ver1.addWidget(btn_answer2)
layout_ans_ver2.addWidget(btn_answer3)
layout_ans_ver2.addWidget(btn_answer4)

#layout_end_hor = QHBoxLayout()
#layout_and_ver1 = QVBoxLayout()
#layout_end_ver2 = QVBoxLayout()
#layout_end_ver1.addWidget(total_question)
#layout_ans_ver2.addWidget(total_score)
#layout_ans_ver2.addWidget(btn_restart)

layout_ans_hor.addLayout(layout_ans_ver1)
layout_ans_hor.addLayout(layout_ans_ver2)

layout_ans_hor.addLayout(layout_ans_ver1)
layout_ans_hor.addLayout(layout_ans_ver2)

RadioGroupBox.setLayout(layout_ans_hor)

#EndGroupBox = QGroupBox('Статистика')
AnsGroupBox = QGroupBox('Результат теста')
lb_Result = QLabel('Всего вопросов:')
lb_Correct = QLabel('Правильных ответов:')

layout_res = QVBoxLayout

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignTop | Qt.AlignLeft))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=1)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignHCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
layout_line3.addWidget(btn_OK, alignment=(Qt.AlignVCenter | Qt.AlignHCenter))

layout_line3.addStretch(3)

layout_card = QVBoxLayout()
layout_card.addStretch(1)

layout_card.addLayout(layout_line1)
layout_card.addStretch(1)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3)
layout_card.addStretch(1)
AnsGroupBox.hide()

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    btn_answer1.setChecked(False)
    btn_answer2.setChecked(False)
    btn_answer3.setChecked(False)
    btn_answer4.setChecked(False)

answer = [btn_answer1, btn_answer2, btn_answer3, btn_answer4]

def ask(q: Question):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct1(res):
    lb_Result.setText(res)
    lb_Correct.setText(res)
    show_result()

def show_correct2(res):
    lb_Correct.setText(res)
    show_result()


def check_answer():
    if answer[0].isChecked():
        main_win.score +=1
        if main_win.score == 1:
            show_correct1('Всего вопросов:')            

def next_question():
    cur_question = randint(0, len(question_list) - 1)
    question_asked.append(cur_question)
    if cur_question in question_asked:    
        q = question_list[cur_question]
        ask(q)
        main_win.total +=1
        question_asked.sort()

def click_OK():
    if main_win.total == len(question_list):
        check_answer()
    else:
        next_question()

main_win.total = 0
main_win.score = 0
main_win.resize(400, 300)
next_question()
main_win.setLayout(layout_card)
btn_OK.clicked.connect(click_OK)
main_win.show()
app.exec()
