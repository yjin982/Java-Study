'''
    mtcars 데이터를 가지고 선형 회귀분석 연습2 (LinearRegression) 
'''
from sklearn.linear_model import LinearRegression
import statsmodels.api
import pandas as pd


mtcars = statsmodels.api.datasets.get_rdataset('mtcars').data
x = mtcars[['hp']].values #matrix로 얻기
y = mtcars[['mpg']].values
# print(x) #(32, 1)
# print(y) #(32, 1)


import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')
# 시각화
plt.scatter(x, y)
plt.xlabel('마력수')
plt.ylabel('연비')
# plt.show()

fit_model = LinearRegression().fit(x, y)  # 가중치(기울기), 추정된 상수, bias, 편향(절편)을 리턴
print('기울기(가중치) : {},    절편(bias) : {}'.format(fit_model.coef_[0], fit_model.intercept_))

# ※dataset을 train / test로 분리(7/3) 후 모델 학습 후 모델 평가를 진행해야 함※
pred = fit_model.predict(x)  # 사실은 train data로 학습하고, test data로 예측값 보기(모델 평가)
print('pred :', pred[:3].flatten())


# 새로운 값으로 연비 추정
new_hp = [[110]]
new_pred = fit_model.predict(new_hp)
print('new_pred : ', new_pred)
print('\n\n')


''' 참고 
평균 제곱 오차(Mean squared error - mse)
  머신러닝 뿐만 아니라 영상처리 영역에서도 자주 사용되는 추측값에 대한 정확성 측정 방법. 
  간단히 말하면 오차의 제곱에 대해 평균을 취한 것이다. 작을 수록 원본과의 오차가 적은 것이므로 추측한 값의 정확성이 높은 것. 
  이것을 근거로 최소평균제곱오차, 평균제곱근오차 등이 있다. 
 
평균 제곱근 편차(Root Mean Square Deviation; RMSD) 또는 평균 제곱근 오차(Root Mean Square Error; RMSE)는 
  추정 값 또는 모델이 예측한 값과 실제 환경에서 관찰되는 값의 차이를 다룰 때 흔히 사용하는 측도이다. 정밀도(precision)를 표현하는데 적합하다. 
  각각의 차이값은 잔차(residual)라고도 하며, 평균 제곱근 편차는 잔차들을 하나의 측도로 종합할 때 사용된다.
'''
from sklearn.metrics import mean_squared_error
import numpy as np
lin_mse = mean_squared_error(y, pred)
lin_rmse = np.sqrt(lin_mse)
print("평균 제곱 오차 : ", lin_mse)
print("평균 제곱근 편차 : ", lin_rmse)


