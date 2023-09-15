from Evcar import Thaievcar

def display_option():
    print("สวัสดี ยินดีต้อนรับสู่โปรแกรม EvCarApp")
    print("1.เพิ่มข้อมูลรถไฟฟ้า")
    print("2.แสดงข้อมูลรถไฟฟ้า")
    print("3.ออก")

    select = int(input("select(1-3)? : "))
    if select == 1:
        add_ev_car()
    elif select == 2:
        display_ev_car()
    elif select == 3:
        print("ออกจากโปรแกรม.")
        exit(0)
    else:
        print("Please, select number 1-3.")

def add_ev_car():
    model = input("กรุณากรอกรุ่นรถ! : ")
    brand = input("กรุณากรอกยี่ห้อรถ!: ")
    accelerationrat = input("กรุณากรอกอัตราเร่งรถ!: ")
    hp = input("กรุณากรอกแรงม้ารถ!: ")
    range = input("กรุณากรอกระยะทางที่รถวิ่งได้/ชาร์จ!: ")
    price = float(input("กรุณากรอกราคารถ! : "))

    Thaievcar.Thaievcar_detail.append(Thaievcar(model, brand, accelerationrat, hp, range, price, ))
    print("\n--------------------------------------")
    print("ทำการเพิ่มข้อมูลรถเรียบร้อยแล้ว.")
    print("--------------------------------------\n")

def display_ev_car():
    if len(Thaievcar.Thaievcar_detail) ==0:
        print("ไม่มีข้อมูลรถให้แสดง! .")
    else:
        print(f'คุณมี {len(Thaievcar.Thaievcar_detail)} following')
        n = 1001 # count
        for x in Thaievcar.Thaievcar_detail:
            print(f'[{n}]:' ,end=" ")
            x.Thaievcar_info()
            n = n+1001
        print("\n")

s = 0
while s == 0:
    display_option()