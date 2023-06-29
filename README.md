# HEG script

I needed to transform the whole planet of snow maps from hdf to geotiff. The best working solution was HDF-EOS, but unfortunately the answer for the question:

> Q:  Is there another way of running batch job for processing thousands of HDF-EOS data sets?

Was a hard no. [Unlike now.](https://wiki.earthdata.nasa.gov/display/DAS/COMMAND+LINE+HEG#COMMANDLINEHEG-multipleDatasets)

This script updates a parameter file for each source data set in the specified folder and runs HEG commands to process it.
