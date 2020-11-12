import sys
from lxml import etree

def insert_votes(votes, d):
    for p in votes:
        d[p.get('name')] = int(p.get('votes'))

def main():
    assert len(sys.argv) == 1
    
    D_election_day = {}
    D_vote_by_mail = {}
    D_advanced_voting = {}
    D_provisional = {}

    R_election_day = {}
    R_vote_by_mail = {}
    R_advanced_voting = {}
    R_provisional = {}

    tree = etree.parse(sys.stdin)
    root = tree.getroot()
    
    pres_race = next(c for c in root if c.tag == 'Contest' and c.get('text') == 'President of the United States/Presidentede los Estados Unidos')
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
    with open('precincts.csv','w') as f, \
         open('precincts_election_day.csv','w') as f_election_day, \
         open('precincts_absentee.csv','w') as f_absentee, \
         open('precincts_early_vote.csv','w') as f_early_vote, \
         open('precincts_provisional.csv','w') as f_provisional:
        # print headers
        for g in f, f_election_day, f_absentee, f_early_vote, f_provisional:
            g.write("Precinct,2020 Votes D,2020 Votes R\n")
        # print bodies
        for c in counties:
            f.write("%s,%d,%d\n" % (c, D_election_day[c] +
                                       D_vote_by_mail[c] +
                                       D_advanced_voting[c] +
                                       D_provisional[c],
                                       R_election_day[c] +
                                       R_vote_by_mail[c] +
                                       R_advanced_voting[c] +
                                       R_provisional[c]))
            f_election_day.write("%s,%d,%d\n" % (c, D_election_day[c], R_election_day[c]))
            f_absentee.write("%s,%d,%d\n" % (c, D_vote_by_mail[c], R_vote_by_mail[c]))
            f_early_vote.write("%s,%d,%d\n" % (c, D_advanced_voting[c], R_advanced_voting[c]))
            f_provisional.write("%s,%d,%d\n" % (c, D_provisional[c], R_provisional[c]))

if __name__ == "__main__":
    main()
