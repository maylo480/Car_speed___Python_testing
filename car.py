class Car:

    def __init__(self):
        self.speed = 0
        self.odometer = 0
        self.time = 0

    def accelerate(self):
        self.speed += 5

    def decelerate(self):
        if self.speed >= 5:
            self.speed -= 5
        else:
            print("You can't decelerate form 0 kph!")

    def brake(self):
        if self.speed >= 5:
            self.speed = 0
        else:
            print("You can't brake form 0 kph!")

    def show_speed(self):
        print("I'm going {} kph!".format(self.speed))

    def step(self):
        self.odometer += self.speed
        self.time += 1

    def average_speed(self):
        if self.time != 0:
            return self.odometer / self.time
        else:
            pass
