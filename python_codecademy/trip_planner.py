__author__ = 'morek'

def hotel_cost(nights):
    return 140*nights
def plane_ride_cost(city):
    if city =="Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city =="Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475

def rental_car_cost(days):
    costs=40*days
    if days >0 and days <3:
        return costs
    if days >= 7:
        costs -=50
        return costs
    elif days >= 3 and days <7:
        costs -=20
        return costs
    else:
        return False

def trip_cost(city, days, spending_money):
    return rental_car_cost(days)+hotel_cost(days)+plane_ride_cost(city)+spending_money


print trip_cost("Los Angeles", 5, 600)