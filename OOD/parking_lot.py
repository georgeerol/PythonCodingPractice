"""
Parking Lot has 2 levels
Each Level has 2 rows
Each row has 2 parking slots
Car will take one parking slot


"""
from abc import ABC, abstractmethod
from enum import Enum
import random
from typing import List, Any


class VehicleType(Enum):
    CAR = 1
    BIKE = 2
    BUS = 3


class Vehicle:
    def __init__(self, license_plate: int, company_name: str, type_of_vehicle: VehicleType):
        self.license_plate = license_plate
        self.company_name = company_name
        self.type_of_vehicle = type_of_vehicle

    def get_type(self):
        return self.type_of_vehicle

    def __eq__(self, other):
        """overwrite __eq__ methods to correctly check if two vehicle objects are same. Otherwise, they will be
        checked at hashcode level not at content level.'''
        """
        if other is None:
            return False
        if self.license_plate != other.license_plate:
            return False
        if self.company_name != other.company_name:
            return False
        if self.type_of_vehicle != other.type_of_vehicle:
            return False
        return True


class Car(Vehicle):
    def __init__(self, license_plate: int, company_name: str):
        Vehicle.__init__(self, license_plate=license_plate, company_name=company_name, type_of_vehicle=VehicleType.CAR)


class Bike(Vehicle):
    def __init__(self, license_plate, company_name):
        Vehicle.__init__(self, license_plate=license_plate, company_name=company_name, type_of_vehicle=VehicleType.BIKE)


class Bus(Vehicle):
    def __init__(self, license_plate, company_name):
        Vehicle.__init__(self, license_plate=license_plate, company_name=company_name, type_of_vehicle=VehicleType.BIKE)


class Slots:
    def __init__(self, lane: int, spot_number: int, type_of_vehicle: VehicleType):
        self.lane = lane
        self.spot_number = spot_number
        self.type_of_vehicle = type_of_vehicle
        self.vehicle = None

    def park(self, vehicle):
        if vehicle.type_of_vehicle == self.type_of_vehicle:
            self.vehicle = vehicle
            return True
        else:
            return False

    def get_vehicle(self):
        return self.vehicle

    def remove_vehicle(self):
        self.vehicle = None
        return self.vehicle


class Level:
    """ Level class - Each level is an independent entity with a floor number,Its lanes and the slots withing it.
    The number of lanes are designed based on the number of slots. 10 slots make one lane
    """

    def __init__(self, floor_number, no_of_slots):
        self.floor_number = floor_number
        self.spots_per_lane = 10
        self.lanes = no_of_slots / self.spots_per_lane
        self.parking_slots = set()
        self.available_spots = []

        # Check available spots in an lane
        for lane in range(int(self.lanes)):
            for i in range(self.spots_per_lane):
                # Randomly assign a type to each slot
                self.available_spots.append(
                    Slots(lane=lane, spot_number=i, type_of_vehicle=random.choice(list(VehicleType))))

    def park(self, vehicle):
        for slot in self.available_spots:
            if slot.park(vehicle):
                return True
        return False

    def remove(self, vehicle):
        for spot in self.available_spots:
            if spot.get_vehicle() == vehicle:
                spot.remove_vehicle()
                return True
        return False

    def company_parked(self, company_name):
        all_vehicles: List[Any] = []
        for spot in self.available_spots:
            vehicle = spot.get_vehicle()
            if (vehicle is not None) and (vehicle.company_name == company_name):
                all_vehicles.append(vehicle)
        return all_vehicles


class ParkingLot:

    def __init__(self, num_of_floor: int, num_of_slot):
        self.Levels = []
        for i in range(num_of_floor):
            self.Levels.append(Level(floor_number=i, no_of_slots=num_of_slot))
            print("Level " + str(i) + " created with " + str(num_of_slot) + " " + "slots")

    def park_vehicle(self, vehicle: Vehicle) -> bool:
        for level in self.Levels:
            if level.park(vehicle):
                return True
        return False

    def leave_operation(self, vehicle: Vehicle) -> bool:
        for level in self.Levels:
            if level.remove(vehicle):
                return True

    def company_parked(self, company_name) -> List:
        all_vehicles = []
        for level in self.Levels:
            all_vehicles.extend(level.company_parked(company_name))
        return all_vehicles


if __name__ == '__main__':
    parking_lot = ParkingLot(num_of_floor=6, num_of_slot=30)
    parking_lot.park_vehicle(Car(license_plate=10, company_name="Amazon"))
