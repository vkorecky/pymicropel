from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.9.0'
DESCRIPTION = 'Python library for communication with Micropel PLC.'
LONG_DESCRIPTION = 'A package that allows to communicate with Micropel PLCs over network.'

# Setting up
setup(
    name="pymicropel",
    version=VERSION,
    author="Vladislav Korecky",
    author_email="<vladislav@korecky.org>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['pytest', 'typing'],
    keywords=['python', 'plc', 'tcp_ip', 'communication', 'iot', 'automation'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)