import pandas as pd

from src.heat_risk import compute_heat_vulnerability
from src.cooling_sim import simulate_day
from src.decision_engine import required_cooling_hours


def main():
    # Load data
    df = pd.read_csv("data/dallas_v1.csv")

    # Compute heat vulnerability
    ranked = compute_heat_vulnerability(df)

    # Simulate cooling capacity
    available_hours = simulate_day()

    # Determine required cooling
    ranked["required_hours"] = ranked["heat_vulnerability_score"].apply(required_cooling_hours)
    ranked["meets_need"] = ranked["required_hours"] <= available_hours

    print("\n=== Solar2Soothe Cooling Feasibility Analysis ===\n")
    print(f"Available cooling hours per day: {available_hours}\n")

    print(ranked[[
        "tract",
        "heat_vulnerability_score",
        "required_hours",
        "meets_need"
    ]])


if __name__ == "__main__":
    main()
