# TI Capital Allocation Simulator

Monte Carlo simulation of what happens if Texas Instruments reallocates $5-8B from dividends to capex, and how much that hurts investor confidence.

## How it works

Tests 5 scenarios (0%, 25%, 50%, 75%, 100% of the money reallocated), running 10,000 randomized simulations each. Capex payoff is random (mean 5%, std 10%). The investor penalty for cutting the dividend is 8% at a full cut, the high end of the -5% to -8% price reaction seen in dividend cut research, since TI is a 23-year Dividend Aristocrat.

## Run

    pip install numpy matplotlib
    python ti_simulation.py

Prints average return per scenario and saves a chart as `ti_basic_simulation.png`.

## Key assumptions

- Dividend yield: 3%
- Baseline stock growth: 7%
- Capex payoff: mean 5%, std 10%
- Full dividend cut penalty: 8%

Educational project, not investment advice.
