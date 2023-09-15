from EvCar import Thaievcar

def display_option():
    print("สวัสดี ยินดีต้อนรับสู่โปรแกรม EvCarApp")
    print("1.เพิ่มข้อมูลรถไฟฟ้า")
    print("2.ลบข้อมูลรถไฟฟ้า")
    print("3.ปรับปรุงหรือแก้ไขข้อมูลราคารถไฟฟ้า")
    print("4.แสดงข้อมูลรถไฟฟ้าทั้งหมด")
    print("5.ออกจากโปรแกรม")
    select = int(input("select(1-5)? : "))
    if select == 1:
        add_ev_car()
    elif select == 2:
        delete_ev_car()
    elif select == 3:
        edit_ev_car_price()
    elif select == 4:
        display_ev_car()
    elif select == 5:
        print("ออกจากโปรแกรม.")
        exit(0)
    else:
        print("Please, select number 1-5.")

def add_ev_car():
    model = input("กรุณากรอกรุ่นรถ! : ")
    brand = input("กรุณากรอกยี่ห้อรถ!: ")
    accelerationrat = input("กรุณากรอกอัตราเร่งรถ!: ")
    hp = input("กรุณากรอกแรงม้ารถ!: ")
    range = input("กรุณากรอกระยะทางที่รถวิ่งได้/ชาร์จ!: ")
    price = float(input("กรุณากรอกราคารถ! : "))

    Thaievcar.ev_car_detail.append(Thaievcar(model, brand, accelerationrat, hp, range, price, ))
    print("\n--------------------------------------")
    print("ทำการเพิ่มข้อมูลรถเรียบร้อยแล้ว.")
    print("--------------------------------------\n")

def display_ev_car():
    if len(Thaievcar.ev_car_detail) ==0:
        print("ไม่มีข้อมูลรถให้แสดง! .")
    else:
        print(f'คุณมี {len(Thaievcar.ev_car_detail)} following')
        n = 1001 # count
        for x in Thaievcar.ev_car_detail:
            print(f'[{n}]:' ,end=" ")
            x.add_ev_car()
            n = n+1001
        print("\n")

def delete_ev_car():
    # display all data in list
    display_ev_car()
    if len(Thaievcar.ev_car_detail) != 0:
        s = int(input("กรอกรหัสรถไฟฟ้าเพื่อทำการลบ! : "))

        Thaievcar.delete_ev_car(Thaievcar, s-1001)
        print("\n--------------------------------------")
        print("ลบข้อมูลรถไฟฟ้าเรียบร้อย! .")
        print("--------------------------------------\n")

def edit_ev_car_price():
    display_ev_car()
    if len(Thaievcar.ev_car_detail) != 0:
        s = int(input("กรอกรหัสรถไฟฟ้าที่ต้องการแก้ไขราคา! : "))
        #display previos price
        print(f'\nprevios price: {Thaievcar.ev_car_detail[s-1001].price}')
        new_price = float(input("new price:" ))
        Thaievcar.edit_ev_car_price(Thaievcar,s-1001,new_price)
        print("\n--------------------------------------")
        print("ทำการแก้ไขข้อมูลเรียบร้อยแล้ว.")
        print("--------------------------------------\n")

s = 0
while s == 0:
    display_option()