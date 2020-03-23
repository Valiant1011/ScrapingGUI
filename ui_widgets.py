from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPalette, QColor, QPixmap
from PyQt5.QtCore import *

# This class creates pages for the setup wizard, based on the page id given to it.
class wizard_page(QWizardPage):
	def __init__(self, page_id = 1, parent=None):
		super(wizard_page, self).__init__(parent)
		# Based on page_id, return the corresponding widget
		if page_id == 1:
			self.main_widget = self.page1()
		elif page_id == 2:
			self.main_widget = self.page2()
		elif page_id == 3:
			self.main_widget = self.page3()
		
		self.top_layout = QVBoxLayout()
		self.top_layout.addWidget(self.main_widget)
		self.top_layout.setStretch(0, 100)
		self.setLayout(self.top_layout)

	def page1(self):
		self.title_label = QLabel('Upload File')
		self.title_label.setObjectName('main_screen_heading')

		self.file_location_label = QLabel('File Location: ')
		self.file_location_label.setObjectName('main_screen_sub_heading')
		self.path_entry = QLineEdit()
		self.path_entry.setPlaceholderText('Enter file path (.xlsx files only)')
		self.path_entry.setFixedSize(350, 40)
		self.registerField("Path", self.path_entry)
		self.browse_button = QPushButton('...')
		self.browse_button.setFixedSize(40, 40)
		self.browse_button.clicked.connect(
			self.browse_manager
		)
		self.browse_button.setToolTip('Browse for file.')
		self.path_entry_layout = QHBoxLayout()
		self.path_entry_layout.addWidget(self.file_location_label)
		self.path_entry_layout.addWidget(self.path_entry)
		self.path_entry_layout.addWidget(self.browse_button)
		self.path_entry_layout.addStretch(50)
		self.path_entry_widget = QWidget()
		self.path_entry_widget.setLayout(self.path_entry_layout)

		self.starting_point_label = QLabel('Start Point:  ')
		self.starting_point_label.setObjectName('main_screen_sub_heading')
		self.starting_point_entry = QLineEdit()
		self.starting_point_entry.setFixedSize(150, 40)
		self.registerField("StartingPoint", self.starting_point_entry)
		self.ending_point_label = QLabel('End Point: ')
		self.ending_point_label.setObjectName('main_screen_sub_heading')
		self.ending_point_entry = QLineEdit()
		self.ending_point_entry.setFixedSize(150, 40)
		self.registerField("EndingPoint", self.ending_point_entry)
		self.points_widget = QWidget()
		self.points_layout = QHBoxLayout(self.points_widget)
		self.points_layout.addWidget(self.starting_point_label)
		self.points_layout.addWidget(self.starting_point_entry)
		self.points_layout.addStretch(1)
		self.points_layout.addWidget(self.ending_point_label)
		self.points_layout.addWidget(self.ending_point_entry)
		self.points_layout.addStretch(1)

		self.sheet_index_label = QLabel('Sheet Index: ')
		self.sheet_index_label.setObjectName('main_screen_sub_heading')
		self.sheet_index_entry = QLineEdit()
		self.sheet_index_entry.setFixedSize(100, 40)
		self.registerField("SheetIndex", self.sheet_index_entry)
		self.sheet_index_widget = self.get_horizontal_widget(
			self.sheet_index_label,
			self.sheet_index_entry
		)

		self.main_widget = QWidget()
		self.main_widget.setObjectName('content_box')
		self.main_layout = QVBoxLayout(self.main_widget)
		self.main_layout.addWidget(self.title_label)
		self.main_layout.addStretch(2)
		self.main_layout.addWidget(self.path_entry_widget)
		self.main_layout.addStretch(1)
		self.main_layout.addWidget(self.points_widget)
		self.main_layout.addStretch(1)
		self.main_layout.addWidget(self.sheet_index_widget)
		self.main_layout.addStretch(2)
		return self.main_widget	

	def page2(self):
		self.whatsapp_logo = QLabel()
		self.whatsapp_logo.setPixmap(QPixmap('Elements/whatsapp.png')) 
		self.caption = QLabel(
			'Scan your QR code on whatsapp web to continue.'
		)
		self.caption.setObjectName('main_screen_content')
		self.faux_entry = QLineEdit()
		self.faux_entry.setFixedSize(0, 0)
		self.registerField("AllowNext*", self.faux_entry)
		# When anything is written to the faux_entry, the next button is enabled.
		self.main_widget = QWidget()
		self.main_widget.setObjectName('content_box')
		self.main_layout = QVBoxLayout(self.main_widget)
		self.main_layout.addWidget(self.faux_entry)
		self.main_layout.addStretch(3)
		self.main_layout.addWidget(self.whatsapp_logo)
		self.main_layout.addStretch(1)
		self.main_layout.addWidget(self.caption)
		self.main_layout.addStretch(3)
		self.main_layout.setAlignment(self.whatsapp_logo, Qt.AlignCenter)
		self.main_layout.setAlignment(self.caption, Qt.AlignCenter)
		return self.main_widget

	def page3(self):
		self.title_label = QLabel('Status')
		self.title_label.setObjectName('main_screen_heading')
		headers = ['Number', 'Message', 'Status']
		self.main_table = QTableWidget()
		self.main_table.setColumnCount(3)
		self.main_table.setRowCount(0)
		self.main_table.setHorizontalHeaderLabels(headers)
		self.main_table.resizeColumnsToContents()
		self.main_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.main_table.setAlternatingRowColors(True)
		self.main_table.setSelectionBehavior(QAbstractItemView.SelectRows)
		self.main_table.setSelectionMode(QAbstractItemView.SingleSelection)
		self.main_table.setSortingEnabled(False)
		vertical_header = self.main_table.verticalHeader()
		vertical_header.setVisible(False)
		horizontal_header = self.main_table.horizontalHeader()
		horizontal_header.setSectionResizeMode(QHeaderView.Stretch)
		self.main_widget = QWidget()
		self.main_widget.setObjectName('content_box')
		self.main_layout = QVBoxLayout(self.main_widget)
		self.main_layout.addWidget(self.title_label)
		self.main_layout.addWidget(self.main_table)
		return self.main_widget

	def get_horizontal_widget(self, widget_1, widget_2):
		layout = QHBoxLayout()
		layout.addWidget(widget_1)
		layout.addWidget(widget_2)
		layout.addStretch(1)
		widget = QWidget()
		widget.setLayout(layout)
		return widget


	def browse_manager(self):
		file_name = ''
		file_name = QFileDialog.getOpenFileName(
			self,
			"Open File", 
			"./", 
			"Excel Docs (*.xlsx)"
		)
		self.path_entry.setText(file_name[0])