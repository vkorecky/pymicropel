# pymicropel
Python library for communication with Micropel PLC. 
The library solves everything for the smooth communication of your program with the Micropel PLC. Communication is over TCP/IP, the library handles everything from packet dropping to encryption.

You can install the library using the command
```bash
pip install pymicropel
```

## Deploy to PyPI
PyPI repository: [https://pypi.org/project/pymicropel/](https://pypi.org/project/pymicropel/)

```bash
pip install setuptools
pip install wheel
pip install twine
python setup.py sdist bdist_wheel
twine upload dist/*
```
