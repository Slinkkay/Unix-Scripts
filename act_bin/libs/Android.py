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

def runApp( props ):
  activity = props.getValue( 'activity' )
  package = props.getValue( 'package' )
  device = props.getValue( 'device' )
  if activity == None or package == None or device == None:
    print 'Activity or Package or device not set'
    return
  action = 'android.intent.action.MAIN'
  appCommand = 'adb -s ' + device + ' shell am' \
    ' start -a ' + action +  ' -n ' + package + '/'+ activity
  print appCommand
  call(appCommand.split())
  

def setApp( props ):
  print "Enter activity"
  activity = raw_input()
  newItem = Item( 'activity', activity )
  props.setPair( newItem )
  

def getCommands():
  commands = {
    "install":sendApk,
    "delete":deleteApk,
    "setpack":setPackage,
    "setapk":setApk,
    "setdev":setDevice,
    "run":runApp,
    "setactivity":setApp
  }
  return commands

