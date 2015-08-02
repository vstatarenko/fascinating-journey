#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import pygtk
pygtk.require('2.0')
import gtk

from backend import get_data

class FormDossier():
	def __init__(self, username):

		keys = ['Name','Lastname','Sex', 'Age', 'Social Sites']
		response = get_data(username)
		data = response['data']

		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_title("Fascinating Trip")
		self.window.connect("delete_event", lambda w,e: gtk.main_quit())
		self.window.set_size_request(300, 300)

		box = gtk.VBox(False, 0)
		self.window.add(box)
		box.show()

		for i in xrange(5):
			label = gtk.Label(keys[i]+': '+str(data[i]))
			box.pack_start(label, False, False, 5)
			label.show()

		self.window.show()

if __name__ == '__main__':
	FormDossier('dbihbka2')
	gtk.main()




