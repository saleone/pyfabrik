#!/usr/bin/env python3

import pytest
from vectormath import Vector2
from vectormath import Vector3
from pyfabrik import Fabrik2D
from pyfabrik import Fabrik3D
from pyfabrik import Fabrik


def test_default_fabrik_class_is_2d_solver():
    assert Fabrik is Fabrik2D


def test_2d_correctly_moves_the_joints():
    poss = [Vector2(0, 0), Vector2(10, 0), Vector2(20, 0)]
    fab = Fabrik2D(poss, 0.01)

    assert fab.move_to(Vector2(20, 0)) == 0
    assert fab.angles_deg == [0.0, 0.0, 0.0]
    print(fab.angles_deg)

    assert fab.move_to(Vector2(60, 60)) == 249
    assert fab.angles_deg == [43.187653094161064, 3.622882738369357, 0.0]
    print(fab.angles_deg)

    assert fab.move_to(Vector2(0, 20)) == 250
    assert fab.angles_deg == [88.19119752090381, 3.6158044811401675, 0.0]
    print(fab.angles_deg)

    assert fab.move_to(Vector2(0, 10)) == 5
    assert fab.angles_deg == [30.05682734132901, 119.97158632933548, 0.0]
    print(fab.angles_deg)


def test_3d_correctly_moves_in_2d_space():
    poss = [Vector3(0, 0, 0), Vector3(10, 0, 0), Vector3(20, 0, 0)]
    fab = Fabrik3D(poss, 0.01)

    assert fab.move_to(Vector3(20, 0, 0)) == 0
    assert fab.angles_deg == [0.0, 0.0, 0.0]
    print(fab.angles_deg)

    assert fab.move_to(Vector3(60, 60, 0)) == 249
    assert fab.angles_deg == [43.187653094161064, 3.622882738369357, 0.0]
    print(fab.angles_deg)

    assert fab.move_to(Vector3(0, 20, 0)) == 250
    assert fab.angles_deg == [88.19119752090381, 3.6158044811401675, 0.0]
    print(fab.angles_deg)

    assert fab.move_to(Vector3(0, 10, 0)) == 5
    assert fab.angles_deg == [30.05682734132901, 119.97158632933548, 0.0]
    print(fab.angles_deg)


def test_value_error_raised_when_joints_overlap():
    poss = [Vector3(0, 0, 0), Vector3(10, 0, 0), Vector3(10, 0, 0)]
    with pytest.raises(ValueError) as exinfo:
        fab = Fabrik3D(poss, 0.01)
    assert str(exinfo.value) == "link lengths must be > 0"


@pytest.mark.parametrize("tolerance", [-1.0, 0.0])
def test_value_error_raised_when_tolerance_isnt_positive(tolerance):
    poss = [Vector3(0, 0, 0), Vector3(10, 0, 0), Vector3(10, 0, 0)]
    with pytest.raises(ValueError) as exinfo:
        fab = Fabrik3D(poss, tolerance)
    assert str(exinfo.value) == "tolerance must be > 0"


if __name__ == "__main__":
    import timeit

    times = timeit.Timer("test_main()", setup="from __main__ import test_main").repeat(
        1, number=1
    )

    times = [time / 100 for time in times]
    print("finished in {}s:".format(sum(times)))
    for i, time in enumerate(times):
        print("\t {} - {}".format(i + 1, time))
