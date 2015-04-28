from pynmea import nmea
import subprocess
import os
os.chmod('script.sh',0o755)
subprocess.call("./script.sh")
s1=0
s2=0
n=0
l='$GPGGA,121841.000,2832.7914,N,07716.3732,E,2,8,1.16,206.5,M,-36.1,M,0000,0000*74'
f=open('input.txt','r')
f2=open('finalpoints.txt','a')
for line in f:
    if(l[1:6]=="GPGGA"):
        #gpgga=nmea.GPGGA()
	#gpgga.parse(l)
	#l1+=float(gpgga.latitude)
	#l2+=float(gpgga.longitude)
	#n+=1
	#print gpgga.latitude,gpgga.longitude
	gpgga=nmea.GPGGA()
        gpgga.parse(l)
        l1=str(gpgga.latitude)[0:2]
        l2=str(gpgga.latitude)[2:]
        l2=float(l2)/60
        l3=str(gpgga.longitude)[0:2]
        l4=str(gpgga.longitude)[2:]
        l4=float(l3)/60
	s1+=float(l1)+l2
	s2+=float(l3)+l4
        print float(l1)+l2,float(l3)+l4	
	n+=1
s1=s1/n
s2=s2/n
print s1,s2
f2.write(str(s1))
f2.write(" ")
f2.write(str(s2))
f2.write("\n")
f2.close()
f.close()