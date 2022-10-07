import nmap
import subprocess

nm = nmap.PortScanner()
print('Scanning, please wait...')
#nm.scan('127.0.0.1','9090')

if 'Werkzeug httpd' in nm['127.0.0.1']['tcp'][9090]['product']:
  print('Identified target service, attempt to auto guess the password..')
  #p = subprocess.run(['hydra', '-l', '', '-P','dictionary.txt','-s','9090', '-w' , '4',   '-f', '127.0.0.1','http-get', '/'  ], stdout=subprocess.PIPE)
  print(p.stdout)
