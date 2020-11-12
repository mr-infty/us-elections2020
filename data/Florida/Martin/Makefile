URL = https://results.enr.clarityelections.com/FL/Martin/106277/269638/reports/detailxml.zip

.PHONY: all update clean

all: precincts.csv

clean:
	rm -f precincts.csv

update:
	curl "$(URL)" -o detailxml.zip
	unzip detailxml.zip
	rm -f detailxml.zip

detail.xml:
	curl "$(URL)" -o detailxml.zip
	unzip detailxml.zip
	rm -f detailxml.zip

precincts.csv: detail.xml
	cat detail.xml | python extract.py > precincts.csv
