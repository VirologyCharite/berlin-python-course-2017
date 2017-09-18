for i in "$@"
do
    # newname=$(echo $i | tr ' ' -)
    newname=$(echo $i | sed 's/(jpg|jpeg)$/JPG/')

    if [ -e "newname" ]
    then
        echo "Will not overwrite $newname"
    else
        mv "$i" "$newname"
    fi
done
