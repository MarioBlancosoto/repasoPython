import gi

import moduloGrid

gi.require_version('Gtk','3.0')
from gi.repository import Gtk


class ventanaPrincipal(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Exemplo Gtk.Notebook")

        notebook = Gtk.Notebook()
        self.add(notebook)
        grid = moduloGrid.GridModificado()
        paxina1 = Gtk.Box()
        paxina1.set_border_width(10)
        paxina1.add(Gtk.Label("Páxina primeira"))
        notebook.append_page(paxina1,Gtk.Label('Título da Páxina'))

        paxina2 = Gtk.Box()
        paxina2.set_border_width(10)
        paxina2.add(Gtk.Label("Páxina con imaxe e título"))
        notebook.append_page(paxina2,Gtk.Image.new_from_icon_name("help-about",Gtk.IconSize.MENU))
        notebook.append_page(grid, Gtk.Label("Página Grid modificado"))

        self.connect("delete-event",Gtk.main_quit)
        self.show_all()




if __name__ == "__main__":
    ventanaPrincipal()
    Gtk.main()