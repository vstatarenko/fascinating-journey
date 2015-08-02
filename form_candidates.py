#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import pygtk
pygtk.require('2.0')
import gtk

from form_dossier import FormDossier

class FormCandidates():
	def __init__(self, candidates_list):
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_title("Fascinating Trip")
		self.window.connect("delete_event", lambda w,e: gtk.main_quit())
		self.window.set_size_request(300, 300)

		box = gtk.VBox(False, 0)
		self.window.add(box)
		box.show()

		for x in candidates_list:
			frame = gtk.Frame()
			frame.set_shadow_type(gtk.SHADOW_OUT)
			box.add(frame)
			frame.show()
			event_box = gtk.EventBox()
			frame.add(event_box)
			event_box.show()
			label = gtk.Label(x[1]+','+x[2])
			event_box.add(label)
			label.show()
			event_box.set_events(gtk.gdk.BUTTON_PRESS_MASK)
			event_box.connect("button_press_event", self.click_frame, x)

		self.window.show()

	def click_frame(self, widget, event, data=None):
		gtk.Widget.destroy(self.window)
		FormDossier(data[0])

if __name__ == '__main__':
	FormCandidates([(1,'valek','tatarenko'),(2,'maka','uka'),(3,'vasya','smith')])
	gtk.main()