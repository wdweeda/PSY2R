# %%
import numpy as np
import pandas as pd
import seaborn as sns

sns.set_theme(style="white")
default_palette = [
    (0.5372549019607843, 0.615686274509804, 0.6431372549019608),
    (0.788235294117647, 0.2, 0.07058823529411765),
    (0.9803921568627451, 0.9372549019607843, 0.8196078431372549),
    (0.8627450980392157, 0.5254901960784314, 0.23137254901960785),
]

# %%
data = pd.read_csv("between2x2.csv", sep=" ")
data["A"] = (data["Group"] - 1) // 2 + 1
data["B"] = (data["Group"] - 1).mod(2) + 1
data

# %%
sns.violinplot(data, y="DependentVariable", x="A", hue="B", palette=default_palette[:2])
