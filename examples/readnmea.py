# avaa tiedosto
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
    print(row)

file.close()