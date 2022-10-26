import unittest
from parking_lot import ParkingLot, Car, Bike, Bus


class TestParkingLot(unittest.TestCase):

    def test_part(self):
        parking_lot = ParkingLot(6, 30)
        res2 = parking_lot.park_vehicle(Car(10, "Amazon"))
        res3 = parking_lot.park_vehicle(Bike(20, "Amazon"))
        res4 = parking_lot.park_vehicle(Bus(30, "Microsoft"))

        self.assertTrue(res2)
        self.assertTrue(res3)
        self.assertTrue(res4)

    def test_leave_operation(self):
        parking_lot = ParkingLot(6, 30)
        self.assertTrue(parking_lot.park_vehicle(Car(10, "Amazon")))
        self.assertTrue(parking_lot.leave_operation(Car(10, "Amazon")))
