#!/bin/bash

echo "Enter your username: "
read username

if [ -z "$username" ]
then
      echo "\$username is empty"
      exit 1
fi

if [ ! -d "./$username" ]
then
      instaloader $username
      exit 1
fi

instaloader $username --fast-update