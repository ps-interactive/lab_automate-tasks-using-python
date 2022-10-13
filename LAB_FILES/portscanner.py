import nmap
import subprocess

nm = nmap.PortScanner()
print('Scanning, please wait...')
nm.scan('127.0.0.1','9090')

if 'Werkzeug httpd' in nm['127.0.0.1']['tcp'][9090]['product']:
  print('Identified target service, attempt to auto guess the password..')
  # Add custom action code here
  print(p.stdout)
