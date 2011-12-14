def timedelta_to_seconds(td):
    return (td.microseconds / 1000000.0) + td.seconds + (td.days * 24.0 * 3600.0)
