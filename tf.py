#for each shop

import csv
import math
import collections

sfile=open("NVshop.csv","r")
sdata=csv.reader(sfile)
slist=[]
sdata.next()
for line in sdata:
	slist.append(line[1])
print len(slist)


for shop in slist:
	ifile=open("NVshop"+shop+".csv","r")
	idata=csv.reader(ifile)
	outfile=open("NVshoptf/"+shop+".csv","wb")
	writer=csv.writer(outfile)
	writer.writerow(["t","n","sum","tf"])
	sum=0
	dword=collections.OrderedDict()
	for line in idata:
		te=line[2]
		text=te.split()
		for num in range(0,len(text)):
			if(text[num] in dword):
				dword[text[num]]=dword[text[num]]+1
			else:
				dword[text[num]]=1
		sum=sum+len(text)
	for num in range(0,len(dword)):
		writer.writerow([dword.keys()[num],dword.values()[num],sum,float(dword.values()[num])/sum])

sfile.close()
outfile.close()
ifile.close()
