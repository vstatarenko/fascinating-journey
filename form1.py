#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygtk
pygtk.require('2.0')
import gtk
 
class EntryExample:
    def enter_callback(self, widget, entry):
        entry_text = entry.get_text()
        print "Entry contents: %s\n" % entry_text
 
    def entry_toggle_editable(self, checkbutton, entry):
        entry.set_editable(checkbutton.get_active())
 
    def entry_toggle_visibility(self, checkbutton, entry):
        entry.set_visibility(checkbutton.get_active())
        
        
 
    def __init__(self):
        # Создаём новое окно
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_size_request(250, 150)
        self.window.set_title("Welcome")
        self.window.connect("delete_event", lambda w,e: gtk.main_quit())
 
        vbox1 = gtk.VBox(False, 0)
        self.window.add(vbox1)
        vbox1.show()
        #first horizontal line
        hbox1=gtk.HBox(False,35)
        vbox1.add(hbox1)
        hbox1.show()
        
        loginlabel=gtk.Label("login")
        hbox1.pack_start(loginlabel,True,False,0)
        loginlabel.show()
        
        self.logentry=gtk.Entry()
        self.logentry.set_max_length(50)
        self.logentry.connect("activate", self.enter_callback, self.logentry)
        hbox1.pack_start(self.logentry,True,False,0)
        self.logentry.show()
        
        #the second horithontal line      
        hbox2=gtk.HBox(False,2)
        vbox1.add(hbox2)
        hbox2.show()
        
        passwordlabel=gtk.Label("password")
        hbox2.pack_start(passwordlabel,True,True,0)
        passwordlabel.show()
        
        self.pasentry=gtk.Entry()
        self.pasentry.set_max_length(50)
        self.pasentry.connect("activate", self.enter_callback, self.pasentry)
        hbox2.pack_start(self.pasentry,True,False,0)
        self.pasentry.show()
        
        #the third horithontal line
        hbox3=gtk.HBox(False,0)
        #hbox3.set_border_width(10)
        vbox1.add(hbox3)
        hbox3.show()
        
        
        
        loginbutton=gtk.Button("Log In")
        loginbutton.connect("clicked",self.login_password_getting)
        hbox3.pack_end(loginbutton,True,False,0)
        loginbutton.show()
        
        #the fourth horizontal line
        hbox4=gtk.HBox(False,0)
        hbox4.set_border_width(10)
        vbox1.add(hbox4)
        hbox4.show()
        
        self.regbutton=gtk.Button("regisrate")
        self.regbutton.connect("activate",self.registrateButton)
        hbox4.pack_end(self.regbutton,False,False,0)
        self.regbutton.show()
        
        """entry = gtk.Entry()
        entry.set_max_length(50)
        entry.connect("activate", self.enter_callback, entry)
        entry.set_text("")
        entry.insert_text("", len(entry.get_text()))
        entry.select_region(0, len(entry.get_text()))
        vbox.pack_start(entry, True, True, 0)
        entry.show()
 
        hbox = gtk.HBox(False, 0)
        vbox.add(hbox)
        hbox.show()
 
       
 
        
 
        button = gtk.Button(stock=gtk.STOCK_CLOSE)
        button.connect("clicked", lambda w: gtk.main_quit())
        vbox.pack_start(button, True, True, 0)
        button.set_flags(gtk.CAN_DEFAULT)
        button.grab_default()
        button.show()"""
        self.window.show()

    def login_password_getting(self,widjet):
        username=self.logentry.get_text()
        password=self.pasentry.get_text()
        print username,password
    
    def registrateButton(self,widget,data=None):
		pass
		 
def main():
    gtk.main()
    return 0
 
if __name__ == "__main__":
    EntryExample()
    main()
 
		
