ALL_URL = https://results.enr.clarityelections.com/GA/Fulton/105430/270902/json/ALL.json
ELECTION_DAY_URL = https://results.enr.clarityelections.com/GA/Fulton/105430/270902/json/Election_Day_Votes.json
ABSENTEE_URL = https://results.enr.clarityelections.com/GA/Fulton/105430/270902/json/Absentee_by_Mail_Votes.json
ADVANCED_VOTING_URL = https://results.enr.clarityelections.com/GA/Fulton/105430/270902/json/Advanced_Voting_Votes.json
PROVISIONAL_URL = https://results.enr.clarityelections.com/GA/Fulton/105430/270902/json/Provisional_Votes.json


.PHONY: all update clean

all: precincts.csv precincts_election_day.csv precincts_absentee.csv precincts_early_vote.csv precincts_provisional.csv

clean:
	rm -f precincts.csv precincts_election_day.csv precincts_absentee.csv precincts_early_vote.csv precincts_provisional.csv

update:
	curl "$(ALL_URL)" -o ALL.json
	curl "$(ELECTION_DAY_URL)" -o Election_Day_Votes.json
	curl "$(ABSENTEE_URL)" -o Absentee_by_Mail_Votes.json
	curl "$(ADVANCED_VOTING_URL)" -o Advanced_Voting_Votes.json
	curl "$(PROVISIONAL_URL)" -o Provisional_Votes.json

ALL.json:
	curl "$(ALL_URL)" -o ALL.json

Election_Day_Votes.json:
	curl "$(ELECTION_DAY_URL)" -o Election_Day_Votes.json

Absentee_by_Mail_Votes.json:
	curl "$(ABSENTEE_URL)" -o Absentee_by_Mail_Votes.json

Advanced_Voting_Votes.json:
	curl "$(ADVANCED_VOTING_URL)" -o Advanced_Voting_Votes.json

Provisional_Votes.json:
	curl "$(PROVISIONAL_URL)" -o Provisional_Votes.json

precincts.csv:
	cat ALL.json | python extract.py > $@

precincts_election_day.csv:
	cat Election_Day_Votes.json | python extract.py > $@

precincts_absentee.csv:
	cat Absentee_by_Mail_Votes.json | python extract.py > $@

precincts_early_vote.csv:
	cat Advanced_Voting_Votes.json | python extract.py > $@

precincts_provisional.csv:
	cat Provisional_Votes.json | python extract.py > $@
