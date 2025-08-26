class Rider:
    def __init__(self, id, name):
        self._id = id
        self._name = name


class Driver:
    def __init__(self, id, name, car):
        self._id = id
        self._name = name
        self._car = car
        self._is_driving = False

    def is_available(self):
        return not self._is_driving

    def set_status(self, busy: bool):
        self._is_driving = busy


class Ride:
    def __init__(self, driver, rider):
        self._driver = driver
        self._rider = rider

    def get_driver(self):
        return self._driver

    def get_rider(self):
        return self._rider


class RideshareSystem:
    def __init__(self):
        self._drivers = []
        self._riders = []
        self._rides = []

    def add_driver(self, driver):
        self._drivers.append(driver)

    def add_rider(self, rider):
        self._riders.append(rider)

    def request_ride(self, rider):
        # Check if rider already has an active ride
        for ride in self._rides:
            if ride.get_rider() == rider:
                print("Rider already in a ride!")
                return

        for driver in self._drivers:
            if driver.is_available():
                ride = Ride(driver, rider)
                driver.set_status(True)  # mark busy
                self._rides.append(ride)
                print(f"Ride started: Driver {driver._id} with Rider {rider._id}")
                return
        print("All drivers busy! Try again later")

    def end_ride(self, ride):
        if ride in self._rides:
            self._rides.remove(ride)
            driver = ride.get_driver()
            driver.set_status(False)  # mark available
            print(f"Ride ended: Driver {driver._id} is now available")
        else:
            print("Ride does not exist")
