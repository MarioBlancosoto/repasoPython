import gi
from gi.overrides import Gdk

gi.require_version("Gtk",'3.0')
from gi.repository import Gtk

class VentanaPrincipal:
    def __init__(self):
        fichero ="/home/local/DANIELCASTELAO/mblancosoto/PycharmProjects/Funcions/cadroCores.glade"
        builder = Gtk.Builder()
        builder.add_from_file (fichero)
        self.ventanaPrincipal = builder.get_object("ventanaPrincipal")
        self.ventanaPrincipal.show_all()
        self.etq = builder.get_object("etq")
        self.btnVerde = builder.get_object("btnVerde")
        self.btnAmarelo = builder.get_object("btnAmarelo")
        self.btnVermello = builder.get_object("btnVermello")
        self.btnAzul = builder.get_object("btnAzul")
      
        sinais ={
            "ventanaPrincipal_destroy":Gtk.main_quit,

            "clickbtnVerde":self.on_clicked_btnAceptar,
            "clickbtnVermello": self.on_clicked_btnAceptar,
            "clickbtnAmarelo": self.on_clicked_btnAceptar,
            "clickbtnAzul": self.on_clicked_btnAceptar

        }
        builder.connect_signals(sinais)
        print(self.btnAzul)


    def on_clicked_btnAceptar(self, btnColor):
        print(btnColor)

        if btnColor == self.btnAzul :
           self.etq.modify_bg(Gtk.StateType.NORMAL,Gdk.Color(0,0,65430))
        if btnColor == self.btnAmarelo:
            self.etq.modify_bg(Gtk.StateType.NORMAL, Gdk.Color(0, 0, 65430))

        if btnColor == self.btnVermello:
            self.etq.modify_bg(Gtk.StateType.NORMAL, Gdk.Color(0, 0, 65430))
        else:
            self.etq.modify_bg(Gtk.StateType.NORMAL, Gdk.Color(0, 0, 65430))







if __name__ =="__main__":
    VentanaPrincipal()
    Gtk.main()