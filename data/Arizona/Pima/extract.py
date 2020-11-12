import csv, sys

def main():
    assert len(sys.argv) == 1

    with sys.stdin as f:
        csvr = csv.reader(f)

        hdr = csvr.next()
        csvr.next()
        sub_hdr = csvr.next()

        PRECINCT_IDX = hdr.index('PRECINCT NAME')
        D_IDX = sub_hdr.index('BIDEN, JOE')
        R_IDX = sub_hdr.index('TRUMP, DONALD')

        # print results
        print "Precinct,2020 Votes D,2020 Votes R"
        for r in csvr:
            # Don't count the total at the end
            if r[PRECINCT_IDX] == 'COUNTY TOTALS':
                break
            d_votes = int(r[D_IDX])
            r_votes = int(r[R_IDX])
            # Note: Precincts occur three times because early votes, poll votes
            #       and provisional votes are counted separately. Moreover, it seems
            #       that in almost all precincts there are no provisional votes.
            if d_votes > 0 or r_votes > 0:
                print "%s,%d,%d" % (r[PRECINCT_IDX], d_votes, r_votes)

if __name__ == "__main__":
    main()
