#!/bin/bash

# Ask for user input and commit file name
echo "Does the file in Windows Downloads begin with a quote? y/n"
read yn
echo "Enter file namw abbreviation without quotes: "
read file_name

# Check user conditions and apply globbing characters to files
# that contain a quotation mark
if [ $yn  == "y" ] ; then
	mv -f /mnt/c/Users/pavel/Downloads/*"$file_name"* ~

elif [ $yn  == "n" ] ; then
	mv /mnt/c/Users/pavel/Downloads/"$file_name"* ~
fi

