cars=100  #how many cars
space_in_a_car=4.0 #how many people can fit in each car
drivers=30 #people able to drive any of the 1000 cars
passengers=90 #number of people that need to fit into
cars_not_driven=cars-drivers #more cars than drivers so all the leftover cars
cars_driven=drivers # how many cars actually get driven
carpool_capacity=cars_driven*space_in_a_car #total number of people in the carpool
average_passengers_per_car=passengers/cars_driven #about how many will be in each car, hence the FPO



print "There are", cars, "cars around"
print "There are only" , drivers, "drivers around"
print "There will be", cars_not_driven, "empty cars today"
print "We can transport", carpool_capacity, "people today"
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."