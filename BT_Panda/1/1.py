import pandas as pd
import numpy as np
import matplotlib.pyplot as plt # Thư viện vẽ biểu đồ

# Đọc file cvs trên máy

# peoples_df = pd.read_csv('E:\\Python\\Python\\PYTHON\\BT_Panda\\1\\CafeF.HSX.Upto30.01.2023.csv')

# in Datafarm ra màn hình
# print(peoples_df.head(5))

# # xem thông tin của dataframe
# print(peoples_df.info())

# Lấy dữ liệu theo 2 cột trên peoples
# print(peoples_df[['<Ticker>', '<Open>']].head(5))

# Kết hợp theo dòng và cột: Lấy dữ liệu cột Ticker, Open, lấy từ dòng 5-10
# print(peoples_df[['<Ticker>', '<Open>']][5:10])

# Kết hợp theo dòng và cột: Lấy các bản ghi theo điều kiện

# young_pp = peoples_df[peoples_df['<Close>'] > peoples_df['<Open>']]
# print(young_pp[:5])

path = "E:\\Python\\Python\\PYTHON\\BT_Panda\\1\\"

'''
Dữ liệu từ cafef.vn
'''

stockData = [] # Dữ liệu chứng khoán
#--------------------------------------

def LoadData2(filename):
    '''
    Nạp dữ liệu bằng thư viện panda, trả về là một dataframe (mảng 2 chiều)
    '''
    print("Loading data ...")
    stock_df = pd.read_csv(path + filename) # Dùng thư viện panda để đọc
    return stock_df # Trả về một dataframe
#--------------------------------------

def GetPriceClose(stockID):
    '''
    Trả về một list là giá trị của giá chứng khoán lúc đóng cửa
    stock: Mã chứng khoán
    '''
    
    listPrice = stockData[stockData["<Ticker>"] == stockID] #Lọc dataframe theo mã chứng khoán
    listPrice = list(listPrice["<Close>"])  # Tách ra chỉ lấy giá lúc đóng cửa
    return listPrice # mảng giá theo stockID sẽ trả về
# -------------------------------------------

def PriceMA(listPrice, nDay):
    '''
    Tham số: listStock - mảng giá chứng khoán từ trước đến nay
    n - chu kỳ n ngày 5, 20, 50
    Trả về một danh sách các giá chứng khoán trung bình trong n ngày
    '''
    
    length = len(listPrice) # Chiều dài của danh sách giá chứng khoán
    print("length:", length)
    listPriceMA = [] # Danh sách giá trung bình cộng chứng khoán sẽ trả
    queue_nDay = [] # Hàng đợi kiểu FIFO với chiều dài n ngày
    value = 0       # Biến để tính giá chứng khoán
    count = 0       # Biến đếm
    n = length - 1      # Biến chỉ số phần tử
    # Tính nDay giá trị đàu tiên
    while count < nDay:
        queue_nDay.append(listPrice[n])  # Cho vào hàng đợi FIFO
        value += listPrice[n]            # Cộng dồn giá
        count += 1                      # Đếm
        n -= 1                          # Phần tử tiếp theo của danh sách
    listPriceMA.append(value/nDay) # Giá trị trung bình đầu tiên
    while n > 0:
        value -= queue_nDay[0] # Bỏ bớt value của phần tử đầu tiên
        queue_nDay.pop(0)      # Loại phần tử đầu tiên ra khỏi hàng
        queue_nDay.append(listPrice[n]) #Thêm giá đóng của của phần tử mới
        value += queue_nDay[nDay - 1]
        listPriceMA.insert(0, value/nDay)
        n -= 1
        print("n:", n)
    return listPriceMA
#---------------------------------------------------
def calculate_RSI(listPrice, nDay):
    delta = [listPrice[i] - listPrice[i - 1] for i in range(1, len(listPrice))]
    gain = [delta[i] if delta[i] > 0 else 0 for i in range(len(delta))]
    loss = [-delta[i] if delta[i] < 0 else 0 for i in range(len(delta))]

    avg_gain = sum(gain[:nDay]) / nDay
    avg_loss = sum(loss[:nDay]) / nDay

    rs_values = []
    for i in range(nDay, len(delta)):
        avg_gain = ((avg_gain * (nDay - 1)) + gain[i]) / nDay
        avg_loss = ((avg_loss * (nDay - 1)) + loss[i]) / nDay
        rs = avg_gain / avg_loss if avg_loss != 0 else 0
        rs_values.append(rs)

    rsi_values = [100 - (100 / (1 + rs)) for rs in rs_values]
    return [None]*(nDay - 1) + rsi_values

#---------------------------------------------------
def ShowPrice(nDay):
    print('Ma Chung Khoan : ')
    stockID = str(input())
    listPrice = GetPriceClose(stockID)
    listPrice.reverse()
    print(listPrice)
    listPriceMA5 = PriceMA(listPrice,5)
    listPriceMA10 = PriceMA(listPrice,10)
    listPriceMA20 = PriceMA(listPrice,20)
    
    # Calculating RSI
    rsi_values = calculate_RSI(listPrice,7)

    plt.subplot(2, 1, 1)
    plt.plot(listPrice[-nDay:],     'ro-',      label = " Gia", color = 'red')
    plt.plot(listPriceMA5[-nDay:],  'bD-',      label = " MA5",  color = 'orange')
    plt.plot(listPriceMA10[-nDay:], 'bD-',      label = " MA10", color = 'green')
    plt.plot(listPriceMA20[-nDay:], 'bD-',      label = " MA20", color = 'yellow')
    plt.plot(0,                label = 'RSI',   color = 'blue')   
    plt.title("Bieu do gia trung binh dong :" + stockID)
    plt.xlabel("Day")
    plt.ylabel("Price - VND")
    plt.legend()
    ax = plt.gca().twinx()
    plt.plot(rsi_values[-nDay:],                label = 'RSI',   color = 'blue')
    ax.set_ylabel("RSI")
    plt.show()

#------------------------------------------------------

# Chương trình chính
print("Phân tích dữ liệu STOCK")
print("------------------------")
stockData = LoadData2("CafeF.HSX.Upto30.01.2023.csv")
stockID = "HBC"
nDay = 100
chon = 1
while chon != 3:
    print("MENU")
    print("*"*35)
    print("1. Đặt lại khung thời gian")
    print("2. Show biểu đồ MA")
    print("3. Thoát")
    print("*"*35)
    print("Nhập vào số của menu:")
    chon = int(input())
    if chon == 1:
        # Đặt lại nDay
        print('Đặt lại khung thời gian nDay=')
        nDay = int(input())
    else:
        if chon == 2:
            ShowPrice(nDay)
print("Done!")