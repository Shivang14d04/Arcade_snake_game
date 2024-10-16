# Class inheritance
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("exhale , inhale" )

class Fish(Animal):
    def __init__(self):
        super().__init__()    # call to the super class
    def swim(self):
        print("swim in water")

    def breathe(self):
        super().breathe()  #  this will inherit the bretahe mehod so i can do all the things inn breathe method ,
        print("breathing under water")  # we want to do the breathe method more

nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)


# Slicing in python

piano_keys =['a','b','c','d','e','f']

print(piano_keys[2:5])

# from index 2 to all the way to the last
print(piano_keys[2:])

# from first index  to the specified index
print(piano_keys[:2])

# third no is incrementing the index
print(piano_keys[2:5:2])

print(piano_keys[::2]) # from beginning till end to get every second item

print(piano_keys[::-1])  # increment start from last (reverse the list)

# also work with tuples
piano_tuples =['as','ed','se','fg','kj','tg']
print(piano_tuples[2:5])
