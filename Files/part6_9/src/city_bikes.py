import math

def get_station_data(filename: str) -> dict:
  stations = {}
  with open(filename, 'r') as file:
    next(file)
    for line in file:
      parts = line.strip().split(';')
      longitude = float(parts[0])
      latitude = float(parts[1])
      name = parts[3]
      stations[name] = (longitude, latitude)
  return stations

def distance(stations: dict, station1: str, station2: str):
  lon1, lat1 = stations[station1]
  lon2, lat2 = stations[station2]

  x_km = (lon1 - lon2) * 55.26
  y_km = (lat1 - lat2) * 111.2

  distance_km = math.sqrt(x_km**2 + y_km**2)

  return distance_km


def greatest_distance(stations: dict):
  max_distance = 0
  station1_name = None
  station2_name = None

  station_names = list(stations.keys())

  for i in range(len(station_names)):
    for j in range(i + 1, len(station_names)):
      station1 = station_names[i]
      station2 = station_names[j]
      dist = distance(stations, station1, station2)
      if dist > max_distance:
        max_distance = dist
        station1_name = station1
        station2_name = station2
  return station1_name, station2_name, max_distance

if __name__ == "__main__":
  stations = get_station_data('stations1.csv')
  d = distance(stations, "Designmuseo", "Hietalahdentori")
  print(d)
  d = distance(stations, "Viiskulma", "Kaivopuisto")
  print(d)

  station1, station2, greatest = greatest_distance(stations)
  print(station1, station2, greatest)