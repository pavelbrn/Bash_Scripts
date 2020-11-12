#!/bin/bash

#commit all files into git master branch
echo "Commit all files in this directory to master branch? y/n "
read yn

#get user input
if [ $yn  == "y" ]; then
        echo "Please enter a commit message:  "
        read commit_message
        
        #show git status, add the files and add commit message to hash
        git status
        git add .
        git commit -m "$commit_message"
else
        echo commit cancelled
        exit
fi

