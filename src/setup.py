'''
The setup.py file is essential for installing and distributing Python projects. 
It is used to configure project metadata, dependencies, and other information 
required to build and install the package. This script is executed by the Python 
package installer (pip) to handle the installation of the package and its dependencies.
'''

from setuptools import setup, find_packages

setup(
    name='Netwrok_security_project',
    version='0.1.0',
    author='Vijayvithal',
    packages=find_packages(),
    install_requires=[],
    )
