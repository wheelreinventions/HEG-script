import shutil
from os import listdir
from os import system
from os import environ
from os import chdir
from os import sep
from os.path import isfile, isdir, join
import subprocess
from  time import sleep

heg_dir = 'D:/Develop/HEG/'

image_back_slash_dir = 'D:\\Develop\\HEG\\'
image_dir = image_back_slash_dir.replace(sep, '/')

current_dir = '5000003320310'
heg_username = 'developer'

in_dir_back_slash = image_back_slash_dir + current_dir +'\\'
in_dir = in_dir_back_slash.replace(sep, '/')

out_dir_back_slash = image_back_slash_dir + current_dir + '_HEG\\'
out_dir = out_dir_back_slash.replace(sep, '/')

files = [f for f in listdir(in_dir) if isfile(join(in_dir, f))]

try:
    environ.pop('PYTHONIOENCODING')
except KeyError:
    pass

for file in files :

	#calling the HEG command
	#D:\Develop\HEG\HEGtools\HEG_Win\bin\hegtool.exe -h D:\Develop\HEG\5000003320310\VNP10A1.A2021001.h08v06.001.2021002082927.h5
	
	fileandpath = join(in_dir, file)
	chdir(heg_dir + 'HEGtools/HEG_Win/bin/')
	print('hegtool -h ' + fileandpath)	
	subprocess.call('hegtool -h ' + fileandpath)

	heghdr = heg_dir + 'HEGtools/HEG_Win/bin/HegHdr.hdr'
	fin = open(heghdr, "r")
	hegprm = heg_dir + 'HEGtools/HEG_Win/bin/HegPrm.prm_' + heg_username
	fout = open(hegprm, "r")

	lin = fin.readlines()
	fin.close()
	lout = fout.readlines()
	fout.close()

	#reading the data from source file
	ul_latlon, lr_latlon, pixelsize = '', '', ''
	for i in lin:
		if 'GRID_UL_CORNER_LATLON' in i:
			ul_latlon = i.strip('GRID_UL_CORNER_LATLON').strip('=').strip('\n')
		if 'GRID_LR_CORNER_LATLON' in i:
			lr_latlon = i.strip('GRID_LR_CORNER_LATLON').strip('=').strip('\n')
		if 'GRID_PIXEL_SIZE=' in i:
			pixelsize = i.strip('GRID_PIXEL_SIZE').strip('=').strip('\n')
		
	#updating the data in parameter file
	c = 0
	for i in lout:
		if 'INPUT_FILENAME' in i:
			t = 'INPUT_FILENAME = ' + in_dir_back_slash  + file + '\n'
			Replacement = i.replace(i, t)
			lout[c] = Replacement
			print(t)
		if 'SPATIAL_SUBSET_UL_CORNER' in i:
			t = 'SPATIAL_SUBSET_UL_CORNER = ( ' + ul_latlon + ')' + '\n'
			Replacement = i.replace(i, t)
			lout[c] = Replacement
			print(t)
		if "SPATIAL_SUBSET_LR_CORNER" in i:
			t = 'SPATIAL_SUBSET_LR_CORNER = ( ' + lr_latlon + ')' + '\n'
			Replacement = i.replace(i, t)
			lout[c] = Replacement
			print(t)
		if 'OUTPUT_PIXEL_SIZE' in i:
			t = 'OUTPUT_PIXEL_SIZE = ' + pixelsize + '\n'
			Replacement = i.replace(i, t)
			lout[c] = Replacement
			print(t)
		if 'OUTPUT_FILENAME' in i:
			t = 'OUTPUT_FILENAME = ' + out_dir_back_slash + file[:-3] + '.tif' + '\n'
			Replacement = i.replace(i, t)
			lout[c] = Replacement
			print(t)

		c += 1
	

	# the pre existing text in the parameter file is erased
	fout = open(hegprm, "r+", newline='\n')
	fout.truncate(0)
	
	# the modified list is written into
	# the file thereby replacing the previous parameter file
	fout.writelines(lout)
	fout.close()

	#calling the HEG command
	#resample -p D:/Develop/HEG/HEGtools/HEG_Win/bin/HegPrm.prm_developer
	fileandpath = join(in_dir, file)
	chdir(heg_dir + 'HEGtools/HEG_Win/bin/')
	print('resample -p ' + hegprm)
	subprocess.call('resample -p ' + hegprm)
