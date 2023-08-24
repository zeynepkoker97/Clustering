import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

RMSD_m = open('rmsd_matrix.dat','r')
RMSD_lines = RMSD_m.readlines()
groups = []
start = 0
finish = 0
names = []
for i in range(0,len(RMSD_lines)):
    group = []
    if "Model:" in RMSD_lines[i]:
        name = RMSD_lines[i].replace('\n','')
        names.append(name)
        start = i+1
    elif "---------------------------------" in RMSD_lines[i]:
        finish = i
    for j in range(start,finish):
        group.append(float(RMSD_lines[j]))
    if group:
        groups.append(group)
print(groups)
print(names)

RMSD_matrix_data = np.array(groups)
print(RMSD_matrix_data)

df = pd.DataFrame(RMSD_matrix_data, index=names, columns=names)


sns.heatmap(df, annot=True, fmt=".1f", linewidth=.5, vmin=0, vmax=5, cmap="coolwarm")


plt.savefig('RMSD_matrix', bbox_inches = 'tight')
plt.show()

