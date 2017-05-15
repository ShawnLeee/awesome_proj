#! /bin/sh
gcc -c -Wall -Werror -fpic simple.c && gcc -shared -o libsimple.so simple.o
cp libsimple.so ../simple