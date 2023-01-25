
import math
import random


# Recall Python. Warming up.
# OOP Python for fun! rock and roll music
# this is main class! 
class main():
	#OOP Constructor
	def __init__(self):
		print("Good Bye! :)")

	#polymorph
	def hold(self):
		return "overide this method. please? onegai?" 

class living(main):
	def __init__(self,  species, pet_name, domesticated=False, extinct=False) -> None:
		print("This is the living class!")
		self.species=species
		self.pet_name=pet_name
		self.domesticated=domesticated
		self.extinct=extinct

	#polymorph
	def hold(self):
		return "The Living have overide this method. please? onegai?"

class undead(main):
	def __init__(self, name, occupation) -> None:
		self.name=name
		self.occupation=occupation
		print("This is the Undead class!")

	#polymorph
	def hold(self):
		return "The Undead have overide method. please? onegai?"


class mecha(main):
	def __init__(self) -> None:
		print("I am a Gundam! This is mecha class!")

	#polymorph
	def hold(self):
		return "The Mecha have overide method. please? onegai?"


# some extra class that extends living class.. oh yea lets go JAVA
class pets(living):
	def pet_species(self):
		return f"species: {self.species}"

	def name_pet(self):
		return f"Name: {self.pet_name}"

	def pet_domesticated(self):
		return f"domesticated: {self.domesticated}"

	def pet_extinct(self):
		return f"extinct: {self.extinct}"
	

# extends undead class zombie 
# sorry i do this code for anti boringness pang pa tanggal ng umay po hehe. onegai
class person(undead):
	
	def say_name(self):
		return f"Hello {self.name}!"

	def job(self):
		return f"you are a {self.occupation}"
	
# extrend class robots! gundams seed voltes 5 optimum pride oha a a a a a
class generate(mecha):

	mecha_version = 3.0

	def gen_numbers(self):
		temp = []
		for i in range(6):
			temp.append(random.randrange(start=1,stop=100))
		return temp

	def upgrade(self):
		self.mecha_version = self.mecha_version+1.0
		return self.mecha_version

	def pythagorean(self, sideA, sideB):
		return math.sqrt(sideA**2+sideB**2)

	def predict_year(self, user_age):
		import datetime
		present_year = datetime.datetime.now().year
		present_year = present_year-user_age-1
		return present_year