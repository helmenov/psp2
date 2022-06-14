#%%
import pandas as pd
import numpy as np

#%%
df = pd.read_csv('heights14.csv',skipinitialspace=True,skiprows=[0])
print(df)

#%%
df2 = pd.pivot(df,index=['ID'],columns=['Q'],values=['A'])
print(df2)

#%%
df2.columns=['性別','身長']
print(df2)

#%%
SexSet = {'男','女'}
df2['性別'] = pd.Categorical(df2['性別'],categories=SexSet,ordered=False)
df2['身長'] = df2['身長'].astype('float')
print(df2)

#%%

df_male = df2[df2['性別']=='男']
df_female = df2[df2['性別']=='女']
print(df_male)
print(df_female)

#%%
mean_male = df_male['身長'].mean()
std_male = df_male['身長'].std(ddof=0)
size_male = df_male['身長'].size
ustd_male = np.sqrt(size_male/(size_male-1)*std_male*std_male)
se_male = ustd_male/np.sqrt(size_male)

print('==男==')
print(f'標本平均:{mean_male:5.2f}')
print(f'標本標準偏差:{std_male:5.2f}')
print(f'母集団平均:{mean_male:5.2f}±{se_male:5.2f}')
print(f'母集団標準偏差:{ustd_male:5.2f}')

# %%
mean_female = df_female['身長'].mean()
std_female = df_female['身長'].std(ddof=0)
size_female = df_female['身長'].size
ustd_female = np.sqrt(size_female/(size_female-1)*std_female*std_female)
se_female = ustd_female/np.sqrt(size_female)

print('==女==')
print(f'標本平均:{mean_female:5.2f}')
print(f'標本標準偏差:{std_female:5.2f}')
print(f'母集団平均:{mean_female:5.2f}±{se_female:5.2f}')
print(f'母集団標準偏差:{ustd_female:5.2f}')

# %%
