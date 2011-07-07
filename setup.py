"""
setup.py for FLiP, Logical Framework in Python
see http://docs.python.org/distutils/packageindex.html

To create or update the FLiP page at PyPI: python setup.py register

To make distribution: python setup.py sdist -v -f --formats=gztar,zip

To upload distribution to PyPI: 
 python setup.py sdist -v -f --formats=gztar,zip upload --show-response

To install from unpacked distribution: python setup.py install

It is not really necessary to install, you can just run out of the
unpacked distrbution.  It is convenient to put FLiP-1.2 on PYTHONPATH
because it contains the flip package, use bin/flip_path.  However,
installing might be even more convenient, because it usually puts the
flip package in a directory which is already on PYTHONPATH.

Most of the distribution contents are all specified in MANIFEST.in,
not in setup.py.
"""

from distutils.core import setup

setup(
    # Metadata for PyPI
    # see http://docs.python.org/distutils/setupscript.html#meta-data
    # also http://docs.python.org/distutils/apiref.html#module-distutils.core
    name = 'FLiP',
    version = '1.2',
    author = 'Jonathan Jacky',
    author_email = 'jon@u.washington.edu',
    maintainer = 'Jonathan Jacky',
    maintainer_email = 'jon@u.washington.edu',
    url = 'http://staff.washington.edu/jon/flip/www/',
    description = 'F L i P : Logical Framework in Python',
    long_description = open('README.rst').read(),
    download_url = 'http://staff.washington.edu/jon/flip/www/download.html',
    license = 'GNU General Public License (GPL)',

    keywords = 'logical framework python theorem prover proof checker natural deduction',

    packages = ['flip', 'flip.grail', 'flip.logic', 'flip.poset', 
                'flip.poset.test', 'flip.test' ],

    # from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.3',
        'Topic :: Scientific/Engineering :: Mathematics',
        ],
    )
