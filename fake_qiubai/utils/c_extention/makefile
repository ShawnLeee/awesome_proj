objects = main.o command.o defs.o list.o simple.o libsimple.so
cc = gcc

main : $(objects)
	cc -o main $(objects)
libsimple.so : simple.o
	cc -shared -o libsimple.so simple.o
simple.o : simple.c
	cc -c simple.c
main.o : main.c command.h list.h
	cc -c main.c
command.o : command.c defs.h
	cc -c command.c
defs.o : defs.c
	cc -c defs.c
list.o : list.h
	cc -c list.c

clean : 
	rm main $(objects) 