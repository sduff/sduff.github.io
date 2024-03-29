---
title:
date: 2017-01-01
tags: []
published: false
layout: default
series: splunk
---
# Working with Australian Census data in Splunk


https://datapacks.censusdata.abs.gov.au/datapacks/

Step 1: Select Census year

Step 2: Select DataPacks type

Step 3: Select Geogrpahy

Then download the Aust DataPack

IMG

Extracting the data
CED codes

It is somewhat disapointing that although the data is in CSV format, the
metadata is stored in XLSX. Despite it being declared an "open" standard, XLSX
is a painful format to work with wihtout using proprietary tools.

Creating the CED lookup

Create a CSV file by exporting the Census_Code_2016 and Census_Name_2016 columns from the 2016_ASGS_Non-ABS_Structures sheet in 2016Census_geog_desc_1st_and_2nd_release.xlsx

Creating a Cell Descriptor lookup


Creating data

There are many tables in this data pack. 



Converting to KML
https://www.karambelkar.info/2016/10/gdal-2-on-mac-with-homebrew/

http://www.aec.gov.au/Electorates/gis/gis_datadownload.htm
http://www.aec.gov.au/Electorates/gis/files/national-midmif-09052016.zip

Install ogr2ogr

  831  brew install gdal2
  832  source .
  833  source .bashrc
  834  ogr2ogr
  835  export PATH=$PATH:/usr/local/opt/gdal-20/bin
  836  export LDFLAGS=-L/usr/local/opt/gdal-20/lib
  837  export CPPFLAGS=-I/usr/local/opt/gdal-20/include
  838  ogr2ogr
  839  cd Downloads/
  840  cd national-midmif-09052016/
  841  ls
  842  ogr2ogr -f "KML" regions.kml COM_ELB.TAB

http://www.bostongis.com/PrinterFriendly.aspx?content_name=ogr_cheatsheet


Party information
https://www.aph.gov.au/Senators_and_Members/Guidelines_for_Contacting_Senators_and_Members/Address_labels_and_CSV_files

https://www.aph.gov.au/~/media/03%20Senators%20and%20Members/Address%20Labels%20and%20CSV%20files/allsenparty.csv?la=en
https://www.aph.gov.au/~/media/03%20Senators%20and%20Members/Address%20Labels%20and%20CSV%20files/PartyRepsCSV.csv?la=en


Splunk
https://www.splunk.com/blog/2015/10/01/use-custom-polygons-in-your-choropleth-maps.html
https://katana1.com/splunk-has-just-levelled-up-in-geospatial-visualisation/


https://marriagesurvey.abs.gov.au/results/downloads.html
https://marriagesurvey.abs.gov.au/results/files/australian_marriage_law_postal_survey_2017_-_participation_final.xls
https://marriagesurvey.abs.gov.au/results/files/australian_marriage_law_postal_survey_2017_-_response_final.xls











source="/Users/sduff/Downloads/ssm_responses.csv" host="sduff-mbpr15" index="main" sourcetype="csv" | stats values(yes_p) by division
| lookup ced Census_Name_2016  as division OUTPUT Census_Code_2016
| lookup reps Electorate  as division OUTPUT "First Name", "Surname", "Political Party", "Gender"



index=main source="/*/2016_GCP_CED_for_AUS_short-header/2016 Census GCP Commonwealth Electoral Divisions for AUST/*G01*"
| stats values(Tot_P_P) as Tot_P_P by CED_CODE_2016
| lookup ced  Census_Code_2016 AS CED_CODE_2016 OUTPUT Census_Name_2016
| lookup reps Electorate as Census_Name_2016 OUTPUT "First Name", "Surname", "Political Party", "Gender"
