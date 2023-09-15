class Thaievcar:
    ev_car_detail = []

    def __init__(self, model, brand, accelerationrate, hp, range, price):
        self.model = model
        self.brand = brand
        self.accelerationrate = accelerationrate
        self.hp = hp
        self.range = range
        self.price = price

    def add_ev_car(self):
        print(f'model:{self.model} '
              f'brand:{self.brand} '
              f'accelerationrate:{self.accelerationrate} '
              f'hp:{self.hp} '
              f'range:{self.range} '
              f'price:{self.price} ')

    def delete_ev_car(self,index):
        self.ev_car_detail.pop(index)

    def edit_ev_car_price(self,index,new_price):
        self.ev_car_detail[index].price = new_price



