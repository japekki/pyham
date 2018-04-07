#!/usr/bin/python

# TODO:
# - CLI client without wxWidgets GUI

import wx

from log import log
from client_gui import Mainwindow
from client_gui import Settingswindow
from config import Config

class Client():
	def __init__(self, filename_config):
		self.filename_config = filename_config

		# Create wxwidgets application:
		#self.app = wx.App(self)	# With separate log console window
		self.app = wx.App(None)		# Without separate log console window
		self.mainwindow = Mainwindow(parent=None)

		# Read configuration:
		self.config = Config()
		self.config.load(filename_config)
		self.mainwindow.comboBox_Preset.Append(self.config.parameters["autoconnect_preset"])

		# TODO:
		# Update parameters in mainwindow:
		# mainwindow.comboBox_Room = self.config.parameters[room]
		self.mainwindow.textCtrl_Callsign.SetValue(self.config.parameters["callsign"])
		self.mainwindow.textCtrl_Description.SetValue(self.config.parameters["description"])
		# mainwindow.choice_Speaker = self.config.parameters[device_speaker]
		# mainwindow.choice_Mic = self.config.parameters[device_mic]

		# Get available sound devices:
			# get_audiodevices()
		# Put them into choice widgets:
			# self.mainwindow.choice_Speaker.Append()
			# self.mainwindow.choice_Mic.Append()

		# Update parameters in settingswindow:
		# settingswindow.choise_Preset = self.config.parameters[]
		# settingswindow.choise_Room = self.config.parameters[]
		# settingswindow.checkBox_Autosave = self.config.parameters[]
		# settingswindow.choice_Speaker = self.config.parameters[device_speaker]
		# settingswindow.choice_Mic = self.config.parameters[device_mic]

	def run(self):
		log("Starting client.")
		# Show main window:
		self.mainwindow.Show()
		# Execute GUI:
		self.app.MainLoop()

	def connect(self):
		pass
