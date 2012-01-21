class Item:
  def __init__(self, key, value):
    self.key = key
    self.value = value

class Properties:
  def __init__( self ):
    self.mList = [ ]

  def printAll( self ):
    for item in self.mList:
      print item.key + " " + item.value

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
  print props.printAll()

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

def printModule( props ):
  print props.getValue( 'modules' )

def getCommands():
  commands ={
    'printModule':printModule,
    'setModule':setModule,
    "printProps":printProps,
    "printCommands":printCommands
  }
  return commands
