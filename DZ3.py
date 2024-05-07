class Human:
 def __init__(self, name="Human"):
    self.name = name
class Auto:
 def __init__(self, brand):
    self.brand = brand
    self.passengers = []
 def add_passenger(self, human):
     self.passengers.append(human)
 def print_passengers_names(self):
  if self.passengers!= []:
    print(f"Names of {self.brand} passengers:")
  for passenger in self.passengers:
    print(passenger.name)
  else:
    print(f"There are no passengers in {self.brand}")

class Human:
 def __init__(self, name="Human"):
    self.name = name

class Auto:
 def __init__(self, brand):
    self.brand = brand
    self.passengers = []

 def add_passenger(self, human):
    self.passengers.append(human)

 def print_passengers_names(self):
  if self.passengers != []:
     print(f"Names of {self.brand} passengers: ")
  for passenger in self.passengers:
     print(passenger.name)
  else:
     print(f"There are no passengers in {self.brand} ")
sasha = Human("Sasha")
masha = Human("Masha")
car = Auto("Mersedes")
car.add_passenger(sasha)
car.add_passenger(masha)
car.print_passengers_names()

class Human:
 def __init__(self, name="Human"):
   self.name = name

class Auto:
 def __init__(self, brand):
  self.brand = brand
  self.passengers = []

 def add_passenger(self, *args):
  for passenger in args:
   self.passengers.append(passenger)
 def print_passengers_names(self):
  if self.passengers!= []:
   print(f"Names of {self.brand} passengers:")
  for passenger in self.passengers:
   print(passenger.name)
  else:
   print(f"There are no passengers in {self.brand}")
nick = Human("Nick")
kate = Human("Kate")
car = Auto("BMW")
car.add_passenger(nick, kate)
car.print_passengers_names()

class Human:
 def __init__(self, name="Human", job=None, home=None, car=None):
  self.name = name
  self.money = 100
  self.gladness = 50
  self.satiety = 50
  self.job = job

def get_home(self):
 pass

def get_car(self):
 pass

def get_job(self):
 pass

def eat(self):
 pass

def work(self):
 pass

def shopping(self, manage):
 pass

def chill(self):
 pass

def clean_home(self):
 pass

def to_repair(self):
 pass

def days_indexes(self, day):
 pass

def is_alive(self):
 pass

def live(self, day):
 pass

class Auto:
 def __init__(self, brand_list):
  self.choice(list (brand_list))
  self.fuel=brand_list[self.brand]["fuel"]
  self.strength = brand_list[self.brand]
  ["strength"]
  self.consumption=brand_list[self.brand]
  ["consumption"]
brand_of_car = {
  "BMW": {"fuel": 100, "strength":100, "consumption": 6},
  "Lada": {"fuel":50, "strength":40, "consumption": 10},
  "Volvo":{"fuel":70, "strength":150, "consumption": 8},
  "Ferrari":{"fuel":80, "strength":120, "consumption": 14},
 }

def drive(self):
 if self.strength>0 and self.fuel>=self.consumption:
  self.fuel-=self.consumption
  self.strength-=1
  return True
 else:
  print("The car cannot move")
  return False

def days_indexes(self, day):
 day = f" Today the {day} of {self.name}'s life "
 print(f"{day:=^50}","\n")
 human_indexes = self.name + "'s indexes"
 print(f"{human_indexes:^50}","\n")
 print(f"Money – {self.money}")
 print(f"Satiety – {self.satiety}")
 print(f"Gladness – {self.gladness}")
 home_indexes = "Home indexes"
 print(f"{home_indexes:^50}", "\n")
 print(f"Food – {self.home.food}")
 print(f"Mess – {self.home.mess}")
 car_indexes = f"{self.car.brand} car indexes"
 print(f"{car_indexes:^50}", "\n")
 print(f"Fuel – {self.car.fuel}")
 print(f"Strength – {self.car.strength}")

def is_alive(self):
 if self.gladness < 0:
  print("Depression…")
  return False

 if self.satiety < 0:
  print("Dead…")
  return False

 if self.money < -500:
   print("Bankrupt…")
   return False

 def live(self, day):
    if self.is_alive() == False:
         return False
    if self.home is None:
      print("Settled in the house")
      self.get_home()
    if self.car is None:
      self.get_car()
      print(f"I bought a car{self.car.brand}")
    if self.job is None:
      self.get_job()
      print(f"I don't have a job, I'm going to get a job")
      self.days_indexes(day)
dice =(1, 4)
print("I want to chill, but there is so much  mess…\nSo I will clean the house")
