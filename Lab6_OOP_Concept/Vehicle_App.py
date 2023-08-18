from Vehicle import Vehicle

def display_option():
    print("Welcome to Vehicle Data Store System (VDSS)")
    print("1.Add Vehicle")
    print("2.Display all Vehicle")
    print("3.Exit")
    select = int(input("select(1-3)? : "))
    if select == 1:
        input_vehicle_info()
    elif select == 2:
        display_vehicle()
    elif select == 3:
        print("Good Bye.")
        exit(0)
    else:
        print("Please, select number 1-3.")

def input_vehicle_info():
    brand = input("Enter vehicle brand: ")
    model = input("Enter vehicle model: ")
    color = input("Enter vehicle color: ")
    maxspeed = input("Enter vehicle maxspeed: ")
    price = float(input("Enter vehicle price: "))

    my_vehicle.append(Vehicle(brand, model, color, maxspeed, price))
    print("\n--------------------------------------")
    print("Already add vehicle to store.")
    print("--------------------------------------\n")

def display_vehicle():
    if len(my_vehicle) ==0:
        print("You had no vehicle data.")
    else:
        print(f'You had {len(my_vehicle)} following')
        for x in my_vehicle:
            x.vehicle_info()
        print("\n")


my_vehicle = []
s = 0
while s == 0:
    display_option()