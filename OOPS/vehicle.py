class bike:

    def start(self):
        print("kicker start")

    def breaking(self):
        print("drum break")

class HeroHondaSplendor(bike):

    def start(self):
        print("self start")

    def breaking(self):
        print("abs breaking")    

hobj=HeroHondaSplendor()

hobj.start()

