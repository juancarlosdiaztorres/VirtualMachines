#!/usr/bin/python
#Juan Carlos Díaz Torres 01/11/2017.
#Ejecutar como sudo Addwebhost.py nombreservidor
import sys 
import subprocess
from subprocess import call
import os


if os.geteuid() != 0:
    print 'Debes tener privilegios root para este script.'
    sys.exit(1)
else:
    print 'Bienvenido usuario root'
    
web = sys.argv[1]
call("sudo cp /etc/apache2/sites-available/000-default.conf /etc/apache2/sites-available/"+web+".conf", shell = True)

fr = open('/etc/apache2/sites-available/'+web+'.conf', 'r')
lineas = fr.readlines()
fr.close()

fw = open('/etc/apache2/sites-available/'+web+'.conf', 'w')
for line in lineas:
    if 'DocumentRoot /var/www' in line:
        fw.write('  DocumentRoot /var/www/'+web+'\n ServerName '+web+'.cdps\n   ServerAlias www.'+web+'.cdps\n')
    else:
        fw.write(line)
fw.close()

call('sudo a2ensite '+web+'.conf', shell = True)
call('service apache2 reload', shell = True)

fh = open('/etc/hosts', 'r+')
fh.write('\n    192.168.122.241 '+web+' www.'+web+'.cdps')

call('mkdir /var/www/'+web, shell = True)
fi = open('/var/www/'+web+'/index.html', 'w')
fi.write('// Fichero index.html de '+web+'\n    <html>\n    <h1> Servidor '+web+' </h1>\n </html>\n')
fi.close()

call('sudo a2ensite '+web+'.conf', shell = True)
call('service apache2 reload', shell = True)

print "web anadida correctamente"


