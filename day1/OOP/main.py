from employee import Manager, Director, Accountant, Dev, Mentor
from base import Team

def main():
    print("1. KHỞI TẠO & KẾ THỪA")
    dev = Dev("Van", "A", 1000, "IT")
    manager = Manager("Van", "B", 2000, "IT")
    accountant = Accountant("Van", "C", 1500)
    
    # Director kế thừa Manager (Multilevel)
    director = Director("Van", "D", 5000, "Board", team=[manager])

    print(f"Dev: {dev.full_name()}")
    print(f"Director Email: {director._email}") 
    print(f"Salary: {dev.get_real_salary()}")

    print("2. ĐA HÌNH (POLYMORPHISM)")
    employee = [dev, manager, accountant, director]
    
    # Duck Typing: Thêm Mentor vào danh sách dù không phải Employee
    mentor = Mentor("Mr.E")
    all_staff = employee + [mentor]

    for staff in all_staff:
        print(f"Action: {staff.work()}")

    print("3. POLYMORPHISM (ARGS/KWARGS)")
    print(manager.work()) # Không tham số
    print(manager.work("Review PR", "Meeting", urgent=True, location="Room 3")) # Có tham số

    print("4. KẾ THỪA ĐA (MULTIPLE INHERITANCE)")
    print(accountant.pay_summary()) 

    print("5. TOÁN TỬ (OPERATOR OVERLOADING)")
    # Cộng 2 nhân viên thành 1 Team
    team_alpha = dev + manager 
    print(f"Team A created: {team_alpha}")
    
    # Cộng Team với nhân viên khác
    team_beta = team_alpha + accountant
    print(f"Team B created: {team_beta}")
    
    print(f"Total Salary of Team B: ${team_beta.total_pay()}")

if __name__ == "__main__":
    main()