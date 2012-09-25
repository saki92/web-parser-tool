import pygtk
import gtk

class Display:
	def __init__(self, string):
		self.window=gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_default_size(600,200)
		self.sw=gtk.ScrolledWindow()
		self.sw.set_policy(gtk.POLICY_AUTOMATIC,gtk.POLICY_AUTOMATIC)
		self.textview=gtk.TextView()
		self.textbuffer=self.textview.get_buffer()
		
		self.textbuffer.set_text('\n'.join(string))
		self.sw.add(self.textview) 
		self.textview.show()
		self.sw.show()
		self.window.add(self.sw)
		self.window.show()

	def main(self):
		gtk.main()

#win=Display("hi saki")
#win.main()
