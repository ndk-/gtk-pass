from gi.repository import Gtk, Gdk
from .pass_wrapper import *


@Gtk.Template(filename="templates/buttons.xml")
class GtkPassButtons(Gtk.Box):
    __gtype_name__ = "GtkPassButtons"
    button_handlers = {}

    @Gtk.Template.Callback()
    def on_button_click(self, button):
        self.button_handlers[button.get_label()]()

    def set_button_handler(self, button, handler):
        self.button_handlers[button] = handler


@Gtk.Template(filename="templates/secret.xml")
class GtkPassSecret(Gtk.Dialog):
    __gtype_name__ = "GtkPassSecret"

    gtkPassSecretView = Gtk.Template.Child()

    @Gtk.Template.Callback()
    def on_close_click(self, button):
        self.destroy()

    def update_content(self, content):
        gtkPassBuffer = Gtk.TextBuffer()
        gtkPassBuffer.insert_at_cursor(content, -1)
        self.gtkPassSecretView.set_buffer(gtkPassBuffer)


@Gtk.Template(filename="templates/app.xml")
class GtkPassWindow(Gtk.ApplicationWindow):
    __gtype_name__ = "GtkPass"

    gtkPassSearch = Gtk.Template.Child()
    gtkPassButtons = Gtk.Template.Child()
    gtkStatusBar = Gtk.Template.Child()

    clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)

    selected_secret = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.gtkPassSearch.set_secret_change_handler(self.on_secret_change)
        self.gtkPassButtons.set_button_handler(
            'View', self.button_handler(self.on_view_press)
        )
        self.gtkPassButtons.set_button_handler(
            'Copy', self.button_handler(self.on_copy_press)
        )
        self.gtkPassButtons.set_button_handler('Exit', self.close)

        self.update_statusbar("thank you for using gtk pass")

    def on_secret_change(self, secret):
        self.selected_secret = secret

    def button_handler(self, function):
        def handler():
            if (self.selected_secret):
                try:
                    function()
                except:
                    self.update_statusbar("Oops, we've encountered an error")
            else:
                self.update_statusbar("Please select one of the secrets")
        return handler

    def on_view_press(self):
        self.show_secret_view(
            get_secret(
                self.selected_secret
            ).decode("utf-8")
        )

    def show_secret_view(self, content):
        gtkPassSecret = GtkPassSecret()
        gtkPassSecret.set_default_size(300, 200)
        gtkPassSecret.update_content(content)
        gtkPassSecret.show_all()

    def on_copy_press(self):
        secret = get_secret(self.selected_secret)
        first_line = secret.splitlines()[0].decode("utf-8")
        self.clipboard.set_text(first_line, -1)
        self.update_statusbar(
            self.selected_secret + " password was copied to a clipboard"
        )

    def update_statusbar(self, message):
        self.gtkStatusBar.set_markup("Status: " + message)
