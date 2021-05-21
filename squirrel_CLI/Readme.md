# Squirrel

Squirrel is a command line interface app that sets up your custom work environment.
This command line interface app was inspired by my two previous bash scripts,
I decided to redo both of the bash scripts using python for training purposes.
This is also a CLI app that I personally use or a regular basis.

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

2) move files from any directory to your target directory

Setup:

sq -from where/you/are/moving/files/from/

sq -target your/target/dir/

Command:

sq -move filenameInsideFromDirectory

3) If you have a git repository in your directory then use the command

sq -gc "Your commit message here"

This will commit all files with a commit message to your local git repository. 



# Installation

To install, run the following:

python setup.py install

Initialize Suirrel inside your working directory:

sq -init

Commands:

sq <plus one if the below commands>

-from <path>: Set the directory where files will be moved from

-targ <path>: sets target directory, your files will be moved here

-work <path>: sets your workig directory

-work_alias <name>: creates an alias that will always take you to THIS directory

-init: initiates work environment in this directory

-uninstall: removes Squirrel data directory

-gc <'Enter your commit message with quotes'> : shows git status, adds all files and commits them with a message you entered

-move: move a file to your target directory that you set up with -from and -targ

