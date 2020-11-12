OBJ = $(shell ls *.eps)

.PHONY: all epstopdf clean

all: epstopdf

clean:
	rm -f *.pdf
	rm -f *.eps

%.pdf: %.eps
	epstopdf $<

epstopdf: $(patsubst %.eps,%.pdf,$(OBJ))
