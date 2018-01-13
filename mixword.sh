#!/bin/bash

word="out of memory error"
counter=0
broken="`echo $word |fmt -w 1`"
rebuild=''

for i in $broken ; do
	if test `expr $counter \% 2` == 0 ; then
		rebuild=$rebuild"`echo $i | sed 's/\([a-z]\)/\U\1/g;s/\(^.\)/\U\1/'`"
	else
		rebuild=$rebuild"`echo $i`" 
	fi
	counter="`expr $counter + 1`"
done
echo $rebuild
