# import librarires
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import median_absolute_error

# load data
data = pd.read_csv('E:\\Python\\Python\\PYTHON\\STOCK\\Fish\\Fish.csv')
# Luu y, chu cai oa X - du lieu ma tran - mang 2 chieu
#        chu cai thuong y - du lieu la vector - mamg 1 chieu
data.drop(['Species'], axis = 1, inplace=True) # bo cot Species
X = data.iloc[: ,[1, 2, 3, 4, 5]]              # du lieu ma tran
y = data.iloc[: ,0]                            # du lieu vector
# y = data[["weight"]]
# Tach thanh cac tap train va test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)


LM = LinearRegression()
LM.fit(X_train, y_train)

print("Hieu suat huan luyen:", LM.score(X_train, y_train))
print("Hieu suat test:", LM.score(X_test, y_test))

y_pred = LM.predict(X_test)
print('Cac gia tri Weight du doan la:\n')
print(y_pred)
print("----------------------------")

MAEValue = mean_absolute_error(y_test, y_pred, multioutput='uniform_average')
print('Mean Absolute Error Value (MAE) : ', MAEValue)

MSEValue = mean_squared_error(y_test, y_pred, multioutput='uniform_average')
print('Mean Squared Error Value (MSE): ', MSEValue)

MdSEValue = median_absolute_error(y_test, y_pred)
print('Median Squared Error Value (MdSE) : ', MdSEValue)

# Do thi
plt.xlabel("Featuares- cac dac trung")
plt.ylabel("Trong luong")
plt.title("Du doan trong luong ca")
plt.plot(X_test, y_pred, "ro", label = "Du doan")
plt.plot(X_train, y_train, "b^", label = "Huan luyen")
plt.legend()
plt.show()
print("Xong!")