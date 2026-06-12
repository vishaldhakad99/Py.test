class Tesla(Vehicle):
    def start(self):
        print("Tesla started")

    def stop(self):
        print("Tesla stopped")

    def fuel_type(self):
        print("Electric")


c = Car()
b = Bike()
t = Tesla()

c.start()
c.stop()
c.fuel_type()

b.start()
b.stop()
b.fuel_type()

t.start()
t.stop()
t.fuel_type()