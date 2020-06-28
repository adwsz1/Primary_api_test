#! /bin/bash
for i in $(ls -l ../har/ | grep .har | awk {'print $9'}); do
  echo $i
  har2case ../har/$i
done
