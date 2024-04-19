# import numpy as np
# import matplotlib.pyplot as plt

# # # Vẽ biểu đồ y = x^2
# # # Chia đoạn từ -20 đến 20 thành 1000 đoạn

# x = np.linspace(-20, 20, 1000)
# # # Tính y
# y = x * x

# # # Vẽ biểu đồ tương quan giữa x và y
# plt.plot(x, y)
# # # Hiển thị
# plt.show()

# # # Vẽ biểu đồ hinhg sin
# import numpy as np
# import matplotlib.pyplot as plt

# # Chia đoạn từ 0 đến 3pi thành các đoạn con 0.1
# x = np.arange(0, 3 * np.pi, 0.1)  # arange: Trải ra
# # Tính sin tương ứng với từng phần của x
# y = np.sin(x)

# # Vẽ
# plt.plot(x, y)
# # Hiển
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt

# x = np.arange(0, 3 * np.pi, 0.1)
# y_sin = np.sin(x)
# y_cos = np.cos(x)

# plt.plot(x, y_sin)
# plt.plot(x, y_cos)
# plt.xlabel('Trục X')
# plt.ylabel('Trục Y')
# plt.title('Hàm SIN và COS trong khoảng 0 đến 3pi')
# plt.legend(['SIN(x)', 'COS(x)'])
# plt.show()

# Ví dụ
# import numpy as np
# import matplotlib.pyplot as plt

# # Chia đoạn 0-5 thành các bước 0.2

# t = np.arange(0., 5., 0.2)

# # Vẽ 3 đường:
# # - màu đỏ nét đút: y = x
# # - màu xanh dương, đánh dẫu ô vuông: y = x^2
# # - màu xanh lá, đánh dấu tam giác: y = x^3
# plt.plot(t, t, 'r--', t, t ** 2, 'bs', t, t**3, 'g^')
# plt.show()

# import matplotlib.pyplot as plt

# D = { 'CTTT': 60,
#     'Kế toán': 310,
#      'Kinh tế': 360,
#      'CNTT': 580,
#      'Cơ khí': 340,
#      'Thủy văn': 290}
# # Chiều dọc
# # plt.bar(range(len(D)), D.values(), align='center')
# # plt.xticks(range(len(D)), D.keys())
# # Chiều ngang
# plt.barh(range(len(D)), list(D.values()))
# plt.yticks(range(len(D)), D.keys())
# plt.title('Các ngành tuyển sinh của Đại học Thủy Lợi')
# plt.show()

# Ghép 2 biểu đồ
# import matplotlib.pyplot as plt

# plt.bar([1,3,5,7,9],[5,2,7,8,2], label = "One")
# plt.bar([2,4,6,8,10],[8,6,2,5,6], label ="Two", color ='g')
# plt.legend()
# plt.xlabel('bar number')
# plt.ylabel('bar height')

# plt.title('Ghép 2 biểu đồ')

# plt.show()

# Biểu đồ bánh

import matplotlib.pyplot as plt

# D = { 'CTTT': 60,
#     'Kế toán': 310,
#      'Kinh tế': 360,
#      'CNTT': 580,
#      'Cơ khí': 340,
#      'Thủy văn': 290}

# plt.pie(D.values(), labels=D.keys(), autopct='%1.1f%%')
# plt.axis('equal')

# plt.show()

# dữ liệu
labels = 'Python', 'C++', 'Ruby', 'Java'
sizes = [215, 130, 245, 210]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)
# vẽ
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.legend(labels)
plt.savefig('1.png')
plt.savefig('1.pdf')
# plt.show()

