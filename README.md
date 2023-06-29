# HEG script

I needed to transform the whole planet of snow maps from hdf to geotiff. The most convenient solution was [HEG](https://wiki.earthdata.nasa.gov/display/DAS/HEG%3A++HDF-EOS+to+GeoTIFF+Conversion+Tool), but unfortunately the answer for the question:

> Q:  Is there another way of running batch job for processing thousands of HDF-EOS data sets?

Was a hard no. [Unlike now.](https://wiki.earthdata.nasa.gov/display/DAS/COMMAND+LINE+HEG#COMMANDLINEHEG-multipleDatasets)

First script order_folders.py gets all the images from standard folders and puts them in the main one.

The main script transform.py updates a parameter file for each source data set in the specified folder and runs HEG commands to process it. The inputs are: the folder where HEGTools are located, folders with data sets and username that was used while installing HEG.

This solution is for Windows.
