import urllib, sys
import lxml.html
import os.path
from urlparse import urljoin

BASE_URL = 'https://electionresults.sos.ca.gov/returns/president'
FORCE_UPDATE = False

def get_tree_from_url_or_file(url, fname, force_update=FORCE_UPDATE):
    if force_update or not os.path.isfile(fname):
        urllib.urlretrieve(url, fname)
    with open(fname, 'r') as f:
        return lxml.html.parse(f)

def main():
    global FORCE_UPDATE

    if len(sys.argv) == 2 and sys.argv[1] == '--update':
        FORCE_UPDATE = True
    else:
        assert len(sys.argv) == 1

    #f = urllib.urlopen(BASE_URL)
    #tree = lxml.html.parse(f)
    #f.close()
    tree = get_tree_from_url_or_file(BASE_URL, 'counties.html', force_update=FORCE_UPDATE)

    root = tree.getroot()
    county_links = root.find_class('findDistrict')[0].xpath('child::ul')[0].iterlinks()
    D_results = {}
    R_results = {}
    for l in county_links:
        if not '/county/' in l[2]:
            continue
        county = l[0].text
        url = urljoin(BASE_URL, l[2])

        #f = urllib.urlopen(url)
        #c_root = lxml.html.parse(f).getroot()
        #f.close()
        c_root = get_tree_from_url_or_file(url, county + '.html', force_update=FORCE_UPDATE).getroot()

        vote_table = c_root.find_class('stateCountyCandResultsTbl')[0]

        for tr in vote_table.xpath('tbody//tr'):
            tds = tr.xpath('td')
            CAND_NAME_IDX = next(i for i in range(len(tds)) if tds[i].get('class') == 'candName')
            candidate_name = tds[CAND_NAME_IDX].text

            if candidate_name == 'Joseph R. Biden':
                D_results[county] = int(tds[CAND_NAME_IDX + 1].text.replace(',', ''))
            elif candidate_name == 'Donald J. Trump':
                R_results[county] = int(tds[CAND_NAME_IDX + 1].text.replace(',', ''))
    # print results
    print "County,2020 Votes D,2020 Votes R"
    counties = list(set.union(set(D_results.keys()),
                              set(R_results.keys())))
    for c in counties:
        print "%s,%d,%d" % (c, D_results[c], R_results[c])

if __name__ == "__main__":
    main()
