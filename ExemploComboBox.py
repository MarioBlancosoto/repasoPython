import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk


class VentanaPrincipal(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self,title="Exemplo ComboBox")

        caixaV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=5)
        #añadimos una lista ao modelo coa función append
        modelo = Gtk.ListStore(int,str)
        modelo.append([1, "Elemento 1"])
        modelo.append([2, "Elemento 2"])
        modelo.append([3, "Elemento 3"])
        modelo.append([4, "Elemento 4"])
        modelo.append([5, "Elemento 5"])
        modelo.append([6, "Elemento 6"])


        #engadimos o modelo no momento de crealo comboBox
        combo1 = Gtk.ComboBox.new_with_model_and_entry(modelo)
       # combo1.connect("changed",self.on_combo1_changed)

        #cando iniciemos o formulario con set entry decimoslle que se poñá no primeiro elemento
        combo1.set_entry_text_column(1)
        caixaV.pack_start(combo1,False,False,0)
        combo1.connect("key_press_event",self.on_combo1_keypressed)
        self.add(caixaV)
        self.connect("delete_event",Gtk.main_quit)
        self.show_all()


    def on_combo1_changed(self,combo):

        #o punteiro marca donde estamos en cada momento de la lista del combo
         punteiro = combo.get_active_iter()
         modelo = combo.get_model()
         if punteiro != None:

            # id_fila,texto = modelo[punteiro][:2]
             id_fila = modelo[punteiro][0]
             texto = modelo[punteiro][1]
             print("Selecionado :  ID= %d, texto = %s"%(id_fila,texto))
         else:
             entry = combo.get_child()
             print("Insertado: %s" % entry.get_text())
             modelo.append([7,entry.get_text()])



    def on_combo1_keypressed(self,combo,enter):
        modelo =combo.get_model()
        entry = combo.get_child()
        if  (enter.keyval ==65293):

          modelo.append([7,entry.get_text()])


if __name__ == "__main__":
    VentanaPrincipal()
    Gtk.main()
