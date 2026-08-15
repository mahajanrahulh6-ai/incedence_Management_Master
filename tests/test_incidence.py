from incidence import record_incident


def test_record_incident():
    inc = record_incident("Database outage", 3)
    assert isinstance(inc, dict)
    assert inc["title"] == "Database outage"
    assert inc["severity"] == 3
