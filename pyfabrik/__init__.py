# __init__.py
#
# Copyright 2019 Saša Savić <sasa@savic.one>
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

import math
import sys

from vectormath import Vector2
from vectormath import Vector3

from typing import Tuple
from typing import List
from typing import Union


class FabrikBase:
    def __init__(
        self,
        joint_positions: List[Union[Vector2, Vector3]],
        link_lengths: List[float],
        tolerance: float,
    ) -> None:

        if not len(joint_positions) == len(link_lengths) + 1:
            raise AttributeError("joints and links counts don't match")

        # Tolerance is measured as distance (no negative values) and
        # when tolerance is 0 solver won't be able to finish.
        if tolerance <= 0:
            raise ValueError("tolerance must be > 0")
        self.tol: float = tolerance

        if any([ll <= 0 for ll in link_lengths]):
            raise ValueError("link lengths must be > 0")

        self.lengths: List[float] = link_lengths
        self.max_len: float = sum(link_lengths)

        # each joint sets an angle between two links
        self._angles: List[float] = [0.0] * len(joint_positions)

        self.joints: List[Union[Vector2, Vector3]] = []

    @property
    def angles(self) -> List[float]:
        self._angles[0] = math.atan2(self.joints[1].y, self.joints[1].x)

        prev_angle: float = self._angles[0]
        for i in range(2, len(self.joints)):
            p = self.joints[i] - self.joints[i - 1]
            abs_angle: float = math.atan2(p.y, p.x)
            self._angles[i - 1] = abs_angle - prev_angle
            prev_angle = abs_angle
        return self._angles

    def solvable(self, target: Union[Vector2, Vector3]) -> bool:
        return self.max_len >= target.length

    @property
    def angles_deg(self) -> List[float]:
        return [math.degrees(val) for val in self.angles]

    def _iterate(
        self, initial_position: Union[Vector2, Vector3], target: Union[Vector2, Vector3]
    ) -> int:
        iteration: int = 0
        while (self.joints[-1] - target).length > self.tol:
            iteration += 1

            self.joints[-1] = target
            for i in range(len(self.joints) - 2, -1, -1):
                next, current = self.joints[i + 1], self.joints[i]
                len_share = self.lengths[i] / (next - current).length
                self.joints[i] = (1 - len_share) * next + len_share * current

            self.joints[0] = initial_position
            for i in range(0, len(self.joints) - 1):
                next, current = self.joints[i + 1], self.joints[i]
                len_share = self.lengths[i] / (next - current).length
                self.joints[i + 1] = (1 - len_share) * current + len_share * next
        return iteration


class Fabrik2D(FabrikBase):
    def __init__(
        self,
        joint_positions: List[Vector2],
        link_lengths: List[float],
        tolerance: float = 0.0,
    ) -> None:

        super().__init__(joint_positions, link_lengths, tolerance)
        self.joints: List[Vector2] = joint_positions

    def move(self, target: Vector2, try_to_reach: bool = True) -> int:
        if not self.solvable(target):
            if not try_to_reach:
                return 0
            target = target.as_length(self.max_len)
        return self._iterate(self.joints[0], target)

    def solvable(self, target: Vector2) -> bool:
        return super().solvable(target)


class Fabrik3D(FabrikBase):
    def __init__(
        self,
        joint_positions: List[Vector3],
        link_lengths: List[float],
        tolerance: float = 0.0,
    ) -> None:
        super().__init__(joint_positions, link_lengths, tolerance)
        self.joints: List[Vector3] = joint_positions

    def solvable(self, target: Vector3) -> bool:
        return super().solvable(target)

    def move(self, target: Vector3, try_to_reach: bool = True) -> int:
        if not self.solvable(target):
            if not try_to_reach:
                return 0
            target = target.as_length(self.max_len)
        return self._iterate(self.joints[0], target)


Fabrik = Fabrik2D

__all__ = ["Fabrik", "Fabrik2D", "Fabrik3D"]
