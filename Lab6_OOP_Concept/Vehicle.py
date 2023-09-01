"""
OOP Exercise Chapter 6

1. จงเขียนโปรแกรมภาษาไพธอนเพื่อสร้างคลาสพาหนะชื่อ Vehicle ที่ประกอบไปด้วยคุณลักษณะ (attributes) คือ
ยี่ห้อรถ (brand)
รุ่นรถ (model)
สีรถ (color)
ความรเร็วสูงสุด (max speed)
ราคา (price)

2.จากข้อที่ 1 เขียนโปรแกรมเพื่อสร้างวัตถุ (object) จากคลาส Vehicle โดยรับข้อมูลจากผู้ใช้ตามคุณลักษณะ (attributes)ของคลาส
จากนั้นแสดงข้อมูลทางหน้าจอภาพ

15 นาที
"""

class Vehicle:
    my_vehicle = []

    def __init__(self,brand,model,color,maxspeed,price):
        self.brand = brand
        self.model = model
        self.color = color
        self.maxspeed = maxspeed
        self.price = price
        #self.my_vihecle.append(self)


    def vehicle_info(self):
        print(f'Brand:{self.brand} '
              f'Model:{self.model} '
              f'Color:{self.color} '
              f'Maxspeed:{self.maxspeed} '
              f'Price:{self.price}')

    def delete_vehicle(self,index):
        self.my_vehicle.pop(index)

    def edit_vehicle_price(self,index,new_price):
        self.my_vehicle[index].price = new_price

    def edit_vehicle_color(self,index,new_color):
        self.my_vehicle[index].color = new_color

# std = []
# n = int(input('How many Vehicle? : '))
# for i in range(n):
#     s = Vehicle()
#     print(f"Please, Enter Vehicle info {i + 1}:")
#     s.Brand = input("Enter Brand: ")
#     s.Model = input("Enter Model: ")
#     s.Color = input("Enter Color: ")
#     s.Maxspeed = input("Enter Maxspeed: ")
#     s.Price = input("Enter Price: ")
#     std.append(s)
#
# # display all student in list
# for i in std:
#     i.vehicle_info()