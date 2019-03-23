#!/usr/bin/env python3
from vectormath import Vector2
from pyfabrik import Fabrik

poss = [Vector2(0, 0), Vector2(10, 0), Vector2(20, 0)]
lens = [10, 10]
fab = Fabrik(poss, lens, 0.05)

def main():
    print(fab.move(Vector2(20, 0)))
    print(fab.joints)

    print(fab.move(Vector2(60, 60)))
    print(fab.joints)
    print(fab.angles_deg)

    print(fab.move(Vector2(0, 20)))
    print(fab.joints)
    print(fab.angles_deg)

    print(fab.move(Vector2(0, 10)))
    print(fab.joints)
    print(fab.angles_deg)

if __name__ == '__main__':
    import timeit
    times = timeit.Timer('main()', setup='from __main__ import main').repeat(5, number=100)

    times = [time / 100 for time in times]
    print('finished in {}s:'.format(sum(times)))
    for i, time in enumerate(times):
        print('\t {} - {}'.format(i+1, time))
