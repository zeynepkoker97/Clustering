
set np [molinfo num]
puts $np

puts "Number of Structure: $np"

for {set i 0 } {$i <= $np -1 } { incr i } {
	set ref [atomselect 0 "nucleic"]
	set sel [atomselect ${i} "nucleic"]
	$sel move [measure fit $sel $ref]
	mol modcolor 0 $i colorid $i
	if { $i >= 8 } {
	set new  [ expr ( ${i} + 1 ) ]
		mol modcolor 0 $i colorid $new
		puts $new
	}
}

