#! /bin/bash
for i in $(ls -l har/ | grep -nE '0817.+har' | awk {'print $9'}); do
  har2case har/$i
done
mv har/*.py testcases/