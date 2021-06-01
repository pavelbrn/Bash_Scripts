import subprocess as s
import json
import os.path

#print("test \n test")

sqrl_path="data_squirrel/data.txt"
sqrl_dir="data_squirrel"
sqrl_aliases ="data_squirrel/aliases.txt"

# Check if Squirrel has been initialized
############ Decorator #####################
def check_initiation(func):
    def wrapper(*args, **kwargs):
        if os.path.exists(sqrl_path):
            func(*args, **kwargs)
        else:
            print("Directory not initialized, initiate Squirrel with 'sq -init'")
    return wrapper

# Add a custom Alias to .bashrc
# TO DO: check if .bash_aliases exists if not then create one
#        otherwise backup .bash_aliases and add custom bash alias to main file
########### ADD ALIAS TO .bashrc #############
@check_initiation
def create_alias(alias_name):
    local_path = s.run("pwd",capture_output=True)
    # Encountered a bug here:
    # When using decode the string will still have a \n hidden inside it
    # Remove the hidden \n by chaining the replace method onto it and removing \n
    local_path= local_path.stdout.decode().replace("\n","")

    # Fixed a bug here, use \n to enter a new line otherwise all aliases will ba stacked next to each other
    # instead of on top of each other line by line. 
    alias_bash = 'alias {name}="cd {path} "\n'.format(name=alias_name,path=local_path)
    user_home = os.path.expanduser('~')
    bashrc_path = os.path.abspath('{}/.bashrc'.format(user_home))

    with open(bashrc_path, "r") as f:
        lines = f.readlines()
        
        if alias_bash not in lines: 
            print(alias_bash)   
            out = open(bashrc_path, 'a')
            out.write(alias_bash)
            out.close()
            print("Created alias inside .bashrc, restart shell to activate")
        else:
            print("Alias already exists, restart shell to activate if running for first time")

    alias_data= {"alias":alias_bash}
    with open(sqrl_aliases,"w") as outfile:
        json.dump(alias_data,outfile) 

########### OS CHECK FILES AND DIR ###############

def initiate_squirrel():

    if os.path.exists(sqrl_path):
        print("Found data.txt")
    else:
        print("Initializing Squirrel...")
        s.run(["mkdir",sqrl_dir])
        data = {"origin": "none","fromdir":"none","work":"none"}
        with open(sqrl_path,"w") as outfile:
            json.dump(data,outfile)   

    if os.path.exists(sqrl_aliases):
        print("Found aliases.txt")
    else:
        print("Initializing aliases.txt file update!...")
        s.run(["touch",sqrl_aliases])
        alias_data = {"alias": "none"}
        with open(sqrl_aliases,"w") as outfile:
            json.dump(alias_data,outfile)  

######### Save paths ##############################

def save(data,dict_key,save_path):
    with open(sqrl_path) as json_file:
        data = json.load(json_file)
        for dt in data:
            if dt == dict_key:
                data[dt] = save_path
                print(data[dt])   
    with open(sqrl_path,"w") as outfile:
        json.dump(data,outfile) 

@check_initiation
def save_path(path_type=None,path_dir="none"):
    data = {"origin": "none","fromdir":"none","work":"none"}
    # Get json data and override our data
    with open(sqrl_path) as json_file:
        data = json.load(json_file)

    # Create a dictionary to store the directory paths: 
    if path_type == "fromdir":
        #data["origin"] = "Save origin dir"
        #save(data)
        with open(sqrl_path) as json_file:
            data = json.load(json_file)
            for dt in data:
                if dt == "fromdir":
                    data[dt] = path_dir
                    print(data[dt])   
        with open(sqrl_path,"w") as outfile:
            json.dump(data,outfile)   
          
    elif path_type == "target":
        with open(sqrl_path) as json_file:
            data = json.load(json_file)
            for dt in data:
                if dt == "origin":
                    data[dt] = path_dir
                    print(data[dt])   
        with open(sqrl_path,"w") as outfile:
            json.dump(data,outfile) 
    elif path_type == "work":
        save(data,"work",path_dir)


########### Uninstalling Squirrel ############

def uninstall_sqrl():
    s.run(["rm","-r",sqrl_dir], capture_output=True)

############## commit to git ###################
def commit_git(message):
    s.run(["git","status"])
    s.run(["git","add","."])
    s.run(["git","commit","-m",message])

############ Move Files to target directory ###############
def move_file(name):
    origin=""
    fromdir=""
    with open(sqrl_path) as json_file:
        data = json.load(json_file)
        for dt in data:
            if dt=="origin":
                #print(data[dt])
                origin = data[dt]
            elif dt=="fromdir":
                fromdir=data[dt]
                #print(data[dt])

    file=fromdir + name+ " "+origin
    #print(file)
    s.call("mv -f "+file, shell=True)
