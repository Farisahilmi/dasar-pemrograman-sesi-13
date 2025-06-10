import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("dasar-pemrograman-sesi-13/Data_Penduduk_EN.xlsx")

grouped = df.groupby(["last education", "sex"]).size().unstack(fill_value=0)
print(grouped)
grouped.plot(kind="bar", figsize=(10, 6))

plt.title("perbandingan pendidikan dan jenis kelamin")
plt.xlabel("pendidikan terakhir")
plt.ylabel("jumlah penduduk")
plt.legend(title="jenis kelamin")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()