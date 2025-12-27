def simulate_day(
    solar_watts=400,
    battery_kwh=4.0,
    ac_watts=300,
    sun_hours=5,
    hours=24
):
    battery_wh = battery_kwh * 1000 * 0.85
    cooling_hours = 0

    for hour in range(hours):
        # solar generation
        if 10 <= hour < 10 + sun_hours:
            battery_wh += solar_watts

        # AC demand
        if battery_wh >= ac_watts:
            battery_wh -= ac_watts
            cooling_hours += 1
        else:
            break

    return cooling_hours
