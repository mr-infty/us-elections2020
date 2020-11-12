import json, sys

def main():
    assert len(sys.argv) == 1
    data = json.load(sys.stdin)

    print "Precinct,2020 Votes D,2020 Votes R"
    for p in data['precincts']:
        print "%s,%d,%d" % (p['name'],
                            p['contests'][0]['c'][1]['t'],
                            p['contests'][0]['c'][0]['t'])


if __name__ == "__main__":
    main()
