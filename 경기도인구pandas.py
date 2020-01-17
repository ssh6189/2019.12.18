import numpy as np
import matplotlib as plt
import pandas as pd
import seaborn as sns
import csv
import re

file_path = 'C:/Users/student/Desktop/datas/datas/경기도인구데이터.xlsx'
df = pd.read_excel(file_path)

#상위 5개 데이터 확인
print(df[0:5])

print("\n")

#배열 크기 확인
print("크기 :", df.shape)

print("\n")

#중복지역존재여부확인

print(df.duplicated())

print("\n")

#2017년 수원시 인구 합
print(df[df['구분'].str.contains('수원시')]['2017'].sum())

#2017년 인구가 50만 이상인 지역 출력

print("\n")


#2017년 경기도 전체 인구의 시별 인구 평균
