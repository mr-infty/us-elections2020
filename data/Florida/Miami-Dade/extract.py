import urllib, sys
import lxml.html
from lxml import etree

# Don't use detailed vote statistics right now because too many precincts don't report them
USE_DETAILED_VOTE_STATISTIC = False

def normalize_vote(s):
    if s == '-':
        return ''
    else:
        return str(int(s.replace(',', '')))

def main():
    assert len(sys.argv) == 1
    tree = lxml.html.parse(sys.stdin)
    root = tree.getroot()

    if USE_DETAILED_VOTE_STATISTIC:
        D_election_day = {}
        D_early_votes = {}
        D_vote_by_mail = {}
        D_provisional = {}

        R_election_day = {}
        R_early_votes = {}
        R_vote_by_mail = {}
        R_provisional = {}
    else:
        D_total_votes = {}
        R_total_votes = {}

    for prec_hdr in root.find_class('PrecinctHeader'):
        precinct = prec_hdr.find_class('PrecinctName')[0].text
        tbl = next(prec_hdr.itersiblings(tag='table'))
        tbl_hdr = tbl.xpath('thead//th')

        CHOICE_IDX = next(i for i in range(len(tbl_hdr)) if tbl_hdr[i].text == 'Choice')
        if USE_DETAILED_VOTE_STATISTIC:
            ELECT_DAY_IDX = next(i for i in range(len(tbl_hdr)) if tbl_hdr[i].text == 'Election Day')
            EARLY_VOTE_IDX = next(i for i in range(len(tbl_hdr)) if tbl_hdr[i].text == 'Early Votes')
            VOTE_BY_MAIL_IDX = next(i for i in range(len(tbl_hdr)) if tbl_hdr[i].text == 'Vote By Mail')
            PROVISIONAL_IDX = next(i for i in range(len(tbl_hdr)) if tbl_hdr[i].text == 'Provisional')
        else:
            TOTAL_VOTE_IDX = next(i for i in range(len(tbl_hdr)) if tbl_hdr[i].text == 'Total Votes')

        for r in tbl.xpath('tbody//tr'):
            if 'Donald J. Trump' in r[CHOICE_IDX].text:
                if USE_DETAILED_VOTE_STATISTIC:
                    R_election_day[precinct] = normalize_vote(r[ELECT_DAY_IDX].text)
                    R_early_votes[precinct] = normalize_vote(r[EARLY_VOTE_IDX].text)
                    R_vote_by_mail[precinct] = normalize_vote(r[VOTE_BY_MAIL_IDX].text)
                    R_provisional[precinct] = normalize_vote(r[PROVISIONAL_IDX].text)
                else:
                    R_total_votes[precinct] = normalize_vote(r[TOTAL_VOTE_IDX].text)
            elif 'Joseph R. Biden' in r[CHOICE_IDX].text:
                if USE_DETAILED_VOTE_STATISTIC:
                    D_election_day[precinct] = normalize_vote(r[ELECT_DAY_IDX].text)
                    D_early_votes[precinct] = normalize_vote(r[EARLY_VOTE_IDX].text)
                    D_vote_by_mail[precinct] = normalize_vote(r[VOTE_BY_MAIL_IDX].text)
                    D_provisional[precinct] = normalize_vote(r[PROVISIONAL_IDX].text)
                else:
                    D_total_votes[precinct] = normalize_vote(r[TOTAL_VOTE_IDX].text)

    if USE_DETAILED_VOTE_STATISTIC:
        precincts = list(set.union(set(D_election_day.keys()),
                                   set(D_early_votes.keys()),
                                   set(D_vote_by_mail.keys()),
                                   set(D_provisional.keys()),
                                   set(R_election_day.keys()),
                                   set(R_early_votes.keys()),
                                   set(R_vote_by_mail.keys()),
                                   set(R_provisional.keys())))
    else:
        precincts = list(set.union(set(D_total_votes.keys()),
                                   set(R_total_votes.keys())))

    precincts.sort()
    # print results
    print "Precinct,2020 Votes D,2020 Votes R"
    for p in precincts:
        if USE_DETAILED_VOTE_STATISTIC:
            # election day votes
            print "%s,%s,%s" % (p, D_election_day[p], R_election_day[p])
            # early votes
            print "%s,%s,%s" % (p, D_early_votes[p], R_early_votes[p])
            # vote-by-mail votes
            print "%s,%s,%s" % (p, D_vote_by_mail[p], R_vote_by_mail[p])
            # provisional votes
            print "%s,%s,%s" % (p, D_provisional[p], R_provisional[p])
        else:
            print "%s,%s,%s" % (p, D_total_votes[p], R_total_votes[p])

if __name__ == '__main__':
    main()
