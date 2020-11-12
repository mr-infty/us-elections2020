import json, sys

def main():
    assert len(sys.argv) == 1
    data = json.load(sys.stdin)

    # reverse-engineered by hand :-(
    PRES_RACE_IDX = 0
    TRUMP_IDX = 0
    BIDEN_IDX = 1

    print "Precinct,2020 Votes D,2020 Votes R"
    for p in data['Contests']: # this is the list of precincts, not of contests
        precinct = p['A']
        if precinct == '-1': # this is the total; skip it
            continue
        votes = p['V'][PRES_RACE_IDX]
        print "%s,%s,%s" % (precinct, votes[BIDEN_IDX], votes[TRUMP_IDX])

if __name__ == "__main__":
    main()
