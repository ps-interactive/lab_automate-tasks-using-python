import subprocess
import time

print('PACKET ANALYZER: Starting tcpdump...')
#dumpprocess = subprocess.Popen(['sudo','tcpdump','-i','lo','-A','port','9090','-w','/home/ubuntu/test.pcap'], start_new_session=True, stdout=subprocess.PIPE)

print('PACKET ANALYZER: Trying to connec to the webserver...')

# Here, any tool connecting to the network can be added
#curlprocess = subprocess.run(['curl','-u', ':password123', '127.0.0.1:9090' ], stdout=subprocess.PIPE)
# print(curlprocess.stdout)

time.sleep(3)
#subprocess.check_call(["sudo","kill", str(dumpprocess.pid)])
time.sleep(2)

# print('PACKET ANALYZER: Analyzing packet capture...')
#scanprocess = subprocess.run(['tcpdump -r /home/ubuntu/test.pcap -A | grep \'href\|User-Agent\' >> /home/ubuntu/reconfile.txt'], shell=True)

print('PACKET ANALYZER: Complete. Results saved to reconfile.txt...')
