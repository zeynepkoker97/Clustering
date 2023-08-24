set outfile [open rmsd_matrix.dat w];                                             
set nf [molinfo top get numframes]
puts $nf
set sel [atomselect top "all"]
set i 0
set j 0
puts $outfile "Number of Frames: $nf"
# rmsd calculation loop
for {set i 0 } {$i <= $nf -1 } { incr i } {
	set ref [atomselect top "all" frame $i]
	puts $outfile "Model: $i"
	for {set j 0 } {$j <= $nf -1 } { incr j } {
		$sel frame $j
    	$sel move [measure fit $sel $ref]
    	puts $outfile "[expr {double(round(10000*[measure rmsd $sel $ref]))/10000}]"
	}
	puts $outfile "---------------------------------"
}
close $outfile

