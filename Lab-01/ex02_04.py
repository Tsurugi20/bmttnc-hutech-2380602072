# Tạo một danh sách rỗng để lưu kết quả
j = []

# Duyệt qua tất cả các số trong đoạn từ 2000 đến 3200
for i in range(2000, 3201):
    # Kiểm tra xem số đó có chia hết cho 7 và không chia hết cho 5 không
    if (i % 7 == 0) and (i % 5 != 0):
        j.append(str(i))

print(",".join(j))