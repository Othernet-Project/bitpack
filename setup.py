import os
from setuptools import setup


NAME = 'bitstream'
VERSION = '0.1'


def read(fname):
        """ Return content of specified file """
        return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name=NAME,
    description='Python data-binary serialization / deserialization library.',
    keywords='bitstream serialization deserialization',
    version=VERSION,
    author='Outernet Inc',
    author_email='apps@outernet.is',
    license='GPLv3',
    url='https://github.com/Outernet-Project/bitstream',
    long_description=read('README.rst'),
    py_modules=[NAME],
    install_required=[
        'bitarray',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
    ],
)
