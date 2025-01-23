import math


earth_rad = 6371.0


def haversine(lat1, long1, lat2,long2): 
    diff_lat = (lat2-lat1) * math.pi / 180.0 #convert to radius
    diff_long= (long2-long1) * math.pi / 180.0 #convert to radius

    lat1 = lat1 * math.pi / 180.0 #convert to rad
    lat2 = lat2 * math.pi / 180.0 #convert to rad
    #apply haversine formula
    #inside square root 
    a = math.sin(diff_lat/2) * math.sin(diff_lat/2) + math.sin(diff_long/2) * math.sin(diff_long/2) * math.cos(lat1) * math.cos(lat2)
    c = 2 * earth_rad * math.asin(math.sqrt(a))
    return c

def least_distance(array1, array2) : 
    matches = [] 
    for loc1 in array1:
        min_distance = float('inf')
        closest_loc = None
        
        for loc2 in array2:
            distance = haversine(loc1[0], loc1[1], loc2[0], loc2[1])
            if distance < min_distance:
                min_distance = distance
                closest_loc = loc2
        
        matches.append((loc1, closest_loc))
    
    return matches

# Example arrays of geo locations
array1 = [
    (34.052235, -118.243683),  # Los Angeles
    (40.712776, -74.005974),   # New York
    (37.774929, -122.419418)   # San Francisco
]

array2 = [
    (51.507351, -0.127758),    # London
    (48.856613, 2.352222),     # Paris
    (35.689487, 139.691711)    # Tokyo
]

# Call the function with example arrays
matches = least_distance(array1, array2)
for match in matches:
    print(f"Point {match[0]} is closest to {match[1]}")