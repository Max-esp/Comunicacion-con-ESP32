import tkinter as tk #para la interfaz grafica
from tkinter import ttk #para agregar mas estilos
import socket #para la comunicacion en red
import threading 
import time #para manejar el tiempo de espera

#------Configuracion------
IP_ESP32 = "192.168.20.10" #Reemplaza con la IP de tu ESP32
PUERTO = 80

#------CLASE DE DATOS------
class DatosSensor:
    def __init__(self, valor):
        self.valor = valor        