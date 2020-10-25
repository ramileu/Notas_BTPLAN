# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Notas_BTPLAN
                                 A QGIS plugin
 Mostra as anotações do BTPlan em Barra de Mesagem.
                              -------------------
        begin                : 2019-09-09
        git sha              : $Format:%H$
        copyright            : (C) 2019 by Eulimar Cunha Tibúrcio
        email                : eulimar.tiburcio@ibge.gov.br
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from PyQt4.QtGui import QAction, QIcon, QFileDialog, QColor, QTreeWidget, QComboBox, QPushButton, QDialog, QToolBar, QDesktopServices
#from PyQt4.QtGui import QDesktopServices
# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
from Notas_BTPLAN_dialog import Notas_BTPLANDialog
import os.path







from qgis.utils import iface









from qgis._core import QgsFillSymbolV2
from qgis.core import QgsVectorLayer, QgsCoordinateReferenceSystem, QgsVectorFileWriter, QgsMapLayerRegistry, QgsLayerTreeLayer, QGis, QgsAction, QgsProject, QgsLayerTreeGroup, QgsSimpleMarkerSymbolLayerBase, QgsPoint, QCoreApplication
from qgis.gui import QgsMessageBar, QgsMapTip
from PyQt4.QtCore import *






from PyQt4.QtGui import *







import os, sys, time
reload(sys)
sys.setdefaultencoding('utf-8')
import csv
import textwrap 
from PyQt4 import QtGui, QtCore
import codecs

from os import startfile
import functools

from shutil import copyfile
from sys import exit
from win32api import GetSystemMetrics

bgMT = ["#f1f1f1"]
lpit = "</div>"
cs = []
cbT = []
cbC = []
le = []
pb = []
cont_cl = [0]
MT = [False]
P = [True]
lb2 =[]
result = []

l_Tons = ["Tons e gama de Cinza", "Tons e gama de Pastel", "Tons e gama de Ciano", "Tons e gama de Verde", "Tons e gama de Marrom", "Tons e gama de Roxo", "Tons e gama de Rosa", "Tons e gama de Vermelho", "Tons e gama de Laranja", "Tons e gama de Amarelo", "Tons e gama de Azul"]
l_Color0 = ["Silver", "LightGrey", "Gainsboro", "White"]
l_Color1 = ["MintCream", "Honeydew", "PaleTurquoise", "PowderBlue", "LightCyan", "Azure", "Thistle", "Lavender", "LavenderBlush", "MistyRose", "PaleGoldenrod", "Moccasin", "PeachPuff", 
			"PapayaWhip", "LightGoldenrodYellow", "LemonChiffon", "LightYellow", "Bisque", "BlanchedAlmond", "AntiqueWhite", "Cornsilk", "Linen", "Ivory", "OldLace", "Beige", 
			"WhiteSmoke", "FloralWhite", "Seashell", "Snow", "GhostWhite", "AliceBlue"]
l_Color2 = ["MediumAquamarine", "Aquamarine", "MediumTurquoise", "Turquoise", "DarkTurquoise", "Aqua / Cyan"]
l_Color3 = ["GreenYellow", "Chartreuse", "LightGreen", "PaleGreen", "SpringGreen", "MediumSpringGreen"]
l_Color4 = ["Tan", "BurlyWood", "Wheat", "NavajoWhite", "SandyBrown", "Goldenrod"]
l_Color5 = ["Plum", "Orchid", "Violet", "Fuchsia / Magenta"]
l_Color6 = ["LightCoral", "Pink", "LightPink"]
l_Color7 = ["LightSalmon", "DarkSalmon", "Salmon"]
l_Color8 = ["Orange", "DarkOrange"]
l_Color9 = ["Khaki", "Yellow", "Gold"]
l_Color10 = ["LightSteelBlue", "LightBlue", "SkyBlue", "LightSkyBlue"]
d_Color0 = {'Silver': '#C0C0C0','LightGrey': '#D3D3D3', 'Gainsboro': '#f1f1f1', 'White': '#FFFFFF'}
d_Color1 = {'MintCream': '#F5FFFA', 'Honeydew': '#F0FFF0', 'PaleTurquoise': '#E0FFFF', 'PowderBlue': '#B0E0E6', 'LightCyan': '#E0FFFF', 'Azure': '#F0FFFF', 'Thistle': '#D8BFD8',
			'Lavender': '#E6E6FA', 'LavenderBlush': '#FFF0F5', 'MistyRose': '#FFE4E1', 'PaleGoldenrod': '#EEE8AA', 'Moccasin': '#FFE4B5', 'PeachPuff': '#FFDAB9', 'PapayaWhip': '#FFEFD5',
			'LightGoldenrodYellow': '#FAFAD2', 'LemonChiffon': '#FFFACD', 'LightYellow': '#FFFFE0', 'Bisque': '#FFE4C4', 'BlanchedAlmond': '#FFEBCD', 'AntiqueWhite': '#FAEBD7',
			'Cornsilk': '#FFF8DC', 'Linen': '#FAF0E6', 'Ivory': '#FFFFF0', 'OldLace': '#FDF5E6', 'Beige': '#F5F5DC', 'WhiteSmoke': '#F5F5F5', 'FloralWhite': '#FFFAF0',
			'Seashell': '#FFF5EE', 'Snow': '#FFFAFA', 'GhostWhite': '#F8F8FF', 'AliceBlue': '#F0F8FF'}
d_Color2 = {'MediumAquamarine': '#66CDAA', 'Aquamarine': '#7FFFD4', 'MediumTurquoise': '#48D1CC', 'Turquoise': '#40E0D0', 'DarkTurquoise': '#00CED1', 'Aqua / Cyan': '#00FFFF'}
d_Color3 = {'GreenYellow': '#ADFF2F', 'Chartreuse': '#7FFF00', 'LightGreen': '#90EE90', 'PaleGreen': '#98FB98', 'SpringGreen': '#00FF7F', 'MediumSpringGreen': '#00FA9A'}
d_Color4 = {'Tan': '#D2B48C', 'BurlyWood': '#DEB887', 'Wheat': '#F5DEB3', 'NavajoWhite': '#FFDEAD', 'SandyBrown': '#F4A460', 'Goldenrod': '#DAA520'}
d_Color5 = {'Plum': '#DDA0DD', 'Orchid': '#DA70D6', 'Violet': '#EE82EE', 'Fuchsia / Magenta': '#FF00FF'}
d_Color6 = {'LightCoral': '#F08080', 'Pink': '#FFC0CB', 'LightPink': '#FFB6C1'}
d_Color7 = {'LightSalmon': '#FFA07A', 'DarkSalmon': '#E9967A', 'Salmon': '#FA8072'}
d_Color8 = {'Orange': '#FFA500', 'DarkOrange': '#FF8C00'}
d_Color9 = {'Khaki': '#F0E68C', 'Yellow': '#FFFF00', 'Gold': '#FFD700'}
d_Color10 = {'LightSteelBlue': '#B0C4DE', 'LightBlue': '#ADD8E6', 'SkyBlue': '#87CEEB', 'LightSkyBlue': '#87CEFA'}
infoAdd = ""
fields = [] 
rows = [] 
index_1 = "0"
index_2 = "0"
add = "N"
folder = ""

def resolve(name, basepath=None):
	if not basepath:
		basepath = os.path.dirname(os.path.realpath(__file__))
	return os.path.join(basepath, name)

def createMapTips( self ):
    """ Create MapTips on the map """
    self.timerMapTips = QTimer( self.canvas )
    self.mapTip = QgsMapTip()
    self.connect( self.canvas, SIGNAL( "xyCoordinates(const QgsPoint&)" ),
        self.mapTipXYChanged )
    self.connect( self.timerMapTips, SIGNAL( "timeout()" ),
        self.showMapTip )

def mapTipXYChanged( self, p ):
    """ SLOT. Initialize the Timer to show MapTips on the map """
    if self.canvas.underMouse(): # Only if mouse is over the map
        # Here you could check if your custom MapTips button is active or sth
        self.lastMapPosition = QgsPoint( p.x(), p.y() )
        self.mapTip.clear( self.canvas )
        self.timerMapTips.start( 750 ) # time in milliseconds

def showMapTip( self ):
    """ SLOT. Show  MapTips on the map """
    self.timerMapTips.stop()

    if self.canvas.underMouse(): 
        # Here you could check if your custom MapTips button is active or sth
        pointQgs = self.lastMapPosition
        pointQt = self.canvas.mouseLastXY()
        self.mapTip.showMapTip( self.layer, pointQgs, pointQt,
            self.canvas )
	
def run_explan():
	startfile(resolve('help/icons/explan.mp4'))

def populate_cbColors( self ):
	if cbT[0].currentText() == "Tons e gama de Cinza":
		cbC[0].clear()
		cbC[0].addItems(l_Color0)
	elif cbT[0].currentText() == "Tons e gama de Pastel":
		cbC[0].clear()
		cbC[0].addItems(l_Color1)	
	elif cbT[0].currentText() == "Tons e gama de Ciano":
		cbC[0].clear()
		cbC[0].addItems(l_Color2)
	elif cbT[0].currentText() == "Tons e gama de Verde":
		cbC[0].clear()
		cbC[0].addItems(l_Color3)
	elif cbT[0].currentText() == "Tons e gama de Marrom":
		cbC[0].clear()
		cbC[0].addItems(l_Color4)
	elif cbT[0].currentText() == "Tons e gama de Roxo":
		cbC[0].clear()
		cbC[0].addItems(l_Color5)
	elif cbT[0].currentText() == "Tons e gama de Rosa":
		cbC[0].clear()
		cbC[0].addItems(l_Color6)
	elif cbT[0].currentText() == "Tons e gama de Vermelho":
		cbC[0].clear()
		cbC[0].addItems(l_Color7)
	elif cbT[0].currentText() == "Tons e gama de Laranja":
		cbC[0].clear()
		cbC[0].addItems(l_Color8)
	elif cbT[0].currentText() == "Tons e gama de Amarelo":
		cbC[0].clear()
		cbC[0].addItems(l_Color9)
	elif cbT[0].currentText() == "Tons e gama de Azul":
		cbC[0].clear()
		cbC[0].addItems(l_Color10)

def le_style( self ):
	if cbT[0].currentText() == "Tons e gama de Cinza":
		for k, v in d_Color0.items():
			if cbC[0].currentText() == k:
				le[0].setStyleSheet("background-color: " + v + "; font: 10pt \"Times New Roman\"; color: #000000;")
				bgMT[0] = v
	elif cbT[0].currentText() == "Tons e gama de Pastel":
		for k, v in d_Color1.items():
			if cbC[0].currentText() == k:
				le[0].setStyleSheet("background-color: " + v + "; font: 10pt \"Times New Roman\"; color: #000000;")
				bgMT[0] = v
	elif cbT[0].currentText() ==  "Tons e gama de Ciano":
		for k, v in d_Color2.items():
			if cbC[0].currentText() == k:
				le[0].setStyleSheet("background-color: " + v + "; font: 10pt \"Times New Roman\"; color: #000000;")
				bgMT[0] = v
	elif cbT[0].currentText() == "Tons e gama de Verde":
		for k, v in d_Color3.items():
			if cbC[0].currentText() == k:
				le[0].setStyleSheet("background-color: " + v + "; font: 10pt \"Times New Roman\"; color: #000000;")
				bgMT[0] = v
	elif cbT[0].currentText() == "Tons e gama de Marrom":
		for k, v in d_Color4.items():
			if cbC[0].currentText() == k:
				le[0].setStyleSheet("background-color: " + v + "; font: 10pt \"Times New Roman\"; color: #000000;")
				bgMT[0] = v
	elif cbT[0].currentText() == "Tons e gama de Roxo":
		for k, v in d_Color5.items():
			if cbC[0].currentText() == k:
				le[0].setStyleSheet("background-color: " + v + "; font: 10pt \"Times New Roman\"; color: #000000;")
				bgMT[0] = v
	elif cbT[0].currentText() == "Tons e gama de Rosa":
		for k, v in d_Color6.items():
			if cbC[0].currentText() == k:
				le[0].setStyleSheet("background-color: " + v + "; font: 10pt \"Times New Roman\"; color: #000000;")
				bgMT[0] = v
	elif cbT[0].currentText() == "Tons e gama de Vermelho":
		for k, v in d_Color7.items():
			if cbC[0].currentText() == k:
				le[0].setStyleSheet("background-color: " + v + "; font: 10pt \"Times New Roman\"; color: #000000;")
				bgMT[0] = v
	elif cbT[0].currentText() == "Tons e gama de Laranja":
		for k, v in d_Color8.items():
			if cbC[0].currentText() == k:
				le[0].setStyleSheet("background-color: " + v + "; font: 10pt \"Times New Roman\"; color: #000000;")
				bgMT[0] = v
	elif cbT[0].currentText() == "Tons e gama de Amarelo":
		for k, v in d_Color9.items():
			if cbC[0].currentText() == k:
				le[0].setStyleSheet("background-color: " + v + "; font: 10pt \"Times New Roman\"; color: #000000;")
				bgMT[0] = v
	elif cbT[0].currentText() == "Tons e gama de Azul":
		for k, v in d_Color10.items():
			if cbC[0].currentText() == k:
				le[0].setStyleSheet("background-color: " + v + "; font: 10pt \"Times New Roman\"; color: #000000;")
				bgMT[0] = v

def zera(): 
	global cont_cl, MT
	cont_cl[0] = 1 
	MT[0] = False
	P[0] = True
	
def pb_RedW():
	global pb, cont_cl, MT
	
	icon1 = QIcon(resolve('help/icons/unchecked.png'))
	icon2 = QIcon(resolve('help/icons/checked.png'))
	
	comp = cont_cl[0]
	if comp == 1:
		pb[0].setIcon(icon2)
		pb[0].setIconSize(QtCore.QSize(16, 16))
		cont_cl[0] = 0
		MT[0] = True
		
		cs[0].setMinimumSize(1290, 220)
		cs[0].setMaximumSize(1290, 220)
		cs[0].resize(1290, 220)
		
		frameGm = cs[0].frameGeometry()
		screen = QtGui.QApplication.desktop().screenNumber(QtGui.QApplication.desktop().cursor().pos())
		centerPoint = QtGui.QApplication.desktop().screenGeometry(screen).center()
		frameGm.moveCenter(centerPoint)
		cs[0].move(frameGm.topLeft())
		
		cs[0].show()	
	elif comp == 0:
		pb[0].setIcon(icon1)
		pb[0].setIconSize(QtCore.QSize(16, 16))
		cont_cl[0] = 1
		MT[0] = False
		
		cs[0].setMinimumSize(1030, 220)
		cs[0].setMaximumSize(1030, 220)
		cs[0].resize(1030, 220)
		
		frameGm = cs[0].frameGeometry()
		screen = QtGui.QApplication.desktop().screenNumber(QtGui.QApplication.desktop().cursor().pos())
		centerPoint = QtGui.QApplication.desktop().screenGeometry(screen).center()
		frameGm.moveCenter(centerPoint)
		cs[0].move(frameGm.topLeft())
		
		cs[0].show()
		
				
def lb_D_RedW(self):
	global pb, cont_cl, MT
	
	icon1 = QIcon(resolve('help/icons/unchecked.png'))
	icon2 = QIcon(resolve('help/icons/checked.png'))
		
	comp = cont_cl[0]
	if comp == 1:
		pb[0].setIcon(icon2)
		pb[0].setIconSize(QtCore.QSize(16, 16))
		cont_cl[0] = 0
		MT[0] = True
		
		cs[0].setMinimumSize(1290, 220)
		cs[0].setMaximumSize(1290, 220)
		cs[0].resize(1290, 220)
		
		frameGm = cs[0].frameGeometry()
		screen = QtGui.QApplication.desktop().screenNumber(QtGui.QApplication.desktop().cursor().pos())
		centerPoint = QtGui.QApplication.desktop().screenGeometry(screen).center()
		frameGm.moveCenter(centerPoint)
		cs[0].move(frameGm.topLeft())
		
		cs[0].show()
		
	elif comp == 0:
		pb[0].setIcon(icon1)
		pb[0].setIconSize(QtCore.QSize(16, 16))
		cont_cl[0] = 1
		MT[0] = False
		
		cs[0].setMinimumSize(1030, 220)
		cs[0].setMaximumSize(1030, 220)
		cs[0].resize(1030, 220)
		
		frameGm = cs[0].frameGeometry()
		screen = QtGui.QApplication.desktop().screenNumber(QtGui.QApplication.desktop().cursor().pos())
		centerPoint = QtGui.QApplication.desktop().screenGeometry(screen).center()
		frameGm.moveCenter(centerPoint)
		cs[0].move(frameGm.topLeft())
		
		cs[0].show()
	
def lb_P_customize(self):	
	global P, cbT, cbC, lb2

	icon1 = QIcon(resolve('help/icons/unchecked.png'))
	icon2 = QIcon(resolve('help/icons/checked.png'))

	if P[0] == True:
		cbT[0].setEnabled(True)
		cbC[0].setEnabled(True)
				
		pb[1].setIcon(icon1)
		pb[1].setIconSize(QtCore.QSize(16, 16))
		
		P[0] = False
		
		movie = QtGui.QMovie(resolve('help/icons/preview.gif'))
		lb2[0].setMovie(movie)
		movie.start()
	else:
		cbT[0].setEnabled(False)
		cbC[0].setEnabled(False)
		
		cbT[0].setCurrentIndex(0)
		cbC[0].setCurrentIndex(2)
		le[0].setStyleSheet("background-color: #f1f1f1; font: 10pt \"Times New Roman\"; color: #000000;")
		
		pb[1].setIcon(icon2)
		pb[1].setIconSize(QtCore.QSize(16, 16))
		
		P[0] = True
		
		movie = QtGui.QMovie(resolve('help/icons/preview.gif'))
		lb2[0].setText(u'Pré-visualização:')
		movie.stop()	

def example(self):
    source = resolve('help/example/Material de exemplo.zip')
    projeto = QgsProject.instance()
    projetoPath = os.path.dirname(projeto.fileName())
    folder2 = QFileDialog.getExistingDirectory(None,"Selecione a pasta que vai armazenar o material de exemplo.",projetoPath)
    target = folder2 + '/Material de exemplo.zip'
    # adding exception handling
    try:
        copyfile(source, target)
    except IOError as e:
        print("Unable to copy file. %s" % e)
        exit(1)
    except:
        print("Unexpected error:", sys.exc_info())
        exit(1)



    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText(u'O arquivo ' + '\"Material de exemplo.zip\"' + ' foi copiado para a pasta\n' + folder2)
    msg.setWindowTitle(u"Material usado no vídeo ilustrativo")
    msg.setWindowIcon( QtGui.QIcon(resolve('help/icons/icon.png')) )
    msg.setStandardButtons(QMessageBox.Ok)
    msg.setDefaultButton(QMessageBox.Ok)
    msg.setEscapeButton(QMessageBox.Ok)
    msg.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    returnValue = msg.exec_()
    
def showdialog(folder):
    global infoAdd
    global fields
    global rows
    global index_1
    global index_2
    global add
    del rows[:]
    msg = QMessageBox()
    
    msg.setIcon(QMessageBox.Question)

    msg.setText(u"Deseja adicionar alguma informação para as camadas de anotação ?")
    msg.setWindowTitle(u"Informação adicional")
    msg.setWindowIcon( QtGui.QIcon(resolve('help/icons/icon.png')) )
    msg.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
    msg.setDefaultButton(QMessageBox.Cancel)
    msg.setEscapeButton(QMessageBox.Cancel)
    msg.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    returnValue = msg.exec_()
    if returnValue == QMessageBox.Ok:
        fname = QFileDialog.getOpenFileName(None, "Abrir planilha CSV", 'c:\\',u"Valores separados por vírgula (*.csv)")
        if fname != "":
            # reading csv file 
            with open(fname, 'r') as csvfile: 
                # creating a csv reader object 
                csvreader = csv.reader(csvfile) 
                  
                # extracting field names through first row 
                fields = next(csvreader) 
              
                # extracting each data row one by one 
                for row in csvreader: 
                    rows.append(row) 
              

            
            index_1, index_2, ok = QInputDialog.getFields(None,u'Informação adicional', "")
            if ok: 
                add = "Y"
                verifica = 0
                caminhos = [os.path.join(folder, nome) for nome in os.listdir(folder)]
                arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
                kmls = [arq for arq in arquivos if arq.lower().endswith(".kml")]
                for nome in kmls:
                    if not os.path.isfile(nome[0:len(nome) -3] + 'shp'):
                        fileroute = nome[0:len(nome) -3] + 'shp'
                        displayName =  nome[0:len(nome) -4].split('\\')[len(nome[0:len(nome) -4].split('\\')) - 1]

                for nome in kmls:
                    if os.path.isfile(nome[0:len(nome) -3] + 'kml'):
                        displayName =  nome[0:len(nome) -4].split('\\')[len(nome[0:len(nome) -4].split('\\')) - 1]
                        for row in rows[:]: 
                            if displayName.split("_")[1] == row[int(index_1)]:
                                verifica+=1

                if verifica == 0:
                        msg2 = QMessageBox()
                        msg2.setIcon(QMessageBox.Warning)
                        msg2.setText(u"Seleção errada do campo de números da anotação\nou nenhum número de anotação corresponde às anotações\nbaixadas em formato KML do BTPlan !!!\n\nTente novamente !")
                        msg2.setWindowTitle(u"Informação adicional")
                        msg2.setWindowIcon( QtGui.QIcon(resolve('help/icons/icon.png')) )
                        msg2.setStandardButtons(QMessageBox.Ok)
                        msg2.setEscapeButton(QMessageBox.Ok)
                        msg2.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
                        returnValue = msg2.exec_()

                        QCoreApplication.processEvents()
                        os.system(cmd)
                        QtCore.QCoreApplication.instance().quit()
            else:
                add = "N"


class _QInputDialog(QDialog):
    """Build a replica interface of QInputDialog.getFields."""
    def __init__(self, parent, title, label, text='', **kwargs):
        super(_QInputDialog, self).__init__(parent, **kwargs)
        if title is not None:
            self.setWindowTitle(title)
        self.setWhatsThis(u"A escolha do formato CSV decorre do fato de que o componente CSV já vem incluído nas distribuições Python, não sendo necessário importar componentes de terceiros!")
        self.setFixedWidth(610)
        self.setFixedHeight(620)
        self.setLayout(QVBoxLayout())
        newfont = QtGui.QFont("Times", 13, QtGui.QFont.Bold) 

        #self.layout().addWidget(QLabel(label))
        self.le1 = QLabel(u"A informação adicional deve ser obtida através de planilha no formato .CSV\nque contenha cabeçalho na primeira linha com, pelo menos, dois campos:\num para número da anotação e outro para texto adicional da anotação.")
        self.le1.setFont(newfont)
        self.layout().addWidget(self.le1)
        self.le = QLabel("")
        self.le.setPixmap(QPixmap(resolve('help/icons/notes.png')))
        self.layout().addWidget(self.le)
        self.label_1 = QLabel(u"Selecione o campo com o número da anotação:")
        self.label_1.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignBottom)

        self.layout().addWidget(self.label_1)
        self.combobox_1 = QComboBox()
        self.combobox_1.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.combobox_1.setFixedWidth(585)
        self.layout().addWidget(self.combobox_1)
        for field in fields:
            txt = unicode(field)
            self.combobox_1.addItem(txt)
        self.label_2 = QLabel(u"Selecione o campo com o texto adicional da anotação:")
        self.label_2.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignBottom)
        self.layout().addWidget(self.label_2)
        self.combobox_2 = QComboBox()
        self.combobox_2.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.combobox_2.setFixedWidth(585)
        self.layout().addWidget(self.combobox_2)
        for field in fields:
            txt = unicode(field)
            self.combobox_2.addItem(txt)

        buttonLayout = QHBoxLayout()
        buttonLayout.addStretch()

        label_3 = QLabel(u'Clique aqui para download do material usado no vídeo ilustrativo !!')
        label_3.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)

        label_3.setStyleSheet("font: 75 8pt ; text-decoration: underline; color: rgb(0, 0, 255);")
        label_3.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        label_3.mousePressEvent = example
        buttonLayout.addWidget(label_3,QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        
        cancelButton = QPushButton('Cancelar')
        cancelButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        buttonLayout.addWidget(cancelButton)
        
        okButton = QPushButton('Adicionar')
        okButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        okButton.setDefault(True)
        buttonLayout.addWidget(okButton)

        self.layout().addLayout(buttonLayout)


        okButton.clicked.connect(self.accept)
        cancelButton.clicked.connect(self.reject)

class QInputDialog(QInputDialog):
    @classmethod
    def getFields(cls, parent, title, label, text='', **kwargs):
        dialog = _QInputDialog(parent, title, label, text, **kwargs)
        dialog.setWindowIcon( QtGui.QIcon(resolve('help/icons/icon.png')) )
        result = dialog.exec_()
        return (str(dialog.combobox_1.currentIndex()), str(dialog.combobox_2.currentIndex()), bool(result))




   
class Notas_BTPLAN:
    """QGIS Plugin Implementation."""
		
    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgisInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
		
		
        
		
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'Notas_BTPLAN_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&IBGE - ToolBox')
        
        # TODO: We are going to let the user set this up in a future iteration
        toolbars = iface.mainWindow().findChildren(QToolBar)
        toolbar_manter=['IBGE']
        t = False
        for tb in toolbars:
            if tb.objectName() == u'&IBGE - ToolBox':
                t = tb
                break
        
        if t == False:
            self.toolbar = self.iface.addToolBar(u'&IBGE - ToolBox')
            self.toolbar.setObjectName(u'&IBGE - ToolBox')
        else:
            self.toolbar = t
    # noinspection PyMethodMayBeStatic

    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('Notas_BTPLAN', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        # Create the dialog (after translation) and keep reference
        self.dlg = Notas_BTPLANDialog()
	

		
		
		
		
		
		
        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)	
		
        self.actions.append(action) 
	
        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""
		
        #icon_path = ':/plugins/Notas_BTPLAN/icon.png'
        icon_path = ':/plugins/Notas_BTPLAN/help/icons/icon.png'

        self.add_action(
            icon_path,
            text=self.tr(u'Anotações BTPlan'),
            callback=self.run,
            parent=self.iface.mainWindow())
		
	self.toolbar.addSeparator()
	
          
    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&Anotações do BTPlan'),
                action)
            self.iface.removeToolBarIcon(action)
        # remove the toolbar
        del self.toolbar

		
    def run(self):
        """Run method that performs all the real work"""
	
	#self.dlg.label_3.setPixmap(QtGui.QPixmap(resolve('help/icons/Mission.png')))
	
	pic = QtGui.QLabel(self.dlg)
	pic.setGeometry(0, -20, 911, 261)
	#use full ABSOLUTE path to the image, not relative
	pic.setPixmap(QtGui.QPixmap(resolve('help/icons/help.png')))
	
	
	zera()
	cs.append(self.dlg)

	rMyIcon = QtGui.QPixmap(resolve('help/icons/explan.png'))
	self.dlg.pushButton.setIcon(QtGui.QIcon(rMyIcon))
	
	self.dlg.cbTons.currentIndexChanged.connect(populate_cbColors)
	self.dlg.cbColors.currentIndexChanged.connect(le_style)
	
	cbT.append(self.dlg.cbTons)
	cbC.append(self.dlg.cbColors)
	le.append(self.dlg.lineEdit)
	pb.append(self.dlg.pBMT)
	pb.append(self.dlg.pBP)
	lb2.append(self.dlg.label_2)
	
	self.dlg.pBMT.setIcon(QIcon(resolve('help/icons/unchecked.png')))
	self.dlg.pBMT.setIconSize(QtCore.QSize(16, 16))
	
	self.dlg.pBP.setIcon(QIcon(resolve('help/icons/checked.png')))
	self.dlg.pBP.setIconSize(QtCore.QSize(16, 16))
	
	self.dlg.setMinimumSize(1030, 220)
	self.dlg.setMaximumSize(1030, 220)
	self.dlg.resize(1030, 220)
	
	movie = QtGui.QMovie(resolve('help/icons/preview.gif'))
	lb2[0].setText(u'Pré-visualização:')
	movie.stop()
	
	cbT[0].setEnabled(False)
	cbC[0].setEnabled(False)
	
	cbT[0].setCurrentIndex(0)
	cbC[0].setCurrentIndex(2)
	le[0].setStyleSheet("background-color: #f1f1f1; font: 10pt \"Times New Roman\"; color: #000000;")
	
	pb[1].setIcon(QIcon(resolve('help/icons/checked.png')))
	pb[1].setIconSize(QtCore.QSize(16, 16))
	
	#P[0] = True	
	zera()
	
	frameGm = self.dlg.frameGeometry()
	screen = QtGui.QApplication.desktop().screenNumber(QtGui.QApplication.desktop().cursor().pos())
	centerPoint = QtGui.QApplication.desktop().screenGeometry(screen).center()
	frameGm.moveCenter(centerPoint)
	self.dlg.move(frameGm.topLeft())
	









	for button in self.dlg.button_box.buttons():
		if button.text() == 'Cancel':
			button.setText('Cancelar')
	for button in self.dlg.button_box.buttons():
		if button.text() == 'OK':
			button.setToolTip(u'Confirmar a execução do plugin !!!       ')
			button.setStyleSheet("""
			QPushButton {
    border: 2px solid #8f8f91;
    border-radius: 6px;
    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                      stop: 0 #f6f7fa, stop: 1 #dadbde);
    min-width: 80px;
}

QPushButton:pressed {
	
	background-color: rgb(0, 255, 0);
}

QPushButton:flat {
    border: none; /* no border for a flat push button */
}

QPushButton:default {
    border-color: navy; /* make the default button prominent */
}
""")
		elif button.text() == 'Cancelar':
			button.setToolTip(u'Cancelar a execução do plugin !!!        ')
			button.setStyleSheet("""
			QPushButton {
    border: 2px solid #8f8f91;
    border-radius: 6px;
    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                      stop: 0 #f6f7fa, stop: 1 #dadbde);
    min-width: 80px;
}

QPushButton:pressed {
	
	background-color: rgb(0, 255, 0);
}

QPushButton:flat {
    border: none; /* no border for a flat push button */
}

QPushButton:default {
    border-color: navy; /* make the default button prominent */
}
""")










	

	
	self.dlg.pBMT.setFlat(True)
	self.dlg.pBMT.setStyleSheet('border:none')
	#QObject.connect(self.dlg.pBMT, SIGNAL("clicked()"), (lambda: pb_RedW()))
	#self.dlg.pBMT.clicked.connect(lambda: pb_RedW())
	
	
	QObject.connect(self.dlg.pushButton, SIGNAL("clicked()"), (lambda: run_explan()))
	
	
	self.dlg.pBP.setFlat(True)
	self.dlg.pBP.setStyleSheet('border:none')
	
	self.dlg.lb_D.mousePressEvent = lb_D_RedW
	self.dlg.pBMT.mousePressEvent = lb_D_RedW
	self.dlg.lb_P.mousePressEvent = lb_P_customize
	self.dlg.pBP.mousePressEvent = lb_P_customize
	
	
	self.dlg.cbTons.addItems(l_Tons)
	self.dlg.cbColors.setCurrentIndex(2)
	

	
	
	self.dlg.setWindowIcon( QtGui.QIcon(resolve('help/icons/icon.png')) )
	
	# Handle high resolution displays:
	if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
		QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
	if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
		QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
	
	if self.iface.actionMapTips().isChecked() == False:
		self.iface.actionMapTips().trigger()

        # show the dialog
        self.dlg.show()	
		
        # Run the dialog event loop
        result = self.dlg.exec_()
		
        # See if OK was pressed
        if result:
			
            # Do something useful here - delete the line containing pass and
            # substitute with your code.
            #pass
			
            
			projeto = QgsProject.instance()
			projetoPath = os.path.dirname(projeto.fileName())
			folder = QFileDialog.getExistingDirectory(None,"Selecione a pasta com os arquivos KML baixados do BTPlan",projetoPath)
			crs = QgsCoordinateReferenceSystem("EPSG:4674")
            
			def removeGroup(name):
				root = QgsProject.instance().layerTreeRoot()
				group = root.findGroup(name)
				if not group is None:
					for child in group.children():
						dump = child.dump()
						id = dump.split("=")[-1].strip()
						QgsMapLayerRegistry.instance().removeMapLayer(id)
					root.removeChildNode(group)
	
			if folder != '':
				showdialog(folder)
				caminhos = [os.path.join(folder, nome) for nome in os.listdir(folder)]
				arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
				kmls = [arq for arq in arquivos if arq.lower().endswith(".kml")]
				
				nome_G = ''

				for n_Grupo in ["2.1","2.2","3.1","4.01","4.02","4.03","4.04","4.05","4.06","4.07","4.08","4.09","4.10","4.11","4.12","4.13"]:
					if n_Grupo == folder.split('\\')[len(folder.split('\\'))-1]:
						nome_G = n_Grupo
				if nome_G != '':
					# Get the legend and its groups:
					legend = self.iface.legendInterface()
					groups = legend.groups()
					
					nomeGrupo = 'BTPlan - Bloco '+folder.split('\\')[len(folder.split('\\'))-1]
                    
					if nomeGrupo not in groups:
						test = os.listdir(folder)
						c_Shp = 0
						for item in test:
							if item.endswith(".shp"):
								c_Shp += 1
						if c_Shp != 0:
							nomeGrupo = 'BTPlan - Bloco '+folder.split('\\')[len(folder.split('\\'))-1]
							self.iface.messageBar().pushMessage("Pasta selecionada", "Antes de criar o grupo \"" + nomeGrupo + u"\", a pasta \"" + folder.split('\\')[len(folder.split('\\'))-1] + "\" deve conter apenas os arquivos KML baixados do BTPlan.", level=QgsMessageBar.WARNING, duration=7 )
						else:
							nomeGrupo = 'BTPlan - Bloco '+folder.split('\\')[len(folder.split('\\'))-1]
							root = QgsProject.instance().layerTreeRoot()
							shapeGroup = root.insertGroup(0, nomeGrupo)

							if folder.split('\\')[len(folder.split('\\'))-1] == '2.1':
								textomessage = u'Atualização Vetorial do Mapeamento - Existe deslocamento no mapa?'
							elif folder.split('\\')[len(folder.split('\\'))-1] == '2.2':
								textomessage = u'Atualização Vetorial do Mapeamento - O mapa está desatualizado?'
							elif folder.split('\\')[len(folder.split('\\'))-1] == '3.1':
								textomessage = u'Malha Setorial - Subdivisão de Setores'
							elif folder.split('\\')[len(folder.split('\\'))-1] == '4.01':
								textomessage = u'Atualização de Áreas Especiais, Aglomerados, AIO e outros tipos - INCLUIR/ATUALIZAR Terra Indígena'
							elif folder.split('\\')[len(folder.split('\\'))-1] == '4.02':
								textomessage = u'Atualização de Áreas Especiais, Aglomerados, AIO e outros tipos - INCLUIR/ATUALIZAR Território Quilombola'
							elif folder.split('\\')[len(folder.split('\\'))-1] == '4.03':
								textomessage = u'Atualização de Áreas Especiais, Aglomerados, AIO e outros tipos - INCLUIR/ATUALIZAR Território UC'
							elif folder.split('\\')[len(folder.split('\\'))-1] == '4.04':
								textomessage = u'Atualização de Áreas Especiais, Aglomerados, AIO e outros tipos - INCLUIR/ATUALIZAR Aglomerado Subnormal'
							elif folder.split('\\')[len(folder.split('\\'))-1] == '4.05':
								textomessage = u'Atualização de Áreas Especiais, Aglomerados, AIO e outros tipos - INCLUIR/ATUALIZAR Aglomerado Rural'
							elif folder.split('\\')[len(folder.split('\\'))-1] == '4.06':
								textomessage = u'Atualização de Áreas Especiais, Aglomerados, AIO e outros tipos - INCLUIR/ATUALIZAR Agrovila'
							elif folder.split('\\')[len(folder.split('\\'))-1] == '4.07':
								textomessage = u'Atualização de Áreas Especiais, Aglomerados, AIO e outros tipos - INCLUIR/ATUALIZAR Agrupamento Indígena'
							elif folder.split('\\')[len(folder.split('\\'))-1] == '4.08':
								textomessage = u'Atualização de Áreas Especiais, Aglomerados, AIO e outros tipos - INCLUIR/ATUALIZAR Agrupamento Quilombola'
							elif folder.split('\\')[len(folder.split('\\'))-1] == '4.09':
								textomessage = u'Atualização de Áreas Especiais, Aglomerados, AIO e outros tipos - INCLUIR/ATUALIZAR Áreas de Interesse Operacional'
							elif folder.split('\\')[len(folder.split('\\'))-1] == '4.10':
								textomessage = u'Atualização de Áreas Especiais, Aglomerados, AIO e outros tipos - Incluir/atualizar quarteis/bases militares'
							elif folder.split('\\')[len(folder.split('\\'))-1] == '4.11':
								textomessage = u'Atualização de Áreas Especiais, Aglomerados, AIO e outros tipos - Incluir/atualizar acampamentos/alojamentos'
							elif folder.split('\\')[len(folder.split('\\'))-1] == '4.12':
								textomessage = u'Atualização de Áreas Especiais, Aglomerados, AIO e outros tipos - Incluir/atualizar unidades prisionais'
							elif folder.split('\\')[len(folder.split('\\'))-1] == '4.13':
								textomessage = u'Atualização de Áreas Especiais, Aglomerados, AIO e outros tipos - Incluir/atualizar conventos, hospitais, ILPI, IACA' 
							else:
								textomessage = u"A pasta que contém os arquivos KML não representa um nome de bloco de questionários ('2.1','2.2','3.1','4.01','4.02','4.03','4.04','4.05','4.06','4.07','4.08','4.09','4.10','4.11','4.12' ou '4.13')"
							self.iface.messageBar().pushMessage(nomeGrupo, textomessage, level=QgsMessageBar.INFO, duration=7 )
							
							
							fileroute = ''
							fKML = []





							for nome in kmls:
								if not os.path.isfile(nome[0:len(nome) -3] + 'shp'):
									fileroute = nome[0:len(nome) -3] + 'shp'
									displayName =  nome[0:len(nome) -4].split('\\')[len(nome[0:len(nome) -4].split('\\')) - 1]
									# Open file
									arq2 = open(nome[0:len(nome)-3] + 'txt' , "a")
									# Open file
									fileHandler = open(nome, "r")
									# Get list of all lines in file
									listOfLines = fileHandler.readlines()
									# Close file
									fileHandler.close()
								
									file_KML =''
									conta_KML = 0
									with open(nome, 'r') as content_file:
										content = content_file.read()
									content_file.close()   
									
									if '<Description>' not in content:
										conta_KML += 1
										file_KML = nome[0:len(nome)].split('\\')[len(nome[0:len(nome)].split('\\')) - 1]
										fKML.append(file_KML)

								
									texto = ''
									# Iterate over the lines
									for line in listOfLines:
										frase = line.strip()   
										if frase[0:].find('<Description>') != -1:
											if  frase[:].find('</Description>') == -1:
												for el in range(len(listOfLines)):
													if listOfLines[el].find('<Description>') != -1:
														b = el
													elif listOfLines[el].find('</Description>') != -1:
														l = el 
														break
												for el in range(b, l +1):
													texto =   texto +listOfLines[el].strip() + ' '
												texto = texto[13:texto.find('</Description>')]
											else:
												texto = frase[13:len(frase)-14].strip()
											arq2.write(texto)
											if (add == "Y"):
												for row in rows[:]: 
													# parsing each column of a row 
													if displayName.split("_")[1] == row[int(index_1)]:
														infoAdd = row[int(index_2)]
												arq2.write('<br><b>Informação adicional: </b>' + infoAdd)
											break
									arq2.close()
								

									vlayer = QgsVectorLayer(nome, "line", "ogr")
									writer = QgsVectorFileWriter.writeAsVectorFormat(vlayer, nome[0:len(nome) -3] + 'shp', "utf-8", crs, "ESRI Shapefile")

								displayName =  nome[0:len(nome) -4].split('\\')[len(nome[0:len(nome) -4].split('\\')) - 1]
								filename = QgsVectorLayer(fileroute,displayName,"ogr")
								QgsMapLayerRegistry.instance().addMapLayer(filename,False)
								shapeGroup.insertChildNode(1,QgsLayerTreeLayer(filename))
								gBTPLAN = root.findGroup(nomeGrupo)
								if gBTPLAN is not None:

									for child in gBTPLAN.children():
										if isinstance(child, QgsLayerTreeLayer):
											layer = QgsMapLayerRegistry.instance().mapLayer(child.layerId())
											if isinstance(layer, QgsVectorLayer):
												vl = QgsMapLayerRegistry.instance().mapLayersByName(child.layerName())[0]
												self.iface.setActiveLayer(vl)
												fonte = self.iface.activeLayer().dataProvider().dataSourceUri().split('|')[0]

												if layer.wkbType()==QGis.WKBLineString:
													symbols = layer.rendererV2().symbols()
													symbol = symbols[0]
													symbol.setColor(QtGui.QColor.fromRgb(0,0,255))
													symbol.setWidth(0.6)
												self.iface.mapCanvas().refresh() 
												self.iface.legendInterface().refreshLayerSymbology(layer)
										
												myVectorLayer = self.iface.activeLayer()
												myRenderer  = myVectorLayer.rendererV2()
												if myVectorLayer.geometryType() == QGis.Polygon:
													mySymbol1 = QgsFillSymbolV2.createSimple({'color':'255,0,0,0','color_border':'#0000FF','width_border':'0.6'})
													myRenderer.setSymbol(mySymbol1)
													myVectorLayer.triggerRepaint()
													self.iface.legendInterface().refreshLayerSymbology(myVectorLayer)
												
												
												
												
												# TRABALHANDO AQUI !!!
												if myVectorLayer.geometryType() == QGis.Point:
													
													myVectorLayer.rendererV2().symbol().setSize(6)
													
													myVectorLayer.rendererV2().symbol().setColor(QColor("blue"))
													myVectorLayer.triggerRepaint()
												
													myVectorLayer.rendererV2().symbol().symbolLayer(0).setShape(QgsSimpleMarkerSymbolLayerBase.Star)
													myVectorLayer.triggerRepaint()
													self.iface.layerTreeView().refreshLayerSymbology(myVectorLayer.id())
													
													
													
												
												mc = self.iface.mapCanvas()
												vl.removeSelection()
												mc.refresh()


							conta = 0
							c_ativa = []
							gBTPLAN = root.findGroup(nomeGrupo)
							if gBTPLAN is not None:
								for child in gBTPLAN.children():
									if isinstance(child, QgsLayerTreeLayer):
										layer = QgsMapLayerRegistry.instance().mapLayer(child.layerId())
										if isinstance(layer, QgsVectorLayer):
											vl = QgsMapLayerRegistry.instance().mapLayersByName(child.layerName())[0]
											if conta == 0:
												c_ativa.append(vl)
											self.iface.setActiveLayer(vl)

											layer_hypothese = self.iface.activeLayer()
											if MT[0] == True:
											
												infile = codecs.open(self.iface.activeLayer().dataProvider().dataSourceUri().split("|")[0][0:len(self.iface.activeLayer().dataProvider().dataSourceUri().split("|")[0]) -3] + "txt", "r", encoding="utf-8").read()
												lines = 0
												words = 0
												characters = 0
												for line in infile:
													wordslist = line.split()
													lines = lines + 1
													words = words + len(wordslist)
													characters = characters + len(line)
												n_L = int(characters/64) + (characters%64>0)
												if (add != "N"):
													height_L = int(15.38461538461534 * n_L*1.3)
													if (height_L < 30):
														height_L = 30
												else:
													height_L = int(15.38461538461534 * n_L)
													if (height_L < 30):
														height_L = 30
												if (GetSystemMetrics(0) == 1920 and GetSystemMetrics(1) == 1080) or (GetSystemMetrics(0) == 1680 and GetSystemMetrics(1) == 1050) or (GetSystemMetrics(0) == 1600 and GetSystemMetrics(1) == 900):
													bpit = "<div style=\"width:600;height:" + str(height_L) + "; background-color: " + bgMT[0] + " ;\">"
												elif (GetSystemMetrics(0) == 1440 and GetSystemMetrics(1) == 900) or (GetSystemMetrics(0) == 1400 and GetSystemMetrics(1) == 1050):
													bpit = "<div style=\"width:500;height:" + str(height_L) + "; background-color: " + bgMT[0] + " ;\">"
												elif (GetSystemMetrics(0) == 1366 and GetSystemMetrics(1) == 768) or (GetSystemMetrics(0) == 1360 and GetSystemMetrics(1) == 768) or (GetSystemMetrics(0) == 1280 and GetSystemMetrics(1) == 1024) or (GetSystemMetrics(0) == 1280 and GetSystemMetrics(1) == 960) or (GetSystemMetrics(0) == 1280 and GetSystemMetrics(1) == 800) or (GetSystemMetrics(0) == 1280 and GetSystemMetrics(1) == 768) or (GetSystemMetrics(0) == 1280 and GetSystemMetrics(1) == 720) or (GetSystemMetrics(0) == 1280 and GetSystemMetrics(1) == 600):
													bpit = "<div style=\"width:400;height:" + str(height_L) + "; background-color: " + bgMT[0] + " ;\">"
												layer_hypothese.setDisplayField(bpit+codecs.open(self.iface.activeLayer().dataProvider().dataSourceUri().split("|")[0][0:len(self.iface.activeLayer().dataProvider().dataSourceUri().split("|")[0]) -3] + "txt", "r", encoding="utf-8").read()+lpit)
											action_layer_hypothese = layer_hypothese.actions()
											actionDescription = layer.name() + ' - Abrir em Barra de Mensagem'
											actionCode = 'from qgis.utils import iface;import codecs;iface.messageBar().pushMessage("Nota",codecs.open(iface.activeLayer().dataProvider().dataSourceUri().split("|")[0][0:len(iface.activeLayer().dataProvider().dataSourceUri().split("|")[0]) -3] + "txt", "r", encoding="utf-8").read(), level=QgsMessageBar.INFO, duration=20 )'
											action_graphique = QgsAction(QgsAction.GenericPython,actionDescription,actionCode,True)
											action_layer_hypothese.addAction(action_graphique)
									conta = conta + 1
									mc = self.iface.mapCanvas()
									mc.refresh()

								self.iface.setActiveLayer(c_ativa[0])
								mc = self.iface.mapCanvas()
								mc.refresh()

							if conta_KML > 0:
								widget = self.iface.messageBar().createMessage(u"KML fora do padrão BTPlan",u"Veja na ComboBox arquivo(s) KML que não representa(m) as anotações do BTPlan !!!")
								combo = QComboBox()
								widget.layout().addWidget(combo)
								self.iface.messageBar().pushWidget(widget, QgsMessageBar.WARNING)
								combo.setSizeAdjustPolicy(QComboBox.AdjustToContents)
								combo.addItems(fKML)
					else:

						# Loop to enable all the groups:
						nomeGrupo = 'BTPlan - Bloco '+folder.split('\\')[len(folder.split('\\'))-1]
						for i in range(len(groups)):
							if groups[i] == nomeGrupo:
								self.iface.messageBar().pushMessage("Nome do grupo", "o grupo " + nomeGrupo + u" já existe !!! Portanto, ele será substituído.", level=QgsMessageBar.WARNING, duration=7 )
							
								test = os.listdir(folder)
								removeGroup(nomeGrupo)
								for item in test:
									if item.endswith(".qpj"):
										os.remove(os.path.join(folder, item))
									elif item.endswith(".prj"):
										os.remove(os.path.join(folder, item))
									elif item.endswith(".dbf"):
										os.remove(os.path.join(folder, item))
									elif item.endswith(".cpg"):
										os.remove(os.path.join(folder, item))
									elif item.endswith(".txt"):
										os.remove(os.path.join(folder, item))
									elif item.endswith(".shp"):
										os.remove(os.path.join(folder, item))
									elif item.endswith(".shx"):
										os.remove(os.path.join(folder, item))
							
								break
						nomeGrupo = 'BTPlan - Bloco '+folder.split('\\')[len(folder.split('\\'))-1]
						root = QgsProject.instance().layerTreeRoot()
						shapeGroup = root.insertGroup(0, nomeGrupo)
								
						fileroute = ''
						fKML = []

						for nome in kmls:
							if not os.path.isfile(nome[0:len(nome) -3] + 'shp'):
								fileroute = nome[0:len(nome) -3] + 'shp'
								displayName =  nome[0:len(nome) -4].split('\\')[len(nome[0:len(nome) -4].split('\\')) - 1]
								# Open file
								arq2 = open(nome[0:len(nome)-3] + 'txt' , "a")
								# Open file
								fileHandler = open(nome, "r")
								# Get list of all lines in file
								listOfLines = fileHandler.readlines()
								# Close file
								fileHandler.close()
							
								file_KML =''
								conta_KML = 0
								with open(nome, 'r') as content_file:
									content = content_file.read()
								content_file.close()   

								if '<Description>' not in content:
									conta_KML += 1
									file_KML = nome[0:len(nome)].split('\\')[len(nome[0:len(nome)].split('\\')) - 1]
									fKML.append(file_KML)
							
								texto = ''
								#showdialog(displayName)                                
								# Iterate over the lines
								for line in listOfLines:
									frase = line.strip()   
									if frase[0:].find('<Description>') != -1:
										if  frase[:].find('</Description>') == -1:
											for el in range(len(listOfLines)):
												if listOfLines[el].find('<Description>') != -1:
													b = el
												elif listOfLines[el].find('</Description>') != -1:
													l = el
													break
											for el in range(b, l +1):
												texto =   texto +listOfLines[el].strip() + ' '
											texto = texto[13:texto.find('</Description>')]
										else:
											texto = frase[13:len(frase)-14].strip()
										arq2.write(texto)
										if (add == "Y"):
											for row in rows[:]: 
												# parsing each column of a row 
												if displayName.split("_")[1] == row[int(index_1)]:
													infoAdd = row[int(index_2)]
											arq2.write('<br><b>Informação adicional: </b>' + infoAdd)
										break
								arq2.close()
							
								
								vlayer = QgsVectorLayer(nome, "line", "ogr")
								writer = QgsVectorFileWriter.writeAsVectorFormat(vlayer, nome[0:len(nome) -3] + 'shp', "utf-8", crs, "ESRI Shapefile")

							displayName =  nome[0:len(nome) -4].split('\\')[len(nome[0:len(nome) -4].split('\\')) - 1]
							filename = QgsVectorLayer(fileroute,displayName,"ogr")
							QgsMapLayerRegistry.instance().addMapLayer(filename,False)
							shapeGroup.insertChildNode(1,QgsLayerTreeLayer(filename))
							gBTPLAN = root.findGroup(nomeGrupo)
							if gBTPLAN is not None:

								for child in gBTPLAN.children():
									if isinstance(child, QgsLayerTreeLayer):
										layer = QgsMapLayerRegistry.instance().mapLayer(child.layerId())
										if isinstance(layer, QgsVectorLayer):
											vl = QgsMapLayerRegistry.instance().mapLayersByName(child.layerName())[0]
											self.iface.setActiveLayer(vl)
											fonte = self.iface.activeLayer().dataProvider().dataSourceUri().split('|')[0]

											if layer.wkbType()==QGis.WKBLineString:
												symbols = layer.rendererV2().symbols()
												symbol = symbols[0]
												symbol.setColor(QtGui.QColor.fromRgb(0,0,255))
												symbol.setWidth(0.6)
											self.iface.mapCanvas().refresh() 
											self.iface.legendInterface().refreshLayerSymbology(layer)
									
											myVectorLayer = self.iface.activeLayer()
											myRenderer  = myVectorLayer.rendererV2()
											if myVectorLayer.geometryType() == QGis.Polygon:
												mySymbol1 = QgsFillSymbolV2.createSimple({'color':'255,0,0,0','color_border':'#0000FF','width_border':'0.6'})
												myRenderer.setSymbol(mySymbol1)
												myVectorLayer.triggerRepaint()
												self.iface.legendInterface().refreshLayerSymbology(myVectorLayer)
											
											
											
											
											# TRABALHANDO AQUI !!!
											if myVectorLayer.geometryType() == QGis.Point:
												
												myVectorLayer.rendererV2().symbol().setSize(6)
												
												myVectorLayer.rendererV2().symbol().setColor(QColor("blue"))
												myVectorLayer.triggerRepaint()
											
												myVectorLayer.rendererV2().symbol().symbolLayer(0).setShape(QgsSimpleMarkerSymbolLayerBase.Star)
												myVectorLayer.triggerRepaint()
												self.iface.layerTreeView().refreshLayerSymbology(myVectorLayer.id())
												
												
												
											
											mc = self.iface.mapCanvas()
											vl.removeSelection()
											mc.refresh()

						conta = 0
						c_ativa = []
						gBTPLAN = root.findGroup(nomeGrupo)
						if gBTPLAN is not None:
							for child in gBTPLAN.children():
								if isinstance(child, QgsLayerTreeLayer):
									layer = QgsMapLayerRegistry.instance().mapLayer(child.layerId())
									if isinstance(layer, QgsVectorLayer):
										vl = QgsMapLayerRegistry.instance().mapLayersByName(child.layerName())[0]
										if conta == 0:
											c_ativa.append(vl)
										self.iface.setActiveLayer(vl)

										layer_hypothese = self.iface.activeLayer()
										if MT[0] == True:
											infile = codecs.open(self.iface.activeLayer().dataProvider().dataSourceUri().split("|")[0][0:len(self.iface.activeLayer().dataProvider().dataSourceUri().split("|")[0]) -3] + "txt", "r", encoding="utf-8").read()
											lines = 0
											words = 0
											characters = 0
											for line in infile:
												wordslist = line.split()
												lines = lines + 1
												words = words + len(wordslist)
												characters = characters + len(line)
											n_L = int(characters/64) + (characters%64>0)
											if (add != "N"):
												height_L = int(15.38461538461534 * n_L*1.3)
												if (height_L < 30):
													height_L = 30
											else:
												height_L = int(15.38461538461534 * n_L)
												if (height_L < 30):
													height_L = 30
											if (GetSystemMetrics(0) == 1920 and GetSystemMetrics(1) == 1080) or (GetSystemMetrics(0) == 1680 and GetSystemMetrics(1) == 1050) or (GetSystemMetrics(0) == 1600 and GetSystemMetrics(1) == 900):
												bpit = "<div style=\"width:600;height:" + str(height_L) + "; background-color: " + bgMT[0] + " ;\">"
											elif (GetSystemMetrics(0) == 1440 and GetSystemMetrics(1) == 900) or (GetSystemMetrics(0) == 1400 and GetSystemMetrics(1) == 1050):
												bpit = "<div style=\"width:500;height:" + str(height_L) + "; background-color: " + bgMT[0] + " ;\">"
											elif (GetSystemMetrics(0) == 1366 and GetSystemMetrics(1) == 768) or (GetSystemMetrics(0) == 1360 and GetSystemMetrics(1) == 768) or (GetSystemMetrics(0) == 1280 and GetSystemMetrics(1) == 1024) or (GetSystemMetrics(0) == 1280 and GetSystemMetrics(1) == 960) or (GetSystemMetrics(0) == 1280 and GetSystemMetrics(1) == 800) or (GetSystemMetrics(0) == 1280 and GetSystemMetrics(1) == 768) or (GetSystemMetrics(0) == 1280 and GetSystemMetrics(1) == 720) or (GetSystemMetrics(0) == 1280 and GetSystemMetrics(1) == 600):
												bpit = "<div style=\"width:400;height:" + str(height_L) + "; background-color: " + bgMT[0] + " ;\">"											
											layer_hypothese.setDisplayField(bpit+codecs.open(self.iface.activeLayer().dataProvider().dataSourceUri().split("|")[0][0:len(self.iface.activeLayer().dataProvider().dataSourceUri().split("|")[0]) -3] + "txt", "r", encoding="utf-8").read()+lpit)
										action_layer_hypothese = layer_hypothese.actions()
										actionDescription = layer.name() + ' - Abrir em Barra de Mensagem'
										actionCode = 'from qgis.utils import iface;import codecs;iface.messageBar().pushMessage("Nota",codecs.open(iface.activeLayer().dataProvider().dataSourceUri().split("|")[0][0:len(iface.activeLayer().dataProvider().dataSourceUri().split("|")[0]) -3] + "txt", "r", encoding="utf-8").read(), level=QgsMessageBar.INFO, duration=20 )'
										action_graphique = QgsAction(QgsAction.GenericPython,actionDescription,actionCode,True)
										action_layer_hypothese.addAction(action_graphique)
								conta = conta + 1
								mc = self.iface.mapCanvas()
								mc.refresh()

							self.iface.setActiveLayer(c_ativa[0])
							mc = self.iface.mapCanvas()
							mc.refresh()

						if conta_KML > 0:
							widget = self.iface.messageBar().createMessage(u"KML fora do padrão BTPlan",u"Veja na ComboBox arquivo(s) KML que não representa(m) as anotações do BTPlan !!!")
							combo = QComboBox()
							widget.layout().addWidget(combo)
							self.iface.messageBar().pushWidget(widget, QgsMessageBar.WARNING)
							combo.setSizeAdjustPolicy(QComboBox.AdjustToContents)
							combo.addItems(fKML)				

				else:
					self.iface.messageBar().pushMessage("Pasta selecionada", "A pasta \"" + folder.split('\\')[len(folder.split('\\'))-1] + u"\" não representa um nome de bloco de questionários ('2.1','2.2','3.1','4.01','4.02','4.03','4.04','4.05','4.06','4.07','4.08','4.09','4.10','4.11','4.12' ou '4.13')", level=QgsMessageBar.WARNING, duration=10 )