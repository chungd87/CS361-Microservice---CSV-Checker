# CS361 Microservice - CSV Checker
 CSV Checker

## General Usage:

python3 -m CSVChecker filename

-Example:
```bash
	python3 -m CSVChecker data.csv
```


## Description:

Takes a file as a parameter.

Checks for condiitions required for a proper .csv file.

-If any condition is not met, returns a .csv file with file name and boolean value False.

-If all conditions are met, returns a .csv file with file name and boolean value True.

.csv file is written to same directory that the module is run from, with file name of {filename}OutputResult.csv

### Example output after running CSVChecker on a valid .csv file named csvFile.csv:
```
csvFileOutputResult.csv

with contents:

filename,boolean
csvFile.csv,TRUE
```


## Conditions:

-Checks for .csv file extension.

-Determines delimiter used by the file. Must be a commonly used delimiter. Checks with csv.Sniffer which will not pick up
 uncommon delimiters. Invalid delimiters will result in invalid .csv files.

-After delimiter is determined, counts number of columns in the header. Verifies that each following row in the file has the appropriate
 number of columns.

-Note that an empty .csv file is considered valid.



## Examples:
	Valid CSV file:
	column1,column2,column3
	1,2,3
	4,5,


	Invalid CSV file (number of columns do not match for header and rows):
	column1,column2,column3
	1,2,3,
	4,5


	Invalid CSV file (bad delimiter which CSV.Sniffer will not pick up on):
	column1.column2.column3
	1.2.3
	4.5.6


	Valid CSV file (commonly used delimiter):
	column1;column2;column3
	1;2;3
	4;5;6