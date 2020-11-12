import csv, sys


def main():
    assert len(sys.argv) == 1

    with sys.stdin as f:
        csvr = csv.reader(f, delimiter='\t')

        hdr = csvr.next()
        CONTEST_NAME_IDX = hdr.index('ContestName')
        PRECINCT_NAME_IDX = hdr.index('PrecinctName')
        CANDIDATE_NAME_IDX = hdr.index('CandidateName')
        VOTES_IDX = hdr.index('Votes')

        results = {}
        for r in csvr:
            if r[CONTEST_NAME_IDX] == 'Presidential Electors' and not r[PRECINCT_NAME_IDX] == '':
                if not r[PRECINCT_NAME_IDX] in results:
                    results[r[PRECINCT_NAME_IDX]] = {}
                if r[CANDIDATE_NAME_IDX] == 'BIDEN / HARRIS':
                    results[r[PRECINCT_NAME_IDX]]['D'] = int(r[VOTES_IDX])
                elif r[CANDIDATE_NAME_IDX] == 'TRUMP / PENCE':
                    results[r[PRECINCT_NAME_IDX]]['R'] = int(r[VOTES_IDX])

        # print results
        print "Precinct,2020 Votes D,2020 Votes R"
        for (key,val) in results.items():
            print "%s,%d,%d" % (key, val['D'], val['R'])

if __name__ == "__main__":
    main()
