#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygtk
pygtk.require('2.0')
import gtk

from backend import wanna_send_email

class NoneForm():
	def __init__(self, username):

		self.username = username

		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_size_request(300,180)
		self.window.set_title("vaivai")
		self.window.connect("delete_event", lambda w,e: gtk.main_quit())
        
		vbox = gtk.VBox(False, 0)
		self.window.add(vbox)
		vbox.show()
		
		hbox1=gtk.HBox(False,0)
		vbox.add(hbox1)
		hbox1.show()
		textview = gtk.TextView()
		textbuffer=textview.get_buffer()
		textbuffer.set_text("  \n  Sorry, there isn't anybody who\n" 
							"   is able  acompany  u on ur trip")
							
		textview.set_editable(False)
		textview.set_cursor_visible(False)
		#textview.set_buffer(text.get_buffer())
		hbox1.pack_start(textview,True,False,0)
		textview.show()
		
		
							
		hbox2=gtk.HBox(False,0)
		vbox.add(hbox2)
		hbox2.show()
		hbox3=gtk.HBox(False,0)
		vbox.add(hbox3)
		hbox3.show()
		
		self.firstVariant=gtk.RadioButton(None,label="Inform me if smb appear")
		self.firstVariant.connect("toggled", self.callback, "Inform me if smb appear")
		#self.firstVariant.set_active(True)
		self.secondVariant=gtk.RadioButton(self.firstVariant,label="So pitty :(")
		self.secondVariant.connect("toggled", self.callback2,"So pitty :(")
		hbox3.pack_start(self.secondVariant,True,True,0)
		hbox2.pack_start(self.firstVariant, True, True, 0)
		self.firstVariant.show()
		self.secondVariant.show()
		
		hbox4=gtk.HBox(False,5)
		vbox.add(hbox4)
		hbox4.show()
		
		self.doneButton=gtk.Button("Done")
		self.doneButton.connect("clicked",self.doneButtonFunc)
		hbox4.pack_end(self.doneButton,False,False,5)
		self.doneButton.show()
		self.requestButton=gtk.Button("Another request")
		self.requestButton.connect("clicked",self.requestButtonFunc)
		hbox4.pack_end(self.requestButton,False,False,0)
		self.requestButton.show()
		
		#self.answer=self.callback(self.firstVariant)
		
		self.window.show()
        
	def callback(self, widget, data=None):
		return ("False", "True")[widget.get_active()]
		        
	def callback2(self, widget, data=None):
		pass
    
	def doneButtonFunc(self,widget):
		wanna_send_email(self.username, self.firstVariant.get_active())
		gtk.main_quit()

		
	def requestButtonFunc(self,widget):
		wanna_send_email(self.username, self.firstVariant.get_active())
		gtk.Widget.destroy(self.window)
        
def main():
    gtk.main()
    return 0
 
if __name__ == "__main__":
    print NoneForm('dbihbka2')
    main()
