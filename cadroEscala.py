import gi
gi.require_version("Gtk",'3.0')
from gi.repository import Gtk

class VentanaPrincipal:
    def __init__(self):
        fichero ="/home/local/DANIELCASTELAO/mblancosoto/PycharmProjects/Funcions/cadroEscala.glade"
        builder = Gtk.Builder()
        builder.add_from_file (fichero)
        self.ventanaPrincipal = builder.get_object("ventanaPrincipal")
        self.ventanaPrincipal.show_all()
        self.escala = builder.get_object("escala")
        self.escala.set_draw_value(True)
        self.ajustes = builder.get_object("ajustes")
        self.etq = builder.get_object("etq")
        sinais ={
            "ventanaPrincipal_destroy":Gtk.main_quit



        }
        builder.connect_signals(sinais)





if __name__ =="__main__":
    VentanaPrincipal()
    Gtk.main()