#!/bin/bash

username=$1

if [ -z "$username" ]; then
    echo "\$username is empty"
    exit 1
fi

if [ ! -d "./$username" ]; then
    timeout 10s instaloader "$username" --no-captions

    files_without_date=$(ls -1tr ./$username/*.json.xz | grep -v "[0-9]\{4\}-[0-9]\{2\}-[0-9]\{2\}")

    if [ -n "$files_without_date" ]; then
        rm $files_without_date
    fi

    find ./$username -type f \( -name "*.txt" -o -name "*.jpg" -o -name "*.mp4" \) -delete
    rm ./$username/id

    exit 1
fi

timeout 10s instaloader "$username" --fast-update --no-captions

files_without_date=$(ls -1tr ./$username/*.json.xz | grep -v "[0-9]\{4\}-[0-9]\{2\}-[0-9]\{2\}")

if [ -n "$files_without_date" ]; then
    rm $files_without_date
fi

find ./$username -type f \( -name "*.txt" -o -name "*.jpg" -o -name "*.mp4" \) -delete
rm ./$username/id
