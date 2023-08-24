import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import ListedColormap
from matplotlib.patches import Rectangle
import re

#INPUTS:
#number_of_cluster = int(input("Please Enter Number of Cluster:"))
#number_of_frame = int(input("Please Enter Number of Frame:"))
#number_of_divided_time = int(input("Please Enter Time Range in Graph:"))

#You can use these parameters for clustering_10_1.75.vmd
#number_of_cluster = 10
#number_of_frame = 25000
#number_of_divided_time = 5000

#You can use these parameters for clustering_5_1.75.vmd
number_of_cluster = 10
number_of_frame = 25000
number_of_divided_time = 5000

infile = open('clustering.vmd','r')
data=infile.read()
xile=re.findall('mol drawframes top (.*?)\nmol clipplane center 0',data,re.DOTALL)
outfile = open("BNT_clustering.txt", "w")
outfile2 = open("BNT_clustering_distribution.txt", "w")
outfile2.write("BNT" + '\n')

clustering_split_array = []
clustering_name = []

for i in range(0,number_of_cluster):
    xile[i]=xile[i][2:]
    xile[i]="".join(xile[i]).replace(' {','')
    xile[i]="".join(xile[i]).replace('{','')
    xile[i]="".join(xile[i]).replace('}','')
    string_list = xile[i].split()
    clustering_split_array.append(string_list)
    clustering_name.append("Cluster " + str(i+1))
    outfile.write("Cluster:" + str(i+1) + '\t' + xile[i] + '\n')
    outfile2.write("Center of Top Cluster:" + '\t' + str(i+1) + '\t' + string_list[0] + '\t' + "# of Cluster:" + str(i+1) + '\t' + str(len(string_list)) + '\n' )
    if i == number_of_cluster-1:
        i = i +1
        xile[i]=xile[i][2:]
        xile[i]="".join(xile[i]).replace(' {','')
        xile[i]="".join(xile[i]).replace('{','')
        xile[i]="".join(xile[i]).replace('}','')
        string_list = xile[i].split()
        clustering_split_array.append(string_list)
        clustering_name.append("Unclustered")
        outfile.write("Unclustered:" + '\t' + xile[i] + '\n')
        outfile2.write("                     " + '\t' + '\t' + '\t' + "# of Unclustered:" + '\t' + str(len(string_list)) + '\n' )

outfile.close()
outfile2.close()
infile.close()

time_ticks = []
time_label = []
count = 0

for time in range(0,number_of_frame+number_of_divided_time,number_of_divided_time):
    time_ticks.append(time)
    time_label.append(str(count))
    count = count + 10

centers = []
clustering = []
distru = []
percentage_matrix = []
num_cluster = []
divided_cluster = np.zeros((len(clustering_split_array), number_of_frame))

for cluster in range(0,len(clustering_split_array)):
    num_cluster.append(cluster+0.5)
    centers.append(int(clustering_split_array[cluster][0]))
    percentage = format(float(len(clustering_split_array[cluster]))/number_of_frame*100, '.2f')
    percentage_matrix.append(percentage)
    clustering.append(clustering_name[cluster])
    distru.append(float(len(clustering_split_array[cluster]))/number_of_frame*100)
    for each_frame in range(0,len(clustering_split_array[cluster])):
        divided_cluster[cluster][int(clustering_split_array[cluster][each_frame])] = cluster + 1

coloring = ['None','blue', 'red', 'gray', 'orange', 'yellow', 'tan', 'silver', 'green','pink', 'cyan', 'purple']
newcmp = ListedColormap(coloring[:len(clustering)+1], name ='clustering')

plt.figure(figsize=(20,10))
ax = sns.heatmap(divided_cluster, cmap=newcmp, cbar=False)
plt.xlabel('time (ns)', fontsize=20)
plt.xticks(time_ticks, time_label, rotation=0,fontsize='20')
plt.yticks(num_cluster, clustering_name, rotation=0, family = "monospace", fontsize='20', ha='right', va='center')

for k in range(0,len(centers)-1):
    ax.add_patch(Rectangle((centers[k]-25, divided_cluster[k][centers[k]]-1), 50, 1, fill='No', ec ='black', fc='None', lw =1.5) )

plt.savefig('clustering_heatmap_graphs.png')
#plt.savefig('clustering_heatmap_graphs.png', bbox_inches = 'tight', dpi=500, transparent='True')

fig = plt.figure(figsize=(20,20))
ax = fig.add_axes([0,0,1,1])
plt.axis('off')
for i in range(0, len(clustering)):
    ax.bar(clustering[i],distru[i], color=coloring[i+1])
    rects = ax.patches
    labels = ["%" + percentage_matrix[i] for i in range(len(rects))]
for rect, percentage_matrix in zip(rects, labels):
    height = rect.get_height()
    ax.text(
        rect.get_x() + rect.get_width() / 2, height + 0.5, percentage_matrix, ha="center", va="bottom",fontsize='40', rotation = 90, weight="bold"
    )

plt.savefig('clustering_bar_plot.png', bbox_inches = 'tight')
#plt.savefig('clustering_bar_plot.png', bbox_inches = 'tight', pad_inches = 0, dpi=500, transparent='True')
