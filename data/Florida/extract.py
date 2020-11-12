import csv, sys

def main():
    assert len(sys.argv) == 1

    D_votes = {}
    R_votes = {}
    with open('counties.txt','r') as f:
        csvr = csv.reader(f, delimiter='\t')

        hdr = csvr.next()
        PARTY_CODE_IDX = hdr.index('PartyCode')
        RACE_CODE_IDX = hdr.index('RaceCode')
        COUNTY_NAME_IDX = hdr.index('CountyName')
        VOTE_IDX = hdr.index('CanVotes')

        for r in csvr:
            if not r[RACE_CODE_IDX] == 'PRE':
                continue
            if r[PARTY_CODE_IDX] == 'DEM':
                D_votes[r[COUNTY_NAME_IDX]] = int(r[VOTE_IDX])
            elif r[PARTY_CODE_IDX] == 'REP':
                R_votes[r[COUNTY_NAME_IDX]] = int(r[VOTE_IDX])

        counties = list(set.union(set(D_votes.keys()),
                                  set(R_votes.keys())))
        counties.sort()
        # print results
        print "County,2020 Votes D,2020 Votes R"
        for c in counties:
            print "%s,%d,%d" % (c, D_votes[c], R_votes[c])

if __name__ == '__main__':
    main()
