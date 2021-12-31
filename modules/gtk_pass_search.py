from gi.repository import Gtk
from .pass_wrapper import *

@Gtk.Template(filename="templates/search.xml")
class GtkPassSearch(Gtk.Box):
    __gtype_name__ = "GtkPassSearch"
    gtkPassResults = Gtk.Template.Child()

    search_results = Gtk.ListStore(int, str)
    search_results_filtered = search_results.filter_new()
    
    search_filter = ""
    secret_change_handler = None

    def __init__(self):
        super()
        self.add_search_results()
        self.search_results_filtered.set_visible_func(self.filter_pass)
        self.gtkPassResults.set_model(self.search_results_filtered)

    def add_search_results(self):
        for each in enumerate(get_secrets()):
            self.search_results.append(each)

    def filter_pass(self, model, iter, data):
           return self.search_filter in model[iter][1]
    
    @Gtk.Template.Callback()
    def on_search_changed(self, entry):
        self.search_filter = entry.get_text()
        self.search_results_filtered.refilter()

    @Gtk.Template.Callback()
    def on_result_selected(self, selection):
        model, iterator = selection.get_selected()
        if (iterator is not None):
            self.secret_change_handler(model[iterator][1])
    
    def set_secret_change_handler(self, handler):
        self.secret_change_handler = handler
