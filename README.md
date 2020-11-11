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

Voit kerätä NMEA-dataa omalta GPS-vastaanottimeltasi ja tallentaa sen tiedostoon. Vaihtoehtoisesti voit kopioida NMEA-dataa esimerkkitiedostosta:
[nmeadata1.txt](https://github.com/SeAMKedu/Paikannustekniikat/blob/main/examples/nmeadata1.txt)






