#!/usr/bin/python
# Standard Library imports
import os, sys, signal, pickle
from subprocess import call

def cleanup():
  f = open(valuePath, 'w+')

  # Write out the new values
  pickle.dump( props, f )
  sys.exit(0)

def signal_handler(signal, frame):
  print "Cleaning up"
  cleanup()

# Register the signal Handler for ^C
signal.signal(signal.SIGINT, signal_handler)

# Add the libs path to the python path
binLoc = os.path.split(os.path.abspath(__file__))
sys.path.append(binLoc[0]+"/libs/")

# import all the modules from the libary
from shared import Properties, Item, commandList

binItem = Item( 'binLoc', binLoc[0] +'/' )

# Setup the path to the object file
valuePath = binItem.value + 'values.object'

try:
  f = open ( valuePath, 'r')
  props = pickle.load( f )
  # Remove the file as we should write it back out at the end
  call(["rm", valuePath])
except IOError:
  props = Properties()

props.setPair( binItem )

if (len(sys.argv) > 1):
  
  # Grab the commands from console  
  commandItems = sys.argv[1:] 

  # Load up the commands
  modules = commandList( props )
   
  # Cycle the commands
  for command in commandItems:
    for commands in modules:
      try:
        commands[command]( props )
      except KeyError:
        pass

cleanup() 
