from setuptools import setup, find_namespace_packages

try:
    with open('README.md', 'r') as readme:
        long_description = readme.read()
except:
    long_description = 'HY_Features python package.'

# Set __version__ to prevent analysis check issues, but later make sure it gets read properly
__version__ = ''
_version_file = 'hypy/_version.py'
exec(open(_version_file).read())
# Raise error if __version__ is still the pre-set empty string
if __version__ == '':
    raise RuntimeError('Failed to read package "__version__" from package version file "{}".'.format(_version_file))

setup(
    name='hypy',
    version=__version__,
    description='Hy_Features Package.',
    long_description=long_description,
    author='',
    author_email='',
    url='https://github.com/noaa-owp/hypy',
    license='',
    install_requires=['pandas', 'hydrotools.nwis-client'],
    packages=find_namespace_packages(exclude=('test', 'src'))
)
