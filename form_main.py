#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygtk
pygtk.require('2.0')
import gtk

from backend import main_data
from datetime import date
from form_candidates import FormCandidates
from form5 import NoneForm
from form7 import PopularPlacesForm

class FormMain():
	def __init__(self, username):

		self.username = username

		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_title("Fascinating Trip")
		self.window.connect("delete_event", lambda w,e: gtk.main_quit())

		box = gtk.VBox(False,0)
		self.window.add(box)
		box.show()

		aframe = gtk.Frame('Journey place')
		box.add(aframe)
		aframe.show()
		a_hbox = gtk.HBox(False,0)
		aframe.add(a_hbox)
		a_hbox.show()

		self.a_place = gtk.Entry()
		a_hbox.pack_start(self.a_place,True,True,0)
		self.a_place.show()
		a_button = gtk.Button("(haven't choosed yet?)")
		a_button.connect("clicked", self.a_button_clicked)
		a_hbox.pack_start(a_button, True, True, 0)
		a_button.show()

		bframe = gtk.Frame("Aim of the trip")
		box.add(bframe)
		bframe.show()
		bbox = gtk.HBox(False,0)
		bframe.add(bbox)
		bbox.show()

		self.aim = gtk.combo_box_new_text()
		self.aim.append_text('communion')
		self.aim.append_text('joint pastime')
		self.aim.append_text('shoping')
		self.aim.append_text('sex-partner')
		self.aim.append_text('guide')
		self.aim.append_text('locals(to improve ur language)')
		self.aim.append_text('cohabitation')
		self.aim.append_text('others')
		bbox.pack_start(self.aim, True, True, 0)
		self.aim.show()

		cframe = gtk.Frame("Whom do u prefer spend ur trip with?")
		box.add(cframe)
		cframe.show()
		cbox = gtk.HBox(False,0)
		cframe.add(cbox)
		cbox.show()

		self.whom = "Male"
		self.male = gtk.RadioButton(None,"Male")
		self.male.connect("toggled", self.rb_callback, "Male")
		cbox.pack_start(self.male, True, True, 0)
		self.male.show()
		self.female = gtk.RadioButton(self.male,"Female")
		self.female.connect("toggled", self.rb_callback, "Female")
		cbox.pack_start(self.female, True, True, 0)
		self.female.show()
		self.group = gtk.RadioButton(self.male,"Group")
		self.group.connect("toggled", self.rb_callback, "Group")
		cbox.pack_start(self.group, True, True, 0)
		self.group.show()
		self.idm = gtk.RadioButton(self.male,"It's doesn't matter")
		self.idm.connect("toggled", self.rb_callback, "It's doesn't matter")
		cbox.pack_start(self.idm, True, True, 0)
		self.idm.show()


		dframe = gtk.Frame("How long is ur trip last?")
		box.add(dframe)
		dframe.show()

		dbox = gtk.HBox(False, 0)
		dframe.add(dbox)
		dbox.show()

		self._from = (date.today().year,date.today().month,date.today().day)
		self.to = (date.today().year,date.today().month,date.today().day)
		frame_from = gtk.Frame("from")
		calendar_from = gtk.Calendar()
		calendar_from.connect("day_selected", self.day_selected, 'from')
		frame_from.add(calendar_from)
		dbox.pack_start(frame_from, True, True, 0)
		frame_from.show()
		calendar_from.show()
		frame_to = gtk.Frame('to')
		calendar_to = gtk.Calendar()
		calendar_to.connect("day_selected", self.day_selected, 'to')
		frame_to.add(calendar_to)
		dbox.pack_start(frame_to, True, True, 0)
		frame_to.show()
		calendar_to.show()

		eframe = gtk.Frame("Describe ur interests and urself")
		box.add(eframe)
		eframe.show()
		ebox = gtk.HBox(False, 0)
		eframe.add(ebox)
		ebox.show()		
		
		self.textview = gtk.TextView()
		ebox.add(self.textview)
		self.textview.show()

		fframe = gtk.Frame("Do u want get a list of places of interesting ur trip-place?")
		box.add(fframe)
		fframe.show()
		fbox = gtk.HBox(False,0)
		fframe.add(fbox)
		fbox.show()

		self.fans = "yes"
		self.fyes = gtk.RadioButton(None,"yes")
		self.fyes.connect('toggled', self.rb_callback_f, "yes")
		fbox.pack_start(self.fyes, True, True, 0)
		self.fyes.show()
		self.fno = gtk.RadioButton(self.fyes,"no")
		self.fno.connect('toggled', self.rb_callback_f, "no")
		fbox.pack_start(self.fno, True, True, 0)
		self.fno.show()

		gframe = gtk.Frame("Do u want know about place of residence providing by locals?")
		box.add(gframe)
		gframe.show()
		gbox = gtk.HBox(False,0)
		gframe.add(gbox)
		gbox.show()

		self.gans = "yes"
		self.gyes = gtk.RadioButton(None,"yes")
		self.gyes.connect('toggled', self.rb_callback_g, "yes")
		gbox.pack_start(self.gyes, True, True, 0)
		self.gyes.show()
		self.gno = gtk.RadioButton(self.gyes,"no")
		self.gno.connect('toggled', self.rb_callback_g, "no")
		gbox.pack_start(self.gno, True, True, 0)
		self.gno.show()

		butbox = gtk.HBox(False, 0)
		box.add(butbox)
		butbox.show()

		buttonDone = gtk.Button("Done")
		buttonDone.connect("clicked", self.button_done)
		butbox.pack_start(buttonDone)
		buttonDone.show()
		buttonCancel = gtk.Button("Cancel")
		buttonCancel.connect("clicked", self.button_cancel)
		butbox.pack_start(buttonCancel)
		buttonCancel.show()

		self.window.show()


	def a_button_clicked(self, widget):
		PopularPlacesForm(self.a_place)


	def day_selected(self, widget, data):
		year, month, day = widget.get_date()
		if data == 'from':
			self._from = (year,month,day)
		else:
			self.to = (year,month,day)

	def get_active_text(self,combobox):
		model = combobox.get_model()
		active = combobox.get_active()
		if active < 0:
			return None
		return model[active][0]

	def rb_callback(self, widget, data=None):
		self.whom = data

	def rb_callback_f(self, widget, data=None):
		self.fans = data

	def rb_callback_g(self, widget, data=None):
		self.gans = data

	def button_done(self, widget):
		place = self.a_place.get_text()
		aim = self.get_active_text(self.aim)
		whom = self.whom
		from_y,from_m,from_d = self._from
		to_y,to_m,to_d = self.to
		start, end = self.textview.get_buffer().get_bounds()
		describe = self.textview.get_buffer().get_text(start,end)
		want_get = self.fans
		want_know = self.gans
		answer = main_data({'username':self.username, 'a':place,'b':aim,'c':whom,'from_y':from_y,'from_m':from_m,'from_d':from_d,'to_y':to_y,'to_m':to_m,'to_d':to_d,'e':describe,'f':want_get,'g':want_know})
		if answer['data'] == []:
			NoneForm(self.username)
		else:
			gtk.Widget.destroy(self.window)
			FormCandidates(answer['data'])

	def button_cancel(self,widget):
		gtk.Widget.destroy(self.window)

if __name__ == '__main__':
	FormMain('dbihbka2')
	gtk.main()
