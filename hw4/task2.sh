#!/bin/bash

grep -l "sample" dataset1/file* | xargs grep -o "CSC510" | uniq -c | grep -E '^\s*([3-9]|[1-9][0-9]+)' | gawk '{gsub(/:CSC510/, "", $2); print $1, $2}' | while read count file; do echo "$count $file $(stat -c%s "$file")"; done | sort -k1,1nr -k3,3nr | sed 's/file_/filtered_/'