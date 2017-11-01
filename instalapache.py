#!/usr/bin/python
#Juan Carlos Díaz Torres 01/11/2017.

import sys 
import subprocess
from subprocess import call


#configuracion de red
fr = open('/etc/network/interfaces', 'r')  #cambiar hola.txt por /etc/network/interfaces hay que ejecutar con sudo 
lineas = fr.readlines()
fr.close()
fw = open('/etc/network/interfaces', 'w') #cambiar hola.txt por /etc/network/interfaces hay que ejecutar con sudo
for line in lineas:
    if '/etc/network/interfaces.d' in line:
        fw.write('auto eth0\niface eth0 inet static\naddress 192.168.122.241\nnetmask 255.255.255.0\ngateway 192.168.122.1\ndns-nameservers 192.168.122.1')
    else:        
        fw.write(line)
fw.close()
call("sudo reboot", shell = True)

#instalacion de paquetes
call("sudo apt-get install apache2", shell = True) #shell true es para que ejecute el comando como en la shell
call("sudo apt-get install lynx", shell = True)
call("sudo apt-get install wget", shell = True)
call("sudo apt-get install curl", shell = True)

print "instalacion inicial realizada con exito"
          
