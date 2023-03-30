#trying to make this work
from Airport import *

class Flight:
    def __init__(self, flightNo, origAirport, destAirport):
        # Check if origin and destination are Airport instances
        if not isinstance(origAirport, Airport) or not isinstance(destAirport, Airport):
            raise TypeError("The origin and destination arguments must be Airport objects")



        # Check if flight number format is correct
        if not isinstance(flightNo, str) or not (len(flightNo) == 6 and flightNo[:3].isalpha() and flightNo[3:].isdigit()):
            raise TypeError("The flight number format is incorrect")

        self._flightNo = flightNo  # Flight number
        self._origin = origAirport  # Origin airport (Airport instance)
        self._destination = destAirport  # Destination airport (Airport instance)

    # Represent the Flight object as a string

    def __repr__(self):
        flight_type = "domestic" if self.isDomesticFlight() else "international"
        return f"Flight({self._flightNo}): {self._origin.getCity()} -> {self._destination.getCity()} [{flight_type}]"

    # Compare two Flight objects for equality based on origin and destination airports
    def __eq__(self, other):
        if not isinstance(other, Flight):
            return False
        return self._origin == other._origin and self._destination == other._destination

    # Getter method to retrieve the flight number
    def getFlightNumber(self):
        return self._flightNo

    # Getter method to retrieve the origin airport
    def getOrigin(self):
        return self._origin

    # Getter method to retrieve the destination airport
    def getDestination(self):
        return self._destination

    # Method to check if the flight is domestic (origin and destination are in the same country)
    def isDomesticFlight(self):
        return self._origin.getCountry() == self._destination.getCountry()

    # Setter method to set/update the origin airport
    def setOrigin(self, origin):
        if not isinstance(origin, Airport):
            raise TypeError("The origin must be an Airport object")
        self._origin = origin

    # Setter method to set/update the destination airport
    def setDestination(self, destination):
        if not isinstance(destination, Airport):
            raise TypeError("The destination must be an Airport object")
        self._destination = destination
