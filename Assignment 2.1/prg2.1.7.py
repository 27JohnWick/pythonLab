def check_speed(speed):
    speed_limit = 70
    points = (speed - speed_limit) // 5

    if speed <= speed_limit:
        print("Ok")
    elif points<=12:
        print("License suspended")
    else:
        print("Points:", points)

speed = int(input("Enter the speed of the driver: "))
