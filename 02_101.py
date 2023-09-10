def yearly_payment_tax(monthly_payment):
    if yearly_payment <= 1200:
        tax_rate = 0.06
    elif yearly_payment <= 4600:
        tax_rate = 0.15
    elif yearly_payment <= 8800:
        tax_rate = 0.24
    elif yearly_payment <= 15000:
        tax_rate = 0.35
    elif yearly_payment <= 30000:
        tax_rate = 0.38
    elif yearly_payment <= 50000:
        tax_rate = 0.40
    else:
        tax_rate = 0.42

    tax = yearly_payment * tax_rate
    return tax

# 연봉 입력
monthly_payment = float(input("월급을 입력하세요 (만원 단위): "))
yearlypayment = "월급"*12
tax = yearly_payment_tax(yearly_payment)

print('세전연봉 : ', (monthly_payment*12))
print('세후연봉 : ', (monthly_payment*12) - (tax))



# # 월급 입력
# monthly_payment = 300
# yearly_payment(monthly_payment)

# # 출력
# 세전 연봉: 3600만원
# 세후 연봉: 3060만원