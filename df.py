#for each shop

import csv
import math
import collections
import glob

l=0
list=collections.OrderedDict()
for n in range(16,17):
	shoplist=glob.glob("result/"+str(n)+"/*")
	for shop in shoplist:
		ifile=open(shop,"r")
		idata=csv.reader(ifile)
		for line in idata:
			if(line[0] in list):
				list[line[0]]=list[line[0]]+1
			else:
				lise[line[0]]=1
		outfile=open("df.csv","wb")
		writer=csv.writer(outfile)
		writer.writerow(["t","df"])
		for num in range(0,len(list)):
			writer.writerow([list.keys()[num],list.values()[num])
		l=l+1
		print l
		if(l>=5):
			break;
	print n
outfile.close()
ifile.close()
