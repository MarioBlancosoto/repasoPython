import gi
from gi.overrides import Gdk

gi.require_version('Gtk','3.0')
from gi.repository import Gtk


class VentanaPrincipal(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title="Exemplo Gtk.Escale e Gtk.Label")

         #creamos un box con spacing 6 llamado cajaV
        self.cajaV = Gtk.Box ( spacing =6)
        self.entrada = Gtk.Entry()
        #Añadimos la caja
        self.add(self.cajaV)

        #Creamos una label llamada lbetiqueta
        self.lbEtiqueta = Gtk.Label ()
        self.lbEtiqueta.set_markup("<span background = 'blue'></span>")
        self.cajaV.pack_start(self.lbEtiqueta,True,True,2)
        #Creación de objeto Scale,dandole orientación,minimo y máximo rango
        self.escala = Gtk.Scale(orientation =Gtk.Orientation.HORIZONTAL,adjustment = Gtk.Adjustment(0,0,100,5,10,0))
        #nos permite cambiarle el valor al escale en un rango
        self.escala.connect("change-value",self.on_escala_change_value)
        self.cajaV.pack_start(self.escala,True,True,2)
        self.cajaV.pack_start(self.entrada,True,True,1)
        self.connect("delete-event",Gtk.main_quit)
        self.show_all()
        self.set_size_request(400,400)

        self.entrada.connect("activate", self.entry_Enter,self.entrada)

    def entry_Enter(self,widget,enter):
        self.lbEtiqueta.modify_bg(Gtk.StateType.NORMAL, Gdk.color_parse(self.entrada.get_text()))

    def on_escala_change_value(self,control,tipoScroll,valor):


        self.lbEtiqueta.modify_bg(Gtk.StateType.NORMAL,Gdk.RGBA(0,0,valor))


if __name__ =="__main__":
    VentanaPrincipal()
    Gtk.main()