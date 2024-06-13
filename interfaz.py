#!/usr/bin/python
# -*- coding: utf-8 -*-

# move.py

from algoritmo import Kruskal
from salida import InterfazSalida
import wx

class Interfaz(wx.Frame):
    def __init__(self, parent, title, n):
        self.zx = 90 + n * 120
        self.zy = 90 + n * 40
        self.n = n
        super(Interfaz, self).__init__(parent, title=title, size=(self.zx, self.zy))
        self.cajasDeTexto = []
        self.mensajex = []
        self.mensajey = []
        self.posix = 60
        self.posiy = 60
        self.caja = []
        for x in range(n):
            self.caja = []
            self.mensajex.append(wx.StaticText(self, id=-1, label="x:" + str(x+1), pos=(self.posix + x * 110 + 30, 40)))
            for y in range(n):
                self.mensajey.append(wx.StaticText(self, id=-1, label="y: " + str(y+1), pos=(35, self.posiy + y * 20 + 5)))
                self.caja.append(wx.TextCtrl(self, id=-1, value="0", pos=(self.posix + x * 110, self.posiy + y * 20)))
            self.cajasDeTexto.append(self.caja)
        self.btAceptar = wx.Button(self, -1, label="aceptar", pos=(60, 70 + n * 20))
        for x in range(n):
            for y in range(n):
                self.cajasDeTexto[x][y].Bind(wx.EVT_KEY_UP, self.copiar)
        self.Bind(wx.EVT_BUTTON, self.analizar, self.btAceptar)
        self.Move((800, 250))
        self.Show()

    def copiar(self, a):
        for x in range(self.n):
            for y in range(self.n):
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
