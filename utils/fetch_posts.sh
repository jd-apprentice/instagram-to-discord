#!/bin/bash

username=$1

if [ -z "$username" ]
then
      echo "\$username is empty"
      exit 1
fi

if [ ! -d "./$username" ]
then
      instaloader "$username"
      exit 1
fi

instaloader "$username" --fast-update