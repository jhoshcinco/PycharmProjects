from Flight import *
from Airport import *

class Aviation:
    def __init__(self):
        self._allAirports = None
        self._allFlights = None
        self._allCountries = None

    # Getter for allAirports
    def getAllAirports(self):
        return self._allAirports

    # Setter for allAirports
    def setAllAirports(self, allAirports):
        self._allAirports = allAirports

    # Getter for allFlights
    def getAllFlights(self):
        return self._allFlights

    # Setter for allFlights
    def setAllFlights(self, allFlights):
        self._allFlights = allFlights

    # Getter for allCountries
    def getAllCountries(self):
        return self._allCountries

    # Setter for allCountries
    def setAllCountries(self, allCountries):
        self._allCountries = allCountries

    def loadData(self, airportFile, flightFile, countriesFile):
        self._allCountries = {}
        self._allAirports = {}
        self._allFlights = {}

        # read countries data
        try:
            with open(countriesFile, "r", encoding='utf8') as f:
                for line in f:
                    country, continent = [s.strip() for s in line.split(',')]#iterate through the csv file and split it then strip with any white space
                    self._allCountries[country] = continent#set the country with its continent
        except Exception:
            return False

        # read airports data
        try:
            with open(airportFile, "r", encoding='utf8') as f:
                for line in f:
                    code, country, city = [s.strip() for s in line.split(',')]
                    # print(code, country, city)
                    continent = self._allCountries.get(country)
                    # print(continent)
                    if continent:#checks if the continent is not empty
                        airport = Airport(code, city, country, continent)#sets airport data
                        self._allAirports[code] = airport
                        # print(self._allAirports[code])

        except Exception:
            return False

        # read flights data
        try:
            with open(flightFile, "r", encoding='utf8') as f:
                for line in f:
                    flightNo, origAirportCode, destAirportCode = [s.strip() for s in line.split(',')] #text processing
                    origAirport = self._allAirports.get(origAirportCode)
                    destAirport = self._allAirports.get(destAirportCode)
                    if origAirport and destAirport:#checks if the airport is not empty
                        flight = Flight(flightNo, origAirport, destAirport)#sets flight data
                        if origAirportCode not in self._allFlights:#checks if the airport code is not in the flight
                            self._allFlights[origAirportCode] = []
                        self._allFlights[origAirportCode].append(flight)#adds the flight to the flight list
        except Exception:
            return False

        return True

    def getAirportByCode(self, code):#Return the Airport object that has the given code (i.e. YYZ should return the Airport object for the YYZ (Pearson) airport). If there is no Airport found for the given code, just return -1.
        # print(self._allAirports.get(code))
        if(self._allAirports.get(code)):
            return self._allAirports.get(code)
        # print(self._allAirports.get(code),-1)
        else: return -1
    #TODO: You can create a helper method for iterate through the airports and flights
    def findAllCityFlights(self, city):
        flights = []
        for flight_list in self._allFlights.values():#iterates through the values of flight
            for flight in flight_list:#iterates through the flight list
                if flight.getOrigin().getCity() == city or flight.getDestination().getCity() == city:
                    flights.append(flight)
        return flights

    def findFlightByNo(self, flightNo):
        for flight_list in self._allFlights.values():#iterates through the values of flight
            for flight in flight_list:#iterates through the flight list
                if flight.getFlightNumber() == flightNo: #finds the flightobject with the flight number
                    return flight
                #   print("flight found") debug

                else:
                    #    print("Flight not found")#debug
                    return -1 #return -1 if not found


    def findAllCountryFlights(self, country):
        flights = []
        for flight_list in self._allFlights.values():#iterates through the values of flight
            for flight in flight_list:#iterates through the flight list
                if flight.getOrigin().getCountry() == country or flight.getDestination().getCountry() == country:#checks for the flight object with the country given
                    flights.append(flight)
        return flights

    def findFlightBetween(self, origAirport, destAirport):
<<<<<<< HEAD
        airport1 = []
        airport2 = []
        direct_flight = None
        connecting_airports = set()
        for flight_list in self._allFlights.values():
        #     for flight in flight_list:
        #         if flight.getOrigin() == origAirport and flight.getDestination() == destAirport:
        #             direct_flight = f"Direct Flight({flight.getFlightNumber()}): {origAirport.getCode()} to {destAirport.getCode()}"
        #         if direct_flight:
        #             return direct_flight



             for flight1 in flight_list:
                 if flight1.getOrigin() == origAirport or flight1.getDestination() == destAirport:
                     airport1.append(flight1)
        for i in airport1:
            if(i[0].getOrigin()== origAirport)
=======
        for flight_list in self._allFlights.values():
            for flight in flight_list:
                if flight.getOrigin() == origAirport and flight.getDestination() == destAirport:
                        return  f"Direct Flight({flight.getFlightNumber()}): {origAirport.getCode()} to {destAirport.getCode()}"

            #check for connecting flights
            xAirport = []
        for flight_list in self._allFlights.values():
            for flight1 in flight_list:
                if flight1.getOrigin() == origAirport or flight1.getDestination() == destAirport:
                    xAirport.append(flight1)
        for i in xAirport:
            if(i.getOrigin()==origAirport and i.getDestination()!=destAirport):
                for j in xAirport:

                print(i)
            print(i)
                    # print(flight1)
                    # for flight2 in flight_list:
                    #     if flight2.getDestination() == destAirport :
                    #         if flight2.getOrigin() == flight1.getDestination():
                    #            print(flight2)
                            # if flight1.getDestination() != origAirport and flight2.getOrigin() != destAirport and flight1.getDestination() != destAirport:
                            #     print(flight1.getDestination())
                                # xAirport.add(flight1.getDestination())



        # airport1 = []
        # airport2 = []
        # direct_flight = None
        # connecting_airports = set()
        # for flight_list in self._allFlights.values():
        # #     for flight in flight_list:
        # #         if flight.getOrigin() == origAirport and flight.getDestination() == destAirport:
        # #             direct_flight = f"Direct Flight({flight.getFlightNumber()}): {origAirport.getCode()} to {destAirport.getCode()}"
        # #         if direct_flight:
        # #             return direct_flight
        #
        #
        #
        #      for flight1 in flight_list:
        #          if flight1.getOrigin() == origAirport or flight1.getDestination() == destAirport:
        #              airport1.append(flight1)
        # for i in airport1:
        #     if(i[0].getOrigin()== origAirport)
>>>>>>> 9603c79 (fuck)
                     # for flight2 in flight_list:
                     #     print(flight2)
                         # if flight2.getDestination() == destAirport:
                         #     print(flight2)
                     # airport1.append(flight1)





        # print(airport1)

        # if airport1.getOrigin() == origAirport and airport1.getDestination() == airport2.getOrigin() and airport2.getDestination() == destAirport:
        #     print(airport1.getDescription())

            # for cFlights in flight_list:
            #     if cFlights.getOrigin() == origAirport or cFlights.getDestination() == destAirport:
            #         print(type(cFlights))
            #         for cFlights2 in flight_list:
            #            if cFlights2.getDestination() == destAirport and cFlights2.getOrigin() == cFlights.getDestination():
            #                 print(cFlights2)
                #         if cFlights2.getDestination() == destAirport and cFlights.getDestination() == cFlights2.getOrigin():
                #             print(cFlights)
                            # connecting_airports.add(cFlights.destAirport)



                # else:
                #     return -1








        # for flight_list in self._allFlights.values():
        #     for flight in flight_list:
        #         if flight.getOrigin() == origAirport and flight.getDestination() == destAirport:
        #             #        print(flight) #debug
        #             direct_flight = f"Direct Flight({flight.getFlightNumber()}): {origAirport.getCode()} to {destAirport.getCode()}"
        #             break
        #     if direct_flight:
        #         return direct_flight
        #               # elif flight.getDestination() == destAirport:
        #
        #         # print("shit", connecting_airports)
        #
        #     for cFlights in flight_list:
        #         if cFlights.getOrigin() == origAirport:
        #             for cFlights2 in flight_list:
        #                 if cFlights2.getDestination() == destAirport and cFlights.destAirport == cFlights2.origAirport:
        #                     print(self._allAirports.getAirportCode(cFlights.destAirport))
        #                     connecting_airports.add(self._allAirports.getAirportCode(cFlights.destAirport))
        #
        #
        #         return connecting_airports
        #             #

                # elif flight.getDestination() == destAirport:



                # break # if there is a direct flight break the loop

                #elif: if there is no direct flights check if there is a single hop connecting flight oriAirport to destAirport
            # for cFlights in flight_list:
            #     if cFlights.getOrigin() == origAirport:
            #         for cFlights2 in flight_list:
            #             if cFlights2.getDestination() == destAirport and cFlights.destAirport == cFlights2.origAirport:
            #                 connecting_airports.add(self._allAirports.get(cFlights.destAirport))
            #     return connecting_airports

                #
                # elif flight.getDestination() == destAirport:
                #     for connecting_flight in flight_list:


        # return -1





#idk where am i right now this shit is not working at all fuck

#     if flight.getOrigin() == origAirport and flight.getDestination() == destAirport:
#         print(flight)
#         return flight
#     else:
#         return -1
# print(self,origAirport,destAirport)#debug


# direct_flight = None #debug
# connecting_flights = set()

# for flight in self._allFlights():
#     # print(flight[0])#debug
#
#
# original working code
# if isinstance(origAirport, Airport) and isinstance(destAirport, Airport):
#       direct_flight = f"Direct Flight({self.getFlightNumber()}): {origAirport.getCode()} to {destAirport.getCode()}" debug
#       print("There is a direct flightt found") debug

#     orig_code = origAirport.getCode()
#     dest_code = destAirport.getCode()
#
#  #   for flight in self._allFlights.get(orig_code, []):
#  #    print(self._allFlights.get(orig_code),[])#debug
#     for flight in self._allFlights.get(orig_code):#debug
#         #print(flight)#debug
#         if flight.getDestination().getCode() == dest_code:
#             direct_flight = f"Direct Flight({flight.getFlightNumber()}): {orig_code} to {dest_code}"
#             # print("aviation.py",direct_flight)#debug
#             return direct_flight
#     # for flight1 in self._allFlights.get(orig_code, []):
#     for flight1 in self._allFlights.get(orig_code):#debug
#         connecting_code = flight1.getDestination().getCode()
#         if connecting_code != dest_code:
#             for flight2 in self._allFlights.get(connecting_code, []):
#                 if flight2.getDestination().getCode() == dest_code:
#                     connecting_flights.add(f"Connecting Flights({flight1.getFlightNumber()}, {flight2.getFlightNumber()}): {orig_code} to {connecting_code} to {dest_code}")
#
#                     if not connecting_flights:
#                         return "No flights found between these airports."
#                     else:
#                         return "\n".join(connecting_flights)
# #end of working code


def findAllFlightsByContinent(self, continent):
    flights = []
    for flight_list in self._allFlights.values():
        for flight in flight_list:
            if flight.getOrigin().getContinent() == continent or flight.getDestination().getContinent() == continent:
                flights.append(flight)
    return flights


def findShortestFlight(self):
    shortest_flight = None
    shortest_distance = float("inf")

    for flight_list in self._allFlights.values():
        for flight in flight_list:
            distance = flight.calculateDistance()
            if distance < shortest_distance:
                shortest_distance = distance
                shortest_flight = flight
    return shortest_flight


def findLongestFlight(self):
    longest_flight = None
    longest_distance = 0

    for flight_list in self._allFlights.values():
        for flight in flight_list:
            distance = flight.calculateDistance()
            if distance > longest_distance:
                longest_distance = distance
                longest_flight = flight
    return longest_flight


def printAllFlights(self):
    for flight_list in self._allFlights.values():
        for flight in flight_list:
            print(flight)
