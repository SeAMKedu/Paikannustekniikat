import numpy as np
import matplotlib.pyplot as plt
import conversions

# avaa tiedosto
file = open("nmeadata1.txt", "r")

# lista GPS-aikaa varten
gpstime = []
# lista korkeutta varten
heightdata = []
# lista leveyspiiridataa varten
latitudedata = []
# lista pituuspiiridataa varten
longitudedata = []

for row in file:
    # poista rivinvaihto
    row = row.strip()
    # otetaan vain $GPGGA-viestit
    if row[:6] == "$GPGGA":
        # $GPGGA,082715.00,6247.33232,N,02249.35854,E,1,07,1.61,51.3,M,20.7,M,,*60
        # palastele rivi pilkkujen kohdalta
        pieces = row.split(',')
        # leveyspiiri
        latitude_degrees = int(pieces[2][:2]) # asteet
        latitude_minutes = float(pieces[2][2:10]) # minuutit ja minuuttien desimaalit
        latitude = latitude_degrees + latitude_minutes * 100.0 / 60.0 / 100.0
        if pieces[3] == 'S':
            latitude *= -1

        # pituuspiiri
        longitude_degrees = int(pieces[4][:3]) # asteet
        longitude_minutes = float(pieces[4][3:11]) # minuutit ja minuuttien desimaalit
        longitude = longitude_degrees + longitude_minutes * 100.0 / 60.0 / 100.0
        if pieces[5] == 'W':
            longitude *= -1

        # korkeus
        height = float(pieces[9])

        # lisää GPS-aika listaan
        gpstime.append(float(pieces[1]))
        # lisää korkeus listaan
        heightdata.append(height) 
        # lisää leveyspiiri listaan
        latitudedata.append(latitude)
        # lisää pituuspiiri listaan
        longitudedata.append(longitude)        

        print(latitude, longitude, height)

file.close()

# keskiarvot
originHeight = np.mean(heightdata)
originLat = np.mean(latitudedata)
originLon = np.mean(longitudedata)

# origon xyz-koordinaatit
originX, originY, originZ = conversions.lla2xyz(originLat, originLon, originHeight)

# listat east, north- ja up-komponentteja varten
eastlist = []
northlist = []
uplist =[]

# käydään lat-lon-alt-listat läpi ja muunnetaan paikalliseen tasokoordinaatistoon
for i in range(len(latitudedata)):
    # muunnos lat-lon-alt koordinaateista xyz-koordinaateiksi
    x, y, z = conversions.lla2xyz(latitudedata[i], longitudedata[i], heightdata[i])
    # muunnos paikalliseen tangenttitasoon (enu)
    # tehdään vektori origosta pisteeseen 
    deltax = x - originX
    deltay = y - originY
    deltaz = z - originZ

    # kierretään vektori origosta pisteeseen leveys- ja pituuspiirit kiertokulmina
    e, n, u = conversions.xyz2enu(deltax, deltay, deltaz, originLat, originLon)

    # lisätään lasketut koordinaatit listoihin
    eastlist.append(e)
    northlist.append(n)
    uplist.append(u)

# keskihajonta
std = np.std(heightdata)
print("Average =", originHeight, "Standard deviation =", std)

plt.plot(gpstime, heightdata)
plt.title("GPS-korkeus")
plt.xlabel("Aika [s]")
plt.ylabel("Korkeus [m]")
plt.show()

plt.plot(eastlist, northlist,"xb")
plt.title("Vaakakomponentit")
plt.xlabel("East [m]")
plt.ylabel("North [m]")
plt.show()