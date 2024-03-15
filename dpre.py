import os
import pandas as pd
import subprocess

output_directory = '/home/doc-bd-a1/service-result'

os.makedirs(output_directory, exist_ok=True)

df = pd.read_csv('/home/doc-bd-a1/tested.csv')
df.drop(["Cabin","Ticket","Name","PassengerId"], axis=1, inplace=True)
df['Age'] = df['Age'].fillna(df['Age'].mean())
df.dropna(inplace=True)
df['Age'] = df['Age'].astype('int')
df["Fare"] = (df["Fare"] - df["Fare"].mean()) / df["Fare"].std()
df = pd.get_dummies(df, columns=["Sex",'Embarked'])
output_file = '/home/doc-bd-a1/service-result/res_dpre.csv'
df.to_csv(output_file, index=False)

subprocess.run(["python3", "eda.py"])
