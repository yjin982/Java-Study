'''
    교차분석 - 카이제곱(chi2, χ) 검정 
    범주형 데이터를 대상으로 교차빈도에 대한 기술통계량을 제공. 교차빈도에 대한 통계적 유의성을 검증하는 추론통계 분석 기법
    카이제곱 분포 : k개의 서로 독립적인 표준정규 확률 변수를 각각 제곱한 다음 합해서 얻어지는 분포
    chi2 = (기대값 - 실제값(=관찰값))제곱의 합 / 기대값
    [독립변수 : 범주형, 종속변수 : 범수형]
    
    검정 철차 : 가설을 설정 -> 유의 수준(α) 결정 -> 기대도수 구하기 -> 카이제곱값 구하기 -> 귀무가설 채택여부를 판단 -> 결과를 진술 
'''
import pandas as pd

data = pd.read_csv('../testdata/pass_cross.csv', encoding='euc-kr')
print(data.head(3), '    ', data.shape) #shape:(50, 4)

'''가설설정
귀무 : 공부하는 것과 합격 여부는 관계가 없다.
대립 : ------------ ---------------- 있다.
유의수준 : 95% 신뢰구간에서 0.05
'''

print()
# 수식 사용
#=======================================================================
print(data[(data['공부함'] == 1) & (data['합격'] == 1)].shape[0])   #공부하고 합격한 수 18
print(data[(data['공부함'] == 1) & (data['불합격'] == 1)].shape[0]) #공부하고 불합격한 수 7


print()
# 관찰값으로 빈도표 작성
data2 = pd.crosstab(index=data['공부안함'], columns=data['불합격'], margins=True)
data2.columns = ['합격', '불합격', '행합']
data2.index = ['공부함', '공부안함', '열합']
print(data2)
#         합격  불합격  행합
# 공부함     18    7  25
# 공부안함  12   13  25
# 열합       30   20  50


print()
# 기대값(기대도수) 얻기 : (각행 주변 합) * (각 열 주변 합) / 총합  == [25*30/50 = 15]
#         합격  불합격
# 공부함     15  10      
# 공부안함  15  10

chi2 = (15 - 18) ** 2 / 15 + (10 - 7) ** 2 / 10 + (15 - 12) ** 2 / 15 + (10 - 13) ** 2 /10
print('chi2 : ', chi2) # 3.0

print()
# 자유도 : (행 갯수 - 1) * (열 갯수 - 1) ==  [2-1 = 1]

'''
    카이제곱표로 유의수준, 자유도(df)를 이용해 임계값 계산
    카이제곱표는 검색 -> 3.84 : 보다 크면 기각, 하지만 카이제곱값은 3.0 이므로 채택

    결론 : chi2 검정 통계량 3.0은 임계값 3.84의 좌측(작음)으로 귀무가설 채택 
    >> 공부와 합격 여부는 관계가 없다 <<
'''

#=======================================================================

# 파이썬 기반의 카이제곱 검정 지원 모듈을 사용
import scipy.stats as stats
chi2, p, df, pred = stats.chi2_contingency(data2)
print(chi2, '    ', p, '    ', df, '\n', pred) #카이제곱값, p-value, 자유도, 기대값     => 3.0      0.5578254003710748      4

'''
    p-value(유의확률)0.5578 > 0.05(유의수준) 이므로 귀무가설 채택
''' 

#=======================================================================

'''
    카이제곱 검정의 목적
      독립성 검정 : 두 범주형 변수 간의 관련성 여부 판단
      적합도 : 두 데이터가 특정한 분포에서 추출된 것인가를 판단
      동질성 : 둘 이상의 다항분포가 동일한지 여부 판단
      ...
'''