#! /usr/bin/env python                                                                    
import iperf3                                                                             
import requests                                                                           
import sys, getopt, random, time, os                                                      
                                                                                          
meta_url = 'http://rancher-metadata/latest/self/stack/services/'                          
self_url = 'http://rancher-metadata/latest/self/container/service_index'
headers = {'Accept': 'application/json'}                                                  
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
                                                                                          
                                                                                          
self_service_index = requests.get(self_url , headers=headers).json()

r = requests.get(meta_url + iperf_server , headers=headers)                               
iperf_service = r.json()                                                                  

for server_container in iperf_service['containers']:                                                  
    if server_container['service_index'] == self_service_index:
        iperf_server_ip = server_container['primary_ip']
                                                                                          
                                                                                          
# I am looping in bash becasue the module is shitty and can't handle it.                  
c = iperf3.Client()                                                                       
c.server_hostname = iperf_server_ip                                          
c.port = 5201                                                                             
c.duration = 30                                                                           
c.bandwidth = 8 *1000 *1000
resultes = c.run()                                                                        
print iperf_server_ip ,container, resultes.sent_Mbps
requests.get("http://%s/?cont=%s&mps=%d" % (logger_server, container, resultes.sent_Mbps))

