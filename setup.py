import os
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as fh:
    install_requires = fh.read().splitlines()

setup(
    name='read-ICESat-2',
    version='1.0.0.15',
    description='Python tools for obtaining and working with elevation data from the NASA ICESat-2 mission',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/tsutterley/read-ICESat-2',
    author='Tyler Sutterley',
    author_email='tsutterl@uw.edu',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Physics',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='ICESat-2 laser altimetry, ATLAS',
    packages=find_packages(),
    install_requires=install_requires,
    scripts=[os.path.join('scripts',f) for f in os.listdir('scripts')],
)
