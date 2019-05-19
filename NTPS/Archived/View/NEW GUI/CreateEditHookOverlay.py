import PySimpleGUI as sg      

    # Very basic window.  Return values as a dictionary      
def savePCAP():
	layout = [            
              [sg.Text('Hook Name:', size=(16, 1)), sg.InputText('', key='_NAME_')],      
              [sg.Text('Description:', size=(16, 1)), sg.InputText('', size=(45, 8), key='_DESCRIPTION_')],
              [sg.Text('Hook Path:', size=(16, 1)), sg.InputText('', key='PATH'), sg.FileBrowse()],    
              [sg.Button('Save'), sg.Cancel()]]      
	window = sg.Window('Save Fuzzed Packets').Layout(layout)  
	while True:      
		button, values = window.Read()      
		if button == 'Save': 
			#needs deffff
			print('yayayayayayayayayya')
		elif button == 'Cancel':
			break
savePCAP()