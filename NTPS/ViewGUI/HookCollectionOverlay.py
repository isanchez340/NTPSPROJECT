import PySimpleGUI as sg      

    # Very basic window.  Return values as a dictionary      
def HookC():
	layout = [            
              [sg.Text('Hook Collection Name:', size=(20, 1)), sg.InputText('', key='_NAME_')],      
              [sg.Text('Description:', size=(20, 1)), sg.InputText('', size=(45, 8), key='_DESCRIPTION_')],
			  [sg.Text('Status:', size=(20, 1)), sg.Combo(values=['ON', 'OFF'], size=(45, 8), key='_DESCRIPTION_')],
              [sg.Text('Execution Sequence:', size=(20, 1)), sg.InputText('', key='Sequence')],
			[sg.Text('Hook     '), sg.Text('Status   '), sg.Text('Hook Execution Sequence')],      
       [sg.Text('col Row 2'), sg.InputCombo(['Disabled', 'Enabled']), sg.Input('')],      
       [sg.Text('col Row 3'), sg.InputCombo(['Disabled', 'Enabled']), sg.Input('')],      
       [sg.Text('col Row 4'), sg.InputCombo(['Off', 'On']), sg.Input('')],      
       [sg.Text('col Row 5'), sg.InputCombo(['Off', 'On']), sg.Input('')],      
       [sg.Text('col Row 6'), sg.InputCombo(['Off', 'On']), sg.Input('')],      
       [sg.Text('col Row 7'), sg.InputCombo(['Off', 'On']), sg.Input('')],
              [sg.Button('Save'), sg.Cancel()]]
	
	window = sg.Window('Create/Edit Hook Collection').Layout(layout)  
	while True:      
		button, values = window.Read()      
		if button == 'Save': 
			#needs deffff
			print('yayayayayayayayayya')
		elif button == 'Cancel':
			break
HookC()