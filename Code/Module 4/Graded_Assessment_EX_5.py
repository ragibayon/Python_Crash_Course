# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 14:43:27 2020
Complete the code to iterate through the keys and values of the car_prices dictionary, 
printing out some information about each one.
@author: Ragib Shahariar Ayon
"""
def car_listing(car_prices):
  result = ""
  for cars, price in car_prices.items():
    result += "{} costs {} dollars".format(cars,price)+ "\n"
  return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))
