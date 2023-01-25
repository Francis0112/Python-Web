
# lets try java style import class from a different file.
# lets go! works like magic ~
import Beginner_training

# my practice oop before
class vehicle():
    
    def __init__(self) -> None:
        print("i am a vehicle")


    def i_am(self):
        print("i am parent class vehicle")


class car(vehicle):
    
    def i_am(self):
        print("i am a car.")

class boat(vehicle):
    
    def i_am(self):
        print("i am a boat.")


class airplane(vehicle):
    
    def i_am(self):
        print("i am a plane.")


#sam = {1,1,2,4,5}
#names = ("francis","francis", "dequito", "software", "engineer");
#print(sam)
#print(type(sam))
#print(names)
#print(type(names))
#print("")
#car().i_am()
#boat().i_am()
#airplane().i_am()
#vehicle().i_am()

#names = ['francis','dequito']
#name_set = {'francis','francis'}
#name_tupple = ('francis','francis')
#print(type(names))
#print(type(name_set))
#print(type(name_tupple))

a = Beginner_training
# b = a.person(name="Francis Earl b. dequito",occupation="Rock and Roll Music! Programmer Trainee lets go!!")
# print(b.sup_bro())
# print(b.job())

# print("")

# c = a.generate()
# print("Generated random numbers: ",c.gen_numbers())
# print(c.pie()+10)
# print("Pythagorean theorem: ",c.Pythagorean(sideA=12.15, sideB=44.15))


d = a.generate()

alist = [1,2,3,4,1]
atupple = (1,2,3,4,1)
aset = {1,2,3,4,1}
rdictionary = {
    "name":"francis",
    "lastname":"dequito"
}
sample = [n for n in range(1, 11)]
print(sample)
print(list(map(lambda x: x % 2 == 1, sample)))

# print(d.give_array(rdictionary))
# print(d.give_array(rdictionary)['name'])


