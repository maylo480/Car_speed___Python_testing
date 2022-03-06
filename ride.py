import car

if __name__ == '__main__':

    my_car = car.Car()
    print("The car has been spawned!")

    while True:
        action = input("\nWhat should I do? [A]ccelerate, [D]ecelerate, "
                 "[B]rake, show [O]dometer, or show average [S]peed, "
                       "[Q]uit: ").upper()
        if action not in "ADBOSQ" or len(action) != 1:
            print("Invalid input! Try again: ")
            continue
        if action == 'A':
            my_car.accelerate()
            my_car.show_speed()
        elif action == 'D':
            my_car.decelerate()
            my_car.show_speed()
        elif action == 'B':
            my_car.brake()
            my_car.show_speed()
        elif action == 'O':
            print("The car has driven {} kilometers".format(my_car.odometer))
        elif action == 'S':
            print("The car's average speed was {} kph".format(my_car.average_speed()))
        elif action == 'Q':
            print("OK, we are done drivin")
            break

        my_car.step()
