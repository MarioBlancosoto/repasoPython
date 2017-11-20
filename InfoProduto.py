import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk


class VentanaPrincipal(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self,title ='Ui Python')
        self.set_border_width(10)
        self.cajaV  = Gtk.Box(orientation = Gtk.Orientation.VERTICAL,spacing =5)
        self.cajaLienzo = Gtk.Box(orientation = Gtk.Orientation.VERTICAL,spacing =3)
        self.lienzo = Gtk.Frame()
        self.etqProduto = Gtk.Label("Información sobre el producto ")
        self.cajaV.add(self.etqProduto)
        self.etqProduto.set_padding(5,10)
        self.lienzo.set_label("Datos Básicos")

        self.cajaV.add(self.lienzo)
        self.add(self.cajaV)
        self.lienzo.add(self.cajaLienzo)
        self.lblNome = Gtk.Label("Nombre")
        self.set_size_request(500,500)
        self.lblNome.set_margin_top(10)
        self.entradaNombre = Gtk.Entry()
        self.lblDescripcion = Gtk.Label("Descripción")
        self.entradaNombre.set_margin_right(80)
        self.lblNome.set_alignment(0,0)
        self.etqProduto.set_alignment(0,0)
        self.lblDescripcion.set_alignment(0,0)
        self.lblDescripcion.set_padding(0,10)
        self.cajaLienzo.add(self.lblNome)
        self.cajaLienzo.add(self.entradaNombre)
        self.cajaLienzo.add(self.lblDescripcion)


        self.show_all()
















if __name__ == "__main__":
            VentanaPrincipal()
            Gtk.main()
