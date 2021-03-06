
# NMEA-muotoisen datan käsittely Python-ohjelmointikielellä

GNSS-vastaanottimet tuottavat paikannukseen liittyvää tietoa NMEA-muodossa. Tällä sivulla kaksi Python-ohjelmointikielellä tehtyä esimerkkiä, joissa käsitellään NMEA-datassa olevaa paikkatietoa. Samalla näytetään, miten paikkakoordinaatit voidaan tulostaa graafisessa muodossa käyttäen matplotlib.pyplot-kirjastoa. Ensimmäisessä esimerkissä luetaan paikkakoordinaatit NMEA:n GGA-viestistä ja tulostetaan korkeus. Toisessa esimerkissä muunnetaan maantieteelliset koordinaatit paikalliseen tasokoordinaatistoon ja tulostetaan vaakasuuntaiset komponentit graafisessa muodossa.

### Harjoitus 1

Tee ohjelma, joka tulostaa paikallaan olevan GPS-vastaanottimen korkeuden kuvaajan näytölle graafisessa muodossa. Ohjelma laskee myös korkeuden keskiarvon sekä keskihajonnan.

Harjoituksessa on seuraavat vaiheet:
1. Kerää NMEA-muotoista dataa GPS-vastaanottimelta. Voit käyttää terminaaliohjelmaa tai sitten tehdä oman ohjelman, joka lukee tekstimuotoista dataa sarjaportista ja tallentaa sen tiedostoon.
2. Kerää NMEA-datasta $GPGGA-viestit ja etsi viestistä korkeus. Kerää GPS-ajat sekä korkeusdata listaan
3. Tulosta korkeusdata graafisessa muodossa (esim. numpy) ajan funktiona.
4. Laske korkeuden keskiarvo sekä keskihajonta.

#### NMEA-tiedoston lukeminen

GPS-vastaanottimet tuottavat dataa NMEA-muodossa. 

Alla on esimerkki GPS-vastaanottimen tuottamasta NMEA-datasta.

```
$GPGGA,082327.00,6247.32927,N,02249.35779,E,1,05,1.73,41.4,M,20.7,M,,*6C
$GPGSA,A,3,32,31,12,21,22,,,,,,,,2.85,1.73,2.27*0C
$GPGSV,2,1,05,12,14,008,53,21,28,158,38,22,77,159,35,31,30,099,44*73
$GPGSV,2,2,05,32,25,056,50*4C
$GPGLL,6247.32927,N,02249.35779,E,082327.00,A,A*6D
$GPZDA,082327.00,11,11,2020,00,00*6A
$GPRMC,082328.00,A,6247.32943,N,02249.35805,E,0.005,,111120,,,A*7A
$GPVTG,,T,,M,0.005,N,0.009,K,A*2F
```
Meitä kiinnostaa nyt eniten $GPGGA-viesti, jossa on muun muassa GPS-vastaanottimen laskema aika, pituuspiiri, leveyspiiri ja korkeus.
(Uudemmissa GNSS-vastaanottimissa vastaava data on $GNGGA-viestissä.)
```
$GPGGA,082327.00,6247.32927,N,02249.35779,E,1,05,1.73,41.4,M,20.7,M,,*6C
```
$GPGGA-viestin sisältö on kuvattu [täällä](https://www.trimble.com/OEM_ReceiverHelp/V4.44/en/NMEA-0183messages_GGA.html)

Voit kerätä NMEA-dataa omalta GPS-vastaanottimeltasi ja tallentaa sen tiedostoon. Voit käyttää terminaaliohjelmaa tai sitten tehdä oman ohjelman, joka lukee tekstimuotoista dataa sarjaportista ja tallentaa sen tiedostoon.

Vaihtoehtoisesti voit kopioida NMEA-dataa esimerkkitiedostosta:
[nmeadata1.txt](/examples/nmeadata1.txt).

Tallenna tiedosto hakemistoosi. Aloita tekemällä Python-ohjelma, joka lukee tiedoston rivi riviltä.

```python
# avaa tiedosto
file = open("nmeadata1.txt", "r")

for row in file:
    # poista rivinvaihto
    row = row.strip()
    # tulosta rivi
    print(row)
file.close()
```
Muokkaa ohjelmaa siten, että se poimii vain $GPGGA-viestit. Palastele $GPGGA-viesti pilkkujen kohdalta merkkijonotaulukon alkioiksi.

```python
file = open("nmeadata1.txt", "r")

for row in file:
    # poista rivinvaihto
    row = row.strip()
    # otetaan vain $GPGGA-viestit
    if row[:6] == "$GPGGA":
        # $GPGGA,082715.00,6247.33232,N,02249.35854,E,1,07,1.61,51.3,M,20.7,M,,*60
        # palastele rivi pilkkujen kohdalta
        pieces = row.split(',')
        # tulosta merkkijonotaulukon sisältö
        for i in range(len(pieces)):
            print(i, pieces[i])
    print()

file.close()
```
#### Leveyspiiri, pituuspiiri ja korkeus

Esimerkkikoodissa on tulostettu $GPGGA-viestin sisältö alkioittain. Tulostuksesta nähdään, että leveyspiiri on kohdassa 2, pituuspiiri kohdassa 4 ja korkeus kohdassa 9. Leveyspiirin ja pistuuspiirin etumerkit ovat kohdissa 3 ja 5 (N on plus, S on miinus, E on plus ja W on miinus). Järjestysnumero vastaa taulukon pieces indeksiä. 

Huomaa, että leveyspiirissä kaksi ensimmäistä numeroa on asteet ja kaksi seuraavaa numeroa on minuutit. Pisteen jälkeen tulevat minuuttien desimaalit. Pituuspiiri on muuten samanlainen, mutta asteita varten on varattu kolme merkkiä.

Muuta ohjelmaa seuraavaksi siten, että se muuntaa leveyspiirin ja pituuspiirin numeroiksi siten, että kokonaisosassa on asteet ja desimaaliosassa on asteiden desimaalit. Minuutit ja niiden osat pitää siis muuntaa asteen sadasosiksi. Muunna myös korkeus numeroksi. 

Tulosta leveyspiiri, pituuspiiri ja korkeus. Voit jättää edellisessä vaiheessa olleen merkkijonotaulukon sisällön tulostuksen pois.

```python
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

        print(latitude, longitude, height)
```

Valmis ohjelma löytyy tiedostosta [readnmea_1.py](/examples/readnmea_1.py)

#### Korkeusdatan tulostaminen graafisessa muodossa

Tulostetaan seuraavaksi korkeusdata ajan funktiona graafisessa muodossa. Kerätään GPS-ajat ja korkeudet listaan ja tulostetaan data käyttäen matplotlib.pyplot-kirjastoa.

Asenna ensin numpy- ja matplotlib-kirjastot pip:llä.
```
pip install numpy
pip install matplotlib
```
Lisää edellisessä harjoituksessa tehdyn ohjelman alkuun seuraavat rivit:
```python
import numpy as np
import matplotlib.pyplot as plt
```
Esittele listat GPS-aikoja ja korkeutta varten
```python
# avaa tiedosto
file = open("nmeadata1.txt", "r")

# lista GPS-aikaa varten
gpstime = []
# lista korkeutta varten
heightdata = []
```
Lisää GPS-ajat ja lasketut korkeudet listoihin:
```python
        # korkeus
        height = float(pieces[9])

        # lisää GPS-aika listaan
        gpstime.append(float(pieces[1]))
        # lisää korkeus listaan
        heightdata.append(height)

        print(latitude, longitude, height)
```
Laske ohjelman lopussa vielä korkeuden keskiarvo ja keskihajonta numpy-kirjaston avulla.
```python
# keskiarvo
average = np.mean(heightdata)
# keskihajonta
std = np.std(heightdata)
print("Average =", average, "Standard deviation =", std)
```
Tulosta korkeus ajan funktiona graafisessa muodossa.
```python
plt.plot(gpstime, heightdata)
plt.title("GPS-korkeus")
plt.xlabel("Aika [s]")
plt.ylabel("Korkeus [m]")
plt.show()
```
Graafinen tulostus näyttää tältä:

![](/images/Korkeusplot.PNG)

### Harjoitus 2

Jatka edellistä ohjelmaa siten, että se piirtää näytölle graafisessa muodossa GPS-vastaanottimen laskemien paikkojen vaakakomponentit. Mitatut pisteet halutaan näyttää tasokoordinaatistossa, jonko origo on mitattujen pisteiden keskiarvo. Tässä paikalliseen tangenttitasoon asetetussa koordinaatistossa X-akseli osoittaa itään ja Y-akseli pohjoiseen. Z-akseli osoittaa ylöspäin tasosta katsojaa kohti.

NMEA-tiedostossa olevat maantieteelliset koordinaatit (lat, lon, alt) muunnetaan ensin maakeskisiksi suorakulmaisiksi koordinaateiksi (X, Y, Z). Tämän jälkeen lasketaan X-, Y-, ja Z-koordinaattien keskiarvo, josta tulee tasokoordinaatiston origo. Seuraavaksi muodostetaan erotusvektorit vähentämällä kunkin pisteen XYZ-koordinaateista origon XYZ-koordinaatit. Koordinaattimuunnos paikalliseen tangenttitasoon tapahtuu tekemällä koordinaatiston kierrot pituuspiirin ja leveyspiirin mukaan. 

Tarvittavat koordinaattimuunnokset löytyvät tiedostossa [conversions.py](/examples/conversions.py)

Funktio lla2xyz muuntaa maantieteelliset koordinaatit (lat, lon alt) suorakulmaisiksi maakeskisiksi koordinaateiksi (X, Y, Z). Funktio xyz2enu muuntaa suorakulmaiset maakeskiset koordinaatit (x, y, z) tasokoordinaatistoon (east, north, up). Tasokoordinaatiston origo maakeskisessä koordinaatisossa annetaan funktiolle paramterina.

#### Ohjeet

Ota pohjaksi edellinen harjoitus. Lisää ohjelman alkuun listat pituuspiiri- ja leveyspiiridataa varten.

```python
# lista GPS-aikaa varten
gpstime = []
# lista korkeutta varten
heightdata = []
# lista leveyspiiridataa varten
latitudedata = []
# lista pituuspiiridataa varten
longitudedata = []
```
Lisää seuraavaksi NMEA-datasta otetut pituuspiirit ja leveyspiirit listoihin.

```python
        # lisää GPS-aika listaan
        gpstime.append(float(pieces[1]))
        # lisää korkeus listaan
        heightdata.append(height) 
        # lisää leveyspiiri listaan
        latitudedata.append(latitude)
        # lisää pituuspiiri listaan
        longitudedata.append(longitude)   
```
Laske ohjelman lopussa pituuspiirien ja leveyspiirien keskiarvo. Tästä tulee paikallisen tasokoordinaatiston origo.

```python
file.close()

# keskiarvot
originHeight = np.mean(heightdata)
originLat = np.mean(latitudedata)
originLon = np.mean(longitudedata)
```
Muunna seuraavaksi origon maantieteelliset koordinaatit xyz-koordinaatistoon.
```python
# origon xyz-koordinaatit
originX, originY, originZ = conversions.lla2xyz(originLat, originLon, originHeight)
```
Tee listat east-, north- ja up-koordinaatteja varten.
```python
eastlist = []
northlist = []
uplist =[]
```
Käy listoissa olevat lat-, lon-, alt-koordinaatistossa olevat pisteet läpi. Muunna kukin piste ensin xyz-koordinaatistoon. Laske sitten vektori xyz-koordinaatistossa origon ja pisteen välillä. Kierrä tämä vektori käyttäen kiertokulmina leveys- ja pituuspiirejä. Lisää lasketut east-, north- ja up-koordinaatit listoihin. 
```python
# käydään lat-lon-alt-listat läpi ja muunnetaan paikalliseen tasokoordinaatistoon
for i in range(len(heightdata)):
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
```
Tulosta ohjelman lopussa GPS-vastaanottimen mittaamat pisteet paikalliseen tangenttitasoon muunnettuna.
```python
plt.plot(eastlist, northlist,"xb")
plt.title("Vaakakomponentit")
plt.xlabel("East [m]")
plt.ylabel("North [m]")
plt.show()
```
Tulostus näyttää tältä.

![](/images/Vaakaplot.png)

### Harjoitus 3

Ensimmäisessä harjoituksessa kerättiin korkeusdataa listaan. Toisessa harjoituksessa muunnettiin lat-lon-alt-data paikalliseen tasokoordinaatistoon (enu). Muunnoksessa syntyi myös pisteiden up-komponentit, jotka kerättiin myös listaan. Alkuperäisen korkeusdatan ja tasokoordinaatiston up-datojen kuvittelisi olevan samoja, mutta ne eivät ole. Mistä ero johtuu?



