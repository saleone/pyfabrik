#!/usr/bin/env python3
# test.py
#
# Copyright 2019 Saša Savić <sasa@sasa-savic.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later


from vectormath import Vector2
from pyfabrik import Fabrik

poss = [Vector2(0, 0), Vector2(10, 0), Vector2(20, 0)]
lens = [10, 10]
fab = Fabrik(poss, lens, 0.01)

def test_main():
    assert fab.move(Vector2(20, 0)) == 0
    assert fab.angles_deg == [0.0, 0.0, 0.0]
    print(fab.angles_deg)

    assert fab.move(Vector2(60, 60)) == 249
    assert fab.angles_deg == [43.187653094161064, 3.622882738369357, 0.0]
    print(fab.angles_deg)

    assert fab.move(Vector2(0, 20)) == 250
    assert fab.angles_deg == [88.19119752090381, 3.6158044811401675, 0.0]
    print(fab.angles_deg)

    assert fab.move(Vector2(0, 10)) == 5
    assert fab.angles_deg == [30.05682734132901, 119.97158632933548, 0.0]
    print(fab.angles_deg)

if __name__ == '__main__':
    import timeit
    times = timeit.Timer('test_main()', setup='from __main__ import test_main').repeat(1, number=1)

    times = [time / 100 for time in times]
    print('finished in {}s:'.format(sum(times)))
    for i, time in enumerate(times):
        print('\t {} - {}'.format(i+1, time))
