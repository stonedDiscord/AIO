import urllib2
import zipfile
import subprocess
import sys
import os

def pip_install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])

print "installing pyinstaller"
pip_install('pyinstaller')

print "installing ini"
pip_install('ini')
pip_install('iniconfig')

print "installing requests"
pip_install('requests')
import requests

print "please download and extract pybass from https://sourceforge.net/projects/pybass/files/pybass_055.zip/download"
print "you also have to rename pybass.py to __init__.py"

print "downloading bass"
filedata = urllib2.urlopen('http://us.un4seen.com/files/bass24.zip')  
datatowrite = filedata.read()

with open('bass24.zip', 'wb') as f:  
    f.write(datatowrite)
    f.close()

print "extracting bass"
zip_ref = zipfile.ZipFile('bass24.zip', 'r')
zip_ref.extract('bass.dll')
zip_ref.close()

if os.name == 'nt':
    print "downloading pyqt4"
    filedata = requests.get('http://raw.githubusercontent.com/dhb52/python-lib/master/PyQt4-4.11.4-cp27-cp27m-win32.whl')  
    datatowrite = filedata.content

    with open('PyQt4-4.11.4-cp27-cp27m-win32.whl', 'wb') as f:  
        f.write(datatowrite)
        f.close()
    

    print "installing pyqt4"
    pip_install('PyQt4-4.11.4-cp27-cp27m-win32.whl')
else:
    
    print "downloading bass-linux"
    filedata = urllib2.urlopen('http://www.un4seen.com/files/bass24-linux.zip')  
    datatowrite = filedata.read()

    with open('bass24-linux.zip', 'wb') as f:  
        f.write(datatowrite)
        f.close()

    print "extracting bass"
    zip_ref = zipfile.ZipFile('bass24-linux.zip', 'r')
    zip_ref.extract('libbass.so')
    zip_ref.close()
    
    
    print "downloading sip"
    filedata = urllib2.urlopen('http://www.riverbankcomputing.com/static/Downloads/sip/4.19.15/sip-4.19.15.tar.gz')  
    datatowrite = filedata.read()

    with open('sip.tar.gz', 'wb') as f:  
        f.write(datatowrite)
        f.close()
        
    print "downloading pyqt4"
    filedata = urllib2.urlopen('http://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-4.12.3/PyQt4_gpl_x11-4.12.3.tar.gz')  
    datatowrite = filedata.read()

    with open('pyqt4.tar.gz', 'wb') as f:  
        f.write(datatowrite)
        f.close()
    print "on linux you will have to build first sip and then pyqt4 yourself..."
    print "to do that, extract the sip.tar.gz and pyqt4.tar.gz and run 'python2 configure.py' then 'make' and lastly 'make install' in both folders"

print "done"
