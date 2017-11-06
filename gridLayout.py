import gi

gi.require_version('Gtk','3.0')
from gi.repository import Gtk


class ventanaPrincipal(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Exemplo Gtk.gridLayout")

        self.rejilla = Gtk.Grid()
        self.btn1 = Gtk.Button(label= 'Resto')
        self.btn2 = Gtk.Button(label='Raiz Cadrada')
        self.btn3 = Gtk.Button(label='Potencia')
        self.etq = Gtk.Label('Resultado : ')
        self.entrada1 = Gtk.Entry()
        self.entrada2 = Gtk.Entry()
        self.add(self.rejilla)
        self.rejilla.add(self.btn1)
        self.rejilla.attach(self.entrada1,1,0,2,1)
        #pone la etiqueta,tomando como referencia el bt1n,en la posición bottom,después le damos el ancho y luego el alto
        self.rejilla.attach_next_to(self.etq,self.btn1,Gtk.PositionType.BOTTOM,1,2)
        self.rejilla.attach_next_to(self.entrada2,self.entrada1,Gtk.PositionType.BOTTOM,2,1)
        self.rejilla.attach_next_to(self.btn2,self.entrada2,Gtk.PositionType.BOTTOM,1,1)
        self.rejilla.attach_next_to(self.btn3,self.btn2,Gtk.PositionType.RIGHT,1,1)
        self.show_all()

        self.btn1.connect("clicked",self.resto)
        self.btn2.connect("clicked", self.resto)
        self.btn3.connect("clicked", self.resto)
    def resto(self,btnoperacion):

      if btnoperacion == self.btn1:
       operacion =  float(self.entrada1.get_text())%float(self.entrada2.get_text())
       self.etq.set_text(str(operacion))
      if btnoperacion == self.btn2:
       operacion = float(self.entrada1.get_text())**float(self.entrada2.get_text())
       self.etq.set_text(str(operacion))
      if btnoperacion == self.btn3:
        operacion = float(self.entrada1.get_text())**float(0.5)



if __name__ == "__main__":
    ventanaPrincipal()
    Gtk.main()