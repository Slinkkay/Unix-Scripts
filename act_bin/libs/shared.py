import pickle, os

class Item:
  def __init__(self, key, value):
    self.key = key
    self.value = value

class Properties:
  def __init__( self ):
    self.mList = [ ]

  def printAll( self ):
    for item in self.mList:
      print item.key + " : " + item.value

  def setPair( self, pair ):
    for item in self.mList:
      if pair.key == item.key:
        item.value = pair.value 
        return
    self.mList.append(pair)

  def getValue( self, key ):
    for item in self.mList:
      if key == item.key:
        return item.value


def printProps( props ):
  props.printAll()

def printCommands( props ):
  print "Command List"
  print " -- Shared --"
  printDictionary(getCommands())
  imports = props.getValue( 'modules' )
  if imports == None:
    return
  imports = imports.split()
  for importStr in imports:
    commands = __import__(importStr).getCommands()
    print "-- " + importStr + " ---"
    printDictionary( commands )

def printDictionary( dict ):
  for key in dict.keys():
    print key 

def setModule( props ):
  print "Set Module" 
  ret = raw_input()
  props.setPair( Item( 'modules', ret ) )

def addModule( props ):
  previous = props.getValue( 'modules' )
  if previous == None:
    previous = ''
    print 'No Modules '
  else: 
    print 'Current Modules: ' + previous 
  ret = raw_input()
  props.setPair( Item( 'modules', previous + ' ' + ret ) )

def printModule( props ):
  print props.getValue( 'modules' )

# Pull the list of commands from the modules
def commandList( props ):
  # Init only the shared commands
  modules = [ getCommands() ]
  
  # Load up the modules
  imports = props.getValue( 'modules' )
  if imports != None:
    imports = imports.split()
    for importStr in imports:
      try:
        module = __import__(importStr)
      except ImportError:
        print "No Module named " + importStr
        continue
      modules.append( module.getCommands() )
  return modules 

def cleanPropLoad( props, path ):
  props.mList=[]
  file = open( path, 'r' )
  inProp = pickle.load( file )
  for item in inProp.mList:
    props.setPair( item )

def loadProfile( props ):
  print "Enter Profile Name"
  name = raw_input()
  name = name + '.profile'
  cleanPropLoad( props, props.getValue('binLoc')+name )

def saveProfile( props ):
  print "Enter Profile Name"
  name = raw_input()
  name = name + '.profile'
  file = open (props.getValue('binLoc')+name, 'w')
  pickle.dump( props, file)

def selectProfile( props ):
  print "Select Profile Name"
  location = props.getValue( 'binLoc' )
  profileSelection = []
  for dirname, dirnames, filenames in os.walk(location):
    for filename in filenames:
      if ".profile" in filename:
        name = filename[0:filename.find( '.profile' ) ]
        path = os.path.join(dirname, filename)
        profileSelection.append( [ name, path ])
  count = 0 
  for pair in profileSelection:
    print "{0} : {1}".format(count + 1, pair[0]) 
    count = count + 1
  
  selection = int( raw_input() ) - 1
  targetPath = profileSelection[selection][1]
  cleanPropLoad( props, targetPath )


# The commands for the shared module
def getCommands():
  commands ={
    'printModule':printModule,
    'setModule':setModule,
    "printProps":printProps,
    'addModule':addModule,
    'loadProfile':loadProfile,
    'saveProfile':saveProfile,
    'selProfile':selectProfile,
    "printCommands":printCommands
  }
  return commands

