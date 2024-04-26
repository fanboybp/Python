import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, median_absolute_error
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file Abalone.data vào một DataFrame
df=pd.read_csv('E:\\Python\\Python\\PYTHON\\Kiem_tra\\Bai_1\\Abalone.data')
df.drop(['Sex'], axis=1, inplace=True) # bỏ cột Sex

X = df[['Length', 'Diam', 'Height', 'Whole', 'Shucked', 'Viscera', 'Shell']]  
y = df['Rings']  # Nhãn

# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Xây dựng và huấn luyện mô hình hồi quy tuyến tính
model = LinearRegression()
model.fit(X_train, y_train)

# Đánh giá mô hình
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
medae = median_absolute_error(y_test, y_pred)

print("Mean Absolute Error:", mae)  
print("Mean Squared Error:", mse)   
print("Median Absolute Error:", medae) 

summary_table = pd.DataFrame({'Min': df.min(), 'Max': df.max(), 'Mean': df.mean()}, index=['Length', 'Diam', 'Height', 'Whole', 'Shucked', 'Viscera', 'Shell', 'Rings'])

# Hiển thị bảng với các thuộc tính nằm theo hàng ngang
summary_table_transposed = summary_table.transpose()
print(summary_table_transposed)

# Biểu đồ tương quan giữa rings (tuổi) và trọng lượng toàn bộ
plt.scatter(df["Rings"], df["Whole"], c='brown', label='Tuổi - Ring', alpha=0.5) 
plt.title('Tuổi vs Trọng lượng toàn bộ')
plt.xlabel('Tuổi (Rings)')
plt.ylabel('Trọng lượng toàn bộ (Whole)')
plt.legend()
plt.show()

# Biểu đồ tương quan giữa rings (tuổi) và chiều dài
plt.scatter(df["Rings"], df["Length"], c='green', label='Length - Chiều dài', alpha=0.5, marker='s') 
plt.title('Tuổi vs Chiều dài')
plt.xlabel('Tuổi (Rings)')
plt.ylabel('Chiều dài (Length)')
plt.legend()
plt.show()

# Biểu đồ tương quan giữa rings (tuổi) và đường kính
plt.scatter(df["Rings"], df["Diam"], c='blue', label='Diameter - Đường kính', alpha=0.5, marker='^') 
plt.title('Tuổi vs Đường kính')
plt.xlabel('Tuổi (Rings)')
plt.ylabel('Đường kính (Diameter)')
plt.legend()
plt.show()

# Biểu đồ tương quan giữa chiều dài (length) và trọng lượng toàn bộ
plt.scatter(df["Length"], df["Whole"], c='red', label='Length - Chiều dài', alpha=0.5, marker='o') 
plt.title('Chiều dài vs Trọng lượng toàn bộ')
plt.xlabel('Chiều dài (Length)')
plt.ylabel('Trọng lượng toàn bộ (Whole)')
plt.legend()
plt.show()