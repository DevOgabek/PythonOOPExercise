from championship import Championship
from grand_prix import Time

# Test create_driver and get_drivers
championship = Championship()
driver1 = championship.create_driver("Lewis Hamilton")
driver2 = championship.create_driver("Sebastian Vettel")
drivers = championship.get_drivers()
print("Drivers:", drivers)
print("Driver1 in drivers:", driver1 in drivers)
print("Driver2 in drivers:", driver2 in drivers)

# Test get_driver
retrieved_driver = championship.get_driver("Lewis Hamilton")
print("Retrieved driver:", retrieved_driver)
print("Drivers equal:", driver1 == retrieved_driver)

# Test define_grand_prix and get_grand_prix
grand_prix1 = championship.define_grand_prix("Monaco Grand Prix")
grand_prix2 = championship.define_grand_prix("Monza Grand Prix")
grand_prixs = championship.grand_prixs
print("Grand Prixs:", grand_prixs)
print("Grand Prix1 in grand_prixs:", grand_prix1 in grand_prixs)
print("Grand Prix2 in grand_prixs:", grand_prix2 in grand_prixs)

# Test set_time
time = championship.set_time(grand_prix1, driver1, 1, 30, 0, 500)
print("Time in race_times:", time in grand_prix1.race_times)
print("Grand Prix1 in driver raced:", grand_prix1 in driver1.get_raced())

# Test get_championship_ranking
grand_prix3 = championship.define_grand_prix("Silverstone Grand Prix")
championship.set_time(grand_prix3, driver1, 1, 28, 0, 500)
championship.set_time(grand_prix3, driver2, 1, 31, 0, 500)
ranking = championship.get_championship_ranking()
print("Championship ranking:", ranking)
print("Ranking equal:", ranking == [driver1, driver2])

# Test get_gp_ranking and get_position
time1 = Time(grand_prix1, driver1, 1, 32, 0, 500)
time2 = Time(grand_prix1, driver2, 1, 30, 0, 500)
grand_prix1.race_times = [time1, time2]  # Update race_times for testing
print("Grand Prix1 ranking:", grand_prix1.get_gp_ranking())
print("Position of driver1:", grand_prix1.get_position(driver1))
print("Position of driver2:", grand_prix1.get_position(driver2))