import PySimpleGUI as sg

# Very basic window.  Return values as a list
def notification(message):
    layout = [
              [sg.Text(message)],
              [sg.T("  "  * 50), sg.Button('OK')]]
    window = sg.Window('System Message').Layout(layout)
    while True:      
        button, values = window.Read()      
        if button == 'OK':      
            window.Close()
            break
        

no = 'bdgvxbvdxvdxbvdfv cbdcxbvdcv xczvadsvdszv adsvdvas'
notification(no)
