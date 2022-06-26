name = input("Enter your name: ")
work_per_week = int(input("Enter number of hours worked in a week: "))
pay_per_hour = float(input("enter hourly pay rate: "))
federal_tax_withholding_rate = float(input("Enter federal tax withholding rate: "))
state_tax_withholding_rate = float(input("Enter state tax withholding rate: "))

pay_rate = pay_per_hour * work_per_week
federal_rate_deduction = (federal_tax_withholding_rate/ 100) * pay_rate
state_rate_deduction = (state_tax_withholding_rate / 100) * pay_rate
total_deduction = federal_rate_deduction + state_rate_deduction
net_pay = pay_rate - total_deduction

print(f"Employee Name: {name}")
print(f"Hours Worked: {work_per_week:.1f}")
print(f"Pay Rate:  ₦{pay_per_hour:.2f}")
print(f"Gross Pay: ₦{pay_rate:.1f}")
print(f"""
Deductions:
    Federal Withholding ({federal_tax_withholding_rate:.1f}%): ₦{federal_rate_deduction:.1f}
    State Withholding ({state_tax_withholding_rate:.1f}%): ₦{state_rate_deduction:.2f}
    Total Deduction: ₦{total_deduction:.2f}
Net Pay: ₦{net_pay:.2f}
        """)