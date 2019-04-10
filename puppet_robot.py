import PySimpleGUI as sg 
import eng_to_ipa as ipa 
import csv
import sys

layout = [[sg.Text('Open Script file. It should be a CSV generated from the template')],      
                 [sg.Input(key='_filename_'),sg.FileBrowse()],      
                 [sg.Button('Process Script'), sg.Text('This may take a while!')],
                 [sg.Text('_'  * 40, size=(30, 1))],
                 [sg.Text('Once the processing is complete you can start the show')],
                 [sg.Button('Start'),sg.Button('Pause'),sg.Button('Cancel')]      
                 ]      

window = sg.Window('Robot Theatre System').Layout(layout)    
window.Location=(0,0)

def ProcessScript():
    text_input = values[0] 
    ipa_text = ipa.convert(text_input)   
    print(ipa_text)

while True:
    event, values = window.ReadNonBlocking() #

    if event == 'Quit':
        break
    
    if event == 'Process Script':
        ProcessScript()
    




window.Close()

#final test routine 1