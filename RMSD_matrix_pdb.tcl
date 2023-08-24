set outfile [open rmsd_matrix_pdb.dat w]; 
set np [molinfo num]
puts $np

puts "Number of Structure: $np"

for {set i 0 } {$i <= $np -1 } { incr i } {
	set ref [atomselect ${i} "nucleic"]
	puts $outfile "Cluster: $i"
	for {set j 0 } {$j <= $np -1 } { incr j } {
		set sel [atomselect ${j} "nucleic"]
		$sel move [measure fit $sel $ref]
    	puts $outfile "[expr {double(round(10000*[measure rmsd $sel $ref]))/10000}]"
	}
	puts $outfile "---------------------------------"
}
close $outfile
