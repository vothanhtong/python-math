import math

# Hàm tính diện tích hình vuông
def dien_tich_hinh_vuong(canh):
    return canh * canh

# Hàm tính diện tích hình chữ nhật
def dien_tich_hinh_chu_nhat(dai, rong):
    return dai * rong

# Hàm tính diện tích hình tròn
def dien_tich_hinh_tron(ban_kinh):
    return math.pi * ban_kinh * ban_kinh

# Hàm tính diện tích hình tam giác (công thức Heron)
def dien_tich_hinh_tam_giac(a, b, c):
    # Tính nửa chu vi
    s = (a + b + c) / 2
    # Công thức Heron
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

# Chương trình chính
print("Chọn hình để tính diện tích:")
print("1. Hình vuông")
print("2. Hình chữ nhật")
print("3. Hình tròn")
print("4. Hình tam giác")

lua_chon = int(input("Nhập lựa chọn của bạn (1-4): "))

if lua_chon == 1:
    canh = float(input("Nhập độ dài cạnh hình vuông: "))
    print(f"Diện tích hình vuông là: {dien_tich_hinh_vuong(canh)}")
    
elif lua_chon == 2:
    dai = float(input("Nhập chiều dài hình chữ nhật: "))
    rong = float(input("Nhập chiều rộng hình chữ nhật: "))
    print(f"Diện tích hình chữ nhật là: {dien_tich_hinh_chu_nhat(dai, rong)}")
    
elif lua_chon == 3:
    ban_kinh = float(input("Nhập bán kính hình tròn: "))
    print(f"Diện tích hình tròn là: {dien_tich_hinh_tron(ban_kinh)}")
    
elif lua_chon == 4:
    a = float(input("Nhập độ dài cạnh thứ nhất: "))
    b = float(input("Nhập độ dài cạnh thứ hai: "))
    c = float(input("Nhập độ dài cạnh thứ ba: "))
    # Kiểm tra xem tam giác có tồn tại không
    if a + b > c and b + c > a and a + c > b:
        print(f"Diện tích hình tam giác là: {dien_tich_hinh_tam_giac(a, b, c)}")
    else:
        print("Ba cạnh này không tạo thành một tam giác hợp lệ!")
        
else:
    print("Lựa chọn không hợp lệ!")