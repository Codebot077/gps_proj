Task: Geolocation Analysis

I am mainly employing two different scripts:
Convertor.py: This script mainly converts the data from kml file into a csv file for 
	      easier processing and data representation. The csv file is named output_coordinates.csv

Calculate.py: This is the main calculaion script. It takes the coordinates as input from output_coordinates.csv 
	      and perform the required calculations to calculate the speed, distance covered and acceleration for 
              every 2s timeframe. The output is stored in output_result.csv file for easy data representation.



To run:
1. First make sure that output_coordinates and output_result are not already present otherwise which may lead to
overwriting error.
2. First run the convertor.py script to convert the .kml to .csv file.
3. Now run the calculate.py file.