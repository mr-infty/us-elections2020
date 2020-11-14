URL = https://results.enr.clarityelections.com/GA/Cobb/105403/271286/reports/detailxml.zip

.PHONY: all update clean

all: precincts.csv precincts_election_day.csv precincts_absentee.csv precincts_early_vote.csv precincts_provisional.csv

clean:
	rm -f precincts.csv precincts_election_day.csv precincts_absentee.csv precincts_early_vote.csv precincts_provisional.csv

update:
	curl "$(URL)" -o detailxml.zip
	unzip detailxml.zip
	rm -f detailxml.zip

detail.xml:
	curl "$(URL)" -o detailxml.zip
	unzip detailxml.zip
	rm -f detailxml.zip

precincts.csv precincts_election_day.csv precincts_absentee.csv precincts_early_vote.csv precincts_provisional.csv &: detail.xml
	cat detail.xml | python extract.py
