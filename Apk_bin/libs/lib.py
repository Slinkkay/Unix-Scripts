import imp, pickle, os
from subprocess import call
from Android import sendApk, deleteApk

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
  if not os.path.exists( path ):
    f = open(path, 'w+')
  else:
    f = open(path, 'r')
  aRet =[]
  line=readLine( f )
  while line != '':
    aRet.append(line)
    line=readLine( f )
  f.close()
  return aRet

class Properties:
   def __init__( self, list ): 
     self.mList = list

# Write the Double List line to the file f
def writeProperties( path, line ):
  prop = Properties( line )
  writeObject( prop )
  f = open(path, 'w+')
  for pair in line:
    f.write(pair[0]+"='"+pair[1]+"'\n"); 
  f.close()


# Display all the properties in the list
def displayProperties( propList ):
  for pair in propList:
    print pair[0] + " : " + pair[1]

# Process the command with the given argument list
def processCommand( command, list ):
  commands = {
    'echo':displayProperties
  }
#def Random():
#  if command == "echo":
#    displayProperties( list )
#  elif command == "setdev":
#    setVar( list, 'TARGET_DEVICE' )
#  elif command == "build":
#    buildFile = getVar( list, 'TARGET_BUILD') 
#    module = __import__(buildFile)
#    module.buildTarget( list )
#  elif command == "setloc":
#    setVar( list, 'TARGET_PWD' )
#  elif command == "setbuild":
#    setVar( list, 'TARGET_BUILD' )
#  elif command == "setpack":
#    setVar( list, 'TARGET_PACKAGE' )
#  elif command == "delete":
#    device = getVar(list, "TARGET_DEVICE")
#    package = getVar(list, "TARGET_PACKAGE")
#    deleteApk( device, package )
#  elif command == "setapk":
#    setVar( list, 'TARGET_APK' )
#  elif command == "sendApk" or command == "install":
#    device = getVar(list, "TARGET_DEVICE")
#    apk = getVar(list, "TARGET_APK")
#    sendApk( device, apk )
