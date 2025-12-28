import matplotlib.pyplot as plt
import numpy as np

from src.resilience_analysis import test_resilience

battery_options = [4, 6, 8, 10]
solar_options = [400, 600, 800]

results = test_resilience(
    battery_kwh_values=battery_options,
    solar_watts_values=solar_options,
    days=5,
    min_daily_hours=12
)

heatmap = np.zeros((len(battery_options), len(solar_options)))

for r in results:
    i = battery_options.index(r["battery_kwh"])
    j = solar_options.index(r["solar_watts"])
    heatmap[i, j] = 1 if r["resilient"] else 0

plt.figure(figsize=(7, 5))
plt.imshow(heatmap, cmap="Greens")

plt.xticks(range(len(solar_options)), solar_options)
plt.yticks(range(len(battery_options)), battery_options)

plt.xlabel("Solar Capacity (Watts)")
plt.ylabel("Battery Capacity (kWh)")
plt.title("System Resilience Under 5-Day Heatwave\n(≥12 Cooling Hours/Day)")

for i in range(len(battery_options)):
    for j in range(len(solar_options)):
        plt.text(
            j, i,
            "✓" if heatmap[i, j] == 1 else "✗",
            ha="center", va="center",
            color="black",
            fontsize=14
        )

plt.tight_layout()
plt.savefig("outputs/resilience_heatmap.png")
print("Saved outputs/resilience_heatmap.png")
