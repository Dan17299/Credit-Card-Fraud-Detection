import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:\Users\Daniel\Documents\creditcard.csv")
print(df.Amount.max())
print(df.Amount.min())
df

