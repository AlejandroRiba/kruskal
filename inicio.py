#!/usr/bin/python
# -*- coding: utf-8 -*-

from interfaz import  Interfaz
import wx

class Inicio(wx.Frame):
    #Función que renderiza la interfaz
    def __init__(self, parent, title):
        super(Inicio, self).__init__(parent, title=title, size=(200, 200)) #Inicialización de la interfaz

        panel = wx.Panel(self) #Creamos un panel para los componentes
        vbox = wx.BoxSizer(wx.VERTICAL) #Creamos un size vertical

        #Añadimos el texto estático
        self.mensaje=wx.StaticText(panel,label="Ingrese el numero de vertices ") #Creamos un label o texto
        vbox.Add(self.mensaje, flag=wx.ALL|wx.CENTER, border=10) #La ponemos en el panel

        #Añadimos el campo de texto
        self.texto=wx.TextCtrl(panel) 
        vbox.Add(self.texto, flag=wx.ALL|wx.CENTER, border=10)

        #Añadimos el botón
        self.boton = wx.Button(panel,label="aceptar") 
        vbox.Add(self.boton, flag=wx.ALL|wx.CENTER, border=10)

        #Asociamos el botón a un evento
        self.Bind(wx.EVT_BUTTON, self.aceptarc, self.boton) 

        #Configuramos el size del panel con los componentes
        panel.SetSizer(vbox)

        #Ajustamos el tamaño de la ventana al contenido
        vbox.Fit(self)

        self.Centre() #Centramos la interfaz
        self.Show() #Mostra al usuario la ventana
    
    #Función al ser apretado el botón
    def aceptarc(self,a):
        self.tamano=int(self.texto.GetValue()) #Obtenemos su valor y validamos que su valor sea entre 0 a 9
        if self.tamano <9 and self.tamano >0:
            #Mandamos a llamar la interfaz junto el dato que adquirimos
            app = wx.App()
            Interfaz(None, title='Tabla del Algoritmo de Kruskal',n=self.tamano)
            app.MainLoop()
        else:
            #Caso contrario mostramos mensaje de erro
            dlg = wx.MessageDialog(self, "Debe ingresar un número de vertices mayor a 0 y menor a 9", "Error al insertar datos", wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

if __name__ == '__main__':
    app = wx.App(False)
    Inicio(None, title='Algoritmo de Kruskal')
    app.MainLoop()