from src.heatwave_sim import simulate_heatwave


def prioritized_heatwave_simulation(
    ranked_df,
    protection_fraction=0.20,
    days=5
):
    n_protected = max(1, int(len(ranked_df) * protection_fraction))
    protected = ranked_df.head(n_protected)["tract"].tolist()

    results = {}

    heatwave_results = simulate_heatwave(days=days)

    for tract in ranked_df["tract"]:
        if tract in protected:
            results[tract] = heatwave_results
        else:
            results[tract] = [
                {
                    "day": d["day"],
                    "cooling_hours": 0,
                    "battery_remaining_wh": 0
                }
                for d in heatwave_results
            ]

    return results, protected

