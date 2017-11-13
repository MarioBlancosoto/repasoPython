import gi

gi.require_version("Gtk","3.0")
from gi.repository import Gtk,Gio

class ventanaPrincipal(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Exemplo Gtk.Flowbox")

        self.set_default_size(500,350)
        self.set_border_width(5)

        cabeceira = Gtk.HeaderBar(title="Exemplo FlowBox")
        cabeceira.set_subtitle("Exemplo de headerBar")
        cabeceira.props.show_close_button = True

        btnBoton = Gtk.Button()
        icono = Gio.ThemedIcon(name ="mail-send-receive-symbolic")
        imaxe = Gtk.Image.new_from_gicon(icono,Gtk.IconSize.BUTTON)
        btnBoton.add(imaxe)
        cabeceira.pack_end(btnBoton)
        self.set_titlebar(cabeceira)
        self.connect("delete-event",Gtk.main_quit)
        self.show_all()


if __name__ == "__main__":
    ventanaPrincipal()
    Gtk.main()