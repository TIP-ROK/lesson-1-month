class Country:

    def __init__(self, name, territory, population, language):
        self.name = name
        self.territory = territory
        self.population = population
        self.language = language

    def __str__(self):
        return f"{self.name} {self.territory} {self.population} {self.language}"

    def live(self):
        return self.population
    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        if value = "Kazakhstan":
            print("WAR!!")
        else:
            self.name = value

class Region(Country):

    def __init__(self, country, region_name, region_territory, region_population):
        super(Region, self).__init__(country.name, country.territory, country.population, country.language)
        self.region_name = region_name
        self.region_territory = region_territory
        self.region_population = region_population

    def __str__(self):
        return f"{super(Region,self).__str__()} {self.region_name} {self.region_territory} {self.region_population}"


country = Country("Kyrgizstan", 100000000, 6000000, "kyrgyz")
talas = Region(country, "Talas", 2222222, 1)

print(talas.name)
print(talas)