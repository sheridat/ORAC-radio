#!/usr/bin/python
"""
raspberryFm01.py

"""
import os
import re
import sys
import socket
import cPickle
from time import sleep
from subprocess import Popen, PIPE
            
def getStatus(self):
        
   status = Popen("mpc", stdout=PIPE).communicate()
   if isinstance(status, basestring):
      print status
      return status
   elif isinstance(status, tuple):
      print status[0]
      return status[0]
      
getStatus(list)
print list


def getData(self):
        """
        Return dict of interesting data.  
        Key/values are {"playing":string, "track":int, "tracks":int, "volume":int}
        
        Note, I've only really spent time parsing SomaFM streams, so anything
        else will just have the first 16 chars displayed.
        """
data = {"playing":None,
        "track":None,
        "tracks":None,
        "volume":None}
                
        # Get system-level mpc data, simply by calling to it and capturing the result:
        # Note, if mpc isn't playing, this won't give us everything we need.
status = getStatus(data)
print status
sysdata = [f.strip() for f in status.split("\r\n") if f != ""]
rawdata = []
print "rawdata printed next"
for d in sysdata:
            splitter = d.splitlines()
            rawdata.extend(splitter)
print rawdata
data["playing"] = rawdata[0]
if "[CROOZE]" in rawdata[0]:
            # Special consideration for SomaFM playlists, since that's what' I listen to most ;)
            # For example:
            # Deep Space One: Deep ambient electronic and space music. [SomaFM]: Sync 24 - Sequor
   chopped = rawdata[0].split(":")
   line1 = ""
   line2 = ""
   if len(chopped) == 3:
		line1 = chopped[0].strip()
		line2 = chopped[2].strip()
   elif len(chopped) == 2:
		line1 = chopped[0].strip()
		line2 = chopped[1].strip()           
		data["playing"] = "%s\n%s"%(line1, line2)
   print "line1 " + line1
   print"\n"
   print "Line2 " + line2
   print data
elif " - " in rawdata[0]:
           # If we find a dash, split things by dash and turn the first two into
            # what we'll display.
   chopped = rawdata[0].split(" - ")
   line1 = chopped[0].strip()
   line2 = chopped[1].strip() 
   data["playing"] = "%s\n%s"%(line1, line2)
   print "Line1" + line1
   print "\n"
   print "Line2" + line2
   print data
        
        
        
'''
        
        # This should give three items, looking like this (if soma FM):
        # Lush: Mostly female vocals with an electronic influence. [SomaFM]: Love Echo - Departure                                                                        
        # [playing] #2/3   0:08/0:00 (0%)                                                                                                                                 
        # volume: 88%   repeat: off   random: off   single: off   consume: off
        
        # Get what's playing
        
        
       
            
 lines=getData()   
 print lines
'''



