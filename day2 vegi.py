# import random
# def generate_employee_details(num_employees):
#     cities = ['Kormangala', 'HSR Layout', 'Ballary', 'Mumbai', 'Chennai', 'Nellore', 'Gurgon', 'Hyderabad']
#
#     for _ in range(num_employees):
#         emp_id = random.randint(1, 9999)
#         emp_location = random.choice(cities)
#         emp_salary = random.randint(20000, 150000)
#
#         yield emp_id, emp_location, emp_salary
#
#
# num_employees = int(input("Enter the number of employee details to generate: "))
#
# employee_generator = generate_employee_details(num_employees)
#
# print("Employee Details:")
# print("---------------")
#
# for emp_id, emp_location, emp_salary in employee_generator:
#     print(f"Emp Id: {emp_id}")
#     print(f"Emp Location: {emp_location}")
import threading
#     print(f"Emp Salary: {emp_salary}")



########        2nd TASK        ==================

# import math
#
#
# class Shape:
#     def area(self):
#         pass
#
#
# class Square(Shape):                             # area of square -> area=side_length^2
#     def __init__(self, side_length):
#         self.side_length = side_length
#
#     def area(self):
#         return self.side_length ** 2
#
#
# class Triangle(Shape):                           # area = 1/2 * base * height
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height
#
#     def area(self):
#         return 0.5 * self.base * self.height
#
#
# class Circle(Shape):                              # area = pi * radius^2
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return math.pi * self.radius ** 2
#
#
# square = Square(5)
# triangle = Triangle(4, 6)
# circle = Circle(6.5)
#
# print(square.area())
# print(triangle.area())
# print(circle.area())
#########       #3RD TASK   =====================

from threading import Thread, current_thread
from time import sleep

producer = int(input("Enter the number of producers want to perform -> "))
consumer = int(input("Enter the number of consumers want to perform -> "))


class Producers(Thread):
    def run(self):
        for pro in range(producer):
            thread_name = current_thread().name
            print("thread__name",thread_name)
            if pro < consumer:
                print(thread_name, "- Producer", pro + 1)
            else:
                print(thread_name, "- Producer", pro + 1, "- Can't produce, consumers are less")
            sleep(1)


class Consumers(Thread):
    def run(self):
        for con in range(consumer):
            thread_name = current_thread().name
            print("thread_name",thread_name)
            if con < producer:
                print(thread_name, "- Consumer", con + 1)
                sleep(1)
            else:
                print(thread_name, "- Producer", con + 1, "- Can't produce, producers are less")

t1 = Producers()
t2 = Consumers()

t1.start()
sleep(0.4)

t2.start()

t1.join()
t2.join()

print("All producers and consumers are done.")
