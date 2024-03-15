import matplotlib.pyplot as plt
import pandas as pd
import subprocess

df = pd.read_csv('/home/doc-bd-a1/service-result/res_dpre.csv')

plt.figure(figsize=(8, 6))
ax = df[['Pclass', 'Survived']].groupby('Pclass').mean().Survived.plot(kind='bar')
ax.set_xlabel('Pclass')
ax.set_ylabel('Survival Probability')

plt.savefig('/home/doc-bd-a1/service-result/vis.png')

plt.close()

subprocess.run(["python3", "model.py"])
