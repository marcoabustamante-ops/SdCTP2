CC = gcc
CFLAGS = -shared -fPIC -W -g
TARGETS = libredondear1.so libredondear2.so

all: $(TARGETS)

libredondear1.so: redondear1.c
	$(CC) $(CFLAGS) -o $@ $<

libredondear2.so: redondear2.c operacion_asm.s
	$(CC) $(CFLAGS) -o $@ $^

clean:
	rm -f $(TARGETS)
