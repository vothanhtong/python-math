# tính tổng hai số 
a = int(input("nhập số thứ nhất : "))
b = int(input("nhập số thứ hai : "))
print ("tổng hai số là : ",a+b)

# 2. kiểm tra số chẵn lẻ 
a = int(input("nhập số nguyên a : "))
if a%2 ==0:
 print ("đây là số chẵn ")
else:
 print ("đây là số lẻ")

# 3. tính giai thừa 
a = int(input("nhập số bất kỳ : "))
if a < 0:
    print("không có giai thừa số âm ")
else:
    giai_thua = 1
    for i in range(1, a + 1):
        giai_thua *= i
    print("giai thừa của số trên là:", giai_thua)

# 4. In ra n số đầu tiên trong dãy Fibonacci
n = int(input("Nhập số n: "))
# Kiểm tra nếu n nhỏ hơn hoặc bằng 0
if n <= 0:
    print("Vui lòng nhập một số nguyên dương.")
else:
    fibonacci = []  # Danh sách để lưu dãy Fibonacci
    a, b = 0, 1  # Hai số đầu tiên trong dãy Fibonacci
    for _ in range(n):
        fibonacci.append(a)  # Thêm số hiện tại vào danh sách
        a, b = b, a + b  # Cập nhật hai số tiếp theo
    print(f"{n} số đầu tiên trong dãy Fibonacci là:", fibonacci)
    
# 5.kiểm tra số nguyên tố 
n = int(input("Nhập một số nguyên: "))
if n < 2:
    print(f"{n} không phải là số nguyên tố.")
else:
    la_so_nguyen_to = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            la_so_nguyen_to = False
            break
    if la_so_nguyen_to:
        print(f"{n} là số nguyên tố.")
    else:
        print(f"{n} không phải là số nguyên tố.")
