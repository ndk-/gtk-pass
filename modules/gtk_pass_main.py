import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk, Gio
from .gtk_pass_window import *

class GtkPass(Gtk.Application):
    def __init__(self, *args, **kwargs):
        super().__init__(
            *args,
            application_id="ask.later.gtkpass",
            **kwargs
        )
        self.window = None

    def do_startup(self):
        Gtk.Application.do_startup(self)
        self.set_menus()

    def do_activate(self):
        if not self.window:
            self.window = GtkPassWindow(application=self, title="Gtk Pass")

        self.window.set_default_size(700,500)
        self.window.present()

    def on_quit(self, action, params):
        self.quit()

    def set_menus(self):
        action = Gio.SimpleAction.new("quit", None)
        action.connect("activate", self.on_quit)
        self.add_action(action)

        builder = Gtk.Builder.new_from_file("templates/menu.xml")
        self.set_menubar(builder.get_object("gpass-menu"))
