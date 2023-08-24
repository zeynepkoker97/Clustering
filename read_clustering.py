import re
infile = open('clustering_1.75.vmd','r')
data=infile.read()
xile=re.findall('mol drawframes top (.*?)\nmol clipplane center 0',data,re.DOTALL)
outfile = open("BNT_clustering.txt", "w")
outfile2 = open("BNT_clustering_distribution.txt", "w")
outfile2.write("BNT" + '\n')
for i in range(11):
	X = []
	if i <= 11:
		xile[i]=xile[i][1:]
	xile[i]=xile[i][2:]
	xile[i]="".join(xile[i]).replace(' {','')
	xile[i]="".join(xile[i]).replace('{','')
	xile[i]="".join(xile[i]).replace('}','')
	string_list = xile[i].split()
	outfile.write("Cluster:" + str(i) + '\t' + xile[i] + '\n')
	outfile2.write("Center of Top Cluster:" + '\t' + str(i) + '\t' + string_list[0] + '\t' + "# of Cluster:" + str(i) + '\t' + str(len(string_list)) + '\n' )

outfile.close()
outfile2.close()
infile.close()


