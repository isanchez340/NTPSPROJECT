import PySimpleGUI as sg      

    # Very basic window.  Return values as a dictionary      
def savePCAP():
	layout = [            
              [sg.Text('Hook Name:', size=(16, 1)), sg.InputText('', key='_NAME_')],      
              [sg.Text('Description:', size=(16, 1)), sg.InputText('', size=(45, 8), key='_DESCRIPTION_')],
              [sg.Text('Hook Path:', size=(16, 1)), sg.InputText('', key='PATH'), sg.FileBrowse()],    
			[sg.Text('_'  * 200, size=(75, 1))],
		[sg.Listbox(values=['Listbox 1', 'Listbox 2', 'Listbox 3'], size=(75, 6))],
		[sg.Button('Save'), sg.Cancel()],
	]
	
	frame_layout = [      
                  [sg.T('Text inside of a frame')],      
                  [sg.CB('Check 1'), sg.CB('Check 2')]     
               ] 
	window = sg.Window('Create/Edit Hook Collection').Layout(layout)  
	while True:      
		button, values = window.Read()      
		if button == 'Save': 
			#needs deffff
			print('yayayayayayayayayya')
		elif button == 'Cancel':
			break
	return

savePCAP()