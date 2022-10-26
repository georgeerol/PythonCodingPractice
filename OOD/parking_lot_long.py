from abc import ABC
from enum import Enum


class VehicleType(Enum):
    CAR, TRUCK, ELECTRIC, VAN, MOTORBIKE = 1, 2, 3, 4, 5


class ParkingSpotType(Enum):
    HANDICAPPED, COMPACT, LARGE, MOTORBIKE, ELECTRIC = 1, 2, 3, 4, 5


class AccountStatus(Enum):
    ACTIVE, BLOCKED, BANNED, COMPROMISED, ARCHIVED, UNKNOWN = 1, 2, 3, 4, 5, 6


class ParkingTicketStatus(Enum):
    ACTIVE, PAID, LOST = 1, 2, 3


class Address:
    def __init__(self, street, city, state, zip_code, country):
        self.street_address = street
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.country = country


class Person:
    def __init__(self, name, address, email, phone):
        self.name = name
        self.address = address
        self.email = email
        self.phone = phone


class Account:
    def __init__(self, user_name, password, person, status=AccountStatus.ACTIVE):
        self.user_name = user_name
        self.password = password
        self.person = person
        self.status = status

    def reset_password(self):
        pass


class Admin(Account):
    def __init__(self, user_name, password, person, status=AccountStatus.ACTIVE):
        super().__init__(user_name, password, person, status)

    def add_parking_floor(self, floor):
        pass

    def add_parking_spot(self, floor_name, spot):
        pass

    def add_parking_display_board(self, floor_name, display_board):
        pass

    def add_customer_info_panel(self, floor_name, info_panel):
        pass

    def add_entrance_panel(self, entrance_panel):
        pass

    def add_exit_panel(self, exit_panel):
        pass


class ParkingAttendant(Account):
    def __init__(self, user_name, password, person, status=AccountStatus.ACTIVE):
        super().__init__(user_name, password, person, status)

    def process_ticket(self, ticket_number):
        pass


class ParkingSpot(ABC):
    def __init__(self, number, parking_spot_type):
        self.number = number
        self.free = True
        self.vehicle = None
        self.parking_spot_type = parking_spot_type

    def is_free(self):
        return self.free

    def assign_vehicle(self, vehicle):
        self.vehicle = vehicle
        free = False

    def remove_vehicle(self):
        self.vehicle = None
        free = True


class CompactSpot(ParkingSpot):
    def __init__(self, number):
        super().__init__(number, ParkingSpotType.COMPACT)


class LargeSpot(ParkingSpot):
    def __init__(self, number):
        super().__init__(number, ParkingSpotType.LARGE)


class Vehicle(ABC):
    def __init__(self, license_number, vehicle_type, ticket=None):
        self.license_number = license_number
        self.type = vehicle_type
        self.ticket = ticket

    def assign_ticket(self, ticket):
        self.ticket = ticket


class Car(Vehicle):
    def __init__(self, license_numbers, ticket=None):
        super().__init__(license_numbers, VehicleType.CAR, ticket)


class Van(Vehicle):
    def __init__(self, license_numbers, ticket=None):
        super().__init__(license_numbers, VehicleType.VAN, ticket)


class Truck(Vehicle):
    def __init__(self, license_number, ticket=None):
        super().__init__(license_number, VehicleType.TRUCK, ticket)


class ParkingFloor:
    def __init__(self, name):
        self.name = name
        self.handicapped_spots = {}
        self.compact_spots = {}
        self.large_spots = {}

    def add_parking_spot(self, spot: ParkingSpot):
        switcher = {
            ParkingSpotType.HANDICAPPED: self.handicapped_spots.update({spot.number, spot}),
            ParkingSpotType.COMPACT: self.compact_spots.update({spot.number, spot}),
            ParkingSpotType.LARGE: self.compact_spots.update({spot.number, spot})
        }
        switcher.get(spot.parking_spot_type, "Wrong parking spot type")

    def assign_vehicleToSpot(self, vehicle, spot):
        pass


if __name__ == '__main__':
    lst = [None] * 10
