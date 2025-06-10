import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("dasar-pemrograman-sesi-13/Data_Penduduk_EN.xlsx")
profesi_counts = df["Profesi"].value_counts()
print(profesi_counts)

plt.figure(figsize=(8, 8))
plt.pie(profesi_counts, labels=profesi_counts.index, autopct="%1.1f%%", startangle=140)
plt.axis("equal")
plt.show()