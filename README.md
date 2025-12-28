# Solar2Soothe-CS

Solar2Soothe-CS is an open-source computational project focused on identifying heat-vulnerable communities and modeling solar-powered cooling feasibility under real-world constraints.

## Problem Motivation
Extreme heat disproportionately impacts low-income communities, the elderly, and households with limited access to reliable cooling. As climate change intensifies heatwaves, equitable allocation of cooling resources becomes a critical challenge.

This project approaches the problem from a computational perspective: rather than building hardware first, it models where cooling interventions would have the greatest impact and whether solar-powered systems can realistically meet local needs.

## Project Scope
This repository focuses on:
- Heat vulnerability scoring
- Data-driven prioritization of communities
- Solar + battery + cooling system simulation
- Transparent, interpretable decision models

This project does **not** represent a deployed cooling system.

## Open Source Commitment
Solar2Soothe-CS is released as an open-source project to promote transparency, reproducibility, and collaboration in addressing heat and energy inequity.

## Key Findings
1. Single day simulations demosntrated that a solar powered cooling system could provide up to about 18 hours of cooling. But, multi-day heatwave simulations revealed rapid battery depletion, causing the system to collapse within 2-3 days of consecutive days of extreme heat.
2. Introducing a priority based allocation strategy saved and preserved cooling access for the most heat-vulnerable communities. However, even prioritized systems failed under prolonged heatwaves when battery and solar capacity were starting to become insufficient.
3. Parameter sweeps showed that the resilience is determined by worst case scenarios rather than just typical daily performance. Systems designed around average conditions consistently failed under sustained heat waves.

## Design Implicaitons
1. The analysis indicates that battery capacity and solar generation must be sized to withstand multi-day heatwaves. Smaller systems that perform well under normal conditions fail catastrophically during prolonged heat events.
2. Algorithmic prioritization can extend protection to the most vulnerable communities, but it cannot compensate for fundamentally undersized systems. To that end, Effective deployment requires both ethical allocation strategies and sufficient energy storage.
3. By stress-testing configurations before physical deployment, this approach helps prevent the installation of systems that provide a false sense of security during extreme heat events.

## Limitations
The project relies on simplified models and publicly available data. Temperature exposure is approximated at the regional level rather than the household level. Grid reliability is represented using proxy variables due to limited outage data availability. Additionally, the cooling and battery models assume that constant power draw and do not account for adaptations, varying insulation quality, or dynamic demand. THese simplifications were intentional to maintain interpretability and transperancy.

## Future work
Future extensions/expansions of this work may include validating simulation assumptions with a small physical prototype, incorporating real time weather forecasts, and refining vulnerability metrics using localized sensor data. Additional work could explore adaptive cooling strategies that dynamically adjust usage based on forecasted heat stress and available energy reserves.
