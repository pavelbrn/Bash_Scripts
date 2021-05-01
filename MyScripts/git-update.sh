#!/bin/bash

# Commit all files into git master branch
echo "Commit all files in this directory to master branch? y/n "
read yn

# Get user input
if [ $yn  == "y" ] && [ -d .git ] ; then
         echo "Please enter a commit message:  "
         read commit_message
         # Show git status, add the files and add commit message to hash
         git status
         git add .
         git commit -m "$commit_message"
 elif [ ! -d .git  ] ; then
        echo "There is no git repository in this directory"
        exit
         
 else   
        echo commit cancelled
        exit
 fi
