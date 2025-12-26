import pandas as pd

def normalize(series):
    return (series - series.min()) / (series.max() - series.min())


def compute_heat_vulnerability(df):
    df["T"] = normalize(df["temp_exposure"])
    df["E"] = normalize(1 / df["median_income"])
    df["A"] = normalize(df["age_sensitive_pct"])
    df["G"] = normalize(df["grid_proxy"])

    df["heat_vulnerability_score"] = (
        0.35 * df["T"] +
        0.30 * df["E"] +
        0.20 * df["A"] +
        0.15 * df["G"]
    )

    return df.sort_values("heat_vulnerability_score", ascending=False)


if __name__ == "__main__":
    df = pd.read_csv("data/dallas_v1.csv")
    ranked = compute_heat_vulnerability(df)
    print(ranked[["tract", "heat_vulnerability_score"]])
