URL = https://recorder.maricopa.gov/media/ArizonaExportByPrecinct_110320.txt

.PHONY: all update clean

all: precincts.csv

clean:
	rm -f precincts.csv

# They use CAPTCHA :-(
#update:
#	curl "$(URL)" -o precincts.txt

precincts.txt:
	#curl "$(URL)" -o precincts.txt

precincts.csv: precincts.txt
	cat precincts.txt | python extract.py > precincts.csv
