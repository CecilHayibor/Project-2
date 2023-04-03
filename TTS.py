'''
Cecil Elorm Kofi Hayibor
10970987
BMEN
'''

import PySimpleGUI as sg
import pyttsx3

Eng_tts = pyttsx3.init()
voice_types = Eng_tts.getProperty('voices')



layout = [    [sg.Text('Select the type of voice:',text_color='#000000', background_color='pink'),sg.Radio('Male', 'RADIO1', default=True, key='male', background_color='pink'),sg.Radio('Female', 'RADIO1', key='female', background_color='pink')],
     [sg.Text('Enter text to speak:',text_color='#000000', background_color='pink')],
          
    [sg.InputText(key='input'),sg.Button('Speak',button_color='green')],
   
    
]

window = sg.Window('TEXT TO SPEECH APP', layout,background_color='blue')

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Speak':
        text = values['input']
        if values['male']:
            Eng_tts.setProperty('voice', voice_types[1].id)
        elif values['female']:
           Eng_tts.setProperty('voice', voice_types[0].id) 
    
        Eng_tts.say(text)
        Eng_tts.runAndWait()

window.close()