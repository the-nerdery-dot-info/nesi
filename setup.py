'''
    Setup package information for PyPi distribution.

    Note:
        Before deploying, you need to build a git tagged version so
        PyPi can get the distribution.

        git tag -a major.minor -m 'Some Release Note(s)'
        git push --tags
'''

# All standard library imports
from distutils.core import setup

# All nesi imports
from nes import settings


NESI_BUILD = settings.build()

setup(
    name='nesi',
    packages=['nes'],
    version='{major}.{minor}'.format(
        major=NESI_BUILD['major_version'],
        minor=NESI_BUILD['minor_version']
    ),
    description='A rom hacking tool for the analysis of .nes rom images.',
    author=NESI_BUILD['author'],
    author_email=NESI_BUILD['author_email'],
    url='https://github.com/prophittcorey/nesi',
    download_url='https://github.com/prophittcorey/nesi/tarball/'
    '{major}.{minor}'.format(
        major=NESI_BUILD['major_version'],
        minor=NESI_BUILD['minor_version'],
    ),
    scripts=['nesi'],
    keywords=['nes', 'rom', 'roms', 'emulation', 'hacking', 'tools'],
    classifiers=[],
)
