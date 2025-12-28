from src.heatwave_sim import simulate_heatwave


def test_resilience(
    battery_kwh_values,
    solar_watts_values,
    days=5,
    min_daily_hours=12
):
    results = []

    for battery_kwh in battery_kwh_values:
        for solar_watts in solar_watts_values:
            heatwave = simulate_heatwave(
                days=days,
                battery_kwh=battery_kwh,
                solar_watts=solar_watts
            )

            meets_requirement = all(
                day["cooling_hours"] >= min_daily_hours
                for day in heatwave
            )

            results.append({
                "battery_kwh": battery_kwh,
                "solar_watts": solar_watts,
                "resilient": meets_requirement,
                "daily_cooling": [d["cooling_hours"] for d in heatwave]
            })

    return results
