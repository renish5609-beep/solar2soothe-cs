def required_cooling_hours(hvs):
    if hvs >= 0.75:
        return 18
    elif hvs >= 0.50:
        return 12
    elif hvs >= 0.30:
        return 8
    else:
        return 4
