# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 16:06:54 2020

@author: parka
"""

import pygame
from pygame.locals import *
from datetime import datetime
import pygame_textinput

import conexion
import Loterias_2
import imagenes_cartas
from importlib import reload

#fonts
font_titulo = pygame.font.Font(r"Recursos\Fonts\PenumbraFlareStdBold.otf", 45)
font_nombre = pygame.font.Font(r"Recursos\Fonts\PenumbraFlareStdBold.otf", 42)
font_nombre_jugadores_partida = pygame.font.Font(r"Recursos\Fonts\PenumbraFlareStdBold.otf", 32)
font_mensaje = pygame.font.Font(r"Recursos\Fonts\OpenSans-Regular.ttf", 40)
font_historial = pygame.font.Font(r"Recursos\Fonts\OpenSans-Regular.ttf", 30)
#colores
color_azul_1 = (11,27,53)
color_azul_2 = (24,40,65)
color_azul_3 = (18,45,88)
dorado = (166,126,0)
white = (255,255,255)

#imagenes de fondo
background = {'main' : r'Recursos\Imagenes\backgrounds\main.jpg',
              'login' : r'Recursos\Imagenes\backgrounds\log_in.png',
              'nuevo_jugador' : r'Recursos\Imagenes\backgrounds\nuevo_jugador.png',
              'perfil' : r'Recursos\Imagenes\backgrounds\perfil.png',
              'historial' : r'Recursos\Imagenes\backgrounds\historial.png',
              'top' : r'Recursos\Imagenes\backgrounds\top.png',
              'seleccionar_tablero' : r'Recursos\Imagenes\backgrounds\seleccionar_tablero.png',
              'juego' : r'Recursos\Imagenes\backgrounds\juego.png',
              'winner' : r'Recursos\Imagenes\backgrounds\winner2.png'}

#imagenes botones
x_button = pygame.image.load(r'Recursos\Imagenes\botones\x.png')
x_button_pressed = pygame.image.load(r'Recursos\Imagenes\botones\x_pressed.png')
    
agregar_button = pygame.image.load(r'Recursos\Imagenes\botones\agregar.png')
agregar_button_pressed = pygame.image.load(r'Recursos\Imagenes\botones\agregar_pressed.png')

agregar_nuevo_button = pygame.image.load(r'Recursos\Imagenes\botones\agregar_nuevo.png')
agregar_nuevo_button_pressed = pygame.image.load(r'Recursos\Imagenes\botones\agregar_nuevo_pressed.png')

atras_button = pygame.image.load(r'Recursos\Imagenes\botones\atras.png')
atras_button_pressed = pygame.image.load(r'Recursos\Imagenes\botones\atras_pressed.png')

generar_otro_button = pygame.image.load(r'Recursos\Imagenes\botones\generar_otro.png')
generar_otro_button_pressed = pygame.image.load(r'Recursos\Imagenes\botones\generar_otro_pressed.png')

jugar_button = pygame.image.load(r'Recursos\Imagenes\botones\jugar.png')
jugar_button_pressed = pygame.image.load(r'Recursos\Imagenes\botones\jugar_pressed.png')

jugar_de_nuevo_button = pygame.image.load(r'Recursos\Imagenes\botones\jugar_de_nuevo.png')
jugar_de_nuevo_button_pressed = pygame.image.load(r'Recursos\Imagenes\botones\jugar_de_nuevo_pressed.png')

log_in_button = pygame.image.load(r'Recursos\Imagenes\botones\log_in.png')
log_in_button_pressed = pygame.image.load(r'Recursos\Imagenes\botones\log_in_pressed.png')

menu_principal_button = pygame.image.load(r'Recursos\Imagenes\botones\menu_principal.png')
menu_principal_button_pressed = pygame.image.load(r'Recursos\Imagenes\botones\menu_principal_pressed.png')

start_button = pygame.image.load(r'Recursos\Imagenes\botones\start.png')
start_button_pressed = pygame.image.load(r'Recursos\Imagenes\botones\start_pressed.png')

top_jugadores_button = pygame.image.load(r'Recursos\Imagenes\botones\top_jugadores.png')
top_jugadores_button_pressed = pygame.image.load(r'Recursos\Imagenes\botones\top_jugadores_pressed.png')

ver_historial_button = pygame.image.load(r'Recursos\Imagenes\botones\ver_historial.png')
ver_historial_button_pressed = pygame.image.load(r'Recursos\Imagenes\botones\ver_historial_pressed.png')

cancelar_button = pygame.image.load(r'Recursos\Imagenes\botones\cancelar.png')
cancelar_button_pressed = pygame.image.load(r'Recursos\Imagenes\botones\cancelar_pressed.png')

cerrar_sesion_button = pygame.image.load(r'Recursos\Imagenes\botones\serrar_sesion.png')
cerrar_sesion_button_pressed = pygame.image.load(r'Recursos\Imagenes\botones\serrar_sesion_pressed.png')

finalizar_button = pygame.image.load(r'Recursos\Imagenes\botones\finalizar.png')
finalizar_button_pressed = pygame.image.load(r'Recursos\Imagenes\botones\finalizar_pressed.png')

cuadro_texto = pygame.image.load(r'Recursos\Imagenes\botones\cuadro_texto.png')

rect_boton_01 = cuadro_texto.get_rect()
rect_boton_02 = cuadro_texto.get_rect()

rect_boton_1 = x_button.get_rect()
rect_boton_2 = agregar_button.get_rect()
rect_boton_3 = agregar_nuevo_button.get_rect()
rect_boton_4 = atras_button.get_rect()
rect_boton_5 = generar_otro_button.get_rect()
rect_boton_6 = jugar_button.get_rect()
rect_boton_7 = jugar_de_nuevo_button.get_rect()
rect_boton_8 = log_in_button.get_rect()
rect_boton_9 = menu_principal_button.get_rect()
rect_boton_10 = start_button.get_rect()
rect_boton_11 = top_jugadores_button.get_rect()
rect_boton_12 = ver_historial_button.get_rect()
#
rect_boton_13 = cancelar_button.get_rect()
rect_boton_14 = cerrar_sesion_button.get_rect()
rect_boton_15 = finalizar_button.get_rect()

def pantalla_error():
    pantalla = None
    click = False
    #imagen de fondo
    background_image = pygame.image.load(background['main'])
    botones = []
    
    rect_boton_1.topleft = [1276, 20]
    rect_boton_10.topleft = [460, 295]  
    
    botones.append({'imagen': x_button, 'imagen_pressed': x_button_pressed, 'rect': rect_boton_1, 'on_click': False})
    botones.append({'imagen': start_button, 'imagen_pressed': start_button_pressed, 'rect': rect_boton_10,'on_click': False})
    
    running = True
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
                pantalla = -1
            if event.type == MOUSEBUTTONDOWN:
                mouse = event.pos
                for boton in botones:
                    boton['on_click'] = boton['rect'].colliderect([mouse[0], mouse[1], 1, 1])
                click = True
            if event.type == MOUSEBUTTONUP:
                for boton in botones:
                    boton['on_click'] = False
                    
        if botones[0]['on_click'] and click:
            print("boton x pulsado")
            click = False           
            running = False
            pantalla = -1
        if botones[1]['on_click'] and click:
            print("boton start pulsado")
            click = False
            running = False
            pantalla = 2
        screen.blit(background_image, [0, 0])
        dibujar_botones(botones,screen)
        pygame.display.flip()     
        pygame.display.update()
        clock.tick(15)
    return pantalla
def pantalla_winner():
    global nombre_usuario
    global winner
    global tiempo
    global combinacion_tablero
    pantalla = None
    click = False
    fecha = datetime.now()
    #imagen de fondo
    background_image = pygame.image.load(background['winner'])
    botones = []
    
    rect_boton_1.topleft = [1276, 20]
    rect_boton_7.topleft = [163,367]  
    rect_boton_9.topleft = [163, 457]
    
    botones.append({'imagen': x_button, 'imagen_pressed': x_button_pressed, 'rect': rect_boton_1, 'on_click': False})
    botones.append({'imagen': jugar_de_nuevo_button, 'imagen_pressed': jugar_de_nuevo_button_pressed, 'rect': rect_boton_7,'on_click': False})
    botones.append({'imagen': menu_principal_button, 'imagen_pressed': menu_principal_button_pressed, 'rect': rect_boton_9,'on_click': False})
    if nombre_usuario == winner:
        conexion.agregar_partida(fecha, winner, tiempo)
    running = True
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
                pantalla = -1
            if event.type == MOUSEBUTTONDOWN:
                mouse = event.pos
                for boton in botones:
                    boton['on_click'] = boton['rect'].colliderect([mouse[0], mouse[1], 1, 1])
                click = True
            if event.type == MOUSEBUTTONUP:
                for boton in botones:
                    boton['on_click'] = False
                    
        if botones[0]['on_click'] and click:
            print("boton x pulsado")
            click = False           
            running = False
            pantalla = -1
        if botones[1]['on_click'] and click:
            print("boton ver jugar de nuevo pulsado")
        
            click = False
            running = False
            pantalla = 7
        if botones[2]['on_click'] and click:
            print("boton menu principal  pulsado")

            click = False
            running = False
            pantalla = 4
         
        screen.blit(background_image, [0, 0])
        dibujar_texto(163,188,382,60,winner,font_nombre, "topleft")
        dibujar_texto(163,278,382,60,tiempo,font_nombre, "topleft")
        dibujar_botones(botones,screen)
        pygame.display.flip()     
        pygame.display.update()
        clock.tick(15)
    return pantalla
def pantalla_jugar():
    global Loterias_2
    Loterias_2 = reload(Loterias_2)
    global nombre_usuario
    global combinacion_tablero
    global tiempo
    global winner
    print(winner)
    message =""
    A = Loterias_2.Griton(name='griton')

    B = Loterias_2.Jugador(name= nombre_usuario, tb = combinacion_tablero)

    C = Loterias_2.Jugador(name='CPU1')

    D = Loterias_2.Jugador(name='CPU2')

    pantalla = None
    click = False
    #imagen de fondo
    background_image = pygame.image.load(background['juego'])
    botones = []
    
    rect_boton_1.topleft = [1276, 20]
    rect_boton_15.topleft = [492, 687]

    botones.append({'imagen': x_button, 'imagen_pressed': x_button_pressed, 'rect': rect_boton_1, 'on_click': False})

    running = True
    start_time = pygame.time.get_ticks()
    A.start()
    B.start()
    C.start()
    D.start()
    fecha = datetime.now()
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
                pantalla = -1
            if event.type == MOUSEBUTTONDOWN:
                mouse = event.pos
                for boton in botones:
                    boton['on_click'] = boton['rect'].colliderect([mouse[0], mouse[1], 1, 1])
                click = True
            if event.type == MOUSEBUTTONUP:
                for boton in botones:
                    boton['on_click'] = False
        winner = Loterias_2.winner                 
        if botones[0]['on_click'] and click:
            print("boton x pulsado")
            click = False           
            running = False
            pantalla = -1

        if winner and len(botones) == 1:
            print("partida terminada")
            botones.append({'imagen': finalizar_button, 'imagen_pressed': finalizar_button_pressed, 'rect': rect_boton_15, 'on_click': False})

        if len(botones) > 1:
            if botones[1]['on_click'] and click:
                print("boton finalizar pulsado")
                click = False           
                running = False
                pantalla = 9        
        screen.blit(background_image, [0, 0])
        dibujar_botones(botones,screen)
        dibujar_carta(Loterias_2.q)
        dibujar_tablero(B.getTablero(),B.getMarcadas(),314,151,70, 111, 7)
        dibujar_tablero(C.getTablero(),C.getMarcadas(),666,151,70, 111, 7)
        dibujar_tablero(D.getTablero(),D.getMarcadas(),1018,151,70, 111, 7)
        dibujar_nombres(nombre_usuario,307,645,"CPU1",659,645,"CPU2",1011,645,315,34,font_nombre_jugadores_partida,"center")
        if not winner:
            time_since_enter = pygame.time.get_ticks() - start_time
            tiempo = millisegundos_to_minutes(time_since_enter)
        message = 'Tiempo: ' + tiempo
        dibujar_texto(0,63,1366,60,message,font_nombre, "center")
        pygame.display.flip()     
        pygame.display.update()
        clock.tick(30)
    combinacion_tablero = None 
    return pantalla
def pantalla_seleccionar_tablero():
    global Loterias_2
    Loterias_2 = reload(Loterias_2)    
    pantalla = None
    click = False
    #imagen de fondo
    background_image = pygame.image.load(background['seleccionar_tablero'])
    global combinacion_tablero
    global nombre_usuario
    botones = []
    
    rect_boton_1.topleft = [1276, 20]
    rect_boton_5.topleft = [163, 234]  
    rect_boton_6.topleft = [163, 324]
    rect_boton_4.topleft = [163, 414]

    botones.append({'imagen': x_button, 'imagen_pressed': x_button_pressed, 'rect': rect_boton_1, 'on_click': False})
    botones.append({'imagen': generar_otro_button, 'imagen_pressed': generar_otro_button_pressed, 'rect': rect_boton_12,'on_click': False})
    botones.append({'imagen': jugar_button, 'imagen_pressed': jugar_button_pressed, 'rect': rect_boton_11,'on_click': False})
    botones.append({'imagen': atras_button, 'imagen_pressed': atras_button_pressed, 'rect': rect_boton_4,'on_click': False})

    Tablero = Loterias_2.Tablero()
    combinacion_tablero = Tablero.getTablero()

    running = True
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
                pantalla = -1
            if event.type == MOUSEBUTTONDOWN:
                mouse = event.pos
                for boton in botones:
                    boton['on_click'] = boton['rect'].colliderect([mouse[0], mouse[1], 1, 1])
                click = True
            if event.type == MOUSEBUTTONUP:
                for boton in botones:
                    boton['on_click'] = False
                    
        if botones[0]['on_click'] and click:
            print("boton x pulsado")
            click = False           
            running = False
            pantalla = -1
        if botones[1]['on_click'] and click:
            print("boton generar nuevo  pulsado")
            click = False
            combinacion_tablero = Tablero.generar_nuevo()
        if botones[2]['on_click'] and click:
            print("boton jugar pulsado")
            click = False
            running = False
            pantalla = 8      
        if botones[3]['on_click'] and click:
            print("boton jugar pulsado")
            
            click = False
            running = False
            pantalla = 4    
        screen.blit(background_image, [0, 0])
        dibujar_texto(163,144,382,60,nombre_usuario,font_nombre, "topleft")
        dibujar_botones(botones,screen)
        dibujar_tablero(combinacion_tablero,None,788,103,91, 141, 7) 
        pygame.display.flip()     
        pygame.display.update()
        clock.tick(15)
    return pantalla 

def pantalla_menu_principal():
    pantalla = None
    click = False
    #imagen de fondo
    background_image = pygame.image.load(background['perfil'])
    global nombre_usuario
    botones = []
    
    rect_boton_1.topleft = [1276, 20]
    rect_boton_12.topleft = [163, 234]  
    rect_boton_11.topleft = [163, 324]
    rect_boton_6.topleft = [163, 414]
    rect_boton_14.topleft = [163, 504]

    botones.append({'imagen': x_button, 'imagen_pressed': x_button_pressed, 'rect': rect_boton_1, 'on_click': False})
    botones.append({'imagen': ver_historial_button, 'imagen_pressed': ver_historial_button_pressed, 'rect': rect_boton_12,'on_click': False})
    botones.append({'imagen': top_jugadores_button, 'imagen_pressed': top_jugadores_button_pressed, 'rect': rect_boton_11,'on_click': False})
    botones.append({'imagen': jugar_button, 'imagen_pressed': jugar_button_pressed, 'rect': rect_boton_6,'on_click': False})
    botones.append({'imagen': cerrar_sesion_button, 'imagen_pressed': cerrar_sesion_button_pressed, 'rect': rect_boton_14,'on_click': False})
    
    running = True
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
                pantalla = -1
            if event.type == MOUSEBUTTONDOWN:
                mouse = event.pos
                for boton in botones:
                    boton['on_click'] = boton['rect'].colliderect([mouse[0], mouse[1], 1, 1])
                click = True
            if event.type == MOUSEBUTTONUP:
                for boton in botones:
                    boton['on_click'] = False
                    
        if botones[0]['on_click'] and click:
            print("boton x pulsado")
            click = False           
            running = False
            pantalla = -1
        if botones[1]['on_click'] and click:
            print("boton ver historial pulsado")
            click = False
            running = False
            pantalla = 5
        if botones[2]['on_click'] and click:
            print("boton top jugadores  pulsado")
            click = False
            running = False
            pantalla = 6
        if botones[3]['on_click'] and click:
            print("boton jugar pulsado")
            click = False
            running = False
            pantalla = 7
        if botones[4]['on_click'] and click:
            print("boton cerrar sesion pulsado")
            click = False
            running = False
            global nombre_usuario
            nombre_usuario = ""
            pantalla = 2

        screen.blit(background_image, [0, 0])
        dibujar_texto(163,144,382,60,nombre_usuario,font_nombre, "topleft")
        dibujar_botones(botones,screen)
        pygame.display.flip()     
        pygame.display.update()
        clock.tick(15) 
    return pantalla   
def pantalla_ver_historial():
    pantalla = None
    click = False
    #imagen de fondo
    background_image = pygame.image.load(background['historial'])
    botones = []
    
    rect_boton_1.topleft = [1276, 20]
    rect_boton_4.topleft = [163, 234] 
    
    botones.append({'imagen': x_button, 'imagen_pressed': x_button_pressed, 'rect': rect_boton_1, 'on_click': False})
    botones.append({'imagen': atras_button, 'imagen_pressed': atras_button_pressed, 'rect': rect_boton_4,'on_click': False})
    global nombre_usuario
    consulta = conexion.consultar_partidas(nombre_usuario)
    running = True
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
                pantalla = -1
            if event.type == MOUSEBUTTONDOWN:
                mouse = event.pos
                for boton in botones:
                    boton['on_click'] = boton['rect'].colliderect([mouse[0], mouse[1], 1, 1])
                click = True
            if event.type == MOUSEBUTTONUP:
                for boton in botones:
                    boton['on_click'] = False
                    
        if botones[0]['on_click'] and click:
            print("boton x pulsado")
            click = False           
            running = False
            pygame.quit()
            quit()
        if botones[1]['on_click'] and click:
            print("boton atras pulsado")
            click = False
            running = False
            pantalla = 4
        screen.blit(background_image, [0, 0])
        dibujar_texto(163,144,382,60,nombre_usuario,font_nombre,"topleft")
        dibujar_botones(botones,screen)
        dibujar_historial(consulta)
        pygame.display.flip()     
        pygame.display.update()
        clock.tick(15)
    return pantalla 
def pantalla_menu_top_jugadores():
    pantalla = None
    click = False
    #imagen de fondo
    background_image = pygame.image.load(background['top'])
    botones = []
    
    rect_boton_1.topleft = [1276, 20]
    rect_boton_4.topleft = [163, 234] 
    
    botones.append({'imagen': x_button, 'imagen_pressed': x_button_pressed, 'rect': rect_boton_1, 'on_click': False})
    botones.append({'imagen': atras_button, 'imagen_pressed': atras_button_pressed, 'rect': rect_boton_4,'on_click': False})
    #global nombre_usuario
    #consulta = conexion.consultar_partidas(nombre_usuario)
    running = True
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
                pantalla = -1
            if event.type == MOUSEBUTTONDOWN:
                mouse = event.pos
                for boton in botones:
                    boton['on_click'] = boton['rect'].colliderect([mouse[0], mouse[1], 1, 1])
                click = True
            if event.type == MOUSEBUTTONUP:
                for boton in botones:
                    boton['on_click'] = False
                    
        if botones[0]['on_click'] and click:
            print("boton x pulsado")
            click = False           
            running = False
            pygame.quit()
            quit()
        if botones[1]['on_click'] and click:
            print("boton atras pulsado")
            click = False
            running = False
            pantalla = 4
        screen.blit(background_image, [0, 0])
        dibujar_texto(163,144,382,60,nombre_usuario,font_nombre,"topleft")
        dibujar_botones(botones,screen)
        #dibujar_historial(consulta)
        pygame.display.flip()     
        pygame.display.update()
        clock.tick(15)
    return pantalla 
def pantalla_inicio():
    pantalla = None
    click = False
    #imagen de fondo
    background_image = pygame.image.load(background['main'])
    botones = []
    
    rect_boton_1.topleft = [1276, 20]
    rect_boton_10.topleft = [460, 295]  
    
    botones.append({'imagen': x_button, 'imagen_pressed': x_button_pressed, 'rect': rect_boton_1, 'on_click': False})
    botones.append({'imagen': start_button, 'imagen_pressed': start_button_pressed, 'rect': rect_boton_10,'on_click': False})
    
    running = True
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
                pantalla = -1
            if event.type == MOUSEBUTTONDOWN:
                mouse = event.pos
                for boton in botones:
                    boton['on_click'] = boton['rect'].colliderect([mouse[0], mouse[1], 1, 1])
                click = True
            if event.type == MOUSEBUTTONUP:
                for boton in botones:
                    boton['on_click'] = False
                    
        if botones[0]['on_click'] and click:
            print("boton x pulsado")
            click = False           
            running = False
            pantalla = -1
        if botones[1]['on_click'] and click:
            print("boton start pulsado")
            click = False
            running = False
            pantalla = 2
        screen.blit(background_image, [0, 0])
        dibujar_botones(botones,screen)
        pygame.display.flip()     
        pygame.display.update()
        clock.tick(15)
    return pantalla
def pantalla_log_in():
    pantalla = None
    click = False
    #imagen de fondo
    background_image = pygame.image.load(background['login'])
    #text_input definicion
    usuario = pygame_textinput.TextInput()
    contraseña = pygame_textinput.TextInput()
    mensaje = ""
    botones = []

    rect_boton_1.topleft = [1276, 20]
    rect_boton_8.topleft = [163, 544]  
    rect_boton_3.topleft = [163, 624] 
    rect_boton_01.topleft = [163, 224]
    rect_boton_02.topleft = [163, 384]
    
    botones.append({'imagen': x_button, 'imagen_pressed': x_button_pressed, 'rect': rect_boton_1, 'on_click': False})
    botones.append({'imagen': log_in_button, 'imagen_pressed': log_in_button_pressed, 'rect': rect_boton_8,'on_click': False})
    botones.append({'imagen': agregar_nuevo_button, 'imagen_pressed': agregar_nuevo_button_pressed, 'rect': rect_boton_3,'on_click': False})
    botones.append({'imagen': cuadro_texto, 'imagen_pressed': cuadro_texto, 'rect': rect_boton_01,'on_click': False})
    botones.append({'imagen': cuadro_texto, 'imagen_pressed': cuadro_texto, 'rect': rect_boton_02,'on_click': False})
    
    cuadro_1 = False
    cuadro_2 = False
    
    running = True
    # main loop
    while running:
        events = pygame.event.get()
        # event handling, gets all event from the event queue
        for event in events:
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
                pantalla = -1
            if event.type == MOUSEBUTTONDOWN:
                mouse = event.pos
                for boton in botones:
                    boton['on_click'] = boton['rect'].colliderect([mouse[0], mouse[1], 1, 1])
                click = True
            if event.type == MOUSEBUTTONUP:
                for boton in botones:
                    boton['on_click'] = False
                    
        if botones[0]['on_click'] and click:
            print("boton x pulsado")
            click = False           
            running = False
            pantalla = -1
        if botones[1]['on_click'] and click:
            print("boton log in pulsado")
            #obtener texto usuario
            user = usuario.get_text()
            #obtener texto
            password = contraseña.get_text()
            #hacer consulkta si la pqassword pertenece al usuario
            if not user or  not password:
                mensaje = "Rellena los campos"
            elif conexion.validar_contraseña(user, password):
            #si contraseña coincide ir a pantalla de juego
                global nombre_usuario
                nombre_usuario = user
                click = False
                running = False
                pantalla = 4
            else:
                mensaje = "Datos incorrectos"
                
        if botones[2]['on_click'] and click:
            print("boton agregar nuevo pulsado")
            click = False
            running = False
            pantalla = 3
        if botones[3]['on_click'] and click:
            print("cuadro 1  pulsado")
            click = False
            cuadro_2 = False
            cuadro_1 = True
        if botones[4]['on_click'] and click:
            print("cuadro 2  pulsado")
            click = False
            cuadro_1 = False
            cuadro_2 = True
        elif click:
            cuadro_1 = False
            cuadro_2 = False
        screen.blit(background_image, [0, 0])
        dibujar_botones(botones,screen)
        dibujar_texto(163,464,382,60,mensaje,font_mensaje, "topleft")
        #---------------------text_input
        # Feed it with events every frame
        if cuadro_1 == True: 
            usuario.update(events)
        # Blit its surface onto the screen
        screen.blit(usuario.get_surface(), (163, 236))
        # Feed it with events every frame
        if cuadro_2 == True: 
            contraseña.update(events)
        # Blit its surface onto the screen
        screen.blit(contraseña.get_surface(), (163, 396))
        #---------------------text_input
        pygame.display.flip()     
        pygame.display.update()
        clock.tick(15)
    return pantalla 
def pantalla_agregar_usuario():
    pantalla = None
    click = False
    #imagen de fondo
    background_image = pygame.image.load(background['nuevo_jugador'])
    #text_input definicion
    usuario = pygame_textinput.TextInput()
    contraseña = pygame_textinput.TextInput()
    mensaje = ""
    botones = []
    
    rect_boton_1.topleft = [1276, 20]    
    rect_boton_2.topleft = [163, 544]  
    
    rect_boton_13.topleft = [163, 624]
    
    rect_boton_01.topleft = [163, 224]
    rect_boton_02.topleft = [163, 384]

    botones.append({'imagen': x_button, 'imagen_pressed': x_button_pressed, 'rect': rect_boton_1, 'on_click': False})
    botones.append({'imagen': agregar_button, 'imagen_pressed': agregar_button_pressed, 'rect': rect_boton_2,'on_click': False})
    botones.append({'imagen': cancelar_button, 'imagen_pressed': agregar_button_pressed, 'rect': rect_boton_13,'on_click': False})
    botones.append({'imagen': cuadro_texto, 'imagen_pressed': cuadro_texto, 'rect': rect_boton_01,'on_click': False})
    botones.append({'imagen': cuadro_texto, 'imagen_pressed': cuadro_texto, 'rect': rect_boton_02,'on_click': False})
    
    cuadro_1 = False
    cuadro_2 = False    
    running = True
    # main loop
    while running:
        events = pygame.event.get()
        # event handling, gets all event from the event queue
        for event in events:
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
                pantalla = -1
            if event.type == MOUSEBUTTONDOWN:
                mouse = event.pos
                for boton in botones:
                    boton['on_click'] = boton['rect'].colliderect([mouse[0], mouse[1], 1, 1])
                click = True
            if event.type == MOUSEBUTTONUP:
                for boton in botones:
                    boton['on_click'] = False
                   
        if botones[0]['on_click'] and click:
            print("boton x pulsado")
            click = False           
            running = False
            pantalla = -1

        if botones[1]['on_click'] and click:
            print("boton agregar pulsado")
            click = False
            #obtener texto usuario
            user = usuario.get_text()
            #obtener texto
            password = contraseña.get_text()
            #hacer consulkta si la pqassword pertenece al usuario
            if not user or  not password:
                mensaje = "Rellena los campos"
            else:
                conexion.agregar_usuario(user,password)
                running = False
                pantalla = 2
        if botones[2]['on_click'] and click:
            print("boton cancelar pulsado")
            click = False
            running = False
            pantalla = 2
        if botones[3]['on_click'] and click:
            print("cuadro 1  pulsado")
            click = False
            cuadro_2 = False
            cuadro_1 = True
        if botones[4]['on_click'] and click:
            print("cuadro 2  pulsado")
            click = False
            cuadro_1 = False
            cuadro_2 = True
        elif click:
            cuadro_1 = False
            cuadro_2 = False            
        screen.blit(background_image, [0, 0])
        dibujar_botones(botones,screen)
        dibujar_texto(163,464,382,60,mensaje,font_mensaje, "topleft")
        #---------------------text_input
        # Feed it with events every frame
        if cuadro_1 == True: 
            usuario.update(events)
        # Blit its surface onto the screen
        screen.blit(usuario.get_surface(), (163, 236))
        # Feed it with events every frame
        if cuadro_2 == True: 
            contraseña.update(events)
        # Blit its surface onto the screen
        screen.blit(contraseña.get_surface(), (163, 396))
        #---------------------text_input
        pygame.display.flip()     
        pygame.display.update()
        clock.tick(15)
    return pantalla  

def dibujar_tablero(tablero,marcadas,x,y,ancho_tarjeta, alto_tarjeta, espacio):
    if not marcadas:
        aux = 0
        for i in range(4):
            aux_x = x
            for j in range(4):
                imagen = pygame.image.load(imagenes.getruta(tablero[aux],'mediana'))
                
                screen.blit(imagen, [aux_x, y])
                aux_x = aux_x + ancho_tarjeta + espacio
                aux =aux+1
            y = y + alto_tarjeta + espacio
    else:
        aux = 0
        for i in range(4):
            aux_x = x
            for j in range(4):
                
                if marcadas[aux] == "marcada":
                    #dibujar_con_frijol
                    imagen = pygame.image.load(imagenes.getruta(tablero[aux], 'chica_frijol'))
                    screen.blit(imagen, [aux_x, y])
                else:
                    #dibujar_sin_frijol
                    imagen = pygame.image.load(imagenes.getruta(tablero[aux], 'chica'))
                    screen.blit(imagen, [aux_x, y])
                
                aux_x = aux_x + ancho_tarjeta + espacio
                
                aux =aux+1
            y = y + alto_tarjeta + espacio        
def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()
def dibujar_texto(x,y,w,h,texto,font,alineado):

    textSurf, textRect = text_objects(texto, font)
    #"topleft" "center"
    if alineado == "center":
        textRect.center = ((x+w/2), (y+h/2))
    elif alineado == "topleft":
        textRect.topleft = [x, y+((h-42)/2)]
        
    screen.blit(textSurf, textRect)
def dibujar_botones(lista_botones,screen):

    for boton in lista_botones:
        if boton['on_click']:
            screen.blit(boton['imagen_pressed'], boton['rect'])
        else:
            screen.blit(boton['imagen'], boton['rect'])
def dibujar_carta(q):
    if not q.empty():
        item = q.get()
        q.put(item)
        carta_gritada = pygame.image.load(imagenes.getruta(item, 'grande'))
        
        screen.blit(carta_gritada, [40, 203])
def dibujar_historial(consulta):
    numero_de_registros = len(consulta)
    top = numero_de_registros
    x = 822
    y = 254
    w = 382
    h = 50
    espacio = 20 
    if numero_de_registros> 6:
        top = 6
    for i in range(top):
        #mensaje = str(consulta[i][0]) + " / "+str(consulta[i][1])+" / "+str(consulta[i][2])
        mensaje = str(consulta[i][0].strftime('%d %b %Y')) + " / "+str(consulta[i][2])
        dibujar_texto(x,y,w,h,mensaje,font_historial,"center") 
        y = y + h+ espacio       
def dibujar_nombres(name1,x1,y1,name2,x2,y2,name3,x3,y3,w,h,font,align):
    #dibujar nombre 1
    dibujar_texto(x1,y1,w,h,name1,font,align)
    #dibujar nombre 2
    dibujar_texto(x2,y2,w,h,name2,font, align)
    #dibujar nombre 3
    dibujar_texto(x3,y3,w,h,name3,font, align)
def millisegundos_to_minutes(millis):
    millis = int(millis)
    seconds=(millis/1000)%60
    seconds = int(seconds)
    minutes=(millis/(1000*60))%60
    minutes = int(minutes)
    mensaje ="%d:%d" % (minutes, seconds)
    return mensaje
#inicia funciones pygame
pygame.init()

#pantalla completa
#screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen = pygame.display.set_mode((1366, 768))

#Caption de la ventana
pygame.display.set_caption('Juego de la lotería')

clock = pygame.time.Clock()
#icono del juego
gameIcon = pygame.image.load(r'Recursos\Imagenes\icono\gameIcon.png')
pygame.display.set_icon(gameIcon)

#obtener tamaño de la pantalla
info = pygame.display.Info()
screen_width,screen_height = info.current_w,info.current_h

#conexion pymongo
conexion = conexion.Conexion()
imagenes = imagenes_cartas.imagenes()
nombre_usuario = None
combinacion_tablero = None
winner = None
tiempo = None
pantalla = 0
while pantalla != -1 :
   if pantalla == 0:
      
      pantalla = pantalla_inicio()
      
   elif pantalla  == 1:
      
      pantalla = pantalla_error()
      
   elif pantalla  == 2:

      pantalla = pantalla_log_in()
      
   elif pantalla  == 3:

      pantalla = pantalla_agregar_usuario()
      
   elif pantalla  == 4:

      pantalla = pantalla_menu_principal()
      
   elif pantalla  == 5:

      pantalla = pantalla_ver_historial()
      
   elif pantalla  == 6:

      pantalla = pantalla_menu_top_jugadores()   
      
   elif pantalla  == 7:

      pantalla = pantalla_seleccionar_tablero()       
      
   elif pantalla  == 8:

      pantalla = pantalla_jugar()    
      
   elif pantalla  == 9:

      pantalla = pantalla_winner()    
         
pygame.quit()
quit()

    
 