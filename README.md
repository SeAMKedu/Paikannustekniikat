# Paikannustekniikat

## Harjoituksia koordinaattimuunnoksiin liittyen

### Harjoitus 1

Tee ohjelma, joka tulostaa paikallaan olevan GPS-vastaanottimen korkeuden kuvaajan näyttöön. Ohjelma laskee myös korkeuden keskiarvon sekä keskihajonnan.

Harjoituksessa on seuraavat vaiheet:
1. Kerää NMEA-muotoista dataa GPS-vastaanottimelta. Voit käyttää terminaaliohjelmaa tai sitten tehdä oman ohjelman, joka lukee tekstimuotoista dataa sarjaportista ja tallentaa sen tiedostoon.
2. Kerää NMEA-datasta $GPGGA-viestit ja etsi viestistä korkeus. Kerää GPS-ajat sekä korkeusdata listaan
3. Tulosta korkeusdata graafisessa muodossa (esim. numpy) ajan funktiona.
4. Laske korkeuden keskiarvo sekä keskihajonta.

#### NMEA-tiedosto

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
```
$GPGGA,082327.00,6247.32927,N,02249.35779,E,1,05,1.73,41.4,M,20.7,M,,*6C
```
$GPGGA-viestin sisältö on kuvattu sivulla [NMEA](https://www.trimble.com/OEM_ReceiverHelp/V4.44/en/NMEA-0183messages_GGA.html)

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
Muokkaa ohjelmaa siten, että se poimii vain $GPGGA-viestit.


