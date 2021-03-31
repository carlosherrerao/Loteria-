# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 13:36:24 2019

@author: parka
"""

#CLASE CARTAS
#contiene una lista con todas las cartas posibles del juego
class imagenes:
    #constructor, no recibe parametros
    def __init__(self):
       
        #imagenes de fondo
        self.background = {
               'main' : r'Recursos\Imagenes\backgrounds\main.jpg',
               'errorconecion_servidor' : r'Recursos\Imagenes\backgrounds\errorconecion_servidor.png',
               'login' : r'Recursos\Imagenes\backgrounds\log_in.png',
               'nuevo_jugador' : r'Recursos\Imagenes\backgrounds\nuevo_jugador.png',
               'perfil' : r'Recursos\Imagenes\backgrounds\perfil.png',
               'historial' : r'Recursos\Imagenes\backgrounds\historial.png',
               'top' : r'Recursos\Imagenes\backgrounds\top.png',
               'seleccionar_tablero' : r'Recursos\Imagenes\backgrounds\seleccionar_tablero.png',
               'juego' : r'Recursos\Imagenes\backgrounds\juego.png',
               'winner' : r'Recursos\Imagenes\backgrounds\winner2.png'
              }
        #imagenes botones
        self.imagenes_botones = {
               'x_button' : r'Recursos\Imagenes\botones\x.png',
               'x_button_pressed' : r'Recursos\Imagenes\botones\x_pressed.png',
               'cuadro_texto' : r'Recursos\Imagenes\botones\cuadro_texto.png',
               'agregar_button' : r'Recursos\Imagenes\botones\agregar.png',
               'agregar_button_pressed' : r'Recursos\Imagenes\botones\agregar_pressed.png',
               
               'agregar_nuevo_button' : r'Recursos\Imagenes\botones\agregar_nuevo.png',
               'agregar_nuevo_button_pressed' : r'Recursos\Imagenes\botones\agregar_nuevo_pressed.png',
               
               'atras_button' : r'Recursos\Imagenes\botones\atras.png',
               'atras_button_pressed' : r'Recursos\Imagenes\botones\atras_pressed.png',
               
               'generar_otro_button' : r'Recursos\Imagenes\botones\generar_otro.png',
               'generar_otro_button_pressed' : r'Recursos\Imagenes\botones\generar_otro_pressed.png',
               
               'jugar_button' : r'Recursos\Imagenes\botones\jugar.png',
               'jugar_button_pressed' : r'Recursos\Imagenes\botones\jugar_pressed.png',
               
               'jugar_de_nuevo_button' : r'Recursos\Imagenes\botones\jugar_de_nuevo.png',
               'jugar_de_nuevo_button_pressed' : r'Recursos\Imagenes\botones\jugar_de_nuevo_pressed.png',
               
               'log_in_button' : r'Recursos\Imagenes\botones\log_in.png',
               'log_in_button_pressed' : r'Recursos\Imagenes\botones\log_in_pressed.png',
               
               'menu_principal_button' : r'Recursos\Imagenes\botones\menu_principal.png',
               'menu_principal_button_pressed' : r'Recursos\Imagenes\botones\menu_principal_pressed.png',
               
               'start_button' : r'Recursos\Imagenes\botones\start.png',
               'start_button_pressed' : r'Recursos\Imagenes\botones\start_pressed.png',
               
               'top_jugadores_button' : r'Recursos\Imagenes\botones\top_jugadores.png',
               'top_jugadores_button_pressed' : r'Recursos\Imagenes\botones\top_jugadores_pressed.png',
               
               'ver_historial_button' : r'Recursos\Imagenes\botones\ver_historial.png',
               'ver_historial_button_pressed' : r'Recursos\Imagenes\botones\ver_historial_pressed.png',
               
               'cancelar_button' : r'Recursos\Imagenes\botones\cancelar.png',
               'cancelar_button_pressed' : r'Recursos\Imagenes\botones\cancelar_pressed.png',
               
               'cerrar_sesion_button' : r'Recursos\Imagenes\botones\serrar_sesion.png',
               'cerrar_sesion_button_pressed' : r'Recursos\Imagenes\botones\serrar_sesion_pressed.png',

               'reintentar_button' : r'Recursos\Imagenes\botones\reintentar.png',
               'reintentar_button_pressed' : r'Recursos\Imagenes\botones\reintentar_pressed.png'
               }
        #lista que contiene todaslas cartas posibles en el juego
        self.imagenes_cartas = {
        'ACHILLES': {
        	'grande': r'Recursos\Imagenes\cartas\grande_achilles_standard-achilles.jpg', 
        	'mediana': r'Recursos\Imagenes\cartas\mediana_achilles_standard-achilles.jpg', 
        	'chica': r'Recursos\Imagenes\cartas\chica_achilles_standard-achilles.jpg', 
        	'chica_frijol': r'Recursos\Imagenes\cartas\chica_frijol_achilles_standard-achilles.jpg'},
        'AGNI': {
        	'grande': r'Recursos\Imagenes\cartas\grande_agni_standard-agni.jpg', 
        	'mediana': r'Recursos\Imagenes\cartas\mediana_agni_standard-agni.jpg', 
        	'chica': r'Recursos\Imagenes\cartas\chica_agni_standard-agni.jpg', 
        	'chica_frijol': r'Recursos\Imagenes\cartas\chica_frijol_agni_standard-agni.jpg'},
        'AH MUZEN CAB': {
        	'grande': r'Recursos\Imagenes\cartas\grande_ah_muzen_cab_standard-ah-muzen-cab.jpg', 
        	'mediana': r'Recursos\Imagenes\cartas\mediana_ah_muzen_cab_standard-ah-muzen-cab.jpg', 
        	'chica': r'Recursos\Imagenes\cartas\chica_ah_muzen_cab_standard-ah-muzen-cab.jpg', 
        	'chica_frijol': r'Recursos\Imagenes\cartas\chica_frijol_ah_muzen_cab_standard-ah-muzen-cab.jpg'},
        'AH PUCH': {
        	'grande': r'Recursos\Imagenes\cartas\grande_ah_puch_standard-ah-puch.jpg', 
        	'mediana': r'Recursos\Imagenes\cartas\mediana_ah_puch_standard-ah-puch.jpg', 
        	'chica': r'Recursos\Imagenes\cartas\chica_ah_puch_standard-ah-puch.jpg', 
        	'chica_frijol': r'Recursos\Imagenes\cartas\chica_frijol_ah_puch_standard-ah-puch.jpg'},
        'AMATERASU': {
        	'grande': r'Recursos\Imagenes\cartas\grande_amaterasu_standard-amaterasu.jpg', 
        	'mediana': r'Recursos\Imagenes\cartas\mediana_amaterasu_standard-amaterasu.jpg', 
        	'chica': r'Recursos\Imagenes\cartas\chica_amaterasu_standard-amaterasu.jpg', 
        	'chica_frijol': r'Recursos\Imagenes\cartas\chica_frijol_amaterasu_standard-amaterasu.jpg'},
        'ANUBIS': {
        	'grande': r'Recursos\Imagenes\cartas\grande_anubis_standard-anubis.jpg', 
        	'mediana': r'Recursos\Imagenes\cartas\mediana_anubis_standard-anubis.jpg', 
        	'chica': r'Recursos\Imagenes\cartas\chica_anubis_standard-anubis.jpg', 
        	'chica_frijol': r'Recursos\Imagenes\cartas\chica_frijol_anubis_standard-anubis.jpg'},
        'APHRODITE': {
        	'grande': r'Recursos\Imagenes\cartas\grande_aphrodite_standard-aphrodite.jpg', 
        	'mediana': r'Recursos\Imagenes\cartas\mediana_aphrodite_standard-aphrodite.jpg', 
        	'chica': r'Recursos\Imagenes\cartas\chica_aphrodite_standard-aphrodite.jpg', 
        	'chica_frijol': r'Recursos\Imagenes\cartas\chica_frijol_aphrodite_standard-aphrodite.jpg'},
        'APOLO': {
        	'grande': r'Recursos\Imagenes\cartas\grande_apollo_standard-apollo.jpg', 
        	'mediana': r'Recursos\Imagenes\cartas\mediana_apollo_standard-apollo.jpg', 
        	'chica': r'Recursos\Imagenes\cartas\chica_apollo_standard-apollo.jpg', 
        	'chica_frijol': r'Recursos\Imagenes\cartas\chica_frijol_apollo_standard-apollo.jpg'},
        'ARES': {
        	'grande': r'Recursos\Imagenes\cartas\grande_ares_standard-ares.jpg', 
        	'mediana': r'Recursos\Imagenes\cartas\mediana_ares_standard-ares.jpg', 
        	'chica': r'Recursos\Imagenes\cartas\chica_ares_standard-ares.jpg', 
        	'chica_frijol': r'Recursos\Imagenes\cartas\chica_frijol_ares_standard-ares.jpg'},
        'ARTEMIS': {
        	'grande': r'Recursos\Imagenes\cartas\grande_artemis_standard-artemis.jpg', 
        	'mediana': r'Recursos\Imagenes\cartas\mediana_artemis_standard-artemis.jpg', 
        	'chica': r'Recursos\Imagenes\cartas\chica_artemis_standard-artemis.jpg', 
        	'chica_frijol': r'Recursos\Imagenes\cartas\chica_frijol_artemis_standard-artemis.jpg'},
        'ATHENEA': {
        	'grande': r'Recursos\Imagenes\cartas\grande_athena_standard-athena.jpg', 
        	'mediana': r'Recursos\Imagenes\cartas\mediana_athena_standard-athena.jpg', 
        	'chica': r'Recursos\Imagenes\cartas\chica_athena_standard-athena.jpg', 
        	'chica_frijol': r'Recursos\Imagenes\cartas\chica_frijol_athena_standard-athena.jpg'},
        'BAKASURA': {
        	'grande': r'Recursos\Imagenes\cartas\grande_bakasura_standard-bakasura.jpg', 
        	'mediana': r'Recursos\Imagenes\cartas\mediana_bakasura_standard-bakasura.jpg', 
        	'chica': r'Recursos\Imagenes\cartas\chica_bakasura_standard-bakasura.jpg', 
        	'chica_frijol': r'Recursos\Imagenes\cartas\chica_frijol_bakasura_standard-bakasura.jpg'},
        'BELLONA': {
        	'grande': r'Recursos\Imagenes\cartas\grande_bellona_standard-bellona.jpg', 
        	'mediana': r'Recursos\Imagenes\cartas\mediana_bellona_standard-bellona.jpg', 
        	'chica': r'Recursos\Imagenes\cartas\chica_bellona_standard-bellona.jpg', 
        	'chica_frijol': r'Recursos\Imagenes\cartas\chica_frijol_bellona_standard-bellona.jpg'},
        'CERBERUS': {
        	'grande': r'Recursos\Imagenes\cartas\grande_cerberus_standard-cerberus.jpg', 
        	'mediana': r'Recursos\Imagenes\cartas\mediana_cerberus_standard-cerberus.jpg', 
        	'chica': r'Recursos\Imagenes\cartas\chica_cerberus_standard-cerberus.jpg', 
        	'chica_frijol': r'Recursos\Imagenes\cartas\chica_frijol_cerberus_standard-cerberus.jpg'},
        'CHAAC': {
        	'grande': r'Recursos\Imagenes\cartas\grande_chaac_standard-chaac.jpg', 
        	'mediana': r'Recursos\Imagenes\cartas\mediana_chaac_standard-chaac.jpg', 
        	'chica': r'Recursos\Imagenes\cartas\chica_chaac_standard-chaac.jpg', 
        	'chica_frijol': r'Recursos\Imagenes\cartas\chica_frijol_chaac_standard-chaac.jpg'},
        'CHANGE': {
        	'grande': r'Recursos\Imagenes\cartas\grande_change_standard-change.jpg', 
        	'mediana': r'Recursos\Imagenes\cartas\mediana_change_standard-change.jpg', 
        	'chica': r'Recursos\Imagenes\cartas\chica_change_standard-change.jpg', 
        	'chica_frijol': r'Recursos\Imagenes\cartas\chica_frijol_change_standard-change.jpg'},
        'CU CHULAINN': {
        	'grande': r'Recursos\Imagenes\cartas\grande_cu_chulainn_standard-cu-chulainn.jpg', 
        	'mediana': r'Recursos\Imagenes\cartas\mediana_cu_chulainn_standard-cu-chulainn.jpg', 
        	'chica': r'Recursos\Imagenes\cartas\chica_cu_chulainn_standard-cu-chulainn.jpg', 
        	'chica_frijol': r'Recursos\Imagenes\cartas\chica_frijol_cu_chulainn_standard-cu-chulainn.jpg'},
        'CUPID': {
        	'grande': r'Recursos\Imagenes\cartas\grande_cupid_standard-cupid.jpg', 
        	'mediana': r'Recursos\Imagenes\cartas\mediana_cupid_standard-cupid.jpg', 
        	'chica': r'Recursos\Imagenes\cartas\chica_cupid_standard-cupid.jpg', 
        	'chica_frijol': r'Recursos\Imagenes\cartas\chica_frijol_cupid_standard-cupid.jpg'},
        'FENRIR': {
        	'grande': r'Recursos\Imagenes\cartas\grande_fenrir_standard-fenrir.jpg', 
        	'mediana': r'Recursos\Imagenes\cartas\mediana_fenrir_standard-fenrir.jpg', 
        	'chica': r'Recursos\Imagenes\cartas\chica_fenrir_standard-fenrir.jpg', 
        	'chica_frijol': r'Recursos\Imagenes\cartas\chica_frijol_fenrir_standard-fenrir.jpg'},
        'FREYA': {
        	'grande': r'Recursos\Imagenes\cartas\grande_freya_standard-freya.jpg', 
        	'mediana': r'Recursos\Imagenes\cartas\mediana_freya_standard-freya.jpg', 
        	'chica': r'Recursos\Imagenes\cartas\chica_freya_standard-freya.jpg', 
        	'chica_frijol': r'Recursos\Imagenes\cartas\chica_frijol_freya_standard-freya.jpg'},
        'GANESHA': {
        	'grande': r'Recursos\Imagenes\cartas\grande_ganesha_standard-ganesha.jpg', 
        	'mediana': r'Recursos\Imagenes\cartas\mediana_ganesha_standard-ganesha.jpg', 
        	'chica': r'Recursos\Imagenes\cartas\chica_ganesha_standard-ganesha.jpg', 
        	'chica_frijol': r'Recursos\Imagenes\cartas\chica_frijol_ganesha_standard-ganesha.jpg'},
        'GUAN YU': {
        	'grande': r'Recursos\Imagenes\cartas\grande_guan_yu_standard-guan-yu.jpg', 
        	'mediana': r'Recursos\Imagenes\cartas\mediana_guan_yu_standard-guan-yu.jpg', 
        	'chica': r'Recursos\Imagenes\cartas\chica_guan_yu_standard-guan-yu.jpg', 
        	'chica_frijol': r'Recursos\Imagenes\cartas\chica_frijol_guan_yu_standard-guan-yu.jpg'},
        'HACHIMAN': {
        	'grande': r'Recursos\Imagenes\cartas\grande_hachiman_standard-hachiman.jpg', 
        	'mediana': r'Recursos\Imagenes\cartas\mediana_hachiman_standard-hachiman.jpg', 
        	'chica': r'Recursos\Imagenes\cartas\chica_hachiman_standard-hachiman.jpg', 
        	'chica_frijol': r'Recursos\Imagenes\cartas\chica_frijol_hachiman_standard-hachiman.jpg'},
        'HADES': {
        	'grande': r'Recursos\Imagenes\cartas\grande_hades_standard-hades.jpg', 
        	'mediana': r'Recursos\Imagenes\cartas\mediana_hades_standard-hades.jpg', 
        	'chica': r'Recursos\Imagenes\cartas\chica_hades_standard-hades.jpg', 
        	'chica_frijol': r'Recursos\Imagenes\cartas\chica_frijol_hades_standard-hades.jpg'},
        'HE BO': {
        	'grande': r'Recursos\Imagenes\cartas\grande_he_bo_standard-he-bo.jpg', 
        	'mediana': r'Recursos\Imagenes\cartas\mediana_he_bo_standard-he-bo.jpg', 
        	'chica': r'Recursos\Imagenes\cartas\chica_he_bo_standard-he-bo.jpg', 
        	'chica_frijol': r'Recursos\Imagenes\cartas\chica_frijol_he_bo_standard-he-bo.jpg'},
        'HERCULES': {
        	'grande': r'Recursos\Imagenes\cartas\grande_hercules_standard-hercules.jpg', 
        	'mediana': r'Recursos\Imagenes\cartas\mediana_hercules_standard-hercules.jpg', 
        	'chica': r'Recursos\Imagenes\cartas\chica_hercules_standard-hercules.jpg', 
        	'chica_frijol': r'Recursos\Imagenes\cartas\chica_frijol_hercules_standard-hercules.jpg'},
        'HOU YI': {
        	'grande': r'Recursos\Imagenes\cartas\grande_hou_yi_standard-hou-yi.jpg', 
        	'mediana': r'Recursos\Imagenes\cartas\mediana_hou_yi_standard-hou-yi.jpg', 
        	'chica': r'Recursos\Imagenes\cartas\chica_hou_yi_standard-hou-yi.jpg', 
        	'chica_frijol': r'Recursos\Imagenes\cartas\chica_frijol_hou_yi_standard-hou-yi.jpg'},
        'ISIS': {
        	'grande': r'Recursos\Imagenes\cartas\grande_isis_standard-isis.jpg', 
        	'mediana': r'Recursos\Imagenes\cartas\mediana_isis_standard-isis.jpg', 
        	'chica': r'Recursos\Imagenes\cartas\chica_isis_standard-isis.jpg', 
        	'chica_frijol': r'Recursos\Imagenes\cartas\chica_frijol_isis_standard-isis.jpg'},
        'IZANAMI': {
        	'grande': r'Recursos\Imagenes\cartas\grande_izanami_standard-izanami.jpg', 
        	'mediana': r'Recursos\Imagenes\cartas\mediana_izanami_standard-izanami.jpg', 
        	'chica': r'Recursos\Imagenes\cartas\chica_izanami_standard-izanami.jpg', 
        	'chica_frijol': r'Recursos\Imagenes\cartas\chica_frijol_izanami_standard-izanami.jpg'},
        'KALI': {
        	'grande': r'Recursos\Imagenes\cartas\grande_kali_standard-kali.jpg', 
        	'mediana': r'Recursos\Imagenes\cartas\mediana_kali_standard-kali.jpg', 
        	'chica': r'Recursos\Imagenes\cartas\chica_kali_standard-kali.jpg', 
        	'chica_frijol': r'Recursos\Imagenes\cartas\chica_frijol_kali_standard-kali.jpg'},
        'KING ARTHUR': {
        	'grande': r'Recursos\Imagenes\cartas\grande_king_arthur_standard-king-arthur.jpg', 
        	'mediana': r'Recursos\Imagenes\cartas\mediana_king_arthur_standard-king-arthur.jpg', 
        	'chica': r'Recursos\Imagenes\cartas\chica_king_arthur_standard-king-arthur.jpg', 
        	'chica_frijol': r'Recursos\Imagenes\cartas\chica_frijol_king_arthur_standard-king-arthur.jpg'},
        'KUKULKAN': {
        	'grande': r'Recursos\Imagenes\cartas\grande_kukulkan_standard-kukulkan.jpg', 
        	'mediana': r'Recursos\Imagenes\cartas\mediana_kukulkan_standard-kukulkan.jpg', 
        	'chica': r'Recursos\Imagenes\cartas\chica_kukulkan_standard-kukulkan.jpg', 
        	'chica_frijol': r'Recursos\Imagenes\cartas\chica_frijol_kukulkan_standard-kukulkan.jpg'},
        'KUZENBO': {
        	'grande': r'Recursos\Imagenes\cartas\grande_kuzenbo_standard-kuzenbo.jpg', 
        	'mediana': r'Recursos\Imagenes\cartas\mediana_kuzenbo_standard-kuzenbo.jpg', 
        	'chica': r'Recursos\Imagenes\cartas\chica_kuzenbo_standard-kuzenbo.jpg', 
        	'chica_frijol': r'Recursos\Imagenes\cartas\chica_frijol_kuzenbo_standard-kuzenbo.jpg'},
        'LOKI': {
        	'grande': r'Recursos\Imagenes\cartas\grande_loki_standard-loki.jpg', 
        	'mediana': r'Recursos\Imagenes\cartas\mediana_loki_standard-loki.jpg', 
        	'chica': r'Recursos\Imagenes\cartas\chica_loki_standard-loki.jpg', 
        	'chica_frijol': r'Recursos\Imagenes\cartas\chica_frijol_loki_standard-loki.jpg'},
        'MEDUSA': {
        	'grande': r'Recursos\Imagenes\cartas\grande_medusa_standard-medusa.jpg', 
        	'mediana': r'Recursos\Imagenes\cartas\mediana_medusa_standard-medusa.jpg', 
        	'chica': r'Recursos\Imagenes\cartas\chica_medusa_standard-medusa.jpg', 
        	'chica_frijol': r'Recursos\Imagenes\cartas\chica_frijol_medusa_standard-medusa.jpg'},
        'MERCURY': {
        	'grande': r'Recursos\Imagenes\cartas\grande_mercury_standard-mercury.jpg', 
        	'mediana': r'Recursos\Imagenes\cartas\mediana_mercury_standard-mercury.jpg', 
        	'chica': r'Recursos\Imagenes\cartas\chica_mercury_standard-mercury.jpg', 
        	'chica_frijol': r'Recursos\Imagenes\cartas\chica_frijol_mercury_standard-mercury.jpg'},
        'MERLIN': {
        	'grande': r'Recursos\Imagenes\cartas\grande_merlin_standard-merlin.jpg', 
        	'mediana': r'Recursos\Imagenes\cartas\mediana_merlin_standard-merlin.jpg', 
        	'chica': r'Recursos\Imagenes\cartas\chica_merlin_standard-merlin.jpg', 
        	'chica_frijol': r'Recursos\Imagenes\cartas\chica_frijol_merlin_standard-merlin.jpg'},
        'NEITH': {
        	'grande': r'Recursos\Imagenes\cartas\grande_neith_standard-neith.jpg', 
        	'mediana': r'Recursos\Imagenes\cartas\mediana_neith_standard-neith.jpg', 
        	'chica': r'Recursos\Imagenes\cartas\chica_neith_standard-neith.jpg', 
        	'chica_frijol': r'Recursos\Imagenes\cartas\chica_frijol_neith_standard-neith.jpg'},
        'NEMESIS': {
        	'grande': r'Recursos\Imagenes\cartas\grande_nemesis_standard-nemesis.jpg', 
        	'mediana': r'Recursos\Imagenes\cartas\mediana_nemesis_standard-nemesis.jpg', 
        	'chica': r'Recursos\Imagenes\cartas\chica_nemesis_standard-nemesis.jpg', 
        	'chica_frijol': r'Recursos\Imagenes\cartas\chica_frijol_nemesis_standard-nemesis.jpg'},
        'ODIN': {
        	'grande': r'Recursos\Imagenes\cartas\grande_odin_standard-odin.jpg', 
        	'mediana': r'Recursos\Imagenes\cartas\mediana_odin_standard-odin.jpg', 
        	'chica': r'Recursos\Imagenes\cartas\chica_odin_standard-odin.jpg', 
        	'chica_frijol': r'Recursos\Imagenes\cartas\chica_frijol_odin_standard-odin.jpg'},
        'POSEIDON': {
        	'grande': r'Recursos\Imagenes\cartas\grande_poseidon_standard-poseidon.jpg', 
        	'mediana': r'Recursos\Imagenes\cartas\mediana_poseidon_standard-poseidon.jpg', 
        	'chica': r'Recursos\Imagenes\cartas\chica_poseidon_standard-poseidon.jpg', 
        	'chica_frijol': r'Recursos\Imagenes\cartas\chica_frijol_poseidon_standard-poseidon.jpg'},
        'RA': {
        	'grande': r'Recursos\Imagenes\cartas\grande_ra_standard-ra.jpg', 
        	'mediana': r'Recursos\Imagenes\cartas\mediana_ra_standard-ra.jpg', 
        	'chica': r'Recursos\Imagenes\cartas\chica_ra_standard-ra.jpg', 
        	'chica_frijol': r'Recursos\Imagenes\cartas\chica_frijol_ra_standard-ra.jpg'},
        'RAMA': {
        	'grande': r'Recursos\Imagenes\cartas\grande_rama_standard-rama.jpg', 
        	'mediana': r'Recursos\Imagenes\cartas\mediana_rama_standard-rama.jpg', 
        	'chica': r'Recursos\Imagenes\cartas\chica_rama_standard-rama.jpg', 
        	'chica_frijol': r'Recursos\Imagenes\cartas\chica_frijol_rama_standard-rama.jpg'},
        'SUN WUKONG': {
        	'grande': r'Recursos\Imagenes\cartas\grande_sun_wukong_standard-sun-wukong.jpg', 
        	'mediana': r'Recursos\Imagenes\cartas\mediana_sun_wukong_standard-sun-wukong.jpg', 
        	'chica': r'Recursos\Imagenes\cartas\chica_sun_wukong_standard-sun-wukong.jpg', 
        	'chica_frijol': r'Recursos\Imagenes\cartas\chica_frijol_sun_wukong_standard-sun-wukong.jpg'},
        'SUSANO': {
        	'grande': r'Recursos\Imagenes\cartas\grande_susano_standard-susano.jpg', 
        	'mediana': r'Recursos\Imagenes\cartas\mediana_susano_standard-susano.jpg', 
        	'chica': r'Recursos\Imagenes\cartas\chica_susano_standard-susano.jpg', 
        	'chica_frijol': r'Recursos\Imagenes\cartas\chica_frijol_susano_standard-susano.jpg'},
        'TERRA': {
        	'grande': r'Recursos\Imagenes\cartas\grande_terra_standard-terra.jpg', 
        	'mediana': r'Recursos\Imagenes\cartas\mediana_terra_standard-terra.jpg', 
        	'chica': r'Recursos\Imagenes\cartas\chica_terra_standard-terra.jpg', 
        	'chica_frijol': r'Recursos\Imagenes\cartas\chica_frijol_terra_standard-terra.jpg'},
        'THANATOS': {
        	'grande': r'Recursos\Imagenes\cartas\grande_thanatos_standard-thanatos.jpg', 
        	'mediana': r'Recursos\Imagenes\cartas\mediana_thanatos_standard-thanatos.jpg', 
        	'chica': r'Recursos\Imagenes\cartas\chica_thanatos_standard-thanatos.jpg', 
        	'chica_frijol': r'Recursos\Imagenes\cartas\chica_frijol_thanatos_standard-thanatos.jpg'},
        'THE MORRIGAN': {
        	'grande': r'Recursos\Imagenes\cartas\grande_the_morrigan_standard-the-morrigan.jpg', 
        	'mediana': r'Recursos\Imagenes\cartas\mediana_the_morrigan_standard-the-morrigan.jpg', 
        	'chica': r'Recursos\Imagenes\cartas\chica_the_morrigan_standard-the-morrigan.jpg', 
        	'chica_frijol': r'Recursos\Imagenes\cartas\chica_frijol_the_morrigan_standard-the-morrigan.jpg'},
        'THOR': {
        	'grande': r'Recursos\Imagenes\cartas\grande_thor_standard-thor.jpg', 
        	'mediana': r'Recursos\Imagenes\cartas\mediana_thor_standard-thor.jpg', 
        	'chica': r'Recursos\Imagenes\cartas\chica_thor_standard-thor.jpg', 
        	'chica_frijol': r'Recursos\Imagenes\cartas\chica_frijol_thor_standard-thor.jpg'},
        'THOTH': {
        	'grande': r'Recursos\Imagenes\cartas\grande_thoth_standard-thoth.jpg', 
        	'mediana': r'Recursos\Imagenes\cartas\mediana_thoth_standard-thoth.jpg', 
        	'chica': r'Recursos\Imagenes\cartas\chica_thoth_standard-thoth.jpg', 
        	'chica_frijol': r'Recursos\Imagenes\cartas\chica_frijol_thoth_standard-thoth.jpg'},
        'VAMANA': {
        	'grande': r'Recursos\Imagenes\cartas\grande_vamana_standard-vamana.jpg', 
        	'mediana': r'Recursos\Imagenes\cartas\mediana_vamana_standard-vamana.jpg', 
        	'chica': r'Recursos\Imagenes\cartas\chica_vamana_standard-vamana.jpg', 
        	'chica_frijol': r'Recursos\Imagenes\cartas\chica_frijol_vamana_standard-vamana.jpg'},
        'XBALANQUE': {
        	'grande': r'Recursos\Imagenes\cartas\grande_xbalanque_standard-xbalanque.jpg', 
        	'mediana': r'Recursos\Imagenes\cartas\mediana_xbalanque_standard-xbalanque.jpg', 
        	'chica': r'Recursos\Imagenes\cartas\chica_xbalanque_standard-xbalanque.jpg', 
        	'chica_frijol': r'Recursos\Imagenes\cartas\chica_frijol_xbalanque_standard-xbalanque.jpg'},
        'YMIR': {
        	'grande': r'Recursos\Imagenes\cartas\grande_ymir_standard-ymir.jpg', 
        	'mediana': r'Recursos\Imagenes\cartas\mediana_ymir_standard-ymir.jpg', 
        	'chica': r'Recursos\Imagenes\cartas\chica_ymir_standard-ymir.jpg', 
        	'chica_frijol': r'Recursos\Imagenes\cartas\chica_frijol_ymir_standard-ymir.jpg'},
        'ZEUS': {
        	'grande': r'Recursos\Imagenes\cartas\grande_zeus_standard-zeus.jpg', 
        	'mediana': r'Recursos\Imagenes\cartas\mediana_zeus_standard-zeus.jpg', 
        	'chica': r'Recursos\Imagenes\cartas\chica_zeus_standard-zeus.jpg', 
        	'chica_frijol': r'Recursos\Imagenes\cartas\chica_frijol_zeus_standard-zeus.jpg'}
        }
        
    #metodo para regresar ruta de la imagen 
    def getruta(self,dios, tipo_carta):
        ruta = self.imagenes_cartas[dios][tipo_carta]
        return ruta
    #metodo para regresar ruta de la imagen   
    def getrutaBackground(self, nombre):
        ruta = self.background[nombre]
        return ruta
    #metodo para regresar ruta de la imagen
    def getrutaImagenBoton(self, nombre):
        ruta = self.imagenes_botones[nombre]
        return ruta