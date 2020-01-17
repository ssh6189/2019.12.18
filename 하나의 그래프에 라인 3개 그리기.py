####figure 객체 사용 (하나의 그래프에 라인 3개 그리기) ####

###서울에서, '충청남도', '경상북도', '강원도'로 이동한 인구 데이터 값 선택 (1970 ~ 2018)###

###matplotlib 라이브러리를 이용한 시각화###
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc


#matplotlib 한글 폰트 오류 문제 해결
#from matplotlib import font_manager, rc
#font_path='./datas/malgun.ttf'      
#font_name= font_manager.FontProperties(fname=font_path).get_name()
#rc('font', fmaily=font_name)

plt.rc('font', family='Malgun Gothic')

#시도별 전출입 인구수.xlsx파일을 결측치는 0으로 대체,  첫번째 행을 header로 데이터 프레임 생서
df = pd.read_excel('C:/Users/student/Desktop/datas/datas/시도별 전출입 인구수.xlsx', fillna=0, header=0)

#데이터 프레임의 데이터중 누락값을 찾아서 앞 행의 동일컬럼의 값으로 채웁니다.
df = df.fillna(method='ffill')

#서울에서 다른 지역으로 이동한 데이터만 추출합니다.
mask = (df['전출지별'] =='서울특별시') & (df['전입지별']!='서울특별시')
df_seoul = df[mask]
df_seoul = df_seoul.drop(['전출지별'], axis=1)
df_seoul.rename({'전입지별': '전입지'}, axis=1, inplace=True)
df_seoul.set_index('전입지', inplace=True)
print(df_seoul)

#서울에서 경기도로 이동한 인구 데이터 값만 선택

sr_one = df_seoul.loc['경기도']

#서울에서 충청남도로 이동한 인구 데이터 값만 선택

sr_two = df_seoul.loc['충청남도']

#서울에서 경상북도로 이동한 인구 데이터 값만 선택

sr_three = df_seoul.loc['경상북도']

plt.plot(sr_one.index, sr_one.values, 'r--', sr_two.index, sr_two.values, 'g--',  sr_three.index, sr_three.values, 'b--')
plt.title('서울 전출인구')

#범례
plt.legend(labels=['서울->경기도', '서울->충청남도', '서울->경상북도'], loc='best')

plt.show()

