import setuptools

setuptools.setup(
    name='pyfabrik',
    version='0.1dev2',
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
