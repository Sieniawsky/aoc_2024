#! /bin/bash

echo "Running..."
if [ -z "$1" ]
then
    echo "Must pass a day number as an argument"
    exit 1
fi

if [ -z "$2" ]
then
    echo "Must pass a part number as an argument"
    exit 1
fi

docker build -t aoc .
docker run -it aoc $1 $2

echo "Ended"
