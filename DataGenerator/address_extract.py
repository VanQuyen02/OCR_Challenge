import json

# Mở tệp label.json
with open("labels.json", "r",encoding='utf-8') as f:
    data = json.load(f)

# Mở tệp address.txt để ghi
with open("address.txt", "w",encoding='utf-8') as f:
    # Duyệt qua tất cả các địa chỉ
    for image_id, address in data.items():
        # Xóa dấu phẩy ở cuối địa chỉ
        address = address.rstrip(",")
        words = address.split(",")
        string =""
        for word in words:
            string = string+ " " +word.strip()
        string = string.strip()
        # Ghi địa chỉ vào tệp
        f.write(string + "\n")