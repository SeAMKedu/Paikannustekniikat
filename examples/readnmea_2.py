import numpy as np
import matplotlib.pyplot as plt

# avaa tiedosto
file = open("nmeadata1.txt", "r")

# lista GPS-aikaa varten
gpstime = []
# lista korkeutta varten
heightdata = []

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

        print(latitude, longitude, height)

file.close()

# keskiarvo
average = np.mean(heightdata)
# keskihajonta
std = np.std(heightdata)
print("Average =", average, "Standard deviation =", std)

plt.plot(gpstime, heightdata)
plt.title("GPS-korkeus")
plt.xlabel("Aika [s]")
plt.ylabel("Korkeus [m]")
plt.show()