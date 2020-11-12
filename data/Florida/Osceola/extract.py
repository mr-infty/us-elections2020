import sys
from lxml import etree

def insert_votes(votes, d):
    for p in votes:
        # we don't convert p.get('votes') to an int because
        # some precincts haven't reported the results for certain (sic)
        # candidates
        votes = p.get('votes')
        if votes == 'N/A':
            votes = ''
        else:
            votes = str(int(votes))
        d[p.get('name')] = votes

def main():
    assert len(sys.argv) == 1

    with sys.stdin as f:
        tree = etree.parse(f)
        root = tree.getroot()
        
        D_election_day = {}
        D_early_vote = {}
        D_vote_by_mail = {}
        D_provisional_election_day = {}
        D_provisional_early_vote = {}

        R_election_day = {}
        R_early_vote = {}
        R_vote_by_mail = {}
        R_provisional_election_day = {}
        R_provisional_early_vote = {}

        pres_race = next(c for c in root if c.tag == 'Contest' and c.get('text') == 'President and Vice President')
        for c in pres_race:
            if not c.tag == 'Choice':
                continue
            if c.get('text') == 'Donald J. Trump':
                for votes in c:
                    if votes.get('name') == 'Election Day':
                        insert_votes(votes, R_election_day)
                    elif votes.get('name') == 'Early Voting':
                        insert_votes(votes, R_early_vote)
                    elif votes.get('name') == 'Vote-by-Mail':
                        insert_votes(votes, R_vote_by_mail)
                    elif votes.get('name') == 'Provisional Election Day':
                        insert_votes(votes, R_provisional_election_day)
                    elif votes.get('name') == 'Provisional Early Voting':
                        insert_votes(votes, R_provisional_early_vote)
            elif c.get('text') == 'Joseph R. Biden':
                for votes in c:
                    if votes.get('name') == 'Election Day':
                        insert_votes(votes, D_election_day)
                    elif votes.get('name') == 'Early Voting':
                        insert_votes(votes, D_early_vote)
                    elif votes.get('name') == 'Vote-by-Mail':
                        insert_votes(votes, D_vote_by_mail)
                    elif votes.get('name') == 'Provisional Election Day':
                        insert_votes(votes, D_provisional_election_day)
                    elif votes.get('name') == 'Provisional Early Voting':
                        insert_votes(votes, D_provisional_early_vote)

        counties = list(set.union(set(D_election_day.keys()),
                                  set(D_early_vote.keys()),
                                  set(D_vote_by_mail.keys()),
                                  set(D_provisional_election_day.keys()),
                                  set(D_provisional_early_vote.keys()),
                                  set(R_election_day.keys()),
                                  set(R_early_vote.keys()),
                                  set(R_vote_by_mail.keys()),
                                  set(R_provisional_election_day.keys()),
                                  set(R_provisional_early_vote.keys())))
        counties.sort()

        # print results
        print "Precinct,2020 Votes D,2020 Votes R"
        for c in counties:
            # election day votes
            print "%s,%s,%s" % (c, D_election_day[c], R_election_day[c])
            # early votes
            print "%s,%s,%s" % (c, D_early_vote[c], R_early_vote[c])
            # vote-by-mail votes
            print "%s,%s,%s" % (c, D_vote_by_mail[c], R_vote_by_mail[c])
            # provisional election day votes
            print "%s,%s,%s" % (c, D_provisional_election_day[c], R_provisional_election_day[c])
            # provisional early votes
            print "%s,%s,%s" % (c, D_provisional_early_vote[c], R_provisional_early_vote[c])

if __name__ == "__main__":
    main()
