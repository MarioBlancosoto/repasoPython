import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk


class VentanaPrincipal(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self,title ='Ui Python')
        self.set_border_width(10)
        self.cajaV  = Gtk.Box(orientation = Gtk.Orientation.VERTICAL,spacing =5)
        self.cajaLienzo = Gtk.Box(orientation = Gtk.Orientation.VERTICAL,spacing =3)
        self.cajaLienzo1 = Gtk.Box(orientation =Gtk.Orientation.VERTICAL,spacing =3)
        self.cajaFoto = Gtk.Box(orientation =Gtk.Orientation.HORIZONTAL,spacing=2)
        self.cajaCheckBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,spacing=2)
        self.cajaImpuestos = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,spacing=2)
        self.entradaImpuestos = Gtk.Entry()
        self.comboPrecio = Gtk.ComboBoxText()
        self.lblPromocion = Gtk.Label("Promoción")
        self.chkbtn1 = Gtk.RadioButton.new_with_label_from_widget(None,"Ninguno")
        self.chkbtn2 = Gtk.RadioButton.new_with_label_from_widget(self.chkbtn1,"Transporte Gratuito")
        self.chkbtn3 = Gtk.RadioButton.new_with_label_from_widget(self.chkbtn2,"Descuento 5%")
        self.bScroll = Gtk.ScrolledWindow()
        self.set_size_request(100,70)
        self.bScroll.set_margin_right(100)
        self.bScroll.set_policy(Gtk.PolicyType.NEVER,Gtk.PolicyType.ALWAYS)
        self.bScroll.set_margin_bottom(20)
        self.bScroll.set_margin_left(10)
        self.lblPromocion.set_alignment(0,0)
        self.lblPromocion.set_margin_top(20)
        self.comboPrecio.insert(0,"0","4%")
        self.comboPrecio.insert(1,"1","7%")
        self.comboPrecio.insert(2, "2", "16%")
        self.comboPrecio.insert(3, "3", "25%")
        self.lblPrecio = Gtk.Label("Precio")
        self.lblEuro = Gtk.Label("€")
        self.lblImpuestos = Gtk.Label("Impuestos")
        self.chkBox = Gtk.CheckButton()
        self.lblVisitas =Gtk.Label("Añadir contador de visitas")
        self.botonFoto = Gtk.Button("Elegir...")
        self.lienzo = Gtk.Frame()
        self.lienzo1 = Gtk.Frame()
        self.etqProduto = Gtk.Label("Información sobre el producto ")
        self.entradaFoto = Gtk.Entry()
        self.cajaV.add(self.etqProduto)
        self.etqProduto.set_padding(5,10)
        self.lblEuro.set_margin_right(30)
        self.lienzo.set_label("Datos Básicos")
        self.lienzo1.set_label("Datos económicos")
        self.lblNome = Gtk.Label("Nombre")
        self.lblFoto = Gtk.Label("Foto")
        self.cajaV.add(self.lienzo)
        self.cajaV.add(self.lienzo1)
        self.add(self.cajaV)
        self.lienzo.add(self.cajaLienzo)
        self.lienzo1.add(self.cajaLienzo1)
        self.cajaFoto.add(self.lblFoto)
        self.cajaFoto.add(self.entradaFoto)
        self.cajaFoto.add(self.botonFoto)
        self.cajaCheckBox.add(self.chkBox)
        self.cajaCheckBox.add(self.lblVisitas)
        self.cajaImpuestos.add(self.lblPrecio)
        self.cajaImpuestos.add(self.entradaImpuestos)
        self.cajaImpuestos.add(self.lblEuro)
        self.cajaImpuestos.add(self.lblImpuestos)
        self.cajaImpuestos.add(self.comboPrecio)



        self.set_size_request(500,500)
        self.lblNome.set_margin_top(10)
        self.entradaNombre = Gtk.Entry()
        self.entradaTexto = Gtk.TextView()

        self.bScroll.add(self.entradaTexto)
        self.lblDescripcion = Gtk.Label("Descripción")
        self.entradaNombre.set_margin_right(100)
        self.lblNome.set_alignment(0,0)
        self.etqProduto.set_alignment(0,0)
        self.lblDescripcion.set_alignment(0,0)
        self.lblDescripcion.set_padding(0,10)
        self.lblFoto.set_alignment(0,0)
        self.lblFoto.set_margin_right(10)

        self.cajaLienzo.add(self.lblNome)
        self.cajaLienzo.add(self.entradaNombre)
        self.cajaLienzo.add(self.lblDescripcion)
        self.cajaLienzo.add(self.bScroll)
        self.cajaLienzo.add(self.cajaFoto)
        self.cajaLienzo.add(self.cajaCheckBox)
        self.cajaLienzo1.add(self.cajaImpuestos)
        self.cajaLienzo1.add(self.lblPromocion)
        self.cajaLienzo1.add(self.chkbtn1)
        self.cajaLienzo1.add(self.chkbtn2)
        self.cajaLienzo1.add(self.chkbtn3)
        self.show_all()
















if __name__ == "__main__":
            VentanaPrincipal()
            Gtk.main()
