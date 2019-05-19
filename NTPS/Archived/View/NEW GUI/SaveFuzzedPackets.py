import PySimpleGUI as sg      

    # Very basic window.  Return values as a dictionary      
def savePCAP():
	layout = [            
              [sg.Text('Fuzzed PCAP Name:', size=(16, 1)), sg.InputText('', key='_NAME_')],      
              [sg.Text('Description:', size=(16, 1)), sg.InputText('', key='_DESCRIPTION_')],      
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