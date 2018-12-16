import sys
import mysql.connector
import pyodbc
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtGui import *

class Ui_MainWindow(QtGui.QMainWindow):

    def __init__(self):

        #Variable que controla la accion al presionar el boton_guardar_configuracion
        self.contador_accion_boton =0 

        QtGui.QMainWindow.__init__(self)
        uic.loadUi("mainGUI.ui", self)
        #Accion del boton_probar_origen
        self.boton_probar_origen.clicked.connect(self.probar_origen)
        #Accion del boton_probar_destino
        self.boton_probar_destino.clicked.connect(self.probar_destino)
        #Accion del boton_guardar_configuracion 
        self.boton_guardar_configuracion.clicked.connect(self.guardar_configuracion)

    #Metodo del boton_guardar_configuracion 
    def guardar_configuracion(self):
        
        if self.contador_accion_boton ==0:
            ###AL PRESIONAR EL BOTON CARGAR##
            #################################
            #################################
            self.nombre_instancia_origen.setText("192.168.1.14")
            self.nombre_basedatos_origen.setText("Northwind")
            self.puerto_origen.setText("1433")
            self.nombre_usuario_origen.setText("JEANCA")
            self.password_origen.setText("1234")
            #################################
            #################################
            

            ###AL PRESIONAR EL BOTON CARGAR##
            #################################
            #################################
            self.nombre_instancia_destino.setText("192.168.1.17")
            self.nombre_basedatos_destino.setText("Northwind")
            self.puerto_destino.setText("3336")
            self.nombre_usuario_destino.setText("JEANCA")
            self.password_destino.setText("holamundo")
            #################################
            #################################
            
            self.contador_accion_boton +=1
        else:

            print ("Contador diferente de 0")
            


    #Metodo del boton_probar_origen
    def probar_origen(self):
        try:
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


            #Contador para verificar que los campos esten llenos 
            vacios =0 

            #Condiciones para asegurar que el usuario llene todos los campos 
            if nom_instancia_origen=="":
                #w = QWidget()
                # Show a message box
                #result = QMessageBox.critical(w, "Message", "Debe llenar todos los campos para establecer una conexion exitosa")
                vacios +=1
            
            if nom_basedatos_origen=="":
                #w = QWidget()
                # Show a message box
                #result = QMessageBox.critical(w, "Message", "Debe llenar todos los campos para establecer una conexion exitosa")
                vacios +=1
            
            if port_origen=="":
                #w = QWidget()
                # Show a message box
                #result = QMessageBox.critical(w, "Message", "Debe llenar todos los campos para establecer una conexion exitosa")
                vacios +=1
            
            if nom_usuario_origen=="":
                #w = QWidget()
                # Show a message box
                #result = QMessageBox.critical(w, "Message", "Debe llenar todos los campos para establecer una conexion exitosa")
                vacios +=1

            if pass_origen=="":
                #w = QWidget()
                # Show a message box
                #result = QMessageBox.critical(w, "Message", "Debe llenar todos los campos para establecer una conexion exitosa")
                vacios +=1

            if vacios ==0:

                cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+str(nom_instancia_origen)+';PORT='+str(port_origen)+';DATABASE='+str(nom_basedatos_origen)+';UID='+str(nom_usuario_origen)+';PWD='+ str(pass_origen))
                cursor = cnxn.cursor()  
                vacios=0
                w = QWidget()
                # Show a message box
                result = QMessageBox.information(w, "Message", "Conexion establecida con exito con: \nEl servidor: "+nom_instancia_origen+"\nBase de datos: "+nom_basedatos_origen+"\nPuerto: "+port_origen+"\nUsuario: "+nom_basedatos_origen)

            else:
                vacios=0
                w = QWidget()
                # Show a message box
                result = QMessageBox.critical(w, "Message", "Debe llenar todos los campos para establecer una conexion exitosa")

            #Conexion en duro que funciona... comprobado
            """
            server = '192.168.1.14' 
            database = 'Northwind'  
            username = 'JEANCA' 
            password = '1234' 

            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)

            cursor = cnxn.cursor() 
            """

            print ('Llego exitosamente hasta el final')
            
        except Exception as e:
            w = QWidget()
            # Show a message box
            result = QMessageBox.critical(w, "Message", "No se ha logrado establecer la conexion con: \nEl servidor: "+nom_instancia_origen+"\nBase de datos: "+nom_basedatos_origen+"\nPuerto: "+port_origen+"\nUsuario: "+nom_basedatos_origen)

    #Metodo del boton_probar_destino
    def probar_destino(self):

        try:
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
            
            #Contador para verificar que los campos esten llenos 
            vacios =0 

            #Condiciones para asegurar que el usuario llene todos los campos 
            if nom_instancia_destino=="":
                #w = QWidget()
                # Show a message box
                #result = QMessageBox.critical(w, "Message", "Debe llenar todos los campos para establecer una conexion exitosa")
                vacios +=1
            
            if nom_basedatos_destino=="":
                #w = QWidget()
                # Show a message box
                #result = QMessageBox.critical(w, "Message", "Debe llenar todos los campos para establecer una conexion exitosa")
                vacios +=1
            
            if port_destino=="":
                #w = QWidget()
                # Show a message box
                #result = QMessageBox.critical(w, "Message", "Debe llenar todos los campos para establecer una conexion exitosa")
                vacios +=1
            
            if nom_usuario_destino=="":
                #w = QWidget()
                # Show a message box
                #result = QMessageBox.critical(w, "Message", "Debe llenar todos los campos para establecer una conexion exitosa")
                vacios +=1

            if pass_destino=="":
                #w = QWidget()
                # Show a message box
                #result = QMessageBox.critical(w, "Message", "Debe llenar todos los campos para establecer una conexion exitosa")
                vacios +=1

            if vacios ==0:

                #cnxn = pyodbc.connect('DRIVER={MYSQL};SERVER='+str(nom_instancia_destino)+';PORT='+str(port_destino)+';DATABASE='+str(nom_basedatos_destino)+';UID='+str(nom_usuario_destino)+';PWD='+ str(pass_destino))
                #cursor = cnxn.cursor()  
                vacios=0
                w = QWidget()
                # Show a message box
                result = QMessageBox.information(w, "Message", "Conexion establecida con exito con: \nEl servidor: "+nom_instancia_destino+"\nBase de datos: "+nom_basedatos_destino+"\nPuerto: "+port_destino+"\nUsuario: "+nom_basedatos_destino)

            else:
                vacios=0
                w = QWidget()
                # Show a message box
                result = QMessageBox.critical(w, "Message", "Debe llenar todos los campos para establecer una conexion exitosa")

            print ('Llego exitosamente hasta el final')
            
        except Exception as e:
            w = QWidget()
            # Show a message box
            result = QMessageBox.critical(w, "Message", "No se ha logrado establecer la conexion con: \nEl servidor: "+nom_instancia_destino+"\nBase de datos: "+nom_basedatos_destino+"\nPuerto: "+port_destino+"\nUsuario: "+nom_basedatos_destino)



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    sys.exit(app.exec_())
