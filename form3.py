#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygtk
pygtk.require('2.0')
import gtk

from backend import register
from form_main import FormMain

class RegistrationForm():	
    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_size_request(340, 450)
        self.window.set_title("Registration")
        self.window.connect("delete_event", lambda w,e: gtk.main_quit())
        
        vbox = gtk.VBox(False, 0)
        self.window.add(vbox)
        vbox.show()
        
        self.urltooltip=gtk.Tooltips()
        
        hbox1=gtk.HBox(False,87)
        vbox.add(hbox1)
        hbox1.show()
        firstnameLabel=gtk.Label("  first name")
        hbox1.pack_start(firstnameLabel,False,False,0)
        firstnameLabel.show()
        self.NameEntry=gtk.Entry()
        #self.NameEntry.connect("activate",self.enter_callback,self.NameEntry)
        hbox1.pack_start(self.NameEntry,False,False,0)
        self.NameEntry.show()
        
        hbox2=gtk.HBox(False,67)
        vbox.add(hbox2)
        hbox2.show()
        secondnameLabel=gtk.Label("  second name")
        hbox2.pack_start(secondnameLabel,False,False,0)
        secondnameLabel.show()
        self.SurnameEntry=gtk.Entry()
        hbox2.pack_start(self.SurnameEntry,False,False,0)
        self.SurnameEntry.show()
        
        hbox3=gtk.HBox(False,121)
        vbox.add(hbox3)
        hbox3.show()
        LoginLabel=gtk.Label("  login")
        hbox3.pack_start(LoginLabel,False,False,0)
        LoginLabel.show()
        self.LoginEntry=gtk.Entry()
        hbox3.pack_start(self.LoginEntry,False,False,0)
        self.LoginEntry.show()
        
        hbox4=gtk.HBox(False,89)
        vbox.add(hbox4)
        hbox4.show()
        PasswordLabel=gtk.Label("  password")
        hbox4.pack_start(PasswordLabel,False,False,0)
        PasswordLabel.show()
        self.PasswordEntry=gtk.Entry()
        self.PasswordEntry.set_visibility(False)
        hbox4.pack_start(self.PasswordEntry,False,False,0)
        self.PasswordEntry.show()
        
        hbox5=gtk.HBox(False,33)
        vbox.add(hbox5)
        hbox5.show()
        PasswordCheckLabel=gtk.Label("  confirm password")
        hbox5.pack_start(PasswordCheckLabel,False,False,0)
        PasswordCheckLabel.show()
        self.PasswordCheckEntry=gtk.Entry()
        self.PasswordCheckEntry.set_visibility(False)
        hbox5.pack_start(self.PasswordCheckEntry,False,False,0)
        self.PasswordCheckEntry.show()
        
        
        hbox6=gtk.HBox(False,118)
        vbox.add(hbox6)
        hbox6.show()
        EmailLabel=gtk.Label("  email")
        hbox6.pack_start(EmailLabel,False,False,0)
        EmailLabel.show()
        self.EmailEntry=gtk.Entry()
        hbox6.pack_start(self.EmailEntry,False,False,0)
        self.EmailEntry.show()
        
        hbox7=gtk.HBox(False,0)
        vbox.add(hbox7)
        hbox7.show()
        SexLabel=gtk.Label("  sex")
        hbox7.pack_start(SexLabel,False,False,0)
        SexLabel.show()
        
        hbox7b=gtk.HBox(False,0)
        vbox.add(hbox7b)
        hbox7b.show()
        
        self.male=gtk.RadioButton(None,label="male")
        self.male.connect("toggled", self.callback, "male")
        self.male.set_active(True)
        hbox7b.pack_start(self.male, True, True, 0)
        self.male.show()
        self.female=gtk.RadioButton(self.male,label="female")
        self.female.connect("toggled", self.callback, "female")
        hbox7b.pack_start(self.female, True, True, 0)
        self.female.show()
			
        hbox8=gtk.HBox(False,130)
        vbox.add(hbox8)
        hbox8.show()
        AgeLabel=gtk.Label("  age")
        hbox8.pack_start(AgeLabel,False,False,0)
        AgeLabel.show()
        self.AgeEntry=gtk.Entry()
        hbox8.pack_start(self.AgeEntry,False,False,0)
        self.AgeEntry.show()
        
       	hbox9=gtk.HBox(False,10)
        vbox.add(hbox9)
        hbox9.show()
        facebookLabel=gtk.Label("  ur social network URL")
        hbox9.pack_start(facebookLabel,False,False,0)
        
        
        facebookLabel.show()
        self.urlEntry=gtk.Entry()
        hbox9.pack_start(self.urlEntry,False,False,0)
        self.urltooltip.set_tip(self.urlEntry,"copy and paste here ur Social Network URL")
        self.urlEntry.show() 
        
        hbox10=gtk.HBox(False,0)
        vbox.add(hbox10)
        hbox10.show()
        self.finishButton=gtk.Button("Finish")
        self.finishButton.connect("clicked",self.finishButtonFunc)
        hbox10.pack_end(self.finishButton,True,False,0)
        self.finishButton.show()

        hbox11=gtk.HBox(False,0)
        vbox.add(hbox11)
        hbox11.show()
        self.errorLabel=gtk.Label(" Passwords don't math! try again")
        hbox11.pack_start(self.errorLabel,True,True,0)
        self.loginerror=gtk.Label(" This login is already register! Choose another one")
        hbox11.pack_start(self.loginerror,True,True,0)

        self.window.show()
        
    def callback(self, widget, data=None):
        self.sex = data
        
    def finishButtonFunc(self,widjet):
    	firstname=self.NameEntry.get_te    xt()
    	secondname=self.SurnameEntry.get_text()
    	login=self.LoginEntry.get_text()
    	password=self.PasswordEntry.get_text()
    	passwordchek=self.PasswordCheckEntry.get_text()
    	if self.passwordmatch(password,passwordchek):
            usersmail=self.EmailEntry.get_text()
            sex=self.sex
            age=self.AgeEntry.get_text()
            url=self.urlEntry.get_text()
            response = register(firstname, secondname, login, password, usersmail, age, sex, url)
            print response
            if response['status'] == 'error':
                """Значит пользователь существует и это я думаю ты сделаешь;)"""
                self.loginerror.show()
            elif response['status'] == 'ok':
                gtk.Widget.destroy(self.window)
                FormMain(login)

    def passwordmatch(self,password,confpassword):
        if (len(password)==len(confpassword)) and (password in confpassword):
            return True
        else:
        	self.errorLabel.show()
        	return False
        	
			
        
def main():
    gtk.main()
    return 0
 
if __name__ == "__main__":
    RegistrationForm()
    main()
