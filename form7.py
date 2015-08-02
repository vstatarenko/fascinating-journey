#! /usr/bin/env python
# -*- coding :utf-8 -*-

import pygtk
pygtk.require('2.0')
import gtk

import random


class  PopularPlacesForm():
	def __init__(self,a_place):
		self.a_place = a_place

		self.places=["Grand Canyon: USA, Arizona","The Great Barrier Reef: Australia,Queensland",
		"Cape Town:Africa","Taj Mahal: India","Rocky Mountains:Canada","Machu Pikchu: Peru",
		"Egypt Pyramid: Egypt","Petra: Jordan","The Greet Wall: China","Iguassu Falls: Brazil,Parana"]
		self.nameplace1=random.choice(self.places)
		self.places.remove(self.nameplace1)
		self.nameplace2=random.choice(self.places)
		self.places.remove(self.nameplace2)
		self.nameplace3=random.choice(self.places)

		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_size_request(300,180)
		self.window.set_title("Popular Places")
		self.window.connect("delete_event", lambda w,e: gtk.main_quit())
		
		vbox=gtk.VBox(False,5)
		self.window.add(vbox)
		vbox.show()

		hbox1=gtk.HBox(False,0)
		vbox.add(hbox1)
		hbox1.show()
		label=gtk.Label("U should see this places in ur life")
		hbox1.pack_start(label,True,False,5)
		label.show()

		hbox2=gtk.HBox(False,0)
		vbox.add(hbox2)
		hbox2.show()
		self.place1=gtk.Button(self.nameplace1)
		self.place1.connect("clicked",self.callback1)
		hbox2.pack_start(self.place1,True,True,8)
		self.place1.show()

		hbox3=gtk.HBox(False,0)
		vbox.add(hbox3)
		hbox3.show()
		self.place2=gtk.Button(self.nameplace2)
		self.place2.connect("clicked",self.callback2)
		hbox3.pack_start(self.place2,True,True,8)
		self.place2.show()

		hbox3=gtk.HBox(False,0)
		vbox.add(hbox3)
		hbox3.show()
		self.place3=gtk.Button(self.nameplace3)
		self.place3.connect("clicked",self.callback3)
		hbox3.pack_start(self.place3,True,True,8)
		self.place3.show()

		

		self.window.show()
		

	def callback1(self,widget,data=None):
		self.a_place.set_text(self.nameplace1)
		gtk.Widget.destroy(self.window)

	def callback2(self,widget,data=None):
		self.a_place.set_text(self.nameplace2)
		gtk.Widget.destroy(self.window)

	def callback3(self,widget,data=None):
		self.a_place.set_text(self.nameplace3)
		gtk.Widget.destroy(self.window)

	



def main():
    gtk.main()
    return 0
 
if __name__ == "__main__":
    PopularPlacesForm("Bruge")
    main()
		



