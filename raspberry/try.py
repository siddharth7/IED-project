from pynmea import nmea
l='$GPGGA,121639.000,2832.7945,N,7716.3733,E,2,8,1.17,206.9,M,-36.1,M,0000,0000*7D'
if(l[1:6]=="GPGGA"):
    gpgga=nmea.GPGGA()
    gpgga.parse(l)
    l1=str(gpgga.latitude)[0:2]
    l2=str(gpgga.latitude)[2:]
    l2=float(l2)/60
    l3=str(gpgga.longitude)[0:2]
    l4=str(gpgga.longitude)[2:]
    l4=float(l3)/60
    print float(l1)+l2,float(l3)+l4