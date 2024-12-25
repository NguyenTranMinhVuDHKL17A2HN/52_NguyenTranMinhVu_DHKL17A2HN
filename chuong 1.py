#Câu 1
class HinhChuNhat:
    def __init__(self, chieu_dai=0, chieu_rong=0):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    def nhap_kich_thuoc(self):
        self.chieu_dai = float(input("Nhập chiều dài: "))
        self.chieu_rong = float(input("Nhập chiều rộng: "))

    def tinh_dien_tich(self):
        return self.chieu_dai * self.chieu_rong

    def tinh_chu_vi(self):
        return 2 * (self.chieu_dai + self.chieu_rong)

    def in_thong_tin(self):
        print(f"Hình chữ nhật có chiều dài {self.chieu_dai} và chiều rộng {self.chieu_rong}.")
        print(f"Diện tích: {self.tinh_dien_tich()}")
        print(f"Chu vi: {self.tinh_chu_vi()}")

hcn = HinhChuNhat()
hcn.nhap_kich_thuoc()
hcn.in_thong_tin()

#Câu 2
class ThiSinh:
    def __init__(self, ten="", diem_toan=0, diem_ly=0, diem_hoa=0):
        self.ten = ten
        self.diem_toan = diem_toan
        self.diem_ly = diem_ly
        self.diem_hoa = diem_hoa

    def nhap_thong_tin(self):
        self.ten = input("Nhập tên thí sinh: ")
        self.diem_toan = float(input("Nhập điểm Toán: "))
        self.diem_ly = float(input("Nhập điểm Lý: "))
        self.diem_hoa = float(input("Nhập điểm Hóa: "))

    def in_thong_tin(self):
        print(f"Tên: {self.ten}, Toán: {self.diem_toan}, Lý: {self.diem_ly}, Hóa: {self.diem_hoa}")

    def tinh_tong_diem(self):
        return self.diem_toan + self.diem_ly + self.diem_hoa

so_luong_thi_sinh = int(input("Nhập số lượng thí sinh: "))
danh_sach_thi_sinh = []

for _ in range(so_luong_thi_sinh):
    ts = ThiSinh()
    ts.nhap_thong_tin()
    danh_sach_thi_sinh.append(ts)

diem_chuan = float(input("Nhập điểm chuẩn: "))
thi_sinh_dau = [ts for ts in danh_sach_thi_sinh if ts.tinh_tong_diem() >= diem_chuan]

thi_sinh_dau.sort(key=lambda ts: ts.tinh_tong_diem(), reverse=True)

print("Danh sách thí sinh đậu:")
for ts in thi_sinh_dau:
    ts.in_thong_tin()

#Câu 3
class PhanSo:
    def __init__(self, tu_so=0, mau_so=1):
        self.tu_so = tu_so
        self.mau_so = mau_so
        self.kiem_tra_hop_le()

    def kiem_tra_hop_le(self):
        if self.mau_so == 0:
            raise ValueError("Mẫu số không được bằng 0")

    def nhap_phan_so(self):
        self.tu_so = int(input("Nhập tử số: "))
        self.mau_so = int(input("Nhập mẫu số: "))
        self.kiem_tra_hop_le()

    def in_phan_so(self):
        print(f"{self.tu_so}/{self.mau_so}")

ps = PhanSo()
ps.nhap_phan_so()
ps.in_phan_so()

#Câu 4
class Stack:
    def __init__(self, kich_thuoc=10):
        self.kich_thuoc = kich_thuoc
        self.stack = [None] * kich_thuoc
        self.top = -1

    def push(self, gia_tri):
        if self.full():
            print("Ngăn xếp đã đầy")
        else:
            self.top += 1
            self.stack[self.top] = gia_tri

    def pop(self):
        if self.empty():
            print("Ngăn xếp rỗng")
        else:
            gia_tri = self.stack[self.top]
            self.top -= 1
            return gia_tri

    def empty(self):
        return self.top == -1

    def full(self):
        return self.top == self.kich_thuoc - 1

stack = Stack()
stack.push(1)
stack.push(2)
print(stack.pop())  # Output: 2
print(stack.pop())  # Output: 1

#Câu 5
class Stack:
    def __init__(self, kich_thuoc=10):
        self.kich_thuoc = kich_thuoc
        self.stack = [None] * kich_thuoc
        self.top = -1
        self.count = 0  

    def push(self, gia_tri):
        if self.full():
            print("Ngăn xếp đã đầy")
        else:
            self.top += 1
            self.stack[self.top] = gia_tri
            self.count += 1  

    def pop(self):
        if self.empty():
            print("Ngăn xếp rỗng")
        else:
            gia_tri = self.stack[self.top]
            self.top -= 1
            self.count -= 1  
            return gia_tri

    def empty(self):
        return self.top == -1

    def full(self):
        return self.top == self.kich_thuoc - 1

    def print_stack(self):
        if self.empty():
            print("Ngăn xếp rỗng")
        else:
            print("Ngăn xếp: ", end="")
            for i in range(self.top + 1):
                print(self.stack[i], end=" ")
            print()
        print(f"Số phần tử trong ngăn xếp: {self.count}")

stack = Stack()
stack.push(1)
stack.push(2)
stack.print_stack()  
print(stack.pop())  
stack.print_stack()  

#Câu 6
class Stack:
    def __init__(self, kich_thuoc=10):
        self.kich_thuoc = kich_thuoc
        self.stack = [None] * kich_thuoc
        self.top = -1

    def push(self, gia_tri):
        if self.full():
            print("Ngăn xếp đã đầy")
        else:
            self.top += 1
            self.stack[self.top] = gia_tri

    def pop(self):
        if self.empty():
            print("Ngăn xếp rỗng")
        else:
            gia_tri = self.stack[self.top]
            self.top -= 1
            return gia_tri

    def empty(self):
        return self.top == -1

    def full(self):
        return self.top == self.kich_thuoc - 1

    def print_stack(self):
        if self.empty():
            print("Ngăn xếp rỗng")
        else:
            print("Ngăn xếp: ", end="")
            for i in range(self.top + 1):
                print(self.stack[i], end=" ")
            print()

stack = Stack()
stack.push(1)
stack.push(2)
stack.print_stack()  

#Câu 7
class Date:
    def __init__(self, ngay=1, thang=1, nam=2000):
        self.ngay = ngay
        self.thang = thang
        self.nam = nam

    def display(self):
        print(f"Ngày: {self.ngay}/{self.thang}/{self.nam}")

    def next_day(self):
        self.ngay += 1
        if self.ngay > 30:
            self.ngay = 1
            self.thang += 1
            if self.thang > 12:
                self.thang = 1
                self.nam += 1

date = Date(30, 12, 2022)
date.display()
date.next_day()
date.display()

#Câu 8
class Date:
    def __init__(self, ngay=1, thang=1, nam=2000):
        self.ngay = ngay
        self.thang = thang
        self.nam = nam

    def display(self):
        print(f"Ngày: {self.ngay}/{self.thang}/{self.nam}")

class Employee:
    def __init__(self, ho_ten="", ngay_sinh=None, ngay_vao_cong_ty=None):
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh if ngay_sinh else Date()
        self.ngay_vao_cong_ty = ngay_vao_cong_ty if ngay_vao_cong_ty else Date()

    def nhap_thong_tin(self):
        self.ho_ten = input("Nhập họ tên: ")
        ngay = int(input("Nhập ngày sinh: "))
        thang = int(input("Nhập tháng sinh: "))
        nam = int(input("Nhập năm sinh: "))
        self.ngay_sinh = Date(ngay, thang, nam)
        ngay = int(input("Nhập ngày vào công ty: "))
        thang = int(input("Nhập tháng vào công ty: "))
        nam = int(input("Nhập năm vào công ty: "))
        self.ngay_vao_cong_ty = Date(ngay, thang, nam)

    def in_thong_tin(self):
        print(f"Họ tên: {self.ho_ten}")
        print("Ngày sinh: ", end="")
        self.ngay_sinh.display()
        print("Ngày vào công ty: ", end="")
        self.ngay_vao_cong_ty.display()

nv = Employee()
nv.nhap_thong_tin()
nv.in_thong_tin()

#Câu 9
class DaGiac:
    def __init__(self, canh=None):
        self.canh = canh if canh else []

    def tinh_chu_vi(self):
        return sum(self.canh)

class HinhBinhHanh(DaGiac):
    def __init__(self, day=0, cao=0):
        super().__init__([day, day, cao, cao])
        self.day = day
        self.cao = cao

    def tinh_dien_tich(self):
        return self.day * self.cao

class HinhChuNhat(HinhBinhHanh):
    def __init__(self, chieu_dai=0, chieu_rong=0):
        super().__init__(chieu_dai, chieu_rong)
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

class HinhVuong(HinhChuNhat):
    def __init__(self, canh=0):
        super().__init__(canh, canh)

hinh_vuong = HinhVuong(4)
print("Chu vi hình vuông:", hinh_vuong.tinh_chu_vi())
print("Diện tích hình vuông:", hinh_vuong.tinh_dien_tich())

#Câu 10
class Diem:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def display(self):
        print(f"Điểm ({self.x}, {self.y})")

class Clip(Diem):
    def __init__(self, x=0, y=0, ban_kinh=0):
        super().__init__(x, y)
        self.ban_kinh = ban_kinh

    def tinh_dien_tich(self):
        return 3.14 * self.ban_kinh * self.ban_kinh

diem = Diem(1, 2)
diem.display()
clip = Clip(1, 2, 3)
print("Diện tích clip:", clip.tinh_dien_tich())

#Câu 11
class TamGiac:
    def __init__(self, canh_a=0, canh_b=0, canh_c=0):
        self.canh_a = canh_a
        self.canh_b = canh_b
        self.canh_c = canh_c

    def tinh_chu_vi(self):
        return self.canh_a + self.canh_b + self.canh_c

class TamGiacCan(TamGiac):
    def __init__(self, canh_day=0, canh_ben=0):
        super().__init__(canh_day, canh_b)