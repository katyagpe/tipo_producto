# -*- coding: utf-8 -*-

#********************************************************#
# Modificación de productos.                             #
#********************************************************#
import os
import csv
import xmlrpclib
import re

HOST='demos2.4toangulogestionintegral.com'
PORT=80
DB='Oris'
USER='katya.salas@4toangulo.com'
PASS='8+qnDM!;tN"6K7H'
url ='http://%s:%d/xmlrpc/' % (HOST,PORT)

common_proxy = xmlrpclib.ServerProxy(url+'common')
object_proxy = xmlrpclib.ServerProxy(url+'object')
uid = common_proxy.login(DB,USER,PASS)


print "Entraste como  %s (uid:%d)" % (USER,uid)

def _update_mass(estado):
    if estado is True:
        path_file = './type.csv'
        archive = csv.DictReader(open(path_file))
        cont = 1


        for field in archive:


            productos = {
                'default_code':field['default_code'],
            }

            
            product = object_proxy.execute(DB,uid,PASS,'product.template','search',[('default_code','=',field['default_code'])])

            for default_code in product:
                users = object_proxy.execute(DB, uid, PASS,'product.template', 'read', product, [])
                
                for user in users:
                    print 'El tipo de producto es: ',user['type'],', con el la referencia interna: ',user['default_code'],"#ID: ",user['id'], "Costo: ",user['standard_price']

def __main__():
    print 'Ha comenzado el proceso'
    _update_mass(True)
    print 'Ha finalizado la carga tabla'
__main__()