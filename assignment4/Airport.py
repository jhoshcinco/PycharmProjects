class Airport:
    def __init__(self, code, city, country, continent):
        self._code = code  # Airport code (IATA/ICAO)
        self._city = city  # City where the airport is located
        self._country = country  # Country where the airport is located
        self._continent = continent  # Continent where the airport is located

    # Represent the Airport object as a string in the format: "code (city, country)"
    def __repr__(self):
        return f"{self._code} ({self._city}, {self._country})"

    # Getter method to retrieve the airport code
    def getCode(self):
        return self._code

    # Getter method of airport city
    def getCity(self):
        return self._city

    # Getter method of country
    def getCountry(self):
        return self._country

    # Getter method of continent
    def getContinent(self):
        return self._continent

    # Setter method for city
    def setCity(self, city):
        self._city = city

    # Setter method for city
    def setCountry(self, country):
        self._country = country

    # Setter method for continent
    def setContinent(self, continent):
        self._continent = continent
