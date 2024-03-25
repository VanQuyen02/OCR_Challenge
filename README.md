# Exploratory Data Analysis

---

**Training data set**: bao gồm **2700** ảnh chụp chữ viết tay đi kèm với nội dung nhãn là địa chỉ tại Việt Nam.

**Public test set**: bao gồm **540** ảnh, trong đó có 1 file trắng không nó nội dung.

Ngoài ra ở giai đoạn 2 của cuộc thi, BTC có public thêm:

- 100 mẫu dữ liệu level 2: Phần text trong ảnh là một địa chỉ nhưng các word bị xáo trộn một cách ngẫu nhiên.
- 100 mẫu dữ liệu level 3: Phần text trong ảnh được chọn ngẫu nhiên một hoặc nhiều cấp địa chỉ và viết tắt toàn bộ cấp địa chỉ này bằng cách ghép các chữ cái đầu tiên của các từ.

Khảo sát một chút về độ dài chuỗi cũng như tỉ lệ chiều rộng/chiều cao của ảnh, ta có 2 biểu đồ sau:

![Biểu đồ phân bố giá trị W/H](https://prod-files-secure.s3.us-west-2.amazonaws.com/25859e4e-08df-4782-9415-d2dde14e7644/4ee32161-a68b-44ce-9b9f-502df6d2467a/image_shape.jpg)

Biểu đồ phân bố giá trị W/H

![Biểu đồ phân bố độ dài nhãn](https://prod-files-secure.s3.us-west-2.amazonaws.com/25859e4e-08df-4782-9415-d2dde14e7644/fc6791dc-cb4f-4d00-8328-da2e207f6fa8/label_len.jpg)

Biểu đồ phân bố độ dài nhãn

    Nhìn vào biểu đồ có thể thấy, giá trị W/H phần lớn nằm dưới mức 18 và độ dài của địa chỉ trong ảnh đa số dưới 60 ký tự. Các giá trị này tương đối quan trọng, nó giúp lựa chọn được **input size** mà **max sequence length** một cách phù hợp. 

Trong trường hợp này, mình lựa chọn **inptut_size** = 48x720 và **max_sequence_length** = 60.
