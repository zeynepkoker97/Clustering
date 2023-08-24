clustering_file = open('BNT_clustering.txt','r')
clustering_distribution_file = open('BNT_clustering_distribution.txt','r')

c_d_f = clustering_distribution_file.readlines()
frame = []
name = []

for i in range(1,len(c_d_f)):
    splitted_lines = c_d_f[i].split()
    save_frame = int(splitted_lines[5])+1
    frame.append(int(splitted_lines[5])+1)
    name_file = 'CTC_' + splitted_lines[4] + '_' + splitted_lines[5]
    name.append(name_file)
print(frame)
print(name)


