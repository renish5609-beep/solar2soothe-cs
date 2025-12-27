def simulate_heatwave(
    days=3,
    solar_watts=400,
    battery_kwh=4.0,
    ac_watts=300,
    sun_hours=5,
):
    battery_wh = battery_kwh * 1000 * 0.85
    daily_results = []

    for day in range(1, days + 1):
        cooling_hours = 0

        for hour in range(24):
            # solar generation window
            if 10 <= hour < 10 + sun_hours:
                battery_wh += solar_watts

            # AC demand
            if battery_wh >= ac_watts:
                battery_wh -= ac_watts
                cooling_hours += 1
            else:
                break

        daily_results.append({
            "day": day,
            "cooling_hours": cooling_hours,
            "battery_remaining_wh": round(battery_wh, 1)
        })

    return daily_results
