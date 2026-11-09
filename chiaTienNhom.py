from collections import defaultdict

class ExpenseSplitter:
    def __init__(self):
        self.members = [] 
        self.balances = defaultdict(float)
        self.total_spent = defaultdict(float)

    def add_member(self, name: str):
        name = name.strip()
        if name and name not in self.members:
            self.members.append(name)

    def add_expense(self, payer: str, amount: float, participants: list[str]) -> bool:
        if not participants or amount <= 0:
            return False

        split_amount = amount / len(participants)
        self.total_spent[payer] += amount
        self.balances[payer] += amount

        for person in participants:
            self.balances[person] -= split_amount
        return True

    def simplify_debts(self):
        debtors = []
        creditors = []

        for person in self.members:
            net = round(self.balances[person], 2)
            if net < -0.01:
                debtors.append([person, -net])
            elif net > 0.01:
                creditors.append([person, net])

        debtors.sort(key=lambda x: x[1], reverse=True)
        creditors.sort(key=lambda x: x[1], reverse=True)

        transactions = []
        i, j = 0, 0

        while i < len(debtors) and j < len(creditors):
            settle_amt = min(debtors[i][1], creditors[j][1])
            transactions.append((debtors[i][0], creditors[j][0], settle_amt))

            debtors[i][1] -= settle_amt
            creditors[j][1] -= settle_amt

            if abs(debtors[i][1]) < 0.01:
                i += 1
            if abs(creditors[j][1]) < 0.01:
                j += 1

        return transactions
    
    def reset_data(self):
        """Xoa trang so lieu chi tieu, giu nguyen danh sach thanh vien."""
        self.balances.clear()
        self.total_spent.clear()

    def display_report(self):
        if not self.members:
            print("\n[!] Chua co thanh vien nao trong he thong.")
            return

        print("\n" + "=" * 50)
        print("              BAO CAO CHI TIEU")
        print("=" * 50)
        print(f"{'Thanh vien':<15} | {'Da chi':<15} | {'So du rong':<15}")
        print("-" * 50)
        for person in self.members:
            spent = self.total_spent[person]
            net = self.balances[person]
            status = f"+{net:,.0f}" if net > 0 else f"{net:,.0f}"
            print(f"{person:<15} | {spent:>12,.0f} d | {status:>12} d")

        print("\n" + "=" * 50)
        print("         LICH CHUYEN KHOAN TOI UU NHAT")
        print("=" * 50)
        txns = self.simplify_debts()
        if not txns:
            print("Tat ca da can bang, khong co ai no ai.")
        else:
            for debtor, creditor, amt in txns:
                print(f"-> {debtor:<10} chuyen cho {creditor:<10} : {amt:>10,.0f} VND")
        print("=" * 50 + "\n")


def main():
    app = ExpenseSplitter()

    print("=== HE THONG QUAN LY CHI TIEU PHONG / NHOM ===")
    raw_members = input("Nhap danh sach ten thanh vien (cach nhau boi dau phay): ")
    for name in raw_members.split(","):
        app.add_member(name.strip())

    if not app.members:
        print("Danh sach trong. Dung chuong trinh.")
        return

    while True:
        print(f"\nDa khoi tao {len(app.members)} thanh vien: {', '.join(app.members)}")
        print("--- MENU ---")
        print("1. Them khoan chi tieu moi")
        print("2. Xem bao cao tong ket va chuyen khoan")
        print("3. Tinh dot moi (Xoa du lieu cu, giu thanh vien)")
        print("4. Thoat chuong trinh")
        choice = input("Chon thao tac (1/2/3/4): ").strip()

        if choice == "1":
            print("\n-- DANH SACH THANH VIEN --")
            for i, name in enumerate(app.members, 1):
                print(f"{i}. {name}")
          
            try:
                payer_idx = int(input("Chon NGUOI TRA TIEN (nhap so): ").strip())
                payer = app.members[payer_idx - 1]
            except (ValueError, IndexError):
                print("[!] Nhap sai so thu tu.")
                continue

            try:
                amount = float(input("So tien da tra (VND): ").strip())
                if amount <= 0: raise ValueError
            except ValueError:
                print("[!] So tien khong hop le.")
                continue

            print("Ai tham gia chung? (Nhan ENTER de chia deu TAT CA, hoac nhap cac so cach nhau dau phay, vd: 1,3): ")
            part_input = input("Lua chon: ").strip()

            if not part_input:
                participants = app.members  
            else:
                try:
                    indices = [int(x.strip()) for x in part_input.split(",")]
                    participants = [app.members[idx - 1] for idx in indices]
                except (ValueError, IndexError):
                    print("[!] Lua chon khong hop le, huy tac vu.")
                    continue

            if app.add_expense(payer, amount, participants):
                print(f"[OK] Da ghi nhan: {payer} tra {amount:,.0f} VND chia cho {len(participants)} nguoi.")

        elif choice == "2":
            app.display_report()

        elif choice == "3":
            confirm = input("Ban co chac muon xoa du lieu chi tieu de tinh lai tu dau? (y/n): ").strip().lower()
            if confirm == 'y':
                app.reset_data()
                print("[OK] Da xoa trang du lieu chi tieu, san sang tinh cho dot moi.")

        elif choice == "4":
            print("Ket thuc chuong trinh.")
            break
            
        else:
            print("[!] Lua chon khong hop le.")

if __name__ == "__main__":
    main()