# 1
# class Country:
#     def __init__(self, name, population):
#         self.name = name
#         self.population = population

#     def add(self, other_country):
#         combined_name = f"{self.name} {other_country.name}"
#         combined_population = self.population + other_country.population
#         combined_country = Country(combined_name, combined_population)
#         return combined_country


# bosnia = Country('Bosnia', 10_000_000)
# herzegovina = Country('Herzegovina', 5_000_000)


# bosnia_herzegovina = bosnia.add(herzegovina)


# print(bosnia_herzegovina.population)  
# print(bosnia_herzegovina.name)
# 2
# class Country:
#     def __init__(self, name, population):
#         self.name = name
#         self.population = population

#     def __add__(self, other_country):
#         combined_name = f"{self.name} {other_country.name}"
#         combined_population = self.population + other_country.population
#         combined_country = Country(combined_name, combined_population)
#         return combined_country


# bosnia = Country('Bosnia', 10_000_000)
# herzegovina = Country('Herzegovina', 5_000_000)

# bosnia_herzegovina = bosnia + herzegovina

# print(bosnia_herzegovina.population)  
# print(bosnia_herzegovina.name)        

# 3
# class Car:
#     def __init__(self, brand, model, year, speed=0):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.speed = speed

#     def accelerate(self):
#         self.speed += 5

#     def brake(self):
#         self.speed -= 5


# my_car = Car(brand="Toyota", model="Corolla", year=2022)

# my_car.accelerate()
# print(f"Current speed: {my_car.speed}") 

# my_car.brake()
# print(f"Current speed: {my_car.speed}")  
# 4
# class Robot:
#     def __init__(self, orientation, position_x, position_y):
#         self.orientation = orientation
#         self.position_x = position_x
#         self.position_y = position_y

#     def move(self, steps):
#         if self.orientation == "up":
#             self.position_y += steps
#         elif self.orientation == "down":
#             self.position_y -= steps
#         elif self.orientation == "left":
#             self.position_x -= steps
#         elif self.orientation == "right":
#             self.position_x += steps

#     def turn(self, direction):
#         if direction == "left":
#             directions = ["up", "left", "down", "right"]
#         elif direction == "right":
#             directions = ["up", "right", "down", "left"]
        
#         current_index = directions.index(self.orientation)
#         self.orientation = directions[(current_index + 1) % 4]

#     def display_position(self):
#         print(f"Position: ({self.position_x}, {self.position_y}), Orientation: {self.orientation}")


# my_robot = Robot(orientation="up", position_x=0, position_y=0)

# my_robot.move(3)
# my_robot.display_position()  

# my_robot.turn("right")
# my_robot.display_position() 