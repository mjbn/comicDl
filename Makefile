mainfile = comicdl.py
binName = comicdl

comicdl.c:
	cython --embed $(mainfile);

compile: comicdl.c
	# gcc $(pkg-config --cflags python3) -o $(binName) $(binName).c -lpython3.10;
	gcc -I/usr/include/python3.10 -o $(binName) $(binName).c -lpython3.10;

install: compile
	mv $(binName) ~/.local/bin/

uninstall:
	rm ~/.local/bin/$(binName)

clean:
	rm $(binName).c