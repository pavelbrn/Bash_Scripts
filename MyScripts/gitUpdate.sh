  1 #!/bin/bash
  2 
  3 #commit all files into git master branch
  4 echo "Commit all files in this directory to master branch? y/n "
  5 read yn
  6 
  7 #get user input
  8 if [ $yn  == "y" ] && [ -d .git ] ; then
  9         echo "Please enter a commit message:  "
 10         read commit_message
 11         #show git status, add the files and add commit message to hash
 12         echo .git
 13         git status
 14         git add .
 15         git commit -m "$commit_message"
 16 elif [ ! -d .git  ] ; then
 17         echo "There is no git repository in this directory"
 18         exit
 19         
 20 else    
 21         echo commit cancelled
 22         exit
 23 fi
