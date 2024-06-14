#!/usr/bin/python
# -*- coding: utf-8 -*-

# move.py

from algoritmo import Kruskal
from salida import InterfazSalida
import wx

class Interfaz(wx.Frame):
    def __init__(self, parent, title, n):
        self.n = n
        super(Interfaz, self).__init__(parent, title=title)
        
        panel = wx.Panel(self)
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        
        grid_sizer = wx.GridSizer(n+1, n+1, 5, 5)  # +1 para incluir los labels de fila y columna
        
        # Añadir labels de columnas
        grid_sizer.Add(wx.StaticText(panel, label=""), 0, wx.ALIGN_CENTER)  # Espacio vacío en la esquina superior izquierda
        for x in range(n):
            grid_sizer.Add(wx.StaticText(panel, label=f"x:{x+1}"), 0, wx.ALIGN_CENTER)
        
        self.cajasDeTexto = []
        for y in range(n):
            # Añadir label de fila
            grid_sizer.Add(wx.StaticText(panel, label=f"y:{y+1}"), 0, wx.ALIGN_CENTER)
            row = []
            for x in range(n):
                text_ctrl = wx.TextCtrl(panel, value="0")
                row.append(text_ctrl)
                grid_sizer.Add(text_ctrl, 0, wx.EXPAND)
            self.cajasDeTexto.append(row)
        
        main_sizer.Add(grid_sizer, 0, wx.ALL | wx.EXPAND, 20)
        
        self.btAceptar = wx.Button(panel, label="Aceptar")
        main_sizer.Add(self.btAceptar, 0, wx.ALL | wx.CENTER, 10)
        
        panel.SetSizer(main_sizer)
        main_sizer.Fit(self)


        for x in range(n):
            for y in range(n):
                self.cajasDeTexto[x][y].Bind(wx.EVT_KEY_UP, self.copiar)
        self.Bind(wx.EVT_BUTTON, self.analizar, self.btAceptar)
        self.Centre()
        self.Show()

    def copiar(self, a):
        for x in range(self.n):
            for y in range(self.n):
                if(x == y):
                  self.cajasDeTexto[y][x].SetValue("0")
                else:
                  self.cajasDeTexto[y][x].SetValue(self.cajasDeTexto[x][y].GetValue())

    def analizar(self, a):
        entrada = []
        for x in range(self.n):
            entradaY = []
            for y in range(self.n):
                value = self.cajasDeTexto[x][y].GetValue()
                if value == '':  # Check for empty string
                    value = '0'  # Replace empty string with '0'
                entradaY.append(int(value))
            entrada.append(entradaY)
        kruska = Kruskal(entrada, self.n)
        kruska.solucionar()
        InterfazSalida(None, title='Algoritmo de Kruskal (Salida)', n=self.n, vectorMostrar=kruska.vectorSalida, vectori=entrada)


if __name__ == '__main__':
    app = wx.App()
    Interfaz(None, title='Algoritmo de Kruskal', n=5)
    app.MainLoop()
