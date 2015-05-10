# -*- coding: utf-8 -*-
"""
Created on Sat May  9 22:52:59 2015

@author: kunwang
"""

def update_up(class_method):
    def inner(self, *args, **kwargs):
        medthod_name = class_method.func_name
        class_method(self, *args, **kwargs)
        for sup in self.super_shops:
            getattr(sup, medthod_name)(*args,**kwargs)
    return inner

def update_up_down(class_method):
    def inner(self, *args, **kwargs):
        medthod_name = class_method.func_name
        if class_method(self, *args, **kwargs):
            for sup in self.super_shops:
                getattr(sup, medthod_name)(*args,**kwargs)
            for sub in self.sub_shops:
                getattr(sub, medthod_name)(*args, **kwargs)
    return inner

class Car():
    def __init__(self, color, owner=None):
        self.color = color
        self.owner = owner

class Car_for_sale():
    def __init__(self, list_cars=None, super_shops=None, sub_shops=None):
        self.available_cars = list_cars
        if super_shops is None:
            self.super_shops = []
        else:
            self.super_shops = super_shops
            for sup in self.super_shops:
                sup.sub_shops.append(self)
        if sub_shops is None:
            self.sub_shops = []
        else:
            self.sub_shops = sub_shops
            for sub in self.sub_shops:
                sub.super_shops.append(self)
        
    @update_up_down
    def sell_car(self, car):
        if car not in self.available_cars:
            return False
        self.available_cars.remove(car)
        return True
     
    @update_up
    def buy_car(self, car):
        if car in self.available_cars:
            return
        self.available_cars.append(car)


def print_color(shop):
    print [x.color for x in shop.available_cars]
def check_shops(cars):
    for car in cars:
        print_color(car)


cars = []
for i in range(5):
    new_car = Car('Red')
    cars.append(new_car)
    new_car = Car('Blue')
    cars.append(new_car)

shop_1 = Car_for_sale(list_cars=cars)
red_cars = filter(lambda x:x.color=='Red', cars)
shop_2 = Car_for_sale(list_cars=red_cars, super_shops=[shop_1])
shops = [shop_1, shop_2]

check_shops(shops)

one_car = shop_2.available_cars[0]
shop_2.sell_car(one_car)
check_shops(shops)

one_car = Car('Red')
shop_2.buy_car(one_car)
check_shops(shops)

one_car = shop_2.available_cars[0]
shop_1.sell_car(one_car)
check_shops(shops)

one_car = Car('Blue')
shop_1.buy_car(one_car)
check_shops(shops)

one_car = shop_1.available_cars[0]
shop_1.sell_car(one_car)
check_shops(shops)    

