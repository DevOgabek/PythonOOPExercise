from grand_prix import GrandPrix,  Time
from driver import Driver

class Championship:
    def __init__(self):
        self.drivers = []
        self.grand_prixs = []

    def create_driver(self, name):
        driver = Driver(name)
        self.drivers.append(driver)
        return driver

    def get_drivers(self):
        return self.drivers

    def get_driver(self, name):
        for driver in self.drivers:
            if driver.get_name() == name:
                return driver

    def define_grand_prix(self, name):
        grand_prix = GrandPrix(name)
        self.grand_prixs.append(grand_prix)
        return grand_prix

    def get_grand_prix(self, name):
        for grand_prix in self.grand_prixs:
            if grand_prix.get_name() == name:
                return grand_prix

    def set_time(self, grand_prix, driver, hours, minutes, seconds, milliseconds):
        time = Time(grand_prix, driver, hours, minutes, seconds, milliseconds)
        grand_prix.race_times.append(time)
        driver.get_raced().append(grand_prix)
        return time

    def get_championship_ranking(self):
        self.drivers.sort(key=lambda x: x.get_points(), reverse=True)
        return self.drivers