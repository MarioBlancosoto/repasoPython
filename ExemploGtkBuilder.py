import gi
gi.require_version("Gtk",'3.0')
from gi.repository import Gtk

class VentanaPrincipal:
    def __init__(self):
        fichero ="/home/local/DANIELCASTELAO/mblancosoto/PycharmProjects/Funcions/Interfaz.xml"
        builder = Gtk.Builder()
        builder.add_from_file (fichero)
        self.ventana = builder.get_object("window1")
        self.ventana.show_all()



if __name__ =="__main__":
    VentanaPrincipal()
    Gtk.main()

