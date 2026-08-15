"""Simple example incidence module."""

def record_incident(title: str, severity: int) -> dict:
    """Record a simple incident structure.

    Args:
        title: Short title of the incident.
        severity: Integer severity (1-5).

    Returns:
        A dict representing the incident.
    """
    return {"title": title, "severity": int(severity)}
