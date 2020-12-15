# pyfabrik

![Badge showing number of total downloads from PyPI.](https://pepy.tech/badge/pyfabrik)

![Badge showing number of monthly downloads from PyPI.](https://pepy.tech/badge/pyfabrik/month)

![Badge showing that code has been formated with Black formatter.](https://img.shields.io/badge/code%20style-black-000000.svg)

Python 3 implementation of
[FABRIK](http://www.andreasaristidou.com/FABRIK.html) (Forward And
Backward Reaching Inverse Kinematics).
## Installation

    pip install pyfabrik

## Usage

**NOTE: API is still very unstable (until the 1.0 release). Suggestions are welcome.**

```python

import pyfabrik
from vectormath import Vector3

initial_joint_positions = [Vector3(0, 0, 0), Vector3(10, 0, 0), Vector3(20, 0, 0)]
tolerance = 0.01

# Initialize the Fabrik class (Fabrik, Fabrik2D or Fabrik3D)
fab = pyfabrik.Fabrik3D(initial_joint_positions, tolerance)

fab.move_to(Vector3(20, 0, 0))
fab.angles_deg # Holds [0.0, 0.0, 0.0]

fab.move_to(Vector3(60, 60, 0)) # Return 249 as number of iterations executed
fab.angles_deg # Holds [43.187653094161064, 3.622882738369357, 0.0]
```


## Goal
![Inverse kinematics example with human skeleton.](http://www.andreasaristidou.com/publications/images/FABRIC_gif_1.gif)

## Roadmap

- [x] Basic 2D (flat chain)
- [x] Basic 3D (flat chain)
- [ ] 3D testing sandbox
- [ ] Basic 2D joint movement restrictions
- [ ] Basic 3D joint movement restrictions
- [ ] Complex chain support 2D
- [ ] Complex chain support 3D

## Contributing

__All contributions are appreciated.__

Read the paper [paper](http://www.andreasaristidou.com/publications/papers/FABRIK.pdf).

FABRIKs [homepage](http://www.andreasaristidou.com/FABRIK.html) has links to other implementations.

## [License](./LICENSE)

MIT License

Copyright (c) 2020 Saša Savić

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
