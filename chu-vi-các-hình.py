import math

def chu_vi_hinh_vuong(canh):
    # Tính chu vi hình vuông 
    return canh * 4 
def chu_vi_hinh_tam_giac(a, b, c):
    # Tính chu vi tam giác
    return a + b + c 
def chu_vi_hinh_chu_nhat(a, b):
    # Tính chu vi hình chữ nhật 
    # Sửa lỗi: Chu vi hình chữ nhật là 2*(a+b)
    return 2 * (a + b)
def chu_vi_hinh_tron(r):
    # Tính chu vi hình tròn 
    return 2 * math.pi * r
def chu_vi_hinh_binh_hanh(a,b):
    # Tính chu vi hình bình hành 
    return 2 * (a + b)
def chu_vi_hinh_binh_hanh(a, b):
    # Tính chu vi hình bình hành 
    return 2 * (a + b)
def chu_vi_hinh_thoi(a):
    # Tính chu vi hình thoi
    return 4 * a
def chu_vi_hinh_ngu_giac(a):
    # Tính chu vi hình ngũ giác đều
    return 5 * a 
if __name__ == "__main__":
    print("Chương trình tính chu vi các hình học")
    print("1. Hình vuông")
    print("2. Hình tam giác")   
    print("3. Hình chữ nhật")
    print("4. Hình tròn")
    print("5. Hình bình hành")
    print("6. Hình thoi")
    print("7. Hình ngũ giác đều")
    
    chon = int(input("Chọn hình muốn tính chu vi (1-7): "))
    # Xử lý lựa chọn của người dùng
    if chon == 1:  # Hình vuông
        canh = float(input("Nhập độ dài cạnh: "))
        print("Chu vi hình vuông:", chu_vi_hinh_vuong(canh))
    elif chon == 2:  # Hình tam giác
        a = float(input("Nhập độ dài cạnh thứ nhất: "))
        b = float(input("Nhập độ dài cạnh thứ hai: "))
        c = float(input("Nhập độ dài cạnh thứ ba: "))
        print("Chu vi hình tam giác:", chu_vi_hinh_tam_giac(a, b, c))
    elif chon == 3:  # Hình chữ nhật
        a = float(input("Nhập chiều dài: "))
        b = float(input("Nhập chiều rộng: "))
        print("Chu vi hình chữ nhật:", chu_vi_hinh_chu_nhat(a, b))   
    elif chon == 4:  # Hình tròn
        r = float(input("Nhập bán kính: "))
        print("Chu vi hình tròn:", chu_vi_hinh_tron(r)) 
    elif chon == 5:  # Hình bình hành
        a = float(input("Nhập độ dài cạnh thứ nhất: "))
        b = float(input("Nhập độ dài cạnh thứ hai: "))
        print("Chu vi hình bình hành:", chu_vi_hinh_binh_hanh(a, b))    
    elif chon == 6:  # Hình thoi
        a = float(input("Nhập độ dài cạnh: "))
        print("Chu vi hình thoi:", chu_vi_hinh_thoi(a))     
    elif chon == 7:  # Hình ngũ giác đều
        a = float(input("Nhập độ dài cạnh: "))
        print("Chu vi hình ngũ giác đều:", chu_vi_hinh_ngu_giac(a))
    else:
        print("Lựa chọn không hợp lệ! Vui lòng chọn từ 1 đến 7.")