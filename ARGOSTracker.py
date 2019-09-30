#-------------------------------------------------------------
# ARGOSTracker.py
# 
# Description: Parses a line of ARGOS tracking data
#
# Created by: Kelly Joyner (klj47@duke.edu)
# Created on: Fall 2019
#--------------------------------------------------------------

# Copy and paste a line of data as the lineString variable value
lineString = "20616	29051	7/3/2003 9:13	3	66	33.898	-77.958	27.369	-46.309	6	0	-126	529	3	401 651134.7	0"
​
# Use the split command to parse the items in lineString into a list object
lineData = lineString
​
# Assign variables to specfic items in the list
recordID = lineData[]              # ARGOS tracking record ID
obsDateTime = lineData[]           # Observation date and time (combined)
obsDate = obsDateTime.split()[]    # Observation date - first item in obsDateTime list object
obsTime = obsDateTime.split()[]    # Observation time - second item in obsDateTime list object
obsLC = lineData[]                 # Observation Location Class
obsLat = lineData[]                # Observation Latitude
obsLon = lineData[]                # Observation Longitude
​
# Print information to the use
print ("Record {0} indicates Sara was seen at {1}N and {2}W on {3}".format(recordID, obsLat,obsLat,obsDate))