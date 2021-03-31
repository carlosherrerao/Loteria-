# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 21:46:59 2019

@author: parka
"""
from datetime import datetime
import pprint
import pymongo
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

class Conexion:
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb+srv://admin:HADES2121@loteria-1egci.mongodb.net/test?retryWrites=true&w=majority")
        #escojer database (bd)
        self.mydb = self.client["Loteria"]
        
    def agregar_usuario(self,nombre, password):
        mycollection = self.mydb["Usuarios"]
        mydict = { "nombre": nombre, "contrasena": password }
        result= mycollection.insert_one(mydict)
        return result

    def validar_contraseña(self,nombre, password):
        mycollection = self.mydb["Usuarios"]
        mydict = { "nombre": nombre}
        documento = mycollection.find_one(mydict)
        if documento and documento['contrasena'] == password:
            return True
        else: 
            return False
        
    def agregar_partida(self,fecha, nombre_ganador, tiempo):
        mycollection = self.mydb["Puntaje"]
        mydict = { "fecha": fecha, "nombre_ganador": nombre_ganador, "tiempo": tiempo }
        result= mycollection.insert_one(mydict)
        return result
    
    def consultar_partidas(self,nombre):
        mycollection = self.mydb["Puntaje"]
        mydict = { "nombre_ganador": nombre}
        consulta = []
        for post in mycollection.find(mydict):
            pprint.pprint(post)
            consulta.append([post['fecha'],post['nombre_ganador'],post['tiempo']])
        return consulta
     
    def validar_conexion(self):
       bandera = True
       try:
          info = self.client.server_info() # Forces a call.
       except ServerSelectionTimeoutError:
          print("server is down.")
          bandera = False
       return bandera

       

#conexion = Conexion()
#result = conexion.validar_contraseña("Oswa","america")
#print(result)
#conexion.agregar_partida(datetime.now(), "Carlos", "1:20")
#consulta = conexion.consultar_partidas("Carlos")

