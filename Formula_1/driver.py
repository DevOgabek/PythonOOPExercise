class Driver:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.raced_in = []

    def get_name(self):
        return self.name

    def get_points(self):
        return self.points

    def add_points(self, position):
        points_array = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]
        if 1 <= position <= 10:
            self.points += points_array[position - 1]

    def get_raced(self):
        return self.raced_in

    def __str__(self):
        return f"Driver(name={self.name}, points={self.points})"