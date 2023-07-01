# HEG script

I needed to transform snow maps for the whole planet from HDF to Geotiff. The most convenient solution was [HEG](https://wiki.earthdata.nasa.gov/display/DAS/HEG%3A++HDF-EOS+to+GeoTIFF+Conversion+Tool), but it could only process one file at a time using GUI. HEG also had a command-line interface, but to process multiple maps in one run, you still need to add settings for all of them to the parameters file by hand. Unfortunately the answer for the question:

> Q:  Is there another way of running batch job for processing thousands of HDF-EOS data sets?

Was a hard no. [Unlike now.](https://wiki.earthdata.nasa.gov/display/DAS/COMMAND+LINE+HEG#COMMANDLINEHEG-multipleDatasets)

So here are the Python scripts that I wrote to deal with this problem.

The first script order_folders.py just gets the maps from standard folders and puts them all in one.

The main script transform.py updates a parameter file for each source map in the specified folder and runs HEG commands to process it. The inputs are: the folder where HEGTools are located, folders with maps, and the username that was used while installing HEG.

This solution is for Windows.
