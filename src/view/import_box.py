import traceback
try:
    from gi.repository import Gtk
    import common.file_util as file_util
    from common.decorators import exc_handler
except ImportError as msg:
    traceback.print_exc()


class Import_Box():


    @exc_handler
    def __init__(self):
        self.interface = file_util.get_user_interface(__file__,
                                        '../../data/glade/importbox.glade')
        self.load_widgets()
        self.list_store = Gtk.ListStore(str, str,str,str,str)
        self.listview.set_model(self.list_store)
        self.create_list_view()
        
    @exc_handler
    def load_widgets(self):
        self.import_box = self.interface.get_object('ImportBox')
        self.file_chooser = self.interface.get_object('ImportFileChooserButon')
        self.listview = self.interface.get_object('ImportChannelList')
        self.import_button = self.interface.get_object('ImportButton')
        self.cancel_button = self.interface.get_object('CancelButon')
        
    @exc_handler
    def add_channel_list_column(self, title, columnId):
		"""This function adds a column to the list view.
		First it create the Gtk.TreeViewColumn and then set
		some needed properties"""
						
		column = Gtk.TreeViewColumn(title, Gtk.CellRendererText()
			, text=columnId)
		column.set_resizable(True)		
		column.set_sort_column_id(columnId)
		self.listview.append_column(column)
    
    @exc_handler
    def create_list_view(self):
	    self.column_string = ["Description","Channel_Name","Splitter_Address","Splitter_Port","Thumbnail_Url",]
	    for i in range(0,len(self.column_string)):
	        self.add_channel_list_column(self.column_string[i],i)