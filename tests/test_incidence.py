
import os
import sys

# Ensure `src/` is on sys.path so tests can be run directly with python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from incidence import record_incident


def test_record_incident():
    inc = record_incident("Database outage", 3)
    assert isinstance(inc, dict)
    assert inc["title"] == "Database outage"
    assert inc["severity"] == 3


