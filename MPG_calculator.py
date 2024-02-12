MPG = 0
car_make = ""
car_model = ""
car_year = 0

def Main():
    Info = Save_Info()
    measurement_options = ["Metric", "Imperial"]
    is_metric = Get_Choice("What measurement do you use?", measurement_options)
    while True:
        distance = Get_Input(f"Please input the distance you have travelled in {measurement_options[is_metric-1]}", int)
        if distance <= 0:
            print("you cannot have 0 or negative distance.\n")
        else:
            break
    while True:
        odometer = Get_Input(f"Please input the reading on your odometer in {measurement_options[is_metric-1]}", int)
        if distance <= 0:
            print("you cannot have 0 or negative distance.\n")
        else:
            break
    while True:
        litres_used = Get_Input(f"How much fuel have you used in {measurement_options[is_metric-1]}", int)
        if litres_used <= 0:
            print("you cannot have 0 or negative litres used.\n")
        else:
            break
    while True:
        capacity = Get_Input(f"How much fuel does your car hold in {measurement_options[is_metric-1]}", int)
        if capacity <= 0:
            print("you cannot have 0 or negative capacity.\n")
        else:
            break

    if is_metric == 2:
        distance = distance * 1.60934
        litres_used = litres_used * 4.546
        capacity = capacity * 4.546
        odometer = odometer * 1.60934

    MPG = (odometer - (odometer - distance))/(capacity - litres_used)
    print(f"Your MPG is {MPG}\n")
    Info = Save_Info()
    if Info == False:
        car_make = Get_Input("What is the make of your car?", str)
        car_model = Get_Input("What is the model of your car?", str)
        while True:
            car_year = Get_Input("What is the year of your car?", int)
            if car_year < 1900 and car_year > 2023:
                print("This is not a valid year for this program")
            else:
                break
    Save_Override(MPG,car_make,car_model,car_year)


def Get_Input(input_message, input_type):
    while (True):
        raw_input = input(f"{input_message}\n")
        try:
            user_input = input_type(raw_input)
            break
        except ValueError:
            print("This is the incorrect data type\n")
    return user_input

def Get_Choice(input_message, options):
    while(True):
        for x in range(len(options)):
            print(f"{x + 1} ---> {options[x]}\n")
        raw_input = input(f"{input_message}\n")
        try:
            user_input = int(raw_input)
            if user_input <= 0 or user_input > len(options):
                print("This input is not a valid option\n")
            else:
                break
        except ValueError:
            print("This is the incorrect data type\n")
    return user_input

def Output_Disclaimer():
    f = open("Storage\Disclaimer.txt","r")
    for x in f:
        print(x)
    f.close()

def Save_Override(MPG,car_make,car_model,car_year):
    f = open("Storage\Save.txt","w")
    f.write(f"MPG - {MPG}\n")
    f.write(f"Car Make - {car_make}\n")
    f.write(f"Car Model - {car_model}\n")
    f.write(f"Car Year - {car_year}\n")
    f.close()

def Save_Info():
    global MPG
    global car_make
    global car_model
    global car_year
    with open("Storage\Save.txt","r") as f:
        lines = [line.rstrip() for line in f]
        split_1 = str.split(lines[1]," ")
        split_2 = str.split(lines[2]," ")
        split_3 = str.split(lines[3]," ")
        if lines[0] == "":
            print("No Information to provide.")
            return False
        elif lines[1] == "Make":
            car_make = split_1[3]
            return True
        elif lines[2] == "Model":
            car_model = split_2[3]
            return True
        elif lines[3] == "Year":
            car_year = split_3[3]
            return True
    f.close()
    

Main()