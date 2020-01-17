import pandas as pd
import matplotlib.pyplot as plt

#데이터 프레임의 시각화
#matplotlib inline#%matplotlib.notebook

df = pd.read_excel('C:/Users/student/Desktop/datas/datas/남북한발전전력량.xlsx')

df_ns = df.iloc[[0,5], 3:] #남한, 북한 발전량 합계 데이터만 추출
                
df_ns.index = ['South', 'North']
df_ns.columns = df_ns.columns.map(int) #열 이름 자료형을 정수형으로 변경
tdf_ns = df_ns.T
print(tdf_ns.head())
tdf_ns.plot(kind='bar')

plt.show()

tdf_ns.plot(kind='hist')


df = pd.read_csv('C:/Users/student/Desktop/datas/datas/auto-mpg.csv', header = None)

print(df.head())

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleation', 'model year', 'origin', 'name']

df.plot(x='weight', y='horsepower', kind='scatter')

df.plot[['mpg', 'cylinders']].plot(kind='box')

plt.show()
