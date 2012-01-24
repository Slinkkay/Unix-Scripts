# act utility

act is a utility used to help streamline atomic commands. The utility can have
any number of modules which can be defined. Then by identifying which modules
are to be access a set of tasks can be listed and exected in order. 

## Setup
The setup for the utility is based around running its commands to setup the
properties. The commands which can be run are avaliable though the
'printCommands' command. This command will cycle though any of the specified
modules and list their commands.

## Commands
The idea around act comes from the need to execute commands in a repetitive 
fashion. This means that before a command is executed all needed information is
populated. This is passed to the command in the form of the Property object.
Each command is supplied the global Property. Using this object the command can
pull whatever information is needed for execution. 

## Modules

Each module is a set of commands that are suppose to encapsulate some kind of
functionality. The standard module is called shared.py and it contains some 
simple commands for setup and execution. The idea is to make a module 
containing what commands you need. The intent of these commands should be 
atomic, or to accomplish one thing.

## Reason for existance 

I first started to create a utility like act when I started to streamline the
build process for an Android application. The project used the normal Android
process along with several additions. This made things rather complicated for
devs who wanted to build using local code. My build command had several flags
with whole file strings being passed. act is an attempt to simplify that whole
thing. 

## More Ramblings about how and why

I initially solved this by setting up small bash scripts which basically had
everything pre-set and where one off commands. I soon found myself wanting a
more Maven type of building. I had considered attempting to use Maven but after
working with it and finding our complicated it all was I decieded to try to find
an easier path. 

The first itteration of act was called Apk as it was targeted at an Android
project. The code was Bash scripting and could build the project, specify a
target and deploy to the device along with removing from the device. As I saw
the code getting more and more complicated I figured this would be a good time
to learn a scritping language. After playing with Python I felt it most
resembled Java to me and I ran with it. 

After a few days of investigation and playing I re-created Apk in Python and 
renamed it to act as I felt it was for actions and not Android anymore. 
