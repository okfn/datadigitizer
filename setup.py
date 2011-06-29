from setuptools import setup, find_packages
from datadigitizer import __version__, __license__, __author__

setup(
    name = 'datadigitizer',
    version = __version__,
    packages = find_packages(),
    install_requires = open('./requirements').readlines(),

    # metadata for upload to PyPI
    author = __author__,
    author_email = 'datadigitizer@okfn.org',
    description = '',
    long_description = '',
    license = __license__,
    download_url = 'http://github.com/okfn/datadigitizer',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
