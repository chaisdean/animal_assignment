class animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 23

    def walk(self):
        self.health = self.health - 1
        return self

    def run(self):
        self.health = self.health - 5
        return self

    def show_health(self):
        print self.name
        print str(self.health)

# animal = animal('liger')
# animal.walk()
# animal.walk()
# animal.walk()
# animal.run()
# animal.run()
# animal.show_health()

class dog(animal):
    def __init__(self,name):
      super(dog,self).__init__(name)
      self.health = 150

    def pet(self):
        self.health = self.health + 5
        return self

dog = dog('java')
dog.walk().walk().walk().run().run().pet().show_health()


class dragon(animal):
    def __init__(self,name):
        self.health = 170

    def fly(self):
        self.health -= 10
        return self

    def display_health(self):
        print ('I am legend')
        print str(self.health)

dragon = dragon('aragorn')
dragon.display_health()
#
# class dragon(animal):
#     def __init__(self):
