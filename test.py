import unittest
import car


class TestCar(unittest.TestCase):
    def setUp(self):
        self.car = car.Car()


class TestInit(TestCar):
    def test_initial_speed(self):
        self.assertEqual(self.car.speed, 0)

    def test_initial_mileage(self):
        self.assertEqual(self.car.odometer, 0)

    def test_initial_time(self):
        self.assertEqual(self.car.time, 0)


class TestAccelerate(TestCar):
    def test_accelerate_form_zero(self):
        self.car.accelerate()
        self.assertEqual(self.car.speed, 5)

    def test_multiple_accelerates(self):
        for i in range(4):
            self.car.accelerate()
        self.assertEqual(self.car.speed, 20)


class TestDecelerate(TestCar):
    def test_decelerate_from_zero(self):
        self.car.speed = 0
        self.car.decelerate()
        self.assertEqual(self.car.speed, 0)

    def test_decelerate(self):
        self.car.speed = 15
        self.car.decelerate()
        self.assertEqual(self.car.speed, 10)

    def test_multiple_decelerates(self):
        self.car.speed = 25
        for i in range(2):
            self.car.decelerate()
        self.assertEqual(self.car.speed, 15)
