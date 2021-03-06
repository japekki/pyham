# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Aug  8 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class FrameMain
###########################################################################

class FrameMain ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Pyham Client 0.022", pos = wx.DefaultPosition, size = wx.Size( 780,540 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL, name = u"pyham" )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		fgSizer21 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer21.AddGrowableCol( 0 )
		fgSizer21.AddGrowableRow( 0 )
		fgSizer21.SetFlexibleDirection( wx.BOTH )
		fgSizer21.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.scrolledWindow_Main = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.scrolledWindow_Main.SetScrollRate( 5, 5 )
		fgSizer_Main = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer_Main.AddGrowableCol( 0 )
		fgSizer_Main.AddGrowableRow( 1 )
		fgSizer_Main.SetFlexibleDirection( wx.BOTH )
		fgSizer_Main.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer_Roomselect = wx.FlexGridSizer( 0, 0, 0, 0 )
		fgSizer_Roomselect.AddGrowableCol( 1 )
		fgSizer_Roomselect.SetFlexibleDirection( wx.BOTH )
		fgSizer_Roomselect.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.staticText_Room = wx.StaticText( self.scrolledWindow_Main, wx.ID_ANY, u"Room", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Room.Wrap( -1 )
		
		self.staticText_Room.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		
		fgSizer_Roomselect.Add( self.staticText_Room, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		choice_RoomChoices = []
		self.choice_Room = wx.Choice( self.scrolledWindow_Main, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choice_RoomChoices, 0 )
		self.choice_Room.SetSelection( 0 )
		fgSizer_Roomselect.Add( self.choice_Room, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.button_Settings = wx.Button( self.scrolledWindow_Main, wx.ID_ANY, u"Settings", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer_Roomselect.Add( self.button_Settings, 0, wx.ALL, 5 )
		
		
		fgSizer_Main.Add( fgSizer_Roomselect, 1, wx.EXPAND, 5 )
		
		listBox_UsersChoices = []
		self.listBox_Users = wx.ListBox( self.scrolledWindow_Main, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listBox_UsersChoices, 0 )
		fgSizer_Main.Add( self.listBox_Users, 0, wx.EXPAND|wx.ALL, 5 )
		
		fgSizer_Send = wx.FlexGridSizer( 0, 6, 0, 0 )
		fgSizer_Send.AddGrowableCol( 3 )
		fgSizer_Send.SetFlexibleDirection( wx.HORIZONTAL )
		fgSizer_Send.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.staticText_Callsign = wx.StaticText( self.scrolledWindow_Main, wx.ID_ANY, u"Callsign", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Callsign.Wrap( -1 )
		
		self.staticText_Callsign.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		
		fgSizer_Send.Add( self.staticText_Callsign, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.textCtrl_Callsign = wx.TextCtrl( self.scrolledWindow_Main, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textCtrl_Callsign.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.textCtrl_Callsign.SetMinSize( wx.Size( 120,-1 ) )
		
		fgSizer_Send.Add( self.textCtrl_Callsign, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.staticText_Description = wx.StaticText( self.scrolledWindow_Main, wx.ID_ANY, u"Description", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Description.Wrap( -1 )
		
		self.staticText_Description.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		
		fgSizer_Send.Add( self.staticText_Description, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.textCtrl_Description = wx.TextCtrl( self.scrolledWindow_Main, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textCtrl_Description.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		
		fgSizer_Send.Add( self.textCtrl_Description, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.button_Send = wx.Button( self.scrolledWindow_Main, wx.ID_ANY, u"Send", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer_Send.Add( self.button_Send, 0, wx.ALL, 5 )
		
		self.button_Discrecorder = wx.Button( self.scrolledWindow_Main, wx.ID_ANY, u"Record to file", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer_Send.Add( self.button_Discrecorder, 0, wx.ALL, 5 )
		
		
		fgSizer_Main.Add( fgSizer_Send, 0, wx.EXPAND, 5 )
		
		fgSizer_Bottom = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer_Bottom.AddGrowableCol( 0 )
		fgSizer_Bottom.SetFlexibleDirection( wx.BOTH )
		fgSizer_Bottom.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.panel_Server = wx.Panel( self.scrolledWindow_Main, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL|wx.BORDER_SUNKEN )
		fgSizer_Preset = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer_Preset.AddGrowableCol( 0 )
		fgSizer_Preset.SetFlexibleDirection( wx.BOTH )
		fgSizer_Preset.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer_PresetSettings = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer_PresetSettings.AddGrowableCol( 1 )
		fgSizer_PresetSettings.SetFlexibleDirection( wx.HORIZONTAL )
		fgSizer_PresetSettings.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.staticText_Preset = wx.StaticText( self.panel_Server, wx.ID_ANY, u"Preset", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Preset.Wrap( -1 )
		
		self.staticText_Preset.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		
		fgSizer_PresetSettings.Add( self.staticText_Preset, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		comboBox_PresetChoices = []
		self.comboBox_Preset = wx.ComboBox( self.panel_Server, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboBox_PresetChoices, 0 )
		fgSizer_PresetSettings.Add( self.comboBox_Preset, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.staticText_Server = wx.StaticText( self.panel_Server, wx.ID_ANY, u"Server", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Server.Wrap( -1 )
		
		self.staticText_Server.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		
		fgSizer_PresetSettings.Add( self.staticText_Server, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.textCtrl_Server = wx.TextCtrl( self.panel_Server, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer_PresetSettings.Add( self.textCtrl_Server, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.staticText_Port = wx.StaticText( self.panel_Server, wx.ID_ANY, u"Port", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Port.Wrap( -1 )
		
		self.staticText_Port.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		
		fgSizer_PresetSettings.Add( self.staticText_Port, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		fgSizer27 = wx.FlexGridSizer( 0, 4, 0, 0 )
		fgSizer27.AddGrowableCol( 0 )
		fgSizer27.SetFlexibleDirection( wx.BOTH )
		fgSizer27.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.textCtrl_Port = wx.TextCtrl( self.panel_Server, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textCtrl_Port.SetMaxSize( wx.Size( 80,-1 ) )
		
		fgSizer27.Add( self.textCtrl_Port, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.staticText_Protocol = wx.StaticText( self.panel_Server, wx.ID_ANY, u"Protocol", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Protocol.Wrap( -1 )
		
		self.staticText_Protocol.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		
		fgSizer27.Add( self.staticText_Protocol, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		choice_ProtocolChoices = [ u"Echolink", u"Eqso", u"Frn", u"Pyham" ]
		self.choice_Protocol = wx.Choice( self.panel_Server, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choice_ProtocolChoices, 0 )
		self.choice_Protocol.SetSelection( 0 )
		fgSizer27.Add( self.choice_Protocol, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		fgSizer_PresetSettings.Add( fgSizer27, 1, wx.EXPAND, 5 )
		
		
		fgSizer_Preset.Add( fgSizer_PresetSettings, 1, wx.EXPAND, 5 )
		
		fgSizer_FileButtons = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer_FileButtons.SetFlexibleDirection( wx.HORIZONTAL )
		fgSizer_FileButtons.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.button_Load = wx.Button( self.panel_Server, wx.ID_ANY, u"Load", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer_FileButtons.Add( self.button_Load, 0, wx.ALL, 5 )
		
		self.button_Delete = wx.Button( self.panel_Server, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer_FileButtons.Add( self.button_Delete, 0, wx.ALL, 5 )
		
		self.button_Save = wx.Button( self.panel_Server, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer_FileButtons.Add( self.button_Save, 0, wx.ALL, 5 )
		
		
		fgSizer_Preset.Add( fgSizer_FileButtons, 1, wx.EXPAND, 5 )
		
		fgSizerConnectionWidgets = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizerConnectionWidgets.SetFlexibleDirection( wx.HORIZONTAL )
		fgSizerConnectionWidgets.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.button_Connect = wx.Button( self.panel_Server, wx.ID_ANY, u"Connect", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizerConnectionWidgets.Add( self.button_Connect, 0, wx.ALL, 5 )
		
		self.checkBox_Reconnect = wx.CheckBox( self.panel_Server, wx.ID_ANY, u"Reconnect", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizerConnectionWidgets.Add( self.checkBox_Reconnect, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		fgSizer_Preset.Add( fgSizerConnectionWidgets, 1, wx.EXPAND, 5 )
		
		
		self.panel_Server.SetSizer( fgSizer_Preset )
		self.panel_Server.Layout()
		fgSizer_Preset.Fit( self.panel_Server )
		fgSizer_Bottom.Add( self.panel_Server, 1, wx.ALL|wx.EXPAND, 5 )
		
		fgSizer_Talk = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer_Talk.AddGrowableRow( 1 )
		fgSizer_Talk.SetFlexibleDirection( wx.BOTH )
		fgSizer_Talk.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer_Audio = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer_Audio.SetFlexibleDirection( wx.BOTH )
		fgSizer_Audio.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.panel_Speaker = wx.Panel( self.scrolledWindow_Main, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL|wx.BORDER_SUNKEN )
		fgSizer_Speaker = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer_Speaker.AddGrowableRow( 0 )
		fgSizer_Speaker.AddGrowableRow( 1 )
		fgSizer_Speaker.AddGrowableRow( 2 )
		fgSizer_Speaker.SetFlexibleDirection( wx.BOTH )
		fgSizer_Speaker.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer_SpeakerSelect = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer_SpeakerSelect.AddGrowableCol( 1 )
		fgSizer_SpeakerSelect.SetFlexibleDirection( wx.BOTH )
		fgSizer_SpeakerSelect.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.staticText_Speaker = wx.StaticText( self.panel_Speaker, wx.ID_ANY, u"Spk", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Speaker.Wrap( -1 )
		
		self.staticText_Speaker.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		
		fgSizer_SpeakerSelect.Add( self.staticText_Speaker, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		choice_SpeakerChoices = [ u"Default", u"Spk 1", u"Spk 2" ]
		self.choice_Speaker = wx.Choice( self.panel_Speaker, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choice_SpeakerChoices, 0 )
		self.choice_Speaker.SetSelection( 0 )
		fgSizer_SpeakerSelect.Add( self.choice_Speaker, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		fgSizer_Speaker.Add( fgSizer_SpeakerSelect, 1, wx.EXPAND, 5 )
		
		self.slider_Speaker = wx.Slider( self.panel_Speaker, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.Size( -1,-1 ), wx.SL_HORIZONTAL )
		fgSizer_Speaker.Add( self.slider_Speaker, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.gauge_Speaker = wx.Gauge( self.panel_Speaker, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.gauge_Speaker.SetValue( 50 ) 
		fgSizer_Speaker.Add( self.gauge_Speaker, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.panel_Speaker.SetSizer( fgSizer_Speaker )
		self.panel_Speaker.Layout()
		fgSizer_Speaker.Fit( self.panel_Speaker )
		fgSizer_Audio.Add( self.panel_Speaker, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.panel_Mic = wx.Panel( self.scrolledWindow_Main, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL|wx.BORDER_SUNKEN )
		fgSizer_Mic = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer_Mic.AddGrowableRow( 0 )
		fgSizer_Mic.AddGrowableRow( 1 )
		fgSizer_Mic.AddGrowableRow( 2 )
		fgSizer_Mic.SetFlexibleDirection( wx.BOTH )
		fgSizer_Mic.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer_MicSelect = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer_MicSelect.AddGrowableCol( 1 )
		fgSizer_MicSelect.SetFlexibleDirection( wx.BOTH )
		fgSizer_MicSelect.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.staticText_Mic = wx.StaticText( self.panel_Mic, wx.ID_ANY, u"Mic", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Mic.Wrap( -1 )
		
		self.staticText_Mic.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		
		fgSizer_MicSelect.Add( self.staticText_Mic, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		choice_MicChoices = [ u"Default", u"Mic 1", u"Mic 2" ]
		self.choice_Mic = wx.Choice( self.panel_Mic, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choice_MicChoices, 0 )
		self.choice_Mic.SetSelection( 0 )
		fgSizer_MicSelect.Add( self.choice_Mic, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		fgSizer_Mic.Add( fgSizer_MicSelect, 1, wx.EXPAND, 5 )
		
		self.slider_Mic = wx.Slider( self.panel_Mic, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		fgSizer_Mic.Add( self.slider_Mic, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.gauge_Mic = wx.Gauge( self.panel_Mic, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.gauge_Mic.SetValue( 50 ) 
		fgSizer_Mic.Add( self.gauge_Mic, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.panel_Mic.SetSizer( fgSizer_Mic )
		self.panel_Mic.Layout()
		fgSizer_Mic.Fit( self.panel_Mic )
		fgSizer_Audio.Add( self.panel_Mic, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		fgSizer_Talk.Add( fgSizer_Audio, 1, wx.EXPAND, 5 )
		
		self.button_Ptt = wx.Button( self.scrolledWindow_Main, wx.ID_ANY, u"Push To Talk", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.button_Ptt.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.button_Ptt.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.button_Ptt.SetBackgroundColour( wx.Colour( 186, 216, 200 ) )
		
		fgSizer_Talk.Add( self.button_Ptt, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		fgSizer_Bottom.Add( fgSizer_Talk, 1, wx.EXPAND, 5 )
		
		
		fgSizer_Main.Add( fgSizer_Bottom, 1, wx.EXPAND, 5 )
		
		
		self.scrolledWindow_Main.SetSizer( fgSizer_Main )
		self.scrolledWindow_Main.Layout()
		fgSizer_Main.Fit( self.scrolledWindow_Main )
		fgSizer21.Add( self.scrolledWindow_Main, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( fgSizer21 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.choice_Room.Bind( wx.EVT_CHOICE, self.choose_room )
		self.button_Settings.Bind( wx.EVT_BUTTON, self.click_settings )
		self.button_Send.Bind( wx.EVT_BUTTON, self.click_send )
		self.button_Discrecorder.Bind( wx.EVT_BUTTON, self.click_Diskrecorder )
		self.comboBox_Preset.Bind( wx.EVT_COMBOBOX, self.choose_Preset )
		self.button_Load.Bind( wx.EVT_BUTTON, self.click_load )
		self.button_Delete.Bind( wx.EVT_BUTTON, self.click_delete )
		self.button_Save.Bind( wx.EVT_BUTTON, self.click_save )
		self.button_Connect.Bind( wx.EVT_BUTTON, self.click_connect )
		self.choice_Speaker.Bind( wx.EVT_CHOICE, self.choose_speaker )
		self.slider_Speaker.Bind( wx.EVT_SCROLL, self.volume_speaker )
		self.choice_Mic.Bind( wx.EVT_CHOICE, self.choose_mic )
		self.slider_Mic.Bind( wx.EVT_SCROLL, self.volume_mic )
		self.button_Ptt.Bind( wx.EVT_KEY_DOWN, self.push_ptt )
		self.button_Ptt.Bind( wx.EVT_KEY_UP, self.release_ptt )
		self.button_Ptt.Bind( wx.EVT_LEFT_DOWN, self.push_ptt )
		self.button_Ptt.Bind( wx.EVT_LEFT_UP, self.release_ptt )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def choose_room( self, event ):
		event.Skip()
	
	def click_settings( self, event ):
		event.Skip()
	
	def click_send( self, event ):
		event.Skip()
	
	def click_Diskrecorder( self, event ):
		event.Skip()
	
	def choose_Preset( self, event ):
		event.Skip()
	
	def click_load( self, event ):
		event.Skip()
	
	def click_delete( self, event ):
		event.Skip()
	
	def click_save( self, event ):
		event.Skip()
	
	def click_connect( self, event ):
		event.Skip()
	
	def choose_speaker( self, event ):
		event.Skip()
	
	def volume_speaker( self, event ):
		event.Skip()
	
	def choose_mic( self, event ):
		event.Skip()
	
	def volume_mic( self, event ):
		event.Skip()
	
	def push_ptt( self, event ):
		event.Skip()
	
	def release_ptt( self, event ):
		event.Skip()
	
	
	

###########################################################################
## Class FrameSettings
###########################################################################

class FrameSettings ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Pyham Client - Settings", pos = wx.DefaultPosition, size = wx.Size( 620,840 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		fgSizer24 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer24.AddGrowableCol( 0 )
		fgSizer24.AddGrowableRow( 0 )
		fgSizer24.SetFlexibleDirection( wx.BOTH )
		fgSizer24.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_scrolledWindow_Settings = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow_Settings.SetScrollRate( 5, 5 )
		fgSizer_Settings = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer_Settings.AddGrowableCol( 0 )
		fgSizer_Settings.AddGrowableRow( 2 )
		fgSizer_Settings.SetFlexibleDirection( wx.BOTH )
		fgSizer_Settings.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer_SettingsWidgets = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer_SettingsWidgets.SetFlexibleDirection( wx.BOTH )
		fgSizer_SettingsWidgets.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.panel_Devices = wx.Panel( self.m_scrolledWindow_Settings, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL|wx.BORDER_SIMPLE )
		fgSizer_Devices = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer_Devices.SetFlexibleDirection( wx.BOTH )
		fgSizer_Devices.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.staticText_Audio = wx.StaticText( self.panel_Devices, wx.ID_ANY, u"Audio device defaults", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Audio.Wrap( -1 )
		
		self.staticText_Audio.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		
		fgSizer_Devices.Add( self.staticText_Audio, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.staticText_Speaker = wx.StaticText( self.panel_Devices, wx.ID_ANY, u"Speaker device:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Speaker.Wrap( -1 )
		
		fgSizer_Devices.Add( self.staticText_Speaker, 0, wx.ALL, 5 )
		
		choice_SpeakerChoices = [ u"Default", u"Spk 1", u"Spk 2" ]
		self.choice_Speaker = wx.Choice( self.panel_Devices, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choice_SpeakerChoices, 0 )
		self.choice_Speaker.SetSelection( 0 )
		fgSizer_Devices.Add( self.choice_Speaker, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText20 = wx.StaticText( self.panel_Devices, wx.ID_ANY, u"Speaker volume:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )
		
		fgSizer_Devices.Add( self.m_staticText20, 0, wx.ALL, 5 )
		
		self.spinCtrl_Speaker = wx.SpinCtrl( self.panel_Devices, wx.ID_ANY, u"50", wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 100, 50 )
		fgSizer_Devices.Add( self.spinCtrl_Speaker, 0, wx.ALL, 5 )
		
		self.m_staticline3 = wx.StaticLine( self.panel_Devices, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer_Devices.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.staticText_Mic = wx.StaticText( self.panel_Devices, wx.ID_ANY, u"Mic device:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Mic.Wrap( -1 )
		
		fgSizer_Devices.Add( self.staticText_Mic, 0, wx.ALL, 5 )
		
		choice_MicChoices = [ u"Default", u"Mic 1", u"Mic 2" ]
		self.choice_Mic = wx.Choice( self.panel_Devices, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choice_MicChoices, 0 )
		self.choice_Mic.SetSelection( 0 )
		fgSizer_Devices.Add( self.choice_Mic, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText21 = wx.StaticText( self.panel_Devices, wx.ID_ANY, u"Mic volume:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		
		fgSizer_Devices.Add( self.m_staticText21, 0, wx.ALL, 5 )
		
		self.spinCtrl_Mic = wx.SpinCtrl( self.panel_Devices, wx.ID_ANY, u"50", wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 100, 50 )
		fgSizer_Devices.Add( self.spinCtrl_Mic, 0, wx.ALL, 5 )
		
		
		self.panel_Devices.SetSizer( fgSizer_Devices )
		self.panel_Devices.Layout()
		fgSizer_Devices.Fit( self.panel_Devices )
		fgSizer_SettingsWidgets.Add( self.panel_Devices, 1, wx.ALL, 5 )
		
		self.panel_Autoconnect = wx.Panel( self.m_scrolledWindow_Settings, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL|wx.BORDER_SIMPLE )
		fgSizer_Autoconnect = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer_Autoconnect.SetFlexibleDirection( wx.BOTH )
		fgSizer_Autoconnect.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.staticText_Autoconnect = wx.StaticText( self.panel_Autoconnect, wx.ID_ANY, u"Autoconnect at startup", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Autoconnect.Wrap( -1 )
		
		self.staticText_Autoconnect.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		
		fgSizer_Autoconnect.Add( self.staticText_Autoconnect, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.staticText_Preset = wx.StaticText( self.panel_Autoconnect, wx.ID_ANY, u"Server preset:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Preset.Wrap( -1 )
		
		fgSizer_Autoconnect.Add( self.staticText_Preset, 0, wx.ALL, 5 )
		
		choice_AutoconnectPresetChoices = []
		self.choice_AutoconnectPreset = wx.Choice( self.panel_Autoconnect, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choice_AutoconnectPresetChoices, 0 )
		self.choice_AutoconnectPreset.SetSelection( 0 )
		fgSizer_Autoconnect.Add( self.choice_AutoconnectPreset, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.staticText_Room = wx.StaticText( self.panel_Autoconnect, wx.ID_ANY, u"Room:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Room.Wrap( -1 )
		
		fgSizer_Autoconnect.Add( self.staticText_Room, 0, wx.ALL, 5 )
		
		choice_RoomChoices = []
		self.choice_Room = wx.Choice( self.panel_Autoconnect, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choice_RoomChoices, 0 )
		self.choice_Room.SetSelection( 0 )
		fgSizer_Autoconnect.Add( self.choice_Room, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.staticText_Callsign = wx.StaticText( self.panel_Autoconnect, wx.ID_ANY, u"Callsign:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Callsign.Wrap( -1 )
		
		fgSizer_Autoconnect.Add( self.staticText_Callsign, 0, wx.ALL, 5 )
		
		self.textCtrl_Callsign = wx.TextCtrl( self.panel_Autoconnect, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer_Autoconnect.Add( self.textCtrl_Callsign, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.panel_Autoconnect.SetSizer( fgSizer_Autoconnect )
		self.panel_Autoconnect.Layout()
		fgSizer_Autoconnect.Fit( self.panel_Autoconnect )
		fgSizer_SettingsWidgets.Add( self.panel_Autoconnect, 1, wx.ALL, 5 )
		
		self.m_panel7 = wx.Panel( self.m_scrolledWindow_Settings, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL|wx.BORDER_SIMPLE )
		fgSizer27 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer27.SetFlexibleDirection( wx.BOTH )
		fgSizer27.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText18 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"PTT trigger", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )
		
		self.m_staticText18.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		
		fgSizer27.Add( self.m_staticText18, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		choice_pttChoices = [ u"UI button", u"COM1", u"LPT1", u"USB serial", u"Joystick 1 button 1" ]
		self.choice_ptt = wx.Choice( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choice_pttChoices, 0 )
		self.choice_ptt.SetSelection( 0 )
		fgSizer27.Add( self.choice_ptt, 0, wx.ALL, 5 )
		
		
		self.m_panel7.SetSizer( fgSizer27 )
		self.m_panel7.Layout()
		fgSizer27.Fit( self.m_panel7 )
		fgSizer_SettingsWidgets.Add( self.m_panel7, 1, wx.ALL, 5 )
		
		
		fgSizer_Settings.Add( fgSizer_SettingsWidgets, 1, wx.EXPAND, 5 )
		
		self.panel_RecordingPath = wx.Panel( self.m_scrolledWindow_Settings, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_SIMPLE|wx.TAB_TRAVERSAL )
		fgSizer_RecorderWidgets = wx.FlexGridSizer( 3, 0, 0, 0 )
		fgSizer_RecorderWidgets.AddGrowableCol( 0 )
		fgSizer_RecorderWidgets.SetFlexibleDirection( wx.BOTH )
		fgSizer_RecorderWidgets.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.staticText_RecordingPath = wx.StaticText( self.panel_RecordingPath, wx.ID_ANY, u"Recording path", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_RecordingPath.Wrap( -1 )
		
		self.staticText_RecordingPath.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		
		fgSizer_RecorderWidgets.Add( self.staticText_RecordingPath, 0, wx.ALL, 5 )
		
		fgSizer_RecorderUpper = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer_RecorderUpper.AddGrowableCol( 0 )
		fgSizer_RecorderUpper.SetFlexibleDirection( wx.BOTH )
		fgSizer_RecorderUpper.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.textCtrl_RecorderPath = wx.TextCtrl( self.panel_RecordingPath, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer_RecorderUpper.Add( self.textCtrl_RecorderPath, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.button_RecorderPath = wx.Button( self.panel_RecordingPath, wx.ID_ANY, u"Browse", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer_RecorderUpper.Add( self.button_RecorderPath, 0, wx.ALL, 5 )
		
		
		fgSizer_RecorderWidgets.Add( fgSizer_RecorderUpper, 1, wx.EXPAND, 5 )
		
		fgSizer_RecorderLower = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer_RecorderLower.SetFlexibleDirection( wx.BOTH )
		fgSizer_RecorderLower.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.staticText_Format = wx.StaticText( self.panel_RecordingPath, wx.ID_ANY, u"Format:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Format.Wrap( -1 )
		
		fgSizer_RecorderLower.Add( self.staticText_Format, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		choice_FormatChoices = [ u"WAV", u"MP3", u"FLAC" ]
		self.choice_Format = wx.Choice( self.panel_RecordingPath, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choice_FormatChoices, 0 )
		self.choice_Format.SetSelection( 0 )
		fgSizer_RecorderLower.Add( self.choice_Format, 0, wx.ALL, 5 )
		
		
		fgSizer_RecorderWidgets.Add( fgSizer_RecorderLower, 1, wx.EXPAND, 5 )
		
		
		self.panel_RecordingPath.SetSizer( fgSizer_RecorderWidgets )
		self.panel_RecordingPath.Layout()
		fgSizer_RecorderWidgets.Fit( self.panel_RecordingPath )
		fgSizer_Settings.Add( self.panel_RecordingPath, 0, wx.ALL|wx.EXPAND, 5 )
		
		fgSizer_NotifyWidgets = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer_NotifyWidgets.AddGrowableCol( 0 )
		fgSizer_NotifyWidgets.SetFlexibleDirection( wx.BOTH )
		fgSizer_NotifyWidgets.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.panel_Notify = wx.Panel( self.m_scrolledWindow_Settings, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL|wx.BORDER_SIMPLE )
		fgSizer_Notify = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer_Notify.AddGrowableCol( 0 )
		fgSizer_Notify.SetFlexibleDirection( wx.BOTH )
		fgSizer_Notify.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.staticText_SoundNotify = wx.StaticText( self.panel_Notify, wx.ID_ANY, u"Sound notifications", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_SoundNotify.Wrap( -1 )
		
		self.staticText_SoundNotify.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		
		fgSizer_Notify.Add( self.staticText_SoundNotify, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.staticText_Roger = wx.StaticText( self.panel_Notify, wx.ID_ANY, u"Roger beep", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Roger.Wrap( -1 )
		
		self.staticText_Roger.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		
		fgSizer_Notify.Add( self.staticText_Roger, 0, wx.ALL, 5 )
		
		fgSizer36 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer36.AddGrowableCol( 0 )
		fgSizer36.SetFlexibleDirection( wx.BOTH )
		fgSizer36.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer34 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer34.AddGrowableCol( 0 )
		fgSizer34.SetFlexibleDirection( wx.BOTH )
		fgSizer34.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer32 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer32.AddGrowableCol( 0 )
		fgSizer32.AddGrowableCol( 1 )
		fgSizer32.AddGrowableCol( 2 )
		fgSizer32.SetFlexibleDirection( wx.BOTH )
		fgSizer32.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.checkBox_PlayRoger = wx.CheckBox( self.panel_Notify, wx.ID_ANY, u"Play on speaker", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer32.Add( self.checkBox_PlayRoger, 0, wx.ALL, 5 )
		
		self.checkBox_TransmitRoger = wx.CheckBox( self.panel_Notify, wx.ID_ANY, u"Transmit", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer32.Add( self.checkBox_TransmitRoger, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.checkBox_RecordRoger = wx.CheckBox( self.panel_Notify, wx.ID_ANY, u"Record to file", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer32.Add( self.checkBox_RecordRoger, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		fgSizer34.Add( fgSizer32, 1, wx.EXPAND, 5 )
		
		fgSizer35 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer35.AddGrowableCol( 1 )
		fgSizer35.SetFlexibleDirection( wx.BOTH )
		fgSizer35.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText22 = wx.StaticText( self.panel_Notify, wx.ID_ANY, u"File:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )
		
		fgSizer35.Add( self.m_staticText22, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.textCtrl_FileRoger = wx.TextCtrl( self.panel_Notify, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer35.Add( self.textCtrl_FileRoger, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		fgSizer34.Add( fgSizer35, 1, wx.EXPAND, 5 )
		
		
		fgSizer36.Add( fgSizer34, 1, wx.EXPAND, 5 )
		
		self.button_FileRoger = wx.Button( self.panel_Notify, wx.ID_ANY, u"Browse...", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer36.Add( self.button_FileRoger, 0, wx.ALIGN_BOTTOM|wx.ALL, 5 )
		
		
		fgSizer_Notify.Add( fgSizer36, 1, wx.EXPAND, 5 )
		
		self.m_staticline1 = wx.StaticLine( self.panel_Notify, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer_Notify.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.staticText_Connect = wx.StaticText( self.panel_Notify, wx.ID_ANY, u"Connect notification", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Connect.Wrap( -1 )
		
		self.staticText_Connect.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		
		fgSizer_Notify.Add( self.staticText_Connect, 0, wx.ALL, 5 )
		
		fgSizer37 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer37.AddGrowableCol( 0 )
		fgSizer37.SetFlexibleDirection( wx.BOTH )
		fgSizer37.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer38 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer38.AddGrowableCol( 0 )
		fgSizer38.SetFlexibleDirection( wx.BOTH )
		fgSizer38.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer322 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer322.AddGrowableCol( 0 )
		fgSizer322.AddGrowableCol( 1 )
		fgSizer322.SetFlexibleDirection( wx.BOTH )
		fgSizer322.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.checkBox_PlayConnect = wx.CheckBox( self.panel_Notify, wx.ID_ANY, u"Play on speaker", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer322.Add( self.checkBox_PlayConnect, 0, wx.ALL, 5 )
		
		self.checkBox_RecordConnect = wx.CheckBox( self.panel_Notify, wx.ID_ANY, u"Record to file", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer322.Add( self.checkBox_RecordConnect, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		fgSizer38.Add( fgSizer322, 1, wx.EXPAND, 5 )
		
		fgSizer28 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer28.AddGrowableCol( 1 )
		fgSizer28.SetFlexibleDirection( wx.BOTH )
		fgSizer28.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText23 = wx.StaticText( self.panel_Notify, wx.ID_ANY, u"File:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )
		
		fgSizer28.Add( self.m_staticText23, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.textCtrl_FileConnect = wx.TextCtrl( self.panel_Notify, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer28.Add( self.textCtrl_FileConnect, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		fgSizer38.Add( fgSizer28, 1, wx.EXPAND, 5 )
		
		
		fgSizer37.Add( fgSizer38, 1, wx.EXPAND, 5 )
		
		self.button_FileConnect = wx.Button( self.panel_Notify, wx.ID_ANY, u"Browse", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer37.Add( self.button_FileConnect, 0, wx.ALIGN_BOTTOM|wx.ALL, 5 )
		
		
		fgSizer_Notify.Add( fgSizer37, 1, wx.EXPAND, 5 )
		
		self.m_staticline2 = wx.StaticLine( self.panel_Notify, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer_Notify.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.staticText_Disconnect = wx.StaticText( self.panel_Notify, wx.ID_ANY, u"Disconnect notification", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_Disconnect.Wrap( -1 )
		
		self.staticText_Disconnect.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		
		fgSizer_Notify.Add( self.staticText_Disconnect, 0, wx.ALL, 5 )
		
		fgSizer39 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer39.AddGrowableCol( 0 )
		fgSizer39.SetFlexibleDirection( wx.BOTH )
		fgSizer39.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer40 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer40.AddGrowableCol( 0 )
		fgSizer40.SetFlexibleDirection( wx.BOTH )
		fgSizer40.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer33 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer33.AddGrowableCol( 0 )
		fgSizer33.AddGrowableCol( 1 )
		fgSizer33.SetFlexibleDirection( wx.BOTH )
		fgSizer33.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.checkBox_PlayDisconnect = wx.CheckBox( self.panel_Notify, wx.ID_ANY, u"Play on speaker", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer33.Add( self.checkBox_PlayDisconnect, 0, wx.ALL, 5 )
		
		self.checkBox_RecordDisconnect = wx.CheckBox( self.panel_Notify, wx.ID_ANY, u"Record to file", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer33.Add( self.checkBox_RecordDisconnect, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		fgSizer40.Add( fgSizer33, 1, wx.EXPAND, 5 )
		
		fgSizer281 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer281.AddGrowableCol( 1 )
		fgSizer281.SetFlexibleDirection( wx.BOTH )
		fgSizer281.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText24 = wx.StaticText( self.panel_Notify, wx.ID_ANY, u"File:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )
		
		fgSizer281.Add( self.m_staticText24, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.textCtrl_FileDisconnect = wx.TextCtrl( self.panel_Notify, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer281.Add( self.textCtrl_FileDisconnect, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		fgSizer40.Add( fgSizer281, 1, wx.EXPAND, 5 )
		
		
		fgSizer39.Add( fgSizer40, 1, wx.EXPAND, 5 )
		
		self.button_FileDisconnect = wx.Button( self.panel_Notify, wx.ID_ANY, u"Browse", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer39.Add( self.button_FileDisconnect, 0, wx.ALIGN_BOTTOM|wx.ALL, 5 )
		
		
		fgSizer_Notify.Add( fgSizer39, 1, wx.EXPAND, 5 )
		
		
		self.panel_Notify.SetSizer( fgSizer_Notify )
		self.panel_Notify.Layout()
		fgSizer_Notify.Fit( self.panel_Notify )
		fgSizer_NotifyWidgets.Add( self.panel_Notify, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		fgSizer_Settings.Add( fgSizer_NotifyWidgets, 1, wx.EXPAND, 5 )
		
		self.m_staticline4 = wx.StaticLine( self.m_scrolledWindow_Settings, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer_Settings.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )
		
		fgSizer_BottomWidgets = wx.FlexGridSizer( 0, 4, 0, 0 )
		fgSizer_BottomWidgets.AddGrowableCol( 1 )
		fgSizer_BottomWidgets.SetFlexibleDirection( wx.BOTH )
		fgSizer_BottomWidgets.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.button_Save = wx.Button( self.m_scrolledWindow_Settings, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer_BottomWidgets.Add( self.button_Save, 0, wx.ALL, 5 )
		
		self.checkBox_Autosave = wx.CheckBox( self.m_scrolledWindow_Settings, wx.ID_ANY, u"Autosave on quit", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer_BottomWidgets.Add( self.checkBox_Autosave, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.button_Cancel = wx.Button( self.m_scrolledWindow_Settings, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer_BottomWidgets.Add( self.button_Cancel, 0, wx.ALL, 5 )
		
		self.button_OK = wx.Button( self.m_scrolledWindow_Settings, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer_BottomWidgets.Add( self.button_OK, 0, wx.ALL, 5 )
		
		
		fgSizer_Settings.Add( fgSizer_BottomWidgets, 1, wx.EXPAND, 5 )
		
		
		self.m_scrolledWindow_Settings.SetSizer( fgSizer_Settings )
		self.m_scrolledWindow_Settings.Layout()
		fgSizer_Settings.Fit( self.m_scrolledWindow_Settings )
		fgSizer24.Add( self.m_scrolledWindow_Settings, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( fgSizer24 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.button_RecorderPath.Bind( wx.EVT_BUTTON, self.click_recorderpath )
		self.button_FileRoger.Bind( wx.EVT_BUTTON, self.click_fileroger )
		self.button_FileConnect.Bind( wx.EVT_BUTTON, self.click_fileconnect )
		self.button_FileDisconnect.Bind( wx.EVT_BUTTON, self.click_filedisconnect )
		self.button_Save.Bind( wx.EVT_BUTTON, self.click_save )
		self.button_Cancel.Bind( wx.EVT_BUTTON, self.click_cancel )
		self.button_OK.Bind( wx.EVT_BUTTON, self.click_ok )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def click_recorderpath( self, event ):
		event.Skip()
	
	def click_fileroger( self, event ):
		event.Skip()
	
	def click_fileconnect( self, event ):
		event.Skip()
	
	def click_filedisconnect( self, event ):
		event.Skip()
	
	def click_save( self, event ):
		event.Skip()
	
	def click_cancel( self, event ):
		event.Skip()
	
	def click_ok( self, event ):
		event.Skip()
	

