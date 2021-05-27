# Squirrel

Squirrel my custom made command line interface app that sets up your custom work environment.
This command line interface app was inspired by my two previous bash scripts,
I decided to redo both of the bash scripts using python for training purposes.
This is also a CLI app that I personally use on a regular basis.

# Installation

To install, run the following:

python setup.py install

# Initialization

Initialize Squirrel inside your project working directory:

sq -init

# Customize Working Directory

For now this CLI app has three functions:
1) Create a custom alias on your Linux system.
This alias switches you into your working directory.

Example: 

First, switch into your working project directory:

cd your/project/directory

Initialize Squirrel if running it for the first time in that directory:

sq -init

Create an alias:

sq -work_alias YourProjectName

Typing YourProjectName in the command line from anywhere will now switch 
you into your working directory.

2) Move files from any directory to your target directory with only
one command after setting up the "-from" and "-target" directories.

Setup:

You only have to run this setup once, the directory
paths will be automatically saved unless you change them
in the future

sq -from dir/moving/files/from/

sq -target your/target/dir/

Command:

sq -move filenameInsideFromDirectory

From now on the only command you need to move files between 
the directories is sq -move fileName.

3) If you have a git repository in your directory then use the command

sq -gc "Your commit message here"

This will commit all files with a commit message to your local git repository. 


# Commands:

sq -plus_one_of_the_below_commands

-from path: Set the directory where files will be moved from

-targ path: sets target directory, your files will be moved here

-work_alias customName: creates an alias that will always take you to THIS directory

-init: initiates work environment in this directory

-uninstall: removes Squirrel data directory

-gc 'Enter your commit message with quotes' : shows git status, adds all files and commits them with a message you entered

-move: move a file to your target directory that you set up with -from and -targ

