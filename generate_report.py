import os, csv, sys, math
import kolmogorov
import graph

ALPHA = 0.01

def print_vote_report(data, race_id, party):
    global ALPHA
    IDX = data[0].index('2020 Votes %s' % party)
    cand = {"R": "Trump",
            "D": "Biden"}[party]

    dps = [int(l) for l in map(lambda x: x[IDX], data[1:]) if len(l.strip()) > 0 and int(l) > 0]
    dps_log = map(lambda x: math.log10(float(x)) % 1.0, dps)
    dmax = kolmogorov.kolmogorov_dmax(kolmogorov.uniform_dist, dps_log)
    dcrit = kolmogorov.dcrit(len(dps))
    if dmax <= dcrit:
        print "The election results for %s **seem to satisfy** Benford's law up to an error of %.0f%%:\n" % (cand, 100.0*ALPHA)
    else:
        print "The election results for %s **violate** Benford's law with %.0f%% certainty:\n" % (cand, 100.0*(1.0 - ALPHA))
    print "- dmax: %f" % dmax
    print "- dcrit: %f" % dcrit
    print "- N: %d" % len(dps)
    print ""

    fpath = os.path.join('graphics', race_id + '_' + party)
    with open(fpath + '.eps', 'w') as f:
        graph.generate_empirical_distribution_illustration(dps_log, f)
    print "![Empirical distribution of fractional part of decimal logarithm of votes for %s (%s) (black line) and uniform distribution (gray line)](%s)" % (race_id, party, fpath + '.pdf')

def main():
    print "# Results"
    states = sorted(list(os.walk('data').next()[1]))
    for state in states:
        print "## " + state

        state_path = os.path.join('data', state)
        # check whether state counts votes per county or per precinct (some states don't have counties)
        if os.path.isfile(os.path.join(state_path, 'counties.csv')):
            print "The test results for the state-wide election results (per county) of %s are as follows.\n" % state
            with open(os.path.join(state_path, 'counties.csv'), 'r') as f:
                data = list(csv.reader(f))
        else:
            print "The test results for the state-wide election results (per precinct) of %s are as follows.\n" % state
            with open(os.path.join(state_path, 'precincts.csv'), 'r') as f:
                data = list(csv.reader(f))

        print_vote_report(data, state, 'D')
        print ""
        print_vote_report(data, state, 'R')
        print ""

        # County-wide Results
        counties = sorted(list(os.walk(state_path).next()[1]))
        for county in counties:
            print "### " + county
            print "The test results for the county-wide election results (per precinct) of %s County, %s are as follows.\n" % (county, state)

            with open(os.path.join(state_path, county, 'precincts.csv'), 'r') as f:
                data = list(csv.reader(f))

            print_vote_report(data, county+','+state, 'D')
            print ""
            print_vote_report(data, county+','+state, 'R')
            print ""

if __name__ == '__main__':
    main()
