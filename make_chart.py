import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("defect-logs/defect-log.csv")
order = ["Critical", "High", "Medium", "Low"]
colors = {"Critical": "#b71c1c", "High": "#f57c00",
          "Medium": "#fbc02d", "Low": "#7cb342"}

table = (pd.crosstab(df["Category"], df["Severity"])
           .reindex(columns=order, fill_value=0))
table["Total"] = table.sum(axis=1)
table = table.sort_values("Total", ascending=True)

ax = table[order].plot(kind="barh", stacked=True, figsize=(9, 5),
                       color=[colors[s] for s in order])
ax.set_xlabel("Number of defects")
ax.set_ylabel("Defect category")
ax.set_title("PSVS S1-S12: Defects by Category and Severity")
for i, total in enumerate(table["Total"]):
    ax.text(total + 0.1, i, str(total), va="center")
plt.tight_layout()
plt.savefig("defect-logs/defect-chart.png", dpi=200)
print(table)
