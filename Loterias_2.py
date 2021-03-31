# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 00:49:21 2019

@author: parka
"""
#se importan librerias
import threading
import time
import logging
import random
import queue
import copy

#para imprimir mensajes
logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)
#tamaño del buffer
BUF_SIZE = 1
#representacion del buffer
q = queue.Queue(BUF_SIZE)
#ganador
winner = ""
#numero de jugadores
no_players = 3
#variable lista que guarda los nombres delos jugadores que 
#ya checaron el item del buffer en sus tableros
checked = []

#CLASE CARTAS
#contiene una lista con todas las cartas posibles del juego
class Cartas:
    #constructor, no recibe parametros
    def __init__(self):
        #lista que contiene todaslas cartas posibles en el juego
        self.cartas = ["AH MUZEN CAB","AH PUCH","CHAAC",
                       "XBALANQUE","KUKULKAN","CUPID","BELLONA",
                       "HERCULES","MERCURY","TERRA","FENRIR",
                       "FREYA","LOKI","ODIN","THOR","YMIR",
                       "AMATERASU","HACHIMAN","IZANAMI",
                       "KUZENBO","SUSANO","AGNI","BAKASURA",
                       "GANESHA","KALI","RAMA","VAMANA",
                       "ACHILLES","APHRODITE","APOLO","ARES",
                       "ARTEMIS","ATHENEA","HADES",
                       "CERBERUS","MEDUSA","NEMESIS","POSEIDON",
                       "KING ARTHUR","MERLIN","CU CHULAINN",
                       "THE MORRIGAN","ZEUS","THANATOS",
                       "ANUBIS","ISIS","NEITH","RA","THOTH",
                       "CHANGE","HE BO","GUAN YU","HOU YI",
                       "SUN WUKONG"]
    #metodo para regresar el arreglo de caracteristicas    
    def getCartas(self):
        return self.cartas
    
#CLASE TABLERO
#Clase que representa el tablero de cada jugador
#Hereda de la clase Cartas
class Tablero(Cartas):
    def __init__(self):
        # Invoca al constructor de clase Cartas
        Cartas.__init__(self)

        self.__tablero = random.sample(self.getCartas(), 16) 
    #regresa el tablero    
    def getTablero(self):
        tablero = self.__tablero
        return tablero
    
    def generar_nuevo(self):
        self.__tablero = random.sample(self.getCartas(), 16) 
        tablero = self.__tablero
        print(tablero)
        return tablero

#CLASE DECK
#Clase que representa la baraja del juego generada de manera aleatoria
#Hereda de la clase Cartas
class Deck(Cartas):
    def __init__(self):
        # Invoca al constructor de clase Cartas
        Cartas.__init__(self)
        #crea una combionacion de 16 cartas para el tablero
        self.__deck_cartas = random.sample(self.getCartas(), 54)
        
    #regresa la configuracion del orden de las cartas del juego    
    def getDeck_cartas(self):
        deck_cartas = self.__deck_cartas
        return deck_cartas

#CLASE GRITON
#Clase que tiene la funcion de "PRODUCTOR"
#Hereda de la clase Thread
class Griton(threading.Thread):
    #Constructor
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        super(Griton,self).__init__()
        self.target = target
        #nombre del hilo
        self.name = name
        #Crea un objeto de tipo Deck()
        self.deck = Deck()
        #Se genera una baraja que es una combinacion aleatoria de
        #las cartas del juego
        self.configuracion_deck = self.deck.getDeck_cartas()
    #cuerpo del hilo
    def run(self):
        #Se hace referencia que se utilizaran las siguientes 
        #variables globales
        global winner
        global checked
        #imprime la configuracion del deck
        print(self.configuracion_deck)
        #while que se ejecuta mientras no exista ganador y
        #aun existan cartas para "gritar"
        while not winner and len(self.configuracion_deck)>0:
            #si el buffer no esta lleno entonces...   
            if not q.full():
                #se toma la primera carta del deck 
                item = self.configuracion_deck.pop()
                #se pone la carta en el buffer
                q.put(item)
                #se imprime operacion
                logging.debug('Grita : ' + str(item))
            #por otro lado si el buffer esta lleno
            else:
                #si el numero de elementos de la lista de 
                #los jugadores que han accedido al buffer
                #es menor al numero total de jugadores
                #entonces...
                if len(checked) <no_players:
                    #duerme el hilo un tiempo aleatorio
                    #time.sleep(random.random())
                    time.sleep(random.randint(1,2))

                #si no entonces...   
                else:
                    #quita el elemento del buffer
                    q.get()
                    #vuelve checked una lista vacia
                    checked = []
        return
    
#CLASE JUGADOR
#Clase que tiene la funcion de "CONSUMIDOR"
#Hereda de la clase Thread
class Jugador(threading.Thread):
    #Constructor
    def __init__(self, group=None, target=None, name=None,tb = None,
                 args=(), kwargs=None, verbose=None):
        super(Jugador,self).__init__()
        self.target = target
        #nombre del hilo
        self.name = name
        #Crea un objeto de tipo Tablero()
        self.tablero = Tablero()
        self.tb  = tb
        if not self.tb:
            #Guarda en una variable la configuracion del tablero
            self.tb = self.tablero.getTablero()
        self.marcadas = copy.deepcopy(self.tb)
        #imprime el tablero
        print(self.tb)
        return
    #cuerpo del hilo
    #regresa el tablero    
    def getTablero(self):
        tablero = self.tb
        return tablero
    def getMarcadas(self):
        tablero = self.marcadas
        return tablero
    def run(self):
        #Se hace referencia que se utilizaran las siguientes 
        #variables globales
        global checked
        global winner
        #while 
        while True:
            #si el buffer no esta vacio y el nombre del hilo
            #no esta en la lista de los hilos que ya accedieron al 
            #recurso del buffer entonces...
            if not q.empty() and self.name not in checked:
                #se obtiene el recurso del buffer
                item = q.get()
                q.put(item)
                #se imprime operacion
                logging.debug('Revisa ' + str(item))
                #si la carta del buffer se encuentra en
                #el tablero del jugador entonces...
                if item in self.marcadas: 
                    #se imprime operacion
                    logging.debug('Tiene ------->' + str(item))
                    #se remueve del tablero
                    indice = self.marcadas.index(item)
                    self.marcadas[indice] = "marcada"
                    #si el tablero ya quedo vacio entonces...
                    if self.marcadas.count("marcada") == 16:
                        #se asigna el nombre del ganador a winner
                        winner = self.name
                        #se imprime el nombre del ganador
                        logging.debug(' <------- GANO')
                #se agrega el nombre del jugador a la lista de
                #jugadores que ya accedieron al recurso del buffer
                checked.append(self.name)
                #duerme el hilo un tiempo aleatorio
                time.sleep(random.randint(1,2))
            
        return

if __name__ == '__main__':
    
    p = Griton(name='griton')
    c = Jugador(name='jg1')
    d = Jugador(name='jg2')
    
    p.start()
    time.sleep(2)
    c.start()
    time.sleep(2)
    d.start()
    time.sleep(2)