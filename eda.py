import pandas as pd
import subprocess

df = pd.read_csv('/home/doc-bd-a1/service-result/res_dpre.csv')
old_df = pd.read_csv('/home/doc-bd-a1/tested.csv')




gender_survival = old_df.groupby('Sex')['Survived'].mean()
class_survival = df.groupby('Pclass')['Survived'].mean()

age_bins = [0, 18, 35, 60, 100]
age_labels = ['Child', 'Young Adult', 'Adult', 'Elderly']

df['AgeGroup'] = pd.cut(df['Age'], bins=age_bins, labels=age_labels)

age_group_survival = df.groupby('AgeGroup',observed=True)['Survived'].mean()

insights =[gender_survival,class_survival,age_group_survival]
ins=[]

for i in insights:
    
    ins.append(i.to_string()) 


for i, insight in enumerate(ins):
    with open(f'/home/doc-bd-a1/service-result/eda-in-{i}.txt', 'w') as file:
        file.write(insight)


subprocess.run(["python3", "vis.py"])
