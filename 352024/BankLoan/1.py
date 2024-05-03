# Dữ liệu vay tín dụng ngân hàng được lưu trữ trong 2 file
# Bank_Personal_Loan_Modelling.csv, bank_loan.pdf
# 1. (3đ) Hãy đọc phần mô tả dữ liệu trong các file trên để hiểu rõ các trường (thuộc tính)
# dữ liệu và cho biết :
# a. Có bao nhiêu trường và bao nhiêu mẫu
# b. Hãy giải thích các trường (thuộc tính) và đơn vị tính
# 2. (2đ) Hãy lập bảng thống kê Min, Max, Trung bình cho các thuộc tính dữ liệu sau:
# Tuổi, Kinh nghiệm, Thu nhập
# 3. (2đ) Cho biết có bao nhiêu:
# a. Người độ tuổi dưới 30 mà có thu nhập trên 50.000$
# b. Người có độ tuổi dưới 30 mà có kinh nghiệm trên 5 năm
# 4. (3đ) Biểu diễn các quan hệ dữ liệu bằng biểu đồ:
# a. Tuổi với kinh nghiệm
# b. Tuổi với thu nhập
# c. Tuổi với chi tiêu trung bình trong tháng
# d. Thu nhập với chi tiêu trung bình trong tháng
# Các kết quả ở mục 1, 2, 3 được ghi vào file ketqua.txt

    
'''
    1. ID : ID Khách hàng
    2. Age: Tuổi của khách hàng tính theo số năm đã hoàn thành
    3. Experience: Kinh nghiệm # năm kinh nghiệm chuyên môn
    4. Income: Thu thập hàng năm của khách hàng
    5. ZIP code: Địa chỉ mã ZIP
    6. Family: Quy mô gia đình khách hàng
    7. CCAvg: Trung bình chỉ tiêu bằng thẻ tín dụng mỗi ngày
    8. Education: Trình độ học vấn
            1. Undergrad: Đại học
            2. Graduate: Tốt nghiệp
            3. Advanced/Professional: Nâng cao/ Chuyên nghiệp
    9. Mortgage: Thế chấp: Giá trị thế chấp căn nhà nếu có
    10. Personal Loan: Khoản vay cá nhân: Khách hàng này có chấp nhận khoản vay cá nhân được cung cấp trong chiến dịch trước không?
    11. Securities Account: Tài khoản chứng khoán : Khách hàng có tài khoản chứng khoán tại ngân hàng không?
    12. CD Account: Tài khoản CD : Khách hàng có tài khoản chứng chỉ tiền gửi (CD) tại ngân hàng không?
    13. Online: Trực tuyến : Khách hàng có sử dụng dịch vụ ngân hàng trực tuyến không?
    14. Credit card: Thẻ tín dụng : Khách hàng có sử dụng thẻ tín dụng do
'''

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, median_absolute_error
import matplotlib.pyplot as plt

data_path = "E:\\Python\\Python\\PYTHON\\352024\\BankLoan\\Bank_Personal_Loan_Modelling.csv"
data = pd.read_csv(data_path)

data.drop(['ID'], axis=1, inplace=True) # bỏ cột ID
# Chuẩn bị dữ liệu cho việc huấn luyện mô hình
X = data[['Experience', 'Income', 'ZIP Code', 'Family', 'CCAvg', 'Education', 'Mortgage', 'Personal Loan', 'Securities Account', 'CD Account', 'Online', 'CreditCard']]  # Đặc trưng
y = data['Age']  # tuổi


# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)

# Xây dựng và huấn luyện mô hình quy hồi tuyến tính
model = LinearRegression()
model.fit(X_train, y_train)

# Đánh giá mô hình
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
medae = median_absolute_error(y_test, y_pred)
# lấy giá trị của người 30 tuổi có trên 50k$

cout = data.loc[(data['Age'] < 30) & (data['Income'] > 50)].shape[0]
cout2 = data.loc[(data['Age'] < 30) & (data['Experience'] > 5)].shape[0]

print("Mean Absolute Error:", mae)  #sai số tuyệt đốitrung bình
print("Mean Squared Error:", mse)   #Sai số bình phương trung bình
print("Median Absolute Error:", medae) #Sai số tuyệt đối trung vị

print("Số người dưới 30 tuổi mà có thu nhập trên 50000 $ :" + str(cout))
print("Số người dưới 30 tuổi mà có kinh nhiệm trên 5 năm :" + str(cout2))

# Tạo dataFame từ các giá trị tối thiểu, tối đa, trung bình
summany_table = pd.DataFrame({'Min': data.min(), 'Max': data.max(), 'Mean': data.mean()}, index = ['Age', 'Experience', 'Income'])

# Hiển thị bảng với các thuộc tính
summany_table_transposed = summany_table.transpose()
print(summany_table_transposed)

# Biểu diễn các tương quan biểu đồ
# Tạo khung và các subplot
fig, axs = plt.subplots(2, 2, figsize=(15, 7))

# Biểu đồ tương quan: Tuổi(Age) với Kinh nghiệm(Experience)
axs[0, 0].scatter(data["Age"], data["Experience"], c='aqua')
axs[0, 0].set_title('Tuổi vs Kinh nhiệm')
axs[0, 0].set_xlabel('Tuổi (Age)')
axs[0, 0].set_ylabel('Kinh nhiệm (Exprrience)')

# Biểu đồ tương quan: Tuổi(Age) với thu nhập cá nhân(Income)
axs[0, 1].scatter(data["Age"], data["Income"], c='green')
axs[0, 1].set_title('Tuổi vs Thu nhập cá nhân')
axs[0, 1].set_xlabel('Tuổi (Rings)')
axs[0, 1].set_ylabel('Thu nhập cá nhân (Income)')

# Biểu đồ tương quan: Tuổi(Age) với chi tiêu hàng thàng(CCAvg)
axs[1, 0].scatter(data["Age"], data["CCAvg"], c='pink')
axs[1, 0].set_title('Tuổi vs Trung bình chi tiêu hàng tháng')
axs[1, 0].set_xlabel('Tuổi (Age)')
axs[1, 0].set_ylabel('Trung bình chi tiêu hàng tháng (CCAvg)')


# Biểu đồ tương quan: Thu thập(Income) với chi tiêu hàng tháng(CCAvg)
axs[1, 1].scatter(data["Income"], data["CCAvg"], c='orange')
axs[1, 1].set_title('Thu nhập cá nhân vs Trung bình chi tiêu hàng tháng')
axs[1, 1].set_xlabel('Thu nhập cá nhân (Income)')
axs[1, 1].set_ylabel('Trung bình chi tiêu hàng tháng (CCAvg)')

# Hiển thị biểu đồ
plt.tight_layout()
plt.show()