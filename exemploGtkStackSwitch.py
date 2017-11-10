import gi
import moduloGrid
gi.require_version("Gtk","3.0")
from gi.repository import Gtk




class ventanaPrincipal(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Exemplo Gtk.stack e Gtk.StackSwitcher")
        caixaV =Gtk.Box(orientation = Gtk.Orientation.VERTICAL,spacing = 6)
        self.add(caixaV)
        #Creación de stack
        stack = Gtk.Stack()
        stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        stack.set_transition_duration(1000)
        #Creación de check button
        chkPulsame = Gtk.CheckButton("Púlsame")
        stack.add_titled(chkPulsame,"Púlsame ","botón,púlsame")
        #Creación de label
        lbEtiqueta = Gtk.Label()
        #Escritura en la etiqueta
        lbEtiqueta.set_markup("<big>A nosa Etiqueta</big>")

        stack.add_titled(lbEtiqueta,"Etiqueta"," Etiqueta para mostrar ")
        #creamos o grid a partir do noso propio importado ao principio da clase
        grid = moduloGrid.GridModificado()
        #añadimos o titulo,"grid modificado",
        stack.add_titled(grid,"grid","grid modificado")
        stack_selector = Gtk.StackSwitcher()
        stack_selector.set_stack(stack)

        caixaV.pack_start(stack_selector,True,True,0)
        caixaV.pack_start(stack, True, True, 0)

        self.connect("delete-event",Gtk.main_quit)
        self.show_all()



if __name__ == "__main__":
            ventanaPrincipal()
            Gtk.main()