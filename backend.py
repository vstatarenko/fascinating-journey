#!/usr/bin/env python
#-*- coding:utf-8 -*-

import urllib
import urllib2
import json

URI = 'http://journey-x4534em7.dotcloud.com/api/'
HEADERS = {'User-Agent' : 'Mozilla/5.0 (X11; U; Linux i686; ru; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3'}

def request_to_api(values):
	data = urllib.urlencode(values)
	request = urllib2.Request(URI, data, HEADERS)
	response = urllib2.urlopen(request)
	return json.loads(response.read())

def register(firstname,lastname,username,password,email,age,sex,social_sites):
	values = {'task':'register','firstname':firstname, 'lastname':lastname, 'username':username, 'password':password, 'email':email, 'age':age,'sex':sex,'social_sites':social_sites}
	return request_to_api(values)

def login(username, password):
	values = {'task':'login','login':username, 'password':password}
	return request_to_api(values)

def main_data(values):
	values.update({'task':'main_data'})
	return request_to_api(values)

def get_data(username):
	values = {'task':'get_data','username':username}
	return request_to_api(values)

def wanna_send_email(username, wanna):
	values = {'task':'send_email','username':username,'wanna':wanna}
	return request_to_api(values)	
	


if __name__ == '__main__':
	print register(**{'firstname':'Danil', 'lastname':'Petrov', 'username':'dbihbka2', 'password':'12', 'email':'ddbihbka@gmail.com', 'age':'21','sex':'female','social_sites':'http://facebook.com/daila'})
	print register(**{'firstname':'Vasya', 'lastname':'Petrov', 'username':'dbihbka', 'password':'12', 'email':'vasya@gmail.com', 'age':'21','sex':'female','social_sites':'http://facebook.com/vasya'})
	print login('dbihbka2','12')
	print get_data('dbihbka')
