from pynmea import nmea
l='$GPGGA,113650.000,2832.8220,N,07716.4021,E,2,5,1.72,239.2,M,-36.1,M,0000,0000*7E'

if(l[1:6]=="GPGGA"):
        gpgga=nmea.GPGGA()
        gpgga.parse(l)
        l1=str(gpgga.latitude)[0:2]
        l2=str(gpgga.latitude)[2:]
        l2=float(l2)/float(60)
        l3=str(gpgga.longitude)[1:3]
        print l3
        l4=str(gpgga.longitude)[3:]
        print l4
        l4=float(l4)/float(60)
        print float(l1)+l2,float(l3)+l4