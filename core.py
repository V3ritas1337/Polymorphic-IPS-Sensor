#!/usr/bin/en python 

import os
import logging #do later
import requests
import subprocess 
import shlex 
from datetime import datetime 

#Consider using bash inside python script 
##create user / group for file, as bash could lead to command injection 
#log here
subprocess.call("blacklist.sh")
date = datetime.now().strftime('%Y-%m-%d %H:%M') 
command = ("snort -A console -q -c /etc/snort/snort.conf -i vmnet8 -l /var/log/snort/ > ~/Desktop/DissertationWork/TechnicalWork/ipset-blacklist/%s").format(date)
#log here 
def whackListUpd():
		word = 'spp_reputation'
		#look for blacklisted IPs in logs

		with open('/var/log/snort/%s','r').format(date) as f: #issue: does not do seconds :( 
			lines = f.read().split("\n")
		#create a log with todays date
		for i,line in enmerate(lines):
			if word in line:
				s = word
				rec = s.split()
				src = rec[14] # or word in line.split() to search for full words
				#can I confirm each src IP will be array position 6?
				#using this for loop, it will look for the IP from the logs 
				with open('ip-blacklist.list','ab') as f:
					f.write(src)
					#appending the adaptive blacklist here
					#logging here
			else
				with open('ip-blacklist.list') as f:
					s = len(f.readlines())
					print("There are currently %s malicious IPs blocked! :)").format(s)
					#once data has been added locally, it will be uploaded to the web server below

with open('ip-blacklist.list', 'rb') as f:
    r = requests.post('http://localhost:8080', files={'ip-blacklist.list': f}



#some sort of authentication? --> unless anyone could upload a file? --> add to crit evaluation

#Example of splitting a line:

# >>> s='08/17-11:41:07.350700 [] [1:1000011:0] [] [Priority: 0] {TCP} 192.168.0.1:24586 -> 192.168.0.8:53804'
# >>> rec = s.split()
# >>> rec
# ['08/17-11:41:07.350700', '[]', '[1:1000011:0]', '[]', '[Priority:', '0]', '{TCP}', '192.168.0.1:24586', '->', '192.168.0.8:53804']
# >>> ts = rec[0]
# >>> src = rec[6]
# >>> dst = rec[7]

			
				#then append ip-blacklist.list locally with IP found and upload file to server
##use this, as you need to remove duplicate IPs, but doesn't snort do this anyway? 
# class appendFiles():
# 	lines_seen = set() # holds lines already seen
# 	outfile = open(outfilename, "w")
# 	for line in open(infilename, "r"):
#     		if line not in lines_seen: # not a duplicate
#         	outfile.write(line)
#         	lines_seen.add(line)
# 	outfile.close()







# if alert is True:
# 	rec = s.split()
# 	src = rec[6] #incoming IPs, outbound IPs could be done later
# 	with open("ip-blacklist.list.ip-blacklist.list", "a") as myfile:
# 		myfile.write(src)
# 	logging here
# else:
# 	pass
	
# try:
# 	if file (larger than current size) #this means IPs have been added extra via cron job
# 		append file locally and upload file to server
# 	else
# 		pass
# except:
# 	print logging info 
