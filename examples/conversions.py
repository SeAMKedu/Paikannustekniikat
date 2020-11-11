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

def xyz2enu(x, y, z, latOrigin, longOrigin, altOrigin):

    cosLatOrigin = math.cos(latOrigin * math.pi / 180)
    sinLatOrigin = math.sin(latOrigin * math.pi / 180)

    cosLongOrigin = math.cos(longOrigin * math.pi / 180)
    sinLongOrigin = math.sin(longOrigin * math.pi / 180)

    cOrigin = 1 / math.sqrt(cosLatOrigin * cosLatOrigin + (1 - f) * (1 - f) * sinLatOrigin * sinLatOrigin)

    x0 = (R*cOrigin + altOrigin) * cosLatOrigin * cosLongOrigin
    y0 = (R*cOrigin + altOrigin) * cosLatOrigin * sinLongOrigin
    z0 = (R*cOrigin*(1-e2) + altOrigin) * sinLatOrigin

    xEast = (-(x-x0) * sinLongOrigin) + ((y-y0)*cosLongOrigin)

    yNorth = (-cosLongOrigin*sinLatOrigin*(x-x0)) - (sinLatOrigin*sinLongOrigin*(y-y0)) + (cosLatOrigin*(z-z0))

    zUp = (cosLatOrigin*cosLongOrigin*(x-x0)) + (cosLatOrigin*sinLongOrigin*(y-y0)) + (sinLatOrigin*(z-z0))

    return xEast, yNorth, zUp

def lla2enu(lat, lon, h, latOrigin, lonOrigin, altOrigin):
    x, y, z = gps_to_ecef(lat, lon, h)

    return ecef_to_enu(x, y, z, latOrigin, lonOrigin, hOrigin)
