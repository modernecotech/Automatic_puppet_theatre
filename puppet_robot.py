import PySimpleGUI as sg 
import eng_to_ipa as ipa 
import sys

layout = [[sg.Text('My one-shot window.')],      
                 [sg.InputText()],      
                 [sg.Submit(), sg.Cancel()]]      

window = sg.Window('Puppet Speech Robot').Layout(layout)    

event, values = window.Read()    
window.Close()

text_input = values[0] 
ipa_text = ipa.convert(text_input)   
print(ipa_text)
#final test routine