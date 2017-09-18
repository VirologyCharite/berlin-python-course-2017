#!/bin/sh

if [ -e sorted-images ]
then
    echo "sorted-images already exists! Exiting."
    exit 1
else
    mkdir sorted-images
fi

for file in "$@"
do
    echo "Processing $file"
    date=$(EXIF.py "$file" | grep 'Image DateTime' | cut -f4,5 -d' ' | tr ' ' -)

    if [ -z "$date" ]
    then
        echo "Could not extract EXIF date from '$file'. Skipping."
    else
        cp "$file" "sorted-images/$date-$(basename $file)"
    fi
done
