import pandas as pd
df = pd.read_csv(r'C:\201408_trip_data.csv')
df1 = df['Start Station'][df['Subscriber Type']=='Subscriber'].value_counts().idxmax()

print(df1)