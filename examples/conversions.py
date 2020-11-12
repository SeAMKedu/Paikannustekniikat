import math

R = 6378137
f = 1.0 / 298.257224
e2 = 1 - (1 - f) * (1 - f)

def lla2xyz(latitude, longitude, altitude):
    # lat, lon degrees
    # alt meters
    cosLat = math.cos(latitude * math.pi / 180)
    sinLat = math.sin(latitude * math.pi / 180)

    cosLong = math.cos(longitude * math.pi / 180)
    sinLong = math.sin(longitude * math.pi / 180)

    c = 1 / math.sqrt(cosLat * cosLat + (1 - f) * (1 - f) * sinLat * sinLat)
    s = (1 - f) * (1 - f) * c

    x = (R*c + altitude) * cosLat * cosLong
    y = (R*c + altitude) * cosLat * sinLong
    z = (R*s + altitude) * sinLat

    return x, y, z

def xyz2enu(deltax, deltay, deltaz, latOrigin, lonOrigin):

    cosLatOrigin = math.cos(latOrigin * math.pi / 180)
    sinLatOrigin = math.sin(latOrigin * math.pi / 180)

    cosLonOrigin = math.cos(lonOrigin * math.pi / 180)
    sinLonOrigin = math.sin(lonOrigin * math.pi / 180)

    east = (-deltax * sinLonOrigin) + (deltay*cosLonOrigin)

    north = (-cosLonOrigin*sinLatOrigin*deltax) - (sinLatOrigin*sinLonOrigin*deltay) + (cosLatOrigin*deltaz)

    up = (cosLatOrigin*cosLonOrigin*deltax) + (cosLatOrigin*sinLonOrigin*deltay) + (sinLatOrigin*deltaz)

    return east, north, up
