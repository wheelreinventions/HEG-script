import shutil
from os import listdir
from os import system
from os import environ
from os import chdir
from os.path import isfile, isdir, join
import subprocess
from  time import sleep

heg_dir = 'D:/Develop/HEG/'
image_dir = heg_dir
heg_reverse_slash_dir = 'D:\\Develop\\HEG\\'

in_dir = image_dir + '5000003320310/'
in_dir_reverse_slash = heg_reverse_slash_dir + '5000003320310\\'
out_dir = image_dir + '5000003320310_HEG/'
out_dir_reverse_slash = heg_reverse_slash_dir + '5000003320310_HEG\\'
files = [f for f in listdir(in_dir) if isfile(join(in_dir, f))]

try:
    environ.pop('PYTHONIOENCODING')
except KeyError:
    pass

for file in files :

	#D:\Develop\HEG\HEGtools\HEG_Win\bin\hegtool.exe -h D:\Develop\HEG\VNP10A1.A2021001.h08v06.001.2021002082927.h5
	#D:\Develop\HEG\HEGtools\HEG_Win\bin\hegtool.exe -h D:\Develop\HEG\5000003320310\VNP10A1.A2021001.h08v06.001.2021002082927.h5
	fileandpath = join(in_dir, file)
	#print(heg_dir + 'HEGtools/HEG_Win/bin/hegtool.exe -h ' + fileandpath)
	#subprocess.run(["D:/Develop/HEGtools/HEG_Win/bin/hegtool.exe", "-h " + join(in_dir, file)], check=True)
	#subprocess.call('d:')
	#print('cd ' + heg_dir + 'HEGtools/HEG_Win/bin/')
	#subprocess.call('cd ' + heg_dir + 'HEGtools/HEG_Win/bin/')
	chdir(heg_dir + 'HEGtools/HEG_Win/bin/')
	print('hegtool -h ' + fileandpath)
	subprocess.call('hegtool -h ' + fileandpath)

	# file.txt should be replaced with
	# the actual text file name

	#sleep(5)
	heghdr = heg_dir + 'HEGtools/HEG_Win/bin/HegHdr.hdr'
	fin = open(heghdr, "r")
	hegprm = heg_dir + 'HEGtools/HEG_Win/bin/HegPrm.prm_developer'
	fout = open(hegprm, "r")
	# each sentence becomes an element in the list l
	lin = fin.readlines()
	fin.close()
	lout = fout.readlines()
	fout.close()
	# acts as a counter to know the
	# index of the element to be replaced

	#x = input("enter text to be replaced:")
	#y = input("enter text that will replace:")
	ul_latlon, lr_latlon, pixelsize = '', '', ''
	for i in lin:
		if 'GRID_UL_CORNER_LATLON' in i:
			ul_latlon = i.strip('GRID_UL_CORNER_LATLON').strip('=').strip('\n')
		if 'GRID_LR_CORNER_LATLON' in i:
			lr_latlon = i.strip('GRID_LR_CORNER_LATLON').strip('=').strip('\n')
		if 'GRID_PIXEL_SIZE=' in i:
			pixelsize = i.strip('GRID_PIXEL_SIZE').strip('=').strip('\n')
		
	
	c = 0
	for i in lout:
		if 'INPUT_FILENAME' in i:
			t = 'INPUT_FILENAME = ' + in_dir_reverse_slash  + file + '\n'
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
			t = 'OUTPUT_FILENAME = ' + out_dir_reverse_slash + file[:-3] + '.tif' + '\n'
			Replacement = i.replace(i, t)
			lout[c] = Replacement
			print(t)
			# Replacement carries the value
			# of the text to be replaced
			#Replacement = i.replace(x, y)
	
			# changes are made in the list
			#l = Replacement
		c += 1
	

	# The pre existing text in the file is erased
	fout = open(hegprm, "r+", newline='\n')
	fout.truncate(0)
	
	# the modified list is written into
	# the file thereby replacing the old text
	fout.writelines(lout)
	fout.close()

	fileandpath = join(in_dir, file)
	chdir(heg_dir + 'HEGtools/HEG_Win/bin/')
	print('resample -p ' + hegprm)
	subprocess.call('resample -p ' + hegprm)
	#print(heg_dir + 'HEGtools/HEG_Win/bin/resample.exe -p ' + hegprm)
	#subprocess.call(heg_dir + 'HEGtools/HEG_Win/bin/resample.exe -p ' + hegprm)
