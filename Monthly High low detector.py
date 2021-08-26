import pandas as pd
import matplotlib.pyplot as plt
data1 = pd.read_csv("F:/2020/Monthly Segregated/January/BANKNIFTY.csv")
data1['DATE'] = pd.to_datetime(data1['DATE'])
data1['TIME'] = pd.to_datetime(data1['TIME']).dt.time
data1['Day'] = pd.DatetimeIndex(data1['DATE']).day

number = int(input("enter the day :"))
for j in data1['Day']:
    if j == number:
        ds = (data1[data1['Day'] == j].index.values)
OD= data1['TIME'][ds]
HD = data1['OPEN'][ds]
HD1 = data1['HIGH'][ds]
LD = data1['LOW'][ds]
OD = pd.DataFrame(OD)
Tq = pd.DataFrame(columns=['OPEN'])
Hq = pd.DataFrame(columns=['HIGH'])
Lq = pd.DataFrame(columns=['LOW'])
for i in OD['TIME']:
    if i.minute <= 30 and i.hour == 9:
         dq = (OD[OD['TIME'] == i].index.values)
         TP = data1['OPEN'][dq]
         THD = data1['HIGH'][dq]
         TLD = data1['LOW'][dq]
         for x in TP:
             Tq = Tq.append({'OPEN': x}, ignore_index=True)
         for a in THD:
             Hq = Hq.append({'HIGH': a}, ignore_index=True)
         for b in TLD:
             Lq = Lq.append({'LOW': b}, ignore_index=True)
df_merged=pd.concat([Tq,Hq,Lq], axis=1, ignore_index=False)
df_fulldata=pd.concat([OD,HD,HD1,LD], axis=1, ignore_index=False)
df_merged['BUY'] = df_merged.apply(lambda x : 'BUY' if x['OPEN'] >= x['HIGH']  else "", axis=1)
df_merged['SELL'] = df_merged.apply(lambda x : 'SELL' if x['OPEN'] <= x['LOW']  else "", axis=1)
df_fulldata['BUY'] = df_fulldata.apply(lambda x : 'BUY' if x['OPEN'] >= x['HIGH']  else "", axis=1)
df_fulldata['SELL'] = df_fulldata.apply(lambda x : 'SELL' if x['OPEN'] <= x['LOW']  else "", axis=1)
print(df_fulldata.describe())