# __init__.py
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

import logging
import math
import sys

from vectormath import Vector2

from typing import Tuple
from typing import List


class Fabrik:
    def __init__(
            self,
            joint_positions: List[Vector2],
            link_lengths: List[float],
            tolerance: float = 0.0) -> None:

        if not len(joint_positions) == len(link_lengths) + 1:
            raise AttributeError("number of joints doesn't match number of links")

        self.joints: List[Vector2] = joint_positions
        self.lengths: List[float] = link_lengths
        self._angles: List[float] = [0.0] * len(joint_positions)
        self.tol: float = tolerance

        self.max_len: float = sum(link_lengths)

    def move(self, target: Vector2, try_to_reach: bool = True) -> int:
        if not self.solvable(target):
            if not try_to_reach:
                return 0
            target = target.as_length(self.max_len)

        initial_pos: Vector2 = self.joints[0]
        iteration: int = 0
        while (self.joints[-1] - target).length > self.tol:
            self.joints[-1] = target
            for i in range(len(self.joints) - 2, 0, -1):
                len_to_new = (self.joints[i+1] - self.joints[i]).length
                len_factor = self.lengths[i] / len_to_new

                self.joints[i] = (1 - len_factor) * self.joints[i+1] + len_factor * self.joints[i]

            self.joints[0] = initial_pos
            for i in range(0, len(self.joints) - 1):
                len_to_new = (self.joints[i+1] - self.joints[i]).length
                len_factor = self.lengths[i] / len_to_new

                self.joints[i+1] = (1 - len_factor) * self.joints[i] + len_factor * self.joints[i+1]
        return iteration

    @property
    def angles(self) -> List[float]:
        self._angles[0] = math.atan2(self.joints[1].y,self.joints[1].x);

        prevAngle: float = self._angles[0];
        for i in range(2, len(self.joints)):
            ax: float = self.joints[i-1].x;
            ay: float = self.joints[i-1].y;
            bx: float = self.joints[i].x;
            by: float = self.joints[i].y;

            aAngle: float = math.atan2(by - ay, bx - ax);

            self._angles[i - 1] = aAngle - prevAngle;

            prevAngle = aAngle;
        return self._angles

    @property
    def angles_deg(self) -> List[float]:
        return [math.degrees(val) for val in self.angles]

    def solvable(self, target: Vector2) -> bool:
        return self.max_len >= target.length

__all__ = ['Fabrik']
