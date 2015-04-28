from pynmea import nmea
l1=0
l2=0
n=0
f=open('pt11.txt','r')
f2=open('finalpoints.txt','a')
for line in f:
	if(line[1:6]=="GPGGA"):
		gpgga=nmea.GPGGA()
		gpgga.parse(line)
		l1+=float(gpgga.latitude)
		l2+=float(gpgga.longitude)
		n+=1
		print gpgga.latitude,gpgga.longitude
l1=l1/n
l2=l2/n
print l1 ,l2
f2.write(str(l1))
f2.write(" ")
f2.write(str(l2))
f2.write("\n")
f2.close()
f.close()
