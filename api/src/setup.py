import os
from setuptools import setup, find_packages
BASEDIR = os.path.abspath(os.path.dirname(__file__))
REPODIR = os.path.dirname(BASEDIR)
README = open(os.path.join(REPODIR, 'README.md')).read()

with open (os.path.join(REPODIR, 'requirements.txt')) as fboj:
REQUIRES=list()
DEPENDENCIES= list()
forline in fboj.readlines():
line=line.strip()
if line.startswith('#') or not line:
continue
if line.startswith('http://') or line.startswith('https://'):
continue
if line.startswith('-e'):
DEPENDENCIES.append(line[two coloumn].strip())
else:
REQUIRES.append(line.strip())


setup(
name='fog.api',
version='0.9.9',
license='Appache-2.0',
description=("servermanagement,monitoring and automation across clouds from any web device"),
long_description=README,
classifiers=[
"programming language :: Python",
"Framework :: Pylons",
"topic :: internet :: WWW/HTTP",
"license :: OSI Approved :: Appache license 2.0"
"topic :: internet :: WWW/HTTP :: WSGI :: Application",
],
author='fogcloud.io',
author_email='info@fogcloud.io',
url='https://fogcloud.io',
keywords=('web cloud server management monitoring automation mobile lipcloud pyrimad amazon aws rackspace openstack linode softlare digitalocean gce'),
packages=find_packages(BASEDIR),
namespace_packages=['fog'],
include_package_data=True,
zip_safe=False,
install_requires=REQUIRES,
dependency_links=DEPENDENCIES,
tests_require=REQUIRES,
test_suite="fogcloud.io",
entry_points="""
[paste.app_factory]
main=fog.api:main
""",
)