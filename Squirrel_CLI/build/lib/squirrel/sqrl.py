import subprocess as s
import argparse 
from squirrel.commonf.common import save_path
from squirrel.commonf.common import create_alias
from squirrel.commonf.common import initiate_squirrel
from squirrel.commonf.common import uninstall_sqrl
from squirrel.commonf.common import commit_git
from squirrel.commonf.common import move_file


#/home/pavel/Downloads/
############### PARSER##################
parser = argparse.ArgumentParser(description="Linux work environment setup")

parser.add_argument("-fromdir",type = str, help = "-from <path>: sets move from directory")
parser.add_argument("-target",type=str,help = "-targ <path>: sets target directory")
parser.add_argument("-work",type=str,help = "-work <path>: sets your workig directory")
parser.add_argument("-work_alias",type=str,help = "-work_alias <name>: creates an alias that will always take you to THIS directory")
parser.add_argument("-init",action="store_true",help = "-init: initiates work environment in this directory")
parser.add_argument("-uninstall",action="store_true",help = "-uninstall: removes Squirrel data directory")
parser.add_argument("-gc",type=str,help = "-gc 'Enter your commit message with quotes': shows git status, adds all files and commits them with a message")
parser.add_argument("-move",type=str,help = "-move: move a file to your target directory")

arguments = parser.parse_args()

def main():

    if arguments.fromdir:
        x= arguments.fromdir 
        print(x)
        save_path(path_type="fromdir", path_dir = x)
        #save_path("test")
    elif arguments.target:
        
        capture = arguments.target
        save_path(path_type="target",path_dir=capture)
        print("Created: "+str(capture))
    elif arguments.work:
        arg_capture = arguments.work
        save_path(path_type="work",path_dir=arg_capture)

    elif arguments.work_alias:
        arg_capture = arguments.work_alias
        create_alias(arg_capture)
    elif arguments.init:
        initiate_squirrel()
        #print("Initiating Squirrel")
    elif arguments.uninstall:
        uninstall_sqrl()
        print("Uninstalling Squirrel")
    elif arguments.gc:
        commit_git(arguments.gc)
        #print("Uninstalling Squirrel")
    elif arguments.move:
        move_file(arguments.move)
        #print("Uninstalling Squirrel")
    else:
        print("Invalid command, use -h for help.")












    
    # data["origin"] = "Save to directory"

    # print(data)

    # with open("data.txt","w") as outfile:
    #     json.dump(data,outfile)

    # with open("data.txt") as json_file:
    #     data = json.load(json_file)
    #     for dt in data:
    #         print(data[dt])


