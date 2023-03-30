class Flight:
    def __init__(self, flightNo, origin, destination):
        self.flightNo = flightNo
        self.origin = origin
        self.destination = destination


class Flight:
    def __init__(self, flightNo, origin, destination):
        self.flightNo = flightNo
        self.origin = origin
        self.destination = destination


def findFlightBetween(orig_airport, dest_airport, flights):
    # Check for direct flight
    for flight in flights:
        if flight.origin == orig_airport and flight.destination == dest_airport:
            return f"Direct Flight({flight.flightNo}): {orig_airport} to {dest_airport}"

    # Check for single-hop connecting flight
    intermediate_airports = []
    for flight1 in flights:
        if flight1.origin == orig_airport:
            for flight2 in flights:
                if flight2.destination == dest_airport and flight1.destination == flight2.origin:
                    if flight1.destination != orig_airport and flight2.origin != dest_airport and flight1.destination != dest_airport:
                        intermediate_airports.append(flight1.destination)
                        # print(flight1.destination)

    if intermediate_airports:
        return intermediate_airports

    # No direct or single-hop connecting flight found
    return -1





# Create some Flight objects
flights = [
    Flight("ABC123", "YYZ", "ORD"),
    Flight("GHI789", "ORD", "LAX"),
    Flight("JKL012", "YYZ", "MAX"),
    Flight("MNO345", "SFO", "LAX"),

]

# Test findFlightBetween function
print(findFlightBetween("YYZ", "ORD", flights))  # Output: Direct Flight(ABC123): YYZ to ORD
print(findFlightBetween("YYZ", "LAX", flights))  # Output: {'ORD'}
print(findFlightBetween("YYZ", "SFO", flights))  # Output: {'LAX'}
print(findFlightBetween("ORD", "SFO", flights))  # Output: -1
