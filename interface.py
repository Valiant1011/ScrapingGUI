# Special thanks to www.pythonspot.com for this!
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPalette, QColor, QPixmap
from PyQt5.QtCore import *
from ui_widgets import *

class main_window(QWizard):
	def __init__(
			self, 
			available_width, 
			available_height, 
			parent=None
		):
		super(main_window, self).__init__(parent)
		self.setWindowIcon(QIcon('Elements/logo.png'))
		self.setWindowTitle("Web Scraping")
		self.setFixedSize(available_width/2, available_height/2)
	
		self.page1 = wizard_page(1)
		self.addPage(self.page1)
		self.page2 = wizard_page(2)
		self.addPage(self.page2)
		self.page3 = wizard_page(3)
		self.addPage(self.page3)

		self.currentIdChanged.connect(self.page_changed_handler)

	def page_changed_handler(self, page):
		if page == -1:
			print('Cancelled')
		elif page == 0:
			print('Home Page')
		elif page == 1:
			# If you want to enable the Next button on page 2, uncomment this
			# self.page2.layout().itemAt(0).widget().layout().itemAt(0).widget().setText('Pass')

			print('Data entry:')
			print('Path: ', self.field("Path"))
			print('Start Point: ', self.field("StartingPoint"))
			print('Ending Point: ', self.field("EndingPoint"))
			print('Sheet Index: ', self.field("SheetIndex"))

			print('Whatsapp Page')
		elif page == 2:
			table = self.page3.layout().itemAt(0).widget().layout().itemAt(1).widget()
			print('Sheets Page')