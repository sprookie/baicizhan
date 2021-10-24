import PySimpleGUI as sg
import pandas as pd
from playsound import playsound
import os
import time

words = pd.read_csv('words.csv')
word = words.sample(1)  # 随机选择一个单词
name = word.iloc[:, 1].values[0]
meaning = word.iloc[:, 2].values[0]
pro = word.iloc[:, 3].values[0]
sound_dir = os.listdir('Speech_US')

for i in sound_dir:
    form, end = i.split('.')
    if form == name:
        sound_name = i
        break
path1 = 'Speech_US/'
path = os.path.join(path1, sound_name)

wd = sg.Window('背单词',
               [[sg.Text('请根据读音拼写单词'), sg.Text(pro, key='pro'), sg.Text()],
                [sg.Input()],
                [sg.Btn('提示'), sg.Btn('答案'), sg.Btn('确认')],
                [sg.Text(size=(30, 1), key='hint'), sg.Text(size=(20, 1), key='hint2')],
                [sg.Text('        ', key='result')],
                [sg.Cancel()]]
               )
time.sleep(1)
playsound(path)
while True:
    event, values = wd.read()
    if event == 'Cancel':
        wd.close()
        break
    if event == '提示':
        wd.Element('hint').Update(meaning)
    if event == '答案':
        wd.Element('hint2').Update(name)
    elif event == '确认':
        if values[0] == name:
            wd.Element('hint').Update('')
            wd.Element('result').Update('correct！')
            wd.Element('hint2').Update(name)
            word = words.sample(1)  # 随机选择一个单词
            name = word.iloc[:, 1].values[0]
            meaning = word.iloc[:, 2].values[0]
            pro = word.iloc[:, 3].values[0]
            for i in sound_dir:
                form, end = i.split('.')
                if form == name:
                    sound_name = i
                    break
            time.sleep(1)
            playsound(os.path.join(path1, sound_name))
            wd.Element('pro').Update(pro)
        else:
            wd.Element('result').Update('wrong')



