#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx  # importando la libreria Wxpython (Manejo de interfaz grafica)
from PosicionP import PosicionP  # Importando la clase PosicionP (Guarda posiciones X y Y)

class InterfazSalida(wx.Frame):  # iniciando la clase del formulario
    # constructor recibe como parámetros el título de la ventana, la cantidad de elementos y el vector resultante
    def __init__(self, parent, title, n, vectorMostrar,vectori):
        # calculamos el tamaño de la ventana
        self.zx = 200 + n * 100
        self.zy = 500 + n * 30
        self.n = n
        self.vector = vectorMostrar
        self.vectori = vectori
        # llamamos al constructor de la clase padre
        super(InterfazSalida, self).__init__(parent, title=title, size=(self.zx, self.zy))
        self.caja = []
        self.cajasDeTexto = []
        self.mensajex = []
        self.mensajey = []
        self.posix = 60
        self.posiy = 60
        """ # creación de variables auxiliares para el manejo de los labels
        self.cajasDeTexto = []
        self.mensajex = []
        self.mensajey = []
        self.posix = 60
        self.posiy = 60
        self.caja = []
        for x in range(n):
            self.caja = []
            self.mensajex.append(wx.StaticText(self, id=-1, label="x:" + str(x + 1), pos=(self.posix + x * 75 + 30, 40)))
            for y in range(n):
                self.mensajey.append(wx.StaticText(self, id=-1, label="y: " + str(y + 1), pos=(35, self.posiy + y * 20 + 5)))
                self.caja.append(wx.StaticText(self, id=-1, label=str(vectori[x][y]), pos=(self.posix + x * 75, self.posiy + y * 20)))
            self.cajasDeTexto.append(self.caja) """
        self.caja = wx.StaticText(self, id=-1, label="Algoritmo de Kruskal", pos=(self.posix, 20))
        font = self.caja.GetFont()
        font.PointSize += 10  # Aumentar el tamaño de la fuente
        self.caja.SetFont(font)
        
        self.caja0 = wx.StaticText(self, id=-1, label="Grafica del algoritmo de Kruskal", pos=(self.posix, 60))
        font = self.caja0.GetFont()
        font.PointSize += 10  # Aumentar el tamaño de la fuente
        self.caja0.SetFont(font)
        
        peso_int = self.calcularPeso()
        peso = "El peso del grafo es de: " + str(peso_int)
        self.caja1 = wx.StaticText(self, id=-1, label=peso, pos=(self.posix, 100))
        font = self.caja1.GetFont()
        font.PointSize += 10  # Aumentar el tamaño de la fuente
        self.caja1.SetFont(font)
        
        # Dibujar Círculos
        self.Bind(wx.EVT_PAINT, self.pintar)  # evento para dibujar
        self.Centre()  # posición de la ventana en el escritorio
        self.Show()  # mostrar la ventana

    # función para calcular peso
    def calcularPeso(self):
        r = 0  # peso o costo
        for x in range(self.n):
            for y in range(self.n):
                if self.vector[x][y] != 0 and x < y:
                    r += int(self.vector[x][y])
        return r

    # dibujando los grafos
    def pintar(self, event):
        aux = []
        dc = wx.PaintDC(self)
        dc.Clear()
        font = dc.GetFont()
        font.SetPointSize(15)  # Ajusta el tamaño de la fuente según tus necesidades
        dc.SetFont(font)
        # Definir la posición de los nodos
        for x in range(self.n):
            if x == 0:
                px = 50
                py = self.zy - 230
            elif x == 7:
                px = 890
                py = self.zy - 230
            elif (x % 2 == 0):
                px = 120 + (120 * (x-1)) 
                py = self.zy - 100
            else:
                px = 120 + (120 * x)
                py = self.zy - 400
            dc.SetPen(wx.Pen(wx.Colour(0,0,255), 5))
            dc.SetBrush(wx.Brush(wx.Colour(255, 255, 255)))
            dc.DrawCircle(px, py, 30)  # Radio de 12 px
            dc.DrawText(str(x + 1), px + 5, py - 25)
            aux.append(PosicionP(x, px, py))

        # Dibujar las líneas
        pen = wx.Pen(wx.Colour(255, 0, 0), 3, wx.SOLID)
        pen1 = wx.Pen(wx.Colour(0, 0, 0), 1, wx.SOLID)
        for x in range(self.n):
            for y in range(self.n):
                if x < y:
                    x1, y1, x2, y2 = None, None, None, None
                    for z in aux:
                        if z.n == x:
                            x1 = z.x
                            y1 = z.y
                        if z.n == y:
                            x2 = z.x
                            y2 = z.y
                    
                    if x1 is not None and x2 is not None:
                        if self.vector[x][y] != 0:
                            dc.SetPen(pen)
                            dc.DrawLine(x1, y1, x2, y2)
                            # Ajuste de la posición del texto para que esté sobre la línea
                            text_x = int((x1 + x2) / 2) - 20  # Ajuste horizontal
                            text_y = int((y1 + y2) / 2) - 25  # Ajuste vertical
                            dc.DrawText(str(self.vector[x][y]), text_x, text_y)
                        elif self.vectori[x][y] != 0:
                            dc.SetPen(pen1)
                            dc.DrawLine(x1, y1, x2, y2)
                            # Ajuste de la posición del texto para que esté sobre la línea
                            text_x = int((x1 + x2) / 2) - 20  # Ajuste horizontal
                            text_y = int((y1 + y2) / 2) - 25  # Ajuste vertical
                            dc.DrawText(str(self.vectori[x][y]), text_x, text_y)

if __name__ == '__main__':
    app = wx.App()
    InterfazSalida(None, title='Algoritmo de Kruskal (Salida)', n=5, 
                  vectorMostrar=[[0, 0, 0, 6, 0], [0, 0, 3, 8, 5], [0, 3, 0, 0, 7], [6, 8, 0, 0, 9], [0, 5, 7, 9, 0]],
                  vectori=[[0, 2, 0, 6, 0], [2, 0, 3, 8, 5], [0, 3, 0, 0, 7], [6, 8, 0, 0, 9], [0, 5, 7, 9, 0]])
    app.MainLoop()
