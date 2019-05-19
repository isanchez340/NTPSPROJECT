import os

import PySimpleGUI as sg
import pickle
from Model.Services.servicesController import servicesController
from Model.Scapy.ScapyController import ScapyController
import threading

class ThreadedApp(threading.Thread):
	def __init__(self):
		super().__init__()
		self._stop_event = threading.Event()

	def run(self):
		ScapyController.start()

	def stop(self):
		ScapyController.stop()



    # Very basic window.  Return values as a dictionary      
layout = [            
		[sg.Text('Network Traffic Proxy System', size=(30, 1), font=("Helvetica", 25), text_color='orange')], 
		[sg.Text('____________________________________________________________________________________________________________________________________________________________________________________', size=(142,1))],      
            
		[sg.Text('Option View', size=(18, 1)),sg.VerticalSeparator(pad=None)],
		[sg.Button('Hook', size=(15, 1)),sg.VerticalSeparator(pad=None)],
		[sg.Button('Hook Collection', size=(15, 1)), sg.VerticalSeparator(pad=None)],
		[sg.Button('Live Packet', size=(15, 1)),sg.VerticalSeparator(pad=None)],
		[sg.Button('Packet from PCAP', size=(15, 1)),sg.VerticalSeparator(pad=None)]
]    
window = sg.Window('Network Traffic Proxy System').Layout(layout)
thread = ThreadedApp()
emp = ""
while True:      
	button, values = window.Read()
	if button == 'Hook': 
		layout = [            
			[sg.Text('Network Traffic Proxy System', size=(30, 1), font=("Helvetica", 25), text_color='orange')], 
			[sg.Text('____________________________________________________________________________________________________________________________________________________________________________________', size=(142,1))],
			[sg.Text('Option View', size=(18, 1)),sg.VerticalSeparator(pad=None), sg.Text('Hook View', size=(35, 1), font=("Helvetica", 25), justification='center')],
			[sg.Button('Hook', size=(15, 1)),sg.VerticalSeparator(pad=None), sg.Text('____________________________________________________________________________________________________________________________________________________________________________________', size=(120,1))],
			[sg.Button('Hook Collection', size=(15, 1)), sg.VerticalSeparator(pad=None), sg.Button('+Hook Collection', key='_+HookC_'), sg.Button('Edit', key='_HookCEdit_'), sg.Button('Delete', key='_HookCDel_'), sg.Text('           '), sg.Text('Search:'), sg.InputText('', size=(45, 8), key='_Search_')],
			[sg.Button('Live Packet', size=(15, 1)),sg.VerticalSeparator(pad=None), sg.Frame('Hook Properties',[      
					[sg.Text('       Hook        '), sg.Button('^'), sg.Text('Description   '), sg.Button('^'), sg.Text('Association to Hook Collection'), sg.Button('^')],      
					[sg.Radio('col Row 2', "RADIO1", default=False), sg.Text('Description'), sg.Text('')],      
					[sg.Radio('col Row 3', "RADIO1", default=False), sg.Text('Description'), sg.Text('')],      
					[sg.Radio('col Row 4', "RADIO1", default=False), sg.Text('Description'), sg.Text('')],      
					[sg.Radio('col Row 5', "RADIO1", default=False), sg.Text('Description'), sg.Text('')],      
					[sg.Radio('col Row 6', "RADIO1", default=False), sg.Text('Description'), sg.Text('')],      
					[sg.Radio('col Row 7', "RADIO1", default=False), sg.Text('Description'), sg.Text('')]], size=(80, 1))
			],
			[sg.Button('Packet From PCAP', size=(15, 1)),sg.VerticalSeparator(pad=None)]
		]
		window.Close()
		window = sg.Window('Network Traffic Proxy System').Layout(layout)  
	elif button == 'Hook Collection':
			layout = [            
				[sg.Text('Network Traffic Proxy System', size=(30, 1), font=("Helvetica", 25), text_color='orange')], 
				[sg.Text('____________________________________________________________________________________________________________________________________________________________________________________', size=(142,1))],
				[sg.Text('Option View', size=(18, 1)),sg.VerticalSeparator(pad=None), sg.Text('Hook Collection View', size=(35, 1), font=("Helvetica", 25), justification='center')],
				[sg.Button('Hook', size=(15, 1)),sg.VerticalSeparator(pad=None), sg.Text('____________________________________________________________________________________________________________________________________________________________________________________', size=(120,1))],
				[sg.Button('Hook Collection', size=(15, 1)), sg.VerticalSeparator(pad=None), sg.Button('+Hook'), sg.Button('Edit'), sg.Button('Delete'), sg.Text('           '), sg.Text('Search:'), sg.InputText('', size=(45, 8), key='_Search_')],
				[sg.Button('Live Packet', size=(15, 1)),sg.VerticalSeparator(pad=None), sg.Frame('Hook Collection Properties',[      
					[sg.Text('       Hook        '), sg.Button('^'), sg.Text('Description   '), sg.Button('^'), sg.Text('Association to Hook Collection'), sg.Button('^')],      
					[sg.Radio('col Row 2', "RADIO1", default=False), sg.Button('>'), sg.Text('Description'), sg.Text('')],      
					[sg.Radio('col Row 3', "RADIO1", default=False), sg.Button('>'), sg.Text('Description'), sg.Text('')],      
					[sg.Radio('col Row 4', "RADIO1", default=False), sg.Button('>'), sg.Text('Description'), sg.Text('')],      
					[sg.Radio('col Row 5', "RADIO1", default=False), sg.Button('>'), sg.Text('Description'), sg.Text('')],      
					[sg.Radio('col Row 6', "RADIO1", default=False), sg.Button('>'), sg.Text('Description'), sg.Text('')],      
					[sg.Radio('col Row 7', "RADIO1", default=False), sg.Button('>'), sg.Text('Description'), sg.Text('')]      
				])
				],
				[sg.Button('Packet From PCAP', size=(15, 1)),sg.VerticalSeparator(pad=None)]
			]
			window.Close()
			window = sg.Window('Network Traffic Proxy System').Layout(layout)  
	elif button == 'Live Packet':
			tab1_layout = [[sg.Multiline('', size=(90,15), key='_live_'), sg.Button('Clear')]]
			tab2_layout = [[sg.Multiline('', size=(110,15))]]
			tab3_layout = [[sg.Multiline('', size=(110,15))]]
			treedata = sg.TreeData()
			
			
			def add_files_in_folder(parent, fullname):
				treedata.Insert(parent,fullname, 'packet', sg.Button('Bleh'))
			add_files_in_folder('', 'rgdgvfdhbfg')
			
			
			
			layout = [            
				[sg.Text('Network Traffic Proxy System', size=(30, 1), font=("Helvetica", 25), text_color='orange')], 
				[sg.Text('____________________________________________________________________________________________________________________________________________________________________________________', size=(142,1))],
				[sg.Text('Option View', size=(18, 1)),sg.VerticalSeparator(pad=None), sg.Text('Live Packet View', size=(35, 1), font=("Helvetica", 25), justification='center')],
				[sg.Button('Hook', size=(15, 1)),sg.VerticalSeparator(pad=None), sg.Text('____________________________________________________________________________________________________________________________________________________________________________________', size=(120,1))],
				[sg.Button('Hook Collection', size=(15, 1)), sg.VerticalSeparator(pad=None), sg.Text('Proxy Behavior:'), sg.Button('On', key='_ProxyOn_'), sg.Button('Off', key='_ProxyOff_'), sg.Text('Interception Behavior:'), sg.Button('On', key='_InterOn_'), sg.Button('Off', key='_InterOff_'), sg.Text('Queue Size:'), sg.InputText('', size=(45, 8), key='_QSize_')],
				[sg.Button('Live Packet', size=(15, 1)),sg.VerticalSeparator(pad=None), sg.Frame('Capture Filter',[
					[sg.Text('Filter:'), sg.InputText('', size=(88, 8), key='_Filter_'), sg.Button('Apply'), sg.Button('Clear', key='_CFilter_')]
				])
				],
				[sg.Button('Packet from PCAP', size=(15, 1)),sg.VerticalSeparator(pad=None), sg.Frame('Packet Area',[
					[sg.TabGroup([[sg.Tab('Dissected', tab1_layout), sg.Tab('Binary', tab2_layout), sg.Tab('HEX', tab3_layout)]])]
				])
				],
				[sg.Text('                                '), sg.VerticalSeparator(pad=None), sg.Frame('Field Area',[
					[sg.Tree(data=treedata, headings=['Field Name', 'Value', 'Mask'], auto_size_columns=False, col_widths=80, num_rows=8, col0_width=-1, key='_TREE_', show_expanded=False), sg.InputCombo(['Format', 'choice 2'])],
					[sg.Button('Edit'), sg.Button('Forward'), sg.Button('Drop')]
				])]
			]
			window.Close()
			window = sg.Window('Network Traffic Proxy System').Layout(layout) 
	elif button == 'Packet from PCAP':
		tab1_layout = [[sg.Multiline('', size=(90,15)), sg.Button('Clear')]]
		tab2_layout = [[sg.Multiline('', size=(110,15))]]
		tab3_layout = [[sg.Multiline('', size=(110,15))]]
		treedata = sg.TreeData()
			
			
		def add_files_in_folder(parent, fullname):
			treedata.Insert(parent,fullname, 'packet', sg.Button('Bleh'))
		add_files_in_folder('', 'rgdgvfdhbfg')
			
		layout = [            
			[sg.Text('Network Traffic Proxy System', size=(30, 1), font=("Helvetica", 25), text_color='orange')], 
			[sg.Text('____________________________________________________________________________________________________________________________________________________________________________________', size=(142,1))],
			[sg.Text('Option View', size=(18, 1)),sg.VerticalSeparator(pad=None), sg.Text('Packet From PCAP View', size=(35, 1), font=("Helvetica", 25), justification='center')],
			[sg.Button('Hook', size=(15, 1)),sg.VerticalSeparator(pad=None), sg.Text('____________________________________________________________________________________________________________________________________________________________________________________', size=(120,1))],
			[sg.Button('Hook Collection', size=(15, 1)), sg.VerticalSeparator(pad=None), sg.Text('PCAP File:'), sg.Input(), sg.FileBrowse('Open'), sg.Button('Cancel')],
			[sg.Button('Live Packet', size=(15, 1)),sg.VerticalSeparator(pad=None), sg.Frame('Capture Filter',[
				[sg.Text('Filter:'), sg.InputText('', size=(88, 8), key='_Filter_'), sg.Button('Apply'), sg.Button('Clear', key='_CFilter_')]
			])
			],
			[sg.Button('Packet from PCAP', size=(15, 1)),sg.VerticalSeparator(pad=None), sg.Frame('Packet Area',[
				[sg.TabGroup([[sg.Tab('Dissected', tab1_layout), sg.Tab('Binary', tab2_layout), sg.Tab('HEX', tab3_layout)]])]
			])
			],
			[sg.Text('                                '), sg.VerticalSeparator(pad=None), sg.Frame('Field Area',[
				[sg.Tree(data=treedata, headings=['Field Name', 'Value', 'Mask'], auto_size_columns=False, col_widths=80, num_rows=8, col0_width=-1, key='_TREE_', show_expanded=False), sg.InputCombo(['Format', 'choice 2'])],
				[sg.Button('Edit'), sg.Button('Forward'), sg.Button('Drop')]
			])]
		]
		window.Close()
		window = sg.Window('Network Traffic Proxy System').Layout(layout)
	elif button == '_CFilter_':
		print('Hello!!!!!!')
	elif button == '_ProxyOn_':
		servicesController(None, None, 0)
	elif button == '_ProxyOff_':
		servicesController(None, None, 1)
	elif button == '_InterOn_':
		thread.start()
	elif button == '_InterOff_':
		thread.stop()
	if os.stat('Emp.pickel').st_size is not 0:
		pickle_off = open("Emp.pickel", "rb")
		emp = pickle.load(pickle_off)
		window.Element('_live_').Update(emp)

