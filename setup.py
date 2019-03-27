# setup.py
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


import setuptools

setuptools.setup(
    name='pyfabrik',
    version='0.1-dev3',
    author='Saša Savić',
    author_email = 'sasa@sasa-savi.com',
    url = 'https://github.com/saleone/pyfabrik',
    packages=setuptools.find_packages(),
    license='GNU GPLv3',
    long_description=open('README.rst').read(),
    install_requires=['vectormath'],
    setup_requires=['wheel'],
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
    ],
)
