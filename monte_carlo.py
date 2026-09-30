import numpy as np
import matplotlib.pyplot as plt
 
dividend_yield = 0.03        # TI's approximate dividend yield
normal_stock_growth = 0.07   # roughly average annual stock growth
 
capex_payoff_mean = 0.05     # conservative, since TI is a legacy/cyclical company
capex_payoff_std = 0.10      # capex payoff is uncertain
 
full_cut_penalty = 0.08      # research-grounded: ~8% price hit for a full dividend cut
 
allocation_scenarios = [0, 25, 50, 75, 100]
n_simulations = 10000
 
averages = []
risks = []
 
for pct in allocation_scenarios:
    allocation_fraction = pct / 100
    outcomes = []
 
    for i in range(n_simulations):
        # Random ingredient: how well does the capex investment pay off?
        capex_payoff = np.random.normal(capex_payoff_mean, capex_payoff_std)
 
        dividend_portion_return = (1 - allocation_fraction) * dividend_yield
        capex_portion_return = allocation_fraction * capex_payoff
        investor_penalty = allocation_fraction * full_cut_penalty
 
        total_return = normal_stock_growth + dividend_portion_return + capex_portion_return - investor_penalty
        outcomes.append(total_return)
 
    averages.append(np.mean(outcomes))
    risks.append(np.std(outcomes))
 
print("Reallocation % | Average Return")
print("-" * 35)
for pct, avg in zip(allocation_scenarios, averages):
    print(f"{pct:>13}% | {avg:>14.1%}")
 
decline = (averages[0] - averages[-1]) * 100
print(f"\nReturn declines by {decline:.1f} percentage points from 0% to 100% reallocation.")
 
plt.figure(figsize=(8, 5))
plt.bar([f"{p}%" for p in allocation_scenarios], averages, yerr=risks, capsize=6, color="steelblue")
plt.title("Average Simulated Return by % Reallocated to Capex")
plt.xlabel("% of $5-8B Reallocated to Capex")
plt.ylabel("Average Annual Return")
plt.axhline(0, color="gray", linestyle="--")
plt.tight_layout()
plt.savefig("ti_basic_simulation.png", dpi=150)
plt.show()
 
print("\nChart saved as ti_basic_simulation.png")
