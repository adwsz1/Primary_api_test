#! /bin/bash
ls -l
for i in $(ls -l har/ | grep .har | awk {'print $9'}); do
  har2case har/$i
done

mv har/*.py testcases/
