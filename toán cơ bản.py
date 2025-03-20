# tính tổng hai số 
# a = int(input("nhập số thứ nhất : "))
# b = int(input("nhập số thứ hai : "))
# print ("tổng hai số là : ",a+b)

# 2. kiểm tra số chẵn lẻ 
# a = int(input("nhập số nguyên a : "))
# if a%2 ==0:
#  print ("đây là số chẵn ")
# else:
#  print ("đây là số lẻ")

# 3. tính giai thừa 
a = int(input("nhập số bất kỳ : "))
if a < 0:
    print("không có giai thừa số âm ")
else:
    giai_thua = 1
    for i in range(1, a + 1):
        giai_thua *= i
    print("giai thừa của số trên là:", giai_thua)