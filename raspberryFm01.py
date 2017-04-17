#!/usr/bin/python
"""

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
		return status
    elif isinstance(status, tuple):
        return status[0]
    
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
        status = self.getStatus()
        print status
        sysdata = [f.strip() for f in status.split("\r\n") if f != ""]
        rawdata = []
        for d in sysdata:
            splitter = d.splitlines()
            rawdata.extend(splitter)
        # This should give three items, looking like this (if soma FM):
        # Lush: Mostly female vocals with an electronic influence. [SomaFM]: Love Echo - Departure                                                                        
        # [playing] #2/3   0:08/0:00 (0%)                                                                                                                                 
        # volume: 88%   repeat: off   random: off   single: off   consume: off
        
        # Get what's playing
        data["playing"] = rawdata[0]
        if "[SomaFM]" in rawdata[0]:
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
        elif " - " in rawdata[0]:
            # If we find a dash, split things by dash and turn the first two into
            # what we'll display.
            chopped = rawdata[0].split(" - ")
            line1 = chopped[0].strip()
            line2 = chopped[1].strip() 
            data["playing"] = "%s\n%s"%(line1, line2)
        
       
            
 lines=getData()   
 print lines
        
        
