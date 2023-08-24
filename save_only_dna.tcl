mol load pdb NAME_pdb
set a [atomselect top "nucleic"]
$a writepdb NAME_pdb

exit
