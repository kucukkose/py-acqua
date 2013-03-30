#!/usr/bin/env python
# -*- coding: iso-8859-15 -*- 
#Copyright (C) 2005, 2008 Py-Acqua
#http://www.pyacqua.net
#email: info@pyacqua.net  
#
#   
#Py-Acqua is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#Py-Acqua is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Py-Acqua; if not, write to the Free Software
#    Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA



import gtk
import app
import utils
import tray
import time
import thread
import impostazioni
from dbwindow import BaseDBWindow, NotifyType

#giorni  = self.main_db.vars[5].get_text ()
def ThreadLoop(self): #Funzione che verrà eseguita dal thread
    num = 0
    while True:
        print "thread"
        for y in app.App.p_backend.select ("*", "manutenzione"):
            self.main_db.store.append ([y[0], y[1], y[2], y[3], y[4], y[5], y[6], y[7]])
        print y[0]
        time.sleep(2)
        

#Avviamo il thread
#thread.start_new_thread(ThreadLoop, (None,)) #start_new_thread8([Funzione_da_eseguire], [Argomenti_da_passare])

def alertManutenzione(db):
    for y in app.App.p_backend.select ("*", "manutenzione"):
            db.store.append ([y[0], y[1], y[2], y[3], y[4], y[5], y[6], y[7]])
            print y[0]




