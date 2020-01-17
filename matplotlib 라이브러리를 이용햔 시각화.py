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

# 그래프 사이즈 지정 
plt.figure(figsize=(14, 5))

plt.plot(sr_one.index, sr_one.values)
#plt.plot(sr_one)
#마커 추가

plt.plot(sr_one.index, sr_one.values, marker='o', markersize=10)

#제목 추가
plt.title('서울->경기도 인구 이동')

#축 이름 
plt.xlabel('기간')
plt.ylabel('이동 인구수')

#범례
plt.legend(labels=['서울->경기'], loc='best')

#y축 범위 (최소값, 최대값) 지정
ylim(50000, 800000)
     
plt.annotate('' 
                xy = (20, 620000),   #화살표의 머리 끝점
                xytext(2, 290000),  #화살표의 꼬리 끝점
                xycoords='data' ,   #좌표체계
                arrowprops=dict(arrowstyle='->', color='skyblue', lw=5)  #화살표 스타일
                )
plt.annotate('' 
                xy = (47, 450000),   #화살표의 머리 끝점
                xytext(30, 480000),  #화살표의 꼬리 끝점
                xycoords='data' ,   #좌표체계
                arrowprops=dict(arrowstyle='->', color='olive', lw=5)  #화살표 스타일
               )

plt.annotate('인구이동 증가 (1070~1995)' 
                xy = (10, 550000),   #텍스트 위치 기준점
                rotation=25 ,          #텍트스의 회전각
                va='baseline',        #텍스트의 상하정렬
                ha = 'center',	  #텍스트의 좌우 정렬
                fontsize=15        #텍스트 크기
                )  


plt.show()   # 변경사항을 적용한 후 출력

####https://python-graph-gallery.com




