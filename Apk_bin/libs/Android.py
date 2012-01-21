from subprocess import call
from shared import Item

# Send the target Apk to the device
def sendApk( props ):
  print 'sendApk'
  device = props.getValue( 'device' )
  apk = props.getValue( 'apk') 
  if device == None or apk == None:
    print "Apk or Device Missing" 
    return
  print "Sending " + apk + " to device " + device
  call(["adb", "-s", device,"install", "-r", apk])

def deleteApk( props ):
  print 'deleteApk'
  device = props.getValue( 'device' )
  package = props.getValue( 'package') 
  print "Deleting " + package + " from device " + device
  call(["adb","-s", device,"uninstall", package])

def setDevice( props ):
  print "Enter the device ID"
  device = raw_input()
  newItem = Item( 'device', device )
  props.setPair( newItem )

def setApk( props ):
  print "Enter the APK Location"
  apk = raw_input()
  newItem = Item( 'apk', apk )
  props.setPair( newItem )

def setPackage( props ):
  print "Enter package"
  package = raw_input()
  newItem = Item( 'package', package )
  props.setPair( newItem )

def getCommands():
  commands = {
    "sendApk":sendApk,
    "deleteApk":deleteApk,
    "setpack":setPackage,
    "setapk":setApk,
    "setdev":setDevice
  }
  return commands

