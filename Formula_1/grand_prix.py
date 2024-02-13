class GrandPrix:
    def __init__(self, name):
        self.name = name
        self.race_times = []

    def get_name(self):
        return self.name

    def get_gp_ranking(self):
        self.race_times.sort(key=lambda x: x.get_time())
        return self.race_times

    def get_position(self, driver):
        for i, race_time in enumerate(self.race_times):
            if race_time.get_driver() == driver:
                return i + 1

class Time:
    def __init__(self, grand_prix, driver, hours, minutes, seconds, milliseconds):
        self.grand_prix = grand_prix
        self.driver = driver
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.milliseconds = milliseconds

    def get_driver(self):
        return self.driver

    def get_time(self):
        return (
            self.hours * 3600
            + self.minutes * 60
            + self.seconds
            + self.milliseconds / 1000
        )

    def __str__(self):
        return f"Time({self.hours}:{self.minutes}:{self.seconds}.{self.milliseconds})"