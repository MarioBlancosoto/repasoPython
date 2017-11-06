import gi
gi.require_version("Gtk",'3.0')
from gi.repository import Gtk

class VentanaPrincipal:
    def __init__(self):
        fichero ="/home/local/DANIELCASTELAO/mblancosoto/PycharmProjects/Funcions/exemploSaudo.glade"
        builder = Gtk.Builder()
        builder.add_from_file (fichero)
        self.txtSaudo = builder.get_object("txtSaudo")
        self.lblSaudo = builder.get_object("lblSaudo")

        sinais ={
            "ventanaPrincipal_destroy":Gtk.main_quit,

             "clickbtnAceptar":self.on_clicked_btnAceptar

        }
        builder.connect_signals(sinais)



    def on_clicked_btnAceptar(self,boton):
         """Rutina de tratamento do evento clicked do botón btnAceptar"""
         self.txtSaudo.get_text()
         #Tb podemos meter el get_Text en una variable -- nome = self.txtSaudo.get_text(),e imprimimos saudo
         self.lblSaudo.set_text("Hola "+self.txtSaudo.get_text())
         self.txtSaudo.set_text("")




if __name__ =="__main__":
    VentanaPrincipal()
    Gtk.main()