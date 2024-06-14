import wx
from PosicionP import PosicionP  # Asegúrate de que esta importación sea correcta

class InterfazSalida(wx.Frame):
    def __init__(self, parent, title, n, vectorMostrar, vectori):
        self.n = n
        self.vector = vectorMostrar
        self.vectori = vectori
        super(InterfazSalida, self).__init__(parent, title=title, size=(600, 800))

        self.init_ui()
        self.Centre()
        self.Show()

    def init_ui(self):
        panel = wx.Panel(self)
        main_sizer = wx.BoxSizer(wx.VERTICAL)

        self.cajasDeTexto = []
        grid_sizer = wx.GridSizer(self.n+1, self.n+1, 10, 10)
        
        # Empty corner for the grid
        grid_sizer.Add(wx.StaticText(panel, label=""), 0, wx.ALIGN_CENTER)
        
        # Adding column labels
        for x in range(self.n):
            grid_sizer.Add(wx.StaticText(panel, label=f"x:{x+1}"), 0, wx.ALIGN_CENTER)

        for y in range(self.n):
            # Adding row label
            grid_sizer.Add(wx.StaticText(panel, label=f"y:{y+1}"), 0, wx.ALIGN_CENTER)
            for x in range(self.n):
                label = wx.StaticText(panel, label=str(self.vectori[x][y]))
                grid_sizer.Add(label, 0, wx.ALIGN_CENTER)
                self.cajasDeTexto.append(label)
        
        main_sizer.Add(grid_sizer, 0, wx.ALL | wx.EXPAND, 20)

        self.caja = wx.StaticText(panel, label="Algoritmo de Kruskal", style=wx.ALIGN_CENTER)
        main_sizer.Add(self.caja, 0, wx.ALL | wx.CENTER, 10)

        self.caja0 = wx.StaticText(panel, label="Gráfica del algoritmo de Kruskal", style=wx.ALIGN_CENTER)
        main_sizer.Add(self.caja0, 0, wx.ALL | wx.CENTER, 10)

        peso_int = self.calcularPeso()
        peso = "El peso del grafo es de: " + str(peso_int)
        self.caja1 = wx.StaticText(panel, label=peso, style=wx.ALIGN_CENTER)
        main_sizer.Add(self.caja1, 0, wx.ALL | wx.CENTER, 10)

        panel.SetSizer(main_sizer)

        # Evento para dibujar el grafo
        self.Bind(wx.EVT_PAINT, self.on_paint)

    def calcularPeso(self):
        r = 0
        for x in range(self.n):
            for y in range(self.n):
                if self.vector[x][y] != 0 and x < y:
                    r += int(self.vector[x][y])
        return r

    def on_paint(self, event):
        dc = wx.PaintDC(self)
        dc.Clear()

        # Definir la posición de los nodos
        aux = []
        node_radius = 20
        node_spacing_x = 120
        node_spacing_y = 100
        offset_x = 50
        offset_y = 150

        for x in range(self.n):
            px = offset_x + (x % 3) * node_spacing_x
            py = offset_y + (x // 3) * node_spacing_y
            dc.DrawCircle(px, py, node_radius)
            dc.DrawText(str(x + 1), px - 5, py - 10)
            aux.append(PosicionP(x, px, py))

        # Dibujar las líneas
        pen_blue = wx.Pen("BLUE", 2, wx.SOLID)
        pen_black = wx.Pen("BLACK", 1, wx.SOLID)

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
                            dc.SetPen(pen_blue)
                            dc.DrawLine(x1, y1, x2, y2)
                            text_x = (x1 + x2) / 2
                            text_y = (y1 + y2) / 2
                            dc.DrawText(str(self.vector[x][y]), text_x, text_y)
                        elif self.vectori[x][y] != 0:
                            dc.SetPen(pen_black)
                            dc.DrawLine(x1, y1, x2, y2)
                            text_x = (x1 + x2) / 2
                            text_y = (y1 + y2) / 2
                            dc.DrawText(str(self.vectori[x][y]), text_x, text_y)

if __name__ == '__main__':
    app = wx.App(False)
    InterfazSalida(None, title='Algoritmo de Kruskal (Salida)', n=5, 
                  vectorMostrar=[[0, 0, 0, 6, 0], [0, 0, 3, 8, 5], [0, 3, 0, 0, 7], [6, 8, 0, 0, 9], [0, 5, 7, 9, 0]],
                  vectori=[[0, 2, 0, 6, 0], [2, 0, 3, 8, 5], [0, 3, 0, 0, 7], [6, 8, 0, 0, 9], [0, 5, 7, 9, 0]])
    app.MainLoop()
