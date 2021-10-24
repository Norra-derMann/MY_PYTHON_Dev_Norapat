price = int(input("Please enter price of goods : "))
pay = int(input("Please enter money to pay : "))
exchange = pay - price  #คำนวนเงินทอน

#array เก็บชนิดของเงินทอน แบ่งเป็น 500,100,50,20,10,5,2,1
money_type = [500, 100, 50, 20, 10, 5, 2, 1]
 
#ลูบ หาเงินทอนโดยการหารเอาเศษ โดยไปลูปใน array ว่า
#ถ้าต้องทอนเงิน 768 บาท เราจะเริ่มจาก
#นำ 500 ไปหารเอาเศษ 768 จะได้ 268 ซึ่งหารได้ 1 ที 
#หลังจากนั้นนำ เลข 268 ไปหารเอาเศษ โดย 100 ซึ่งค่าที่จะได้คือ 68 และหารได้สองที เหลือ 68 แล้วไปวนค่าเรื่อยๆจนถึง 1 บาท
for t in money_type:
    #ถ้ามีเงินทอน ให้ปริ้นใน if
    if exchange >= t:
        print("{} Baht : {}".format(t, int(exchange / t)))
        exchange = exchange % t
    #ถ้าไม่มีเงินทอนให้ปริ้น เลข 0
    else :
        print("{} Baht : 0". format(t))
