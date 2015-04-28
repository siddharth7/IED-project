f2=open('finalpoints.txt','a')
f1=open("dump.txt")
while(1):
	for line in f1:
		if(line[1:6]=="GPGGA"):
			gpgga=nmea.GPGGA()
			gpgga.parse(line)
			l1=str(gpgga.latitude)
			l2=str(gpgga.longitude)
			print gpgga.latitude,gpgga.longitude
			break
	for line in f2:
		if(line[0]is near l1 or line[1] is near l2):
			move bot
