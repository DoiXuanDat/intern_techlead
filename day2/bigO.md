# 1. Big O notation

Big O là một cách để diển giả một giới hạn trên của độ phức tạp về thời gian hoặc không gian của một thuật toán. Big O không đo lương thời gian thực tế mà đo tốc độ tăng trưởng của thuật toán khi input lớn hơn. Khi nói một thuật toán có time complexity là O(n), nó chỉ quan tâm đến tốc độ tăng trưởng, không phải thời gian chạy cụ thể.


# 2. Các Big O Notation hay gặp 

1. O(1)

Đây là thời gian chạy mà nó là một hằng số, thời gian nó chạy sẽ không phụ thuộc vào kích thước đầu vào 

    def Even_or_Odd(n):
        return 'even' if n%2 else 'odd'

2. O(log(n))

Đây là độ phức tạp Logarit cơ số 2, nghĩa là thời gian chạy sẽ tăng chậm theo kích thước đầu vào của input

    def binary_seưarch(arr, target):
        left = 0
        right = len(arr)-1

        while left < right:
            mid = (left + right) // 2  
            if arr[mid] == target:
                return mid 
            elif arr[mid] < target:
                left = mid + 1
            else: right = mid - 1
        
        return -1

3. O($n^2$)
Đây là độ phức tạp tuyến tính, nghĩa là thời gian chạy sẽ tăng tương ứng cùng với kích thước của input

    def find_number(arr, target):
        for i in range(len(arr)):
            if arr[i] == target:
                return i
        
4. 


    

