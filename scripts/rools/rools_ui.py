import sys
import importlib
from PySide2.QtCore import (
    QSize, 
    Qt,
    QTimer
)
    
from PySide2.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QWidget,
    QSizePolicy,
    QDockWidget,
    QHBoxLayout,
    QVBoxLayout, 
    QPushButton,
    QListWidget,
    QTabWidget,
    QSlider,
    QDial
)

from PySide2.QtGui import QPalette, QColor, QFont, QFontMetrics
import maya.cmds as mc
import maya.mel as mel
import math
sys.path.append("P:\Glasses\Preproduction\Glasses_Tools\scripts")
from scripts.glasses_tools import rools_utils as glutils
from scripts.glasses_tools import rools_widget_functions as glwidgetfuncs
importlib.reload(glutils)
importlib.reload(glwidgetfuncs)

class Rools(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()

        # Naming and Sizing
        self.window_name = "Glasses Tools"
        self.setWindowTitle(self.window_name)
        self.setFixedSize(QSize(800,600))
        self.setMinimumSize(QSize(800,600))
        self.setMaximumSize(QSize(1200,800))
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        # Make sure only one window
        if mc.window(self.window_name, ex = True):
            mc.deleteUI(self.window_name)

        # Initial setup
        self.master_widget = QWidget()
        self.master_layout = QHBoxLayout(self.master_widget)
        self.master_tab = QTabWidget()
        self.master_layout.addWidget(self.master_tab)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.is_list_one_selected)
        self.timer.start(10)

        # Tab one
        self.tab_one_widget = QWidget()
        self.master_tab_one_layout = QHBoxLayout(self.tab_one_widget)
    
        # Tab one, layout one
        self.tab_one_layout_one = QVBoxLayout(self.tab_one_widget)
        self.master_tab_one_layout.addLayout(self.tab_one_layout_one)
        self.retransform_asset_button = QPushButton("Retransform Asset")
        self.center_selection_button = QPushButton("Center Selection")
        self.realign_asset_button = QPushButton("Realign Asset")
        self.realign_asset_button.setEnabled(False)
        self.rotate_ninety_button = QPushButton("Rotate 90")

        self.retransform_asset_button.clicked.connect(self.retransform_asset_button_clicked)
        self.center_selection_button.clicked.connect(self.center_selection_button_clicked)
        self.realign_asset_button.clicked.connect(self.realign_asset_button_clicked)
        self.rotate_ninety_button.clicked.connect(self.rotate_ninety_button_clicked)
        
        self.edges_list = QListWidget()
        self.edges_list.SelectionMode(1)
        
        self.tab_one_layout_one.addSpacing(10)
        self.tab_one_layout_one.addWidget(self.retransform_asset_button)
        self.tab_one_layout_one.addWidget(self.edges_list)
        self.tab_one_layout_one.addWidget(self.center_selection_button)
        self.tab_one_layout_one.addWidget(self.realign_asset_button)
        self.tab_one_layout_one.addWidget(self.rotate_ninety_button)
        self.tab_one_layout_one.addSpacing(50)

        # Tab one, layout two
        self.tab_one_layout_two = QVBoxLayout()
        self.master_tab_one_layout.addLayout(self.tab_one_layout_two)
        self.horizontal_dummy_one = QWidget()
        self.horizontal_dummy_two = QWidget()
        self.horizontal_dummy_three = QWidget()
        self.horizontal_one = QHBoxLayout(self.horizontal_dummy_one)
        self.horizontal_two = QHBoxLayout(self.horizontal_dummy_two)
        self.horizontal_three = QHBoxLayout(self.horizontal_dummy_three)

        self.variable_list = glutils.make_variables_for_instancing('vertical_dummy', 3)
        for self.var in self.variable_list:
            self.widget = QWidget()
            self.var = QVBoxLayout(self.widget)
            # self.var.setAlignment(Qt.AlignCenter)
            self.horizontal_one.addWidget(self.widget)

            self.dial = QDial()
            self.dial.setNotchTarget(0.0)
            self.dial.setNotchesVisible(True)
            self.dial.setRange(1,20)
            self.dial.setValue(50)

            self.slider = QSlider(Qt.Horizontal)
            self.slider.setMinimum(0)
            self.slider.setMaximum(100)
            self.slider.setValue(20)
            self.slider.setTickPosition(QSlider.TicksBelow)
            self.slider.setTickInterval(100)
            # self.button.setFixedSize(50,50)z
            # self.button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            # self.font = self.button.font()
            # self.font_metrics = QFontMetrics(self.font)
            # self.font_width = self.font_metrics.width(self.button.text())
            # self.font_height = self.font_metrics.height()
            # self.button.setMinimumSize(self.font_width, self.font_height)
            # self.button.setMaximumSize(self.font_width*2, self.font_height*2)
            # self.button.adjustSize()

            self.var.addWidget(self.dial)
            self.var.addWidget(self.slider)

        self.variable_list = glutils.make_variables_for_instancing('vertical_dummy', 3)
        for self.var in self.variable_list:
            self.widget = QWidget()
            self.var = QVBoxLayout(self.widget)
            self.horizontal_two.addWidget(self.widget)

            self.dial = QDial()
            self.dial.setNotchesVisible(True)
            self.dial.setRange(1,20)
            self.dial.setValue(50)

            self.button = QPushButton("Test")

            self.var.addWidget(self.dial)
            self.var.addWidget(self.button)

        self.variable_list = glutils.make_variables_for_instancing('vertical_dummy', 3)
        for self.var in self.variable_list:
            self.widget = QWidget()
            self.var = QVBoxLayout(self.widget)
            self.horizontal_three.addWidget(self.widget)

            self.dial = QDial()
            self.dial.setNotchesVisible(True)
            self.dial.setRange(1,20)
            self.dial.setValue(50)

            self.button = QPushButton("Test")

            self.var.addWidget(self.dial)
            self.var.addWidget(self.button)

        self.button_four = QPushButton("Button Four")
        self.button_five = QPushButton("Button Five")

        self.tab_one_layout_two.addWidget(self.horizontal_dummy_one)
        self.tab_one_layout_two.addWidget(self.horizontal_dummy_two)
        self.tab_one_layout_two.addWidget(self.horizontal_dummy_three)

        # Tab two
        self.tab_two_widget = QWidget()
        self.master_tab_two_layout = QHBoxLayout(self.tab_two_widget)

        # Parening
        self.master_tab.addTab(self.tab_one_widget, "Asset Adjust")
        self.master_tab.addTab(self.tab_two_widget, "Pack and Ship")
        self.master_tab_one_layout.setStretchFactor(self.tab_one_layout_one, 1)
        self.master_tab_one_layout.setStretchFactor(self.tab_one_layout_two, 5)        
        self.setCentralWidget(self.master_widget)
        self.setLayout(self.master_layout)

    # Funcs
    def is_list_one_selected(self):
        if self.edges_list.selectedItems():
            self.realign_asset_button.setEnabled(True)
        else:
            self.realign_asset_button.setEnabled(False)

    def retransform_asset_button_clicked(self):
        cur_sel = mc.ls(sl=True)
        glwidgetfuncs.retransform_asset(cur_sel, self.edges_list)  

    def center_selection_button_clicked(self):
        cur_sel = mc.ls(sl=True)
        glwidgetfuncs.center_selection(cur_sel)

    def realign_asset_button_clicked(self):
        glwidgetfuncs.realign_asset(self.edges_list)

    def rotate_ninety_button_clicked(self):
        cur_sel = mc.ls(sl=True)[0]
        if '.' in cur_sel:
            mc.select(cl=True)
            cur_sel = mc.select(cur_sel.split('.'))[0]
            cur_sel = mc.ls(sl=True)[0]
        glwidgetfuncs.rotate_ninety(cur_sel)