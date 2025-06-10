import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("dasar-pemrograman-sesi-13/Data_Penduduk_EN.xlsx")

df["Monthly Income"] = pd.to_numeric(df["Monthly Income"], errors="coerce")


bins = [0, 1_000_000, 3_000_000, 6_000_000, float("inf")]
labels = ["very low", "low", "middle", "high"]

df['Income Category'] = pd.cut(df['Monthly Income'], bins=bins, labels=labels, right=False)

income_counts = df["Income Category"].value_counts().sort_index()
print(income_counts)

plt.figure(figsize=(8, 8))
plt.pie(income_counts, labels=income_counts.index, autopct="%1.1f%%", startangle=140)
plt.title("Distribusi Kategori Pendapatan Warga")
plt.axis("equal")
plt.show()
