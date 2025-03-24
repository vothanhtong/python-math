import math 
def chu_vi_hinh_vuông(cạnh):
    # tính chu vi hình vuông 
    return cạnh * 4 
def chu_vi_hình_tam_giác(a,b,c):
    # tính chu vi tam giác
    return a+b+c 
def chu_vi_hinh_chu_nhat(a,b):
    # tính chu vi hình chữ nhật 
    return (a+b)
def chu_vi_hinh_tron(r):
    # tính chu vi hình tròn 
    return 2*math.pi*r
def chu_vi_hinh_binh_hanh(a,b):
    # tính chu vi hình bình hành 
    return 2*(a+b)
def chu_vi_hinh_thoi(a):
    # tính chu vi hình thoi
    return 4*a
def chu_vi_hinh_ngu_giac(a):
    # tính hình ngũ giác 
    return 5*a 
if __name__ == "__main__":
    print("Chương trình tính chu vi các hình học")
    print("1. Hình vuông")
    print("2. Hình tam giác")   
    print("3. Hình chữ nhật")
    print("4. Hình tròn")
    print("5. Hình bình hành")
    print("6. Hình thoi")
    print("7. Hình ngũ giác")
    chon = int(input("Chọn hình muốn tính chu vi: "))
    