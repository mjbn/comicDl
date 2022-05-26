mainfile = comicdl.py
binName = comicdl

.c:
	cython --embed $(mainfile);

compile: .c
	# gcc $(pkg-config --cflags python3) -o $(binName) $(binName).c -lpython3.10;
	$(CC) -I/usr/include/python3.10 -o $(binName) $(binName).c -lpython3.10;

install: compile
	mv $(binName) ~/.local/bin/

doc:
	cp README.html README.md

uninstall:
	rm ~/.local/bin/$(binName)

clean:
	rm $(binName).c $(binName) $(binName).exe