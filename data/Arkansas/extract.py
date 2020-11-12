import sys
from lxml import etree

def main():
    assert len(sys.argv) == 1

    with sys.stdin as f:
        tree = etree.parse(f)
        root = tree.getroot()
        
        D_election_day = {}
        D_early_vote = {}
        D_absentee = {}
        D_provisional = {}

        R_election_day = {}
        R_early_vote = {}
        R_absentee = {}
        R_provisional = {}

        for c in root:
            if c.tag != 'Contest' or c.get('text') != 'U.S. President, Vice President':
                continue
            for cc in c:
                if cc.tag != 'Choice':
                    continue
                if cc.get('text') == 'Joseph R. Biden/Kamala Harris':
                    for votes in cc:
                        if votes.get('name') == 'Election Day':
                            for v in votes:
                                D_election_day[v.get('name')] = int(v.get('votes'))
                        elif votes.get('name') == 'Early Vote':
                            for v in votes:
                                D_early_vote[v.get('name')] = int(v.get('votes'))
                        elif votes.get('name') == 'Absentee':
                            for v in votes:
                                D_absentee[v.get('name')] = int(v.get('votes'))
                        elif votes.get('name') == 'Provisional':
                            for v in votes:
                                D_provisional[v.get('name')] = int(v.get('votes'))
                        else:
                            assert 0 == 1
                elif cc.get('text') == 'Donald J. Trump/Michael R. Pence':
                    for votes in cc:
                        if votes.get('name') == 'Election Day':
                            for v in votes:
                                R_election_day[v.get('name')] = int(v.get('votes'))
                        elif votes.get('name') == 'Early Vote':
                            for v in votes:
                                R_early_vote[v.get('name')] = int(v.get('votes'))
                        elif votes.get('name') == 'Absentee':
                            for v in votes:
                                R_absentee[v.get('name')] = int(v.get('votes'))
                        elif votes.get('name') == 'Provisional':
                            for v in votes:
                                R_provisional[v.get('name')] = int(v.get('votes'))
                        else:
                            assert 0 == 1

        counties = list(set.union(set(D_election_day.keys()),
                                  set(D_early_vote.keys()),
                                  set(D_absentee.keys()),
                                  set(D_provisional.keys()),
                                  set(R_election_day.keys()),
                                  set(R_early_vote.keys()),
                                  set(R_absentee.keys()),
                                  set(R_provisional.keys())))

        # print results
        print "County,2020 Votes D,2020 Votes R"
        for c in counties:
            # election day votes
            print "%s,%d,%d" % (c, D_election_day[c], R_election_day[c])
            # early votes
            print "%s,%d,%d" % (c, D_early_vote[c], R_early_vote[c])
            # absentee votes
            print "%s,%d,%d" % (c, D_absentee[c], R_absentee[c])
            # provisional votes
            print "%s,%d,%d" % (c, D_provisional[c], R_provisional[c])

if __name__ == "__main__":
    main()
