# 1. Base Class (Parent)
class Animal:
    def make_sound(self):
        print("Some generic animal sound")

# 2. Derived Classes (Children) overriding the parent method
class Dog(Animal):
    def make_sound(self):
        print("Woof Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

class Cow(Animal):
    def make_sound(self):
        print("Moo!")

# 3. Polymorphic Function
def play_sound(animal_object):
    # This single line handles ANY animal type dynamically!
    animal_object.make_sound()

# --- Execution ---
dog = Dog()
cat = Cat()
cow = Cow()

play_sound(dog)  # Output: Woof Woof!
play_sound(cat)  # Output: Meow!
play_sound(cow)  # Output: Moo!