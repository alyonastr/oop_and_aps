class Planet:
    @staticmethod
    def is_big_planet(diametr):
        if diametr > 10000:
            return True
        else:
            return False
        
print(Planet.is_big_planet(100))