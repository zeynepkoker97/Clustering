#!/bin/bash

#After clustering save clustering_1.75.vmd

python read_clustering.py

OUTPUT=($(python save_ctc_pdb.py attr attr attr | tr -d '[],'))
declare -a FRAME
declare -a NAME
declare -a NAME_pdb

for i in ${OUTPUT[@]};
do
	echo $i
	if [[ "$i" =~ ^[0-9]+$ ]]
	then
		FRAME+=("$i")
	else
		eval i=$i
		NAME+=("$i")
		NAME_pdb+=("$i.pdb")
	fi
done
# echo ${FRAME[0]} ${NAME[0]}
# echo ${FRAME[1]} ${NAME[1]}
# echo ${FRAME[2]} ${NAME[2]}
# echo ${FRAME[3]} ${NAME[3]}
# echo ${FRAME[4]} ${NAME[4]}
# echo ${FRAME[5]} ${NAME[5]}
# echo ${FRAME[6]} ${NAME[6]}
# echo ${FRAME[7]} ${NAME[7]}
# echo ${FRAME[8]} ${NAME[8]}
# echo ${FRAME[9]} ${NAME[9]}
# echo ${FRAME[10]} ${NAME[10]}

echo "CHECK THE CTC numbers and names!!!!!"

before=1

len=${#NAME[@]}

for (( j=0; j<$len; j++ ));
do
	echo $j
	cp save_ctc.ptraj save_ctc_temp.ptraj
	sed -i 's/FRAME/'${FRAME[j]}'/g' save_ctc_temp.ptraj
	sed -i 's/NAME/'${NAME[j]}'/g' save_ctc_temp.ptraj
	cpptraj -p system_water.prmtop -i save_ctc_temp.ptraj
	
	cp save_only_dna.tcl save_only_dna_temp.tcl
	sed -i 's/NAME_pdb/'${NAME_pdb[j]}'/g' save_only_dna_temp.tcl
	vmd -dispdev text -e save_only_dna_temp.tcl
	file_name="${NAME_pdb[j]}"
	sed -i 's/END/'TER'/g' $file_name
	after=$(($before+1))
	echo -e "MODEL        ${before}                                                                  " >> clusters_as_frame_${before}.pdb
	cat  clusters_as_frame_${before}.pdb ${file_name} > clusters_as_frame_${after}.pdb
	rm clusters_as_frame_${before}.pdb
	before=$(($before+1))
	echo -e "ENDMDL                                                                          " >> clusters_as_frame_${after}.pdb
done

cp clusters_as_frame_${after}.pdb clusters_as_frame.pdb

rm save_ctc_temp.ptraj
rm save_only_dna_temp.tcl
rm clusters_as_frame_${after}.pdb

#vmd -dispdev text -pdb clusters_as_frame.pdb -e rmsd_matrix_data.tcl

vmd -pdb clusters_as_frame.pdb -e rmsd_matrix_data.tcl

#vmd clusters_as_frame.pdb

vmd -m ${NAME_pdb[@]}



