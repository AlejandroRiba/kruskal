#!/usr/bin/python
# -*- coding: utf-8 -*-

# move.py

import wx
from PosicionP import PosicionP
class InterfazSalida(wx.Frame):
  
    def __init__(self, parent, title, n,vectorMostrar):
    	self.zx=200+n*100
    	self.zy=600+n*30
    	self.n=n
        self.vector=vectorMostrar
        super(InterfazSalida, self).__init__(parent, title=title, size=(self.zx,self.zy))
        self.cajasDeTexto= []
        self.mensajex=[]
        self.mensajey=[]
        self.posix=60
        self.posiy=60
        self.caja=[]
        for x in xrange(0, n):
        	self.caja=[]
        	self.mensajex.append(wx.StaticText(self,id=-1,label="x:"+str(x),pos=(self.posix+x*75+30, 40)))
        	for y in xrange(0,n):
        		self.mensajey.append(wx.StaticText(self,id=-1,label="y: "+str(y),pos=(35, self.posiy+y*20+5)))
        	   	self.caja.append(wx.TextCtrl(self,id=-1,value=str(vectorMostrar[x][y]),pos=(self.posix+x*75, self.posiy+y*20)))
        	self.cajasDeTexto.append(self.caja)
        #######################################################################################
        ##################################Dibujar Circulos###################################3333
        self.Bind(wx.EVT_PAINT, self.pintar)
        self.Move((800, 250))
        self.Show()
    def pintar(self, a):
        auxX = []
        aux = []
        dc = wx.PaintDC(self)
        dc.Clear()
        dc.BeginDrawing()      
        for x in xrange(0, self.n):
            print "pintando: "+str(x)
            if x == 0:
                px = 50
                py = self.zy-300
                dc.DrawCircle(px, py, 30)
                dc.DrawText(str(x), px+5, py-10)
                aux.append(PosicionP(x, px, py))
                print "pintadoa: "+str(x)
            elif x == 7:
                px = 400
                py = self.zy-300
                dc.DrawCircle(px, py, 30)
                dc.DrawText(str(x),px+5,py-10)
                aux.append(PosicionP(x, px, py))
                print "pintadob: "+str(x)
            elif x == 1:
                px = 50+(80*x)+(10*x)
                py = self.zy-350
                dc.DrawCircle(px, py, 30)
                dc.DrawText(str(x), px+5, py-10)
                aux.append(PosicionP(x, px, py))
                print "pintadoc: "+str(x)
            elif (x % 2) == 0:
                px = 50+(40*x)+(10*x)
                py = self.zy-250
                dc.DrawCircle(px, py, 30)
                dc.DrawText(str(x),px+5,py-10)
                aux.append(PosicionP(x, px, py))
                print "pintadoc: "+str(x)
            elif (x % 2) == 1:
                px = 50+(40*x)+(20*x)
                py = self.zy-350
                dc.DrawCircle(px, py, 30)
                dc.DrawText(str(x), px+5, py-10)
                aux.append(PosicionP(x, px, py))
                print "pintadod: "+str(x)
        x1 = None
        x2 = None
        y1 = None
        y2 = None
        for x in xrange(0, self.n):
            for y in xrange(0, self.n):
                if self.vector[x][y] != 0:
                    if x < y:
                        for z in aux:
                            if z.n == x:
                                x1 = z.x
                                y1 = z.y
                            if z.n == y:
                                x2 = z.x
                                y2 = z.y
                        dc.DrawLine(x1+30, y1+15, x2-30, y2)
                        dc.DrawText(str(self.vector[x][y]),x1+((x2-x1)/2)+5,y1+((y2-y1)/2))
