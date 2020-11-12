import sys
from lxml import etree

def insert_votes(votes, d):
    for p in votes:
        d[p.get('name')] = int(p.get('votes'))

def main():
    assert len(sys.argv) == 1

    with sys.stdin as f:
        tree = etree.parse(f)
        root = tree.getroot()
        
        D_election_day = {}
        D_vote_by_mail = {}
        D_advanced_voting = {}
        D_provisional = {}

        R_election_day = {}
        R_vote_by_mail = {}
        R_advanced_voting = {}
        R_provisional = {}

        pres_race = next(c for c in root if c.tag == 'Contest' and c.get('text') == 'President of the United States')
        for c in pres_race:
            if not c.tag == 'Choice':
                continue
            if c.get('text') == 'Donald J. Trump (I) (Rep)':
                for votes in c:
                    if votes.get('name') == 'Election Day Votes':
                        insert_votes(votes, R_election_day)
                    elif votes.get('name') == 'Absentee by Mail Votes':
                        insert_votes(votes, R_vote_by_mail)
                    elif votes.get('name') == 'Advanced Voting Votes':
                        insert_votes(votes, R_advanced_voting)
                    elif votes.get('name') == 'Provisional Votes':
                        insert_votes(votes, R_provisional)
            elif c.get('text') == 'Joseph R. Biden (Dem)':
                for votes in c:
                    if votes.get('name') == 'Election Day Votes':
                        insert_votes(votes, D_election_day)
                    elif votes.get('name') == 'Absentee by Mail Votes':
                        insert_votes(votes, D_vote_by_mail)
                    elif votes.get('name') == 'Advanced Voting Votes':
                        insert_votes(votes, D_advanced_voting)
                    elif votes.get('name') == 'Provisional Votes':
                        insert_votes(votes, D_provisional)

        counties = list(set.union(set(D_election_day.keys()),
                                  set(D_vote_by_mail.keys()),
                                  set(D_advanced_voting.keys()),
                                  set(D_provisional.keys()),
                                  set(R_election_day.keys()),
                                  set(R_vote_by_mail.keys()),
                                  set(R_advanced_voting.keys()),
                                  set(R_provisional.keys())))
        counties.sort()

        # print results
        print "County,2020 Votes D,2020 Votes R"
        for c in counties:
            # election day votes
            print "%s,%d,%d" % (c, D_election_day[c], R_election_day[c])
            # vote-by-mail votes
            print "%s,%d,%d" % (c, D_vote_by_mail[c], R_vote_by_mail[c])
            # advanced voting votes
            print "%s,%d,%d" % (c, D_advanced_voting[c], R_advanced_voting[c])
            # provisional votes
            print "%s,%d,%d" % (c, D_provisional[c], R_provisional[c])

if __name__ == "__main__":
    main()
