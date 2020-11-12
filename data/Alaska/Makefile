URL = https://www.elections.alaska.gov/results/20GENR/Map/results/precincts.js?_=1604950981268

.PHONY: all update clean

all: precincts.csv

clean:
	rm -f precincts.csv

update:
	curl "$(URL)" -o precincts.js

precincts.js:
	curl "$(URL)" -o precincts.js

precincts.csv: precincts.js
	cat precincts.js | python extract.py > precincts.csv
