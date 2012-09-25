import pygtk
import gtk
import urllister, urllib
from callwin import Display

class Base():
	def entry_callback(self, widget, entry):
		entry_text=entry.get_text()
		self.urllist(entry_text)

	def __init__(self):
		self.window=gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_border_width(10)
		self.window.set_title("html parser")
		self.entry=gtk.Entry(max=0)
		self.button=gtk.Button("Click me")
		self.text=self.entry.get_text()
		self.button.connect("clicked",self.entry_callback,self.entry)
		self.vbox=gtk.VBox(False, 0)
		self.vbox.pack_start(self.entry,False,False,0)
		self.vbox.pack_start(self.button,False,False,0)
		self.entry.show()
		self.button.show()
		self.window.add(self.vbox)
		self.vbox.show()
		self.window.show()

	def main(self):
		gtk.main()

	def urllist(self,data):
		usock=urllib.urlopen(data)
		parser=urllister.UrlLister()
		parser.feed(usock.read())
		usock.close()
		parser.close()
		win=Display(parser.urls)
		win.main()
#		print parser.urls[1]
		#for url in parser.urls:
		#	print url

base=Base()
base.main()
#base.urllist()
