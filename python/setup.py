from setuptools import setup, find_namespace_packages

try:
    with open('README.md', 'r') as readme:
        long_description = readme.read()
except:
    long_description = 'HY_Features python package.'

exec(open('hypy/_version.py').read())

setup(
    name='hypy',
    version=__version__,
    description='Hy_Features Package.',
    long_description=long_description,
    author='',
    author_email='',
    url='https://github.com/noaa-owp/hypy',
    license='',
    install_requires=['pandas'],
    packages=find_namespace_packages(exclude=('test', 'src'))
)
