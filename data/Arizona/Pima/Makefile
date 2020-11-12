URL = https://webcms.pima.gov/UserFiles/Servers/Server_6/File/Government/elections/Election%20Results/ENR.CSV

.PHONY: all update clean

all: precincts.csv

clean:
	rm -f precincts.csv

update:
	curl "$(URL)" -o ENR.CSV

ENR.CSV:
	curl "$(URL)" -o ENR.CSV

precincts.csv: ENR.CSV
	cat ENR.CSV | python extract.py > precincts.csv
