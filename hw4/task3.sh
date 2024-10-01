#!/bin/bash

# passengers=`gawk -F, '$3 == 2 { print }' titanic.csv | sed -e 's/female/F/g' -e 's/male/M/g' ` 

# echo "$passengers"

# echo ""

gawk -F, '$3 == 2 { print }' titanic.csv | sed -e 's/female/F/g' -e 's/male/M/g' | gawk -F, 'BEGIN { sum=0; count=0 } $7 != "" && $7 ~ /^[0-9]+(\.[0-9]+)?$/ { sum += $7; count++ } END { if (count > 0) print "Average age: " sum/count; else print "Average age could not be computed" }'