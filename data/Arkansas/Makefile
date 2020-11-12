URL = https://results.enr.clarityelections.com//AR//106124/270330/reports/detailxml.zip

.PHONY: all update clean

all: counties.csv

clean:
	rm -f counties.csv

update:
	curl "$(URL)" -o detailxml.zip
	unzip detailxml.zip
	rm -f detailxml.zip

detail.xml:
	curl "$(URL)" -o detailxml.zip
	unzip detailxml.zip
	rm -f detailxml.zip

counties.csv: detail.xml
	cat detail.xml | python extract.py > counties.csv
