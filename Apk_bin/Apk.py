#!/usr/bin/python
# Standard Library imports
import os, sys, signal, pickle
from subprocess import call

def signal_handler(signal, frame):
  print "Cleaning up"
  writeProperties( valuePath, line )
  sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# Add the libs path to the python path
binLoc = os.path.split(os.path.abspath(__file__))
sys.path.append(binLoc[0]+"/libs/")

# import all the modules from the libary
from lib import processCommand, writeProperties, readFile
from shared import Properties
import shared

# Setup the path to the object file
valuePath = binLoc[0] + '/values.object'

try:
  f = open ( valuePath, 'r')
  props = pickle.load( f )
  # Remove the file as we should write it back out at the end
  call(["rm", valuePath])
except IOError:
  props = Properties()

if (len(sys.argv) > 1):
  commandList = sys.argv[1:] 
  for command in commandList:
    # check the command against the internal commands
    internal = shared.getCommands()
    try:
      internal[command]( props )
      continue
    except KeyError:
      pass
    # if the command isn't internal check the modules
    imports = props.getValue( 'modules' )
    if imports == None:
      break
    imports = imports.split()
    for importStr in imports:
      try:
        module = __import__(importStr)
      except ImportError:
        print "No Module named " + importStr
        continue
      commands = module.getCommands()
      try:
        commands[command]( props )
        continue
      except KeyError:
        pass

f = open(valuePath, 'w+')

# Write out the new values
pickle.dump( props, f )
