# Smart Expense Splitter

Ung dung dong lenh (CLI) bang Python giup quan ly chi tieu nhom, phong tro va tu dong toi uu hoa so luot chuyen tien bu tru giua cac thanh vien.

---

## 1. Tinh nang chinh

- Quan ly danh sach thanh vien trong nhom.
- Nhap chi phi linh hoat: chia deu cho ca phong hoac chia cho cac thanh vien cu the.
- Tu dong tinh toan so du (Net Balance): ai con no va ai can nhan lai tien.
- Toi uu hoa giao dich: Su dung thuat toan tham lam (Greedy) de giam thieu so lan chuyen khoan ve muc thap nhat (toi da N - 1 giao dich).

---

## 2. Giai thuat va do phuc tap

### Nguyen ly hoat dong
1. Tinh so du rong cua tung nguoi:
   So du = Tong tien da chi - Tong tien phai chiu
   - So du > 0: Nguoi can nhan lai tien (chu no).
   - So du < 0: Nguoi can tra them tien (con no).

2. Xu ly no bang thuat toan tham lam:
   - Sap xep danh sach nguoi no va nguoi nhan theo thu tu giam dan.
   - Ghep cap nguoi no nhieu nhat tra cho nguoi can nhan nhieu nhat.
   - Cap nhat lai so tien va lap lai den khi tat ca ve 0.

### Do phuc tap thuat toan
- Thoi gian (Time Complexity): O(N log N) voi N la so thanh vien (chu yeu do buoc sap xep).
- Bo nho (Space Complexity): O(N) de luu bang bam so du va danh sach giao dich.

---

