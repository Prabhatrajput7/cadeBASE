"""

if you want to run single file
pytest -v -s filename.py

now test file is in subdirectory
pytest -v -s directoryname/

to run a fx only
pytest -v -s -k "fxname"

to run a fx only
pytest -v -s -k "fxnameorfxname"

@mark
pytest -v -s -m "fxname"
"""