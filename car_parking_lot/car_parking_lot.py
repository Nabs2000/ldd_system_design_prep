from typing import List, Set


class Car:
    """Base class for cars"""
    def __init__(self, car_id: str, size: str, has_pass: bool):
        self.id = car_id
        self.size = size   # "COMPACT" or "LARGE"
        self.has_pass = has_pass


class NonElectricCar(Car):
    def __init__(self, car_id: str, size: str, has_pass: bool):
        super().__init__(car_id, size, has_pass)


# Future extension: ElectricCar(Car) with charging_support = True/False


class ParkingSpot:
    """Represents a single parking spot of a given size"""
    def __init__(self, size: str):
        self.size = size   # "COMPACT" or "LARGE"
        self.car: Car | None = None

    def is_free(self) -> bool:
        return self.car is None

    def can_accept(self, car: Car) -> bool:
        if not car.has_pass:
            return False
        if self.size == "LARGE":
            # large spots can take both compact and large cars
            return True
        return car.size == self.size

    def park(self, car: Car):
        self.car = car

    def remove(self):
        self.car = None


class ParkingLot:
    """Manages multiple parking spots"""
    def __init__(self, spots: List[ParkingSpot]):
        self.spots = spots
        self.registered_cars: Set[Car] = set()

    def park_car(self, car: Car):
        if car in self.registered_cars:
            print(f"Car {car.id} is already parked.")
            return

        for spot in self.spots:
            if spot.is_free() and spot.can_accept(car):
                spot.park(car)
                self.registered_cars.add(car)
                print(f"Parked car {car.id} in a {spot.size} spot")
                return
        print(f"No available spot for car {car.id}")

    def remove_car(self, car: Car):
        if car not in self.registered_cars:
            print(f"Car {car.id} not found in lot.")
            return

        for spot in self.spots:
            if spot.car == car:
                spot.remove()
                self.registered_cars.remove(car)
                print(f"Removed car {car.id}")
                return


# ---------------- TEST CASES ---------------- #
if __name__ == "__main__":
    # Create parking lot with 2 compact and 2 large spots
    spots = [ParkingSpot("COMPACT"), ParkingSpot("COMPACT"),
             ParkingSpot("LARGE"), ParkingSpot("LARGE")]
    lot = ParkingLot(spots)

    # Cars
    c1 = NonElectricCar("C1", "COMPACT", True)
    c2 = NonElectricCar("C2", "LARGE", True)
    c3 = NonElectricCar("C3", "COMPACT", False)  # no pass
    c4 = NonElectricCar("C4", "COMPACT", True)
    c5 = NonElectricCar("C5", "COMPACT", True)   # should go in large spot

    # Park cars
    lot.park_car(c1)  # ✅ should succeed
    lot.park_car(c2)  # ✅ should succeed
    lot.park_car(c3)  # ❌ no pass
    lot.park_car(c4)  # ✅ should succeed
    lot.park_car(c5)  # ✅ should take a large spot

    # Try to park c1 again
    lot.park_car(c1)  # ❌ already parked

    # Remove c2
    lot.remove_car(c2)

    # Try to remove a car not in lot
    lot.remove_car(c2)
