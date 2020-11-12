.PHONY: all update clean

all: counties.csv

clean:
	rm -f counties.csv

update:
	python extract.py --update > counties.csv

counties.csv:
	python extract.py > counties.csv
