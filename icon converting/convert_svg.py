import os

INKSCAPE_EXE_PATH = "C:\Program Files\Inkscape\inkscape.exe"
GENERATED_DENSITIES = [1, 1.5, 2, 3, 4]

def main():
	input_file = "mySvg_32px"	# svg name
	size = 32.0					# Base icon size (square)
	cmd = '"' + INKSCAPE_EXE_PATH + '" -z -f %s.svg -w %d -j -e %s.png'
	
	for scale in GENERATED_DENSITIES:
		name = input_file + "@%sx"% ("%.1f" if type(scale)==float else "%d")  # "@%.1fx" or "@%dx"
		name = name % scale				#t_32@1x  t_32@1.5x t_32@2x etc
		name = name.replace(".", ",")  	# @1.5 -> @1,5
		os.system(cmd % (input_file, scale*size, name) )
	
main()