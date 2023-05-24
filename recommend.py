import openai
import pandas as pd

df = pd.read_csv("음식점_10.csv", sep=",")

keyword = str(input())

for i in range(len(df)):
    if keyword in str(df['해시태그'][i]):
        print(df['명칭'][i], str(df['해시태그'][i]))

