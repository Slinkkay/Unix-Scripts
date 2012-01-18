from subprocess import call

# Function to read the properties file                                                                                                       
def readLine( f ):
  input = f.readline().rstrip()
  if input =='':
    return input
  strSplit = input.split('=')
  strSplit[1] = strSplit[1].replace('\'','')
  return strSplit

# read the file at path and return a list with the items read 
def readFile( path ):
  f = open(path, 'r')
  aRet =[]
  line=readLine( f )
  while line != '':
    aRet.append(line)
    line=readLine( f )
  f.close()
  return aRet

# Write the Double List line to the file f
def writeProperties( path, line ):
  f = open(path, 'w+')
  for pair in line:
    f.write(pair[0]+"='"+pair[1]+"'\n"); 
  f.close()

# Display all the properties in the list
def displayProperties( propList ):
  for pair in propList:
    print pair[0] + " : " + pair[1]

# Pull the variable out of the list
def getVar( list, key ):
  for pair in list:
    if pair[0] == key:
      return pair[1]

# Set the variable in the list
def setVar( list, key ):
  print "Enter value for " + key
  value = raw_input(  )
  for pair in list:
    if pair[0] == key:
      pair[1]=value
      return;

# Send the target Apk to the device
def sendApk( device, apk ):
  print "Sending " + apk + " to device " + device
  call(["adb", "-s", device,"install", "-r", apk])

def deleteApk( device, package):
  print "Deleting " + package + " from device " + device
  call(["adb","-s", device,"uninstall", package])

# Process the command with the given argument list
def processCommand( command, list ):
  if command == "echo":
    displayProperties( list )
  elif command == "setdev":
    setVar( list, 'TARGET_DEVICE' )
  elif command == "build":
    buildFile = getVar( list, 'TARGET_BUILD')
    module = __import__(buildFile, 'buildTarget')
    module.buildTarget( list )
  elif command == "setloc":
    setVar( list, 'TARGET_PWD' )
  elif command == "setbuild":
    setVar( list, 'TARGET_BUILD' )
  elif command == "setpack":
    setVar( list, 'TARGET_PACKAGE' )
  elif command == "delete":
    device = getVar(list, "TARGET_DEVICE")
    package = getVar(list, "TARGET_PACKAGE")
    deleteApk( device, package )
  elif command == "setapk":
    setVar( list, 'TARGET_APK' )
  elif command == "sendApk" or command == "install":
    device = getVar(list, "TARGET_DEVICE")
    apk = getVar(list, "TARGET_APK")
    sendApk( device, apk )
