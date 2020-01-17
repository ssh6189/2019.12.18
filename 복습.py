DataFrame의 정수인덱스 라벨인덱스를 변경하려면 속성 df객체.index = 또는 df객체.set_index()
DataFrame의 데이터만 ....속성 df객체.values
DataFrame의 컬럼라벨(인덱스).... df객체의.columns
DataFrame의 데이터를 정수인덱스를 사용해서 행 단위 접근.... df객체.iloc[]
DataFrame의 데이터를 정수인덱스를 라벨인덱스를 사용해서 행 단위 접근....df객체.loc[]
DataFrame의 데이터를 정수인덱스를 사용해서 하나의 데이터 접근 df객체.iat[정수인덱스, 정수인덱스]
DataFrame의 데이터를 정수인덱스를 사용해서 하나의 데이터 접근 df객체.at[정수인덱스, 정수인덱스]
DataFrame의 특정 열(컬럼)의 모든 데이터를 접근....df객체.열이름 또는 df[열이름]
DataFrame의 특정 열(컬럼)을 삭제 del df객체[열이름]

두개의 DataFrame객체 산술연산 - 행인덱스와 열인덱스가 같은 데이터 요소끼리 산술연산수행
연산결과는  NA 대체하기 위한 옵션 fill_value
두개의 DataFrame 객체 산술연산 결과는 행인덱스와 열인덱스 모두에 정렬이 적용이 되어 결과 반환

pd.Series()
pd.DataFrame()
pd.Index()
DataFrame의 메타정보가 저장된 인덱스 객체는 생성된 데이터 프레임의 메타정보인 인덱스 데이터를 변경할 수 없다.
인덱스객체의 메서드 - append(), isin(), delete(), drop(), unique(), is_unique, reindex(), reset_index(), sort_index()

DataFrame의 행 삭제, 열(컬럼)삭제 메서드 - drop(,axis=1 또는 'columns', inplace=True)
DataFrame의 행, 열(컬럼) 단위로 함수를 적용을 해서 결과를 반환 받으려면 - apply()
DataFrame의 각각의 모든 데이터별로 함수를 적용, 결과 반환 - applymap()

기본 기술 요약 통계함수 - count(), describe(), min(), max(), quantile(), sum(), prod()
, cumsum(), pct_change(), corr(), cov(), corwith()

DataFrame의 행, 열(컬럼)단위로 데이터의 유일값 반환 - unique()
DataFrame의 행, 열(컬럼)단위로 데이터의 유일값 정렬된 형태로 반환 - unique.sort()
DataFrame의 행, 열(컬럼)단위로 데이터의 유일값 기준으로 빈도수를 반환 - value_count()
DataFrame의 행, 열(컬럼)단위로 데이터의가 존재하는지 확인 - isin()

pandas에서 제공하는 다양한 형태의 이용해서 dataframe으로 반환해주는 메서드 - read_XXXX()
pandas에서 제공하는 파서객체를 이용해서 다양한 형태의 파일들로 저장해주는 메서드 - to_XXXX()

DataFrame의 행단위의 중복체크 메서드 - duplicated()
DataFrame의 행단위의 중복체크후에 중복 행을 삭제하는 메서드 - drop_duplicates()
DataFrame의 각각의 모든 데이터별로 매핑작업 또는 매핑작업함수를 적용, 결과 반환 - map(), (단순 변환 작업은 replace())
