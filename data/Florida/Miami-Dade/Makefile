URL = https://enr.electionsfl.org/DAD/2779/Precincts/35849/0/865/

.PHONY: all update clean

all: precincts.csv

clean:
	rm -f precincts.csv

update:
	curl "$(URL)" -o precincts.html

precincts.html:
	curl "$(URL)" -o precincts.html

precincts.csv: precincts.html
	cat precincts.html | python extract.py > precincts.csv
