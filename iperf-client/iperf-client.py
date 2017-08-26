#! /usr/bin/env python                                                                    
import iperf3                                                                             
import requests                                                                           
import sys, getopt, random, time, os                                                      
                                                                                          
meta_url = 'http://rancher-metadata/latest/self/stack/services/'                          
container = os.uname()[1]                                                                 
try:                                                                                      
  opts, args = getopt.getopt(sys.argv[1:],"s:l:")                                         
except getopt.GetoptError:                                                                
  print 'iperf-client.py -s <iperf-server> -l <logger-server>'                            
  sys.exit(2)                                                                             
                                                                                          
for opt, arg in opts:                                                                     
    if opt == '-s':                                                                       
        iperf_server = arg                                                                
    elif opt == '-l':                                                                     
        logger_server = arg                                                               
                                                                                          
                                                                                          
headers = {'Accept': 'application/json'}                                                  
                                                                                          
r = requests.get(meta_url + iperf_server , headers=headers)                               
iperf_service = r.json()                                                                  
                                                                                          
iperf_addrs = []                                                                          
for cont in iperf_service['containers']:                                                  
    iperf_addrs.append(cont['primary_ip'])                                                
                                                                                          
                                                                                          
# I am looping in bash becasue the module is shitty and can't handle it.                  
c = iperf3.Client()                                                                       
c.server_hostname = random.choice(iperf_addrs)                                            
c.port = 5201                                                                             
c.duration = 30                                                                           
resultes = c.run()                                                                        
print container, resultes.sent_Mbps
requests.get("http://%s/?cont=%s&mps=%d" % (logger_server, container, resultes.sent_Mbps))

