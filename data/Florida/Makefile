URL = https://flelectionfiles.floridados.gov/enightfilespublic/20201103_ElecResultsFL.txt

.PHONY: all update clean

all: counties.csv

clean:
	rm -f counties.csv

update:
	#curl "$(URL)" -o counties.txt # They use CAPTCHA :-(

counties.txt:
	#curl "$(URL)" -o counties.txt

counties.csv: counties.txt
	cat counties.txt | python extract.py > counties.csv
