PyScope
=======

Python scope interface for Rigol Oscilloscopes (Tested with a Rigol DS1102E, but should work with other series). There are basically three different files :

- instrument.py, which is the low-level interface to the scope
- ScopeInterface.py, which contains the functions to measure data on the scope
- interface_test.py, to test the scope functionnalities