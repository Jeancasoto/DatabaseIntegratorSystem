import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtGui import *

class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        uic.loadUi("mainGUI.ui", self)
        #Accion del boton_probar_origen
        self.boton_probar_origen.clicked.connect(self.probar_origen)
        #Accion del boton_probar_destino
        self.boton_probar_destino.clicked.connect(self.probar_destino)

    #Metodo del boton_probar_origen
    def probar_origen(self):
        w = QWidget()
        # Show a message box
        result = QMessageBox.information(w, "Message", "Probando la conexion con la base de datos ")

    #Metodo del boton_probar_destino
    def probar_destino(self):
        w = QWidget()
        # Show a message box
        result = QMessageBox.information(w, "Message", "Probando la conexion con la base de datos ")

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    sys.exit(app.exec_())
