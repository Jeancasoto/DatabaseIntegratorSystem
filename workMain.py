import sys
import pyodbc
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
        #Inicio de recuperacion de datos
        nom_instancia_origen = self.nombre_instancia_origen.text()
        nom_basedatos_origen = self.nombre_basedatos_origen.text()
        port_origen = self.puerto_origen.text()
        nom_usuario_origen = self.nombre_usuario_origen.text()
        pass_origen = self.password_origen.text()
        print ('########################################')
        print ('##########-DATOS RECUPERADOS-###########')
        print ('########################################')
        print (nom_instancia_origen)
        print (nom_basedatos_origen)
        print (port_origen)
        print (nom_usuario_origen)
        print (pass_origen)
        print ('#######-FIN RECUPERACION DE DATOS-######')

        server = '192.168.1.14' 
        database = 'Northwind'  
        username = 'JEANCA' 
        password = '1234' 

        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)

        cursor = cnxn.cursor() 

        print ('Llego exitosamente hasta el final')

    #Metodo del boton_probar_destino
    def probar_destino(self):
        w = QWidget()
        # Show a message box
        result = QMessageBox.information(w, "Message", "Probando la conexion con la base de datos ")
        #Inicio de recuperacion de datos
        nom_instancia_destino = self.nombre_instancia_destino.text()
        nom_basedatos_destino = self.nombre_basedatos_destino.text()
        port_destino = self.puerto_destino.text()
        nom_usuario_destino = self.nombre_usuario_destino.text()
        pass_destino = self.password_destino.text()
        print ('########################################')
        print ('##########-DATOS RECUPERADOS-###########')
        print ('########################################')
        print (nom_instancia_destino)
        print (nom_basedatos_destino)
        print (port_destino)
        print (nom_usuario_destino)
        print (pass_destino)
        print ('#######-FIN RECUPERACION DE DATOS-######')

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    sys.exit(app.exec_())
