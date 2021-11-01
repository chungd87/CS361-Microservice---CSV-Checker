#Author: Danny Chung
#Date: 10/29/2021
#Description: Microservice: Checks a .csv for file validity.

import csv
import sys

def CSVChecker(csvFile):
    """
    Takes a csvFile as parameter.
    Checks for conditions required for a proper .csv file.
    -If any condition is not met, returns a .csv file with file name and boolean value False.
    -If all conditions are met, returns a .csv file with file name and boolean value True.
    """
    #Checks for .csv file extension.
    if csvFile[len(csvFile)-4:] != ".csv":
        return outputFalse(csvFile)

    #Determine the Delimiter
    with open(csvFile, 'r') as file:
        fileContent = file.readlines()

        if fileContent == []:
            return outputTrue(csvFile)
        try:
            dialect = csv.Sniffer().sniff(fileContent[0])
            delimiter = dialect.delimiter
            print(delimiter)
        except:
            return outputFalse(csvFile)

        file.seek(0) #File reader back to beginning of file.

    #Determine number of columns.
        rowContent = csv.reader(file, delimiter=delimiter, skipinitialspace=True)
        rowStorage = []
        for rows in rowContent:
            rowStorage.append(rows)

        columnNumber = len(rowStorage[0])

    #Verify that each row has the appropriate number of columns.
        for rows in rowStorage:
            if len(rows) != columnNumber:
                return outputFalse(csvFile)

        return outputTrue(csvFile)

def outputFalse(csvFile):
    """
    Helper method, outputs a .csv file containing csvFile file name and boolean value in the
    case that the csvFile is determined to not be a proper csv file.
    """
    print("FALSE")
    with open(f"{csvFile[:-4]}OutputResult.csv", 'w') as outputFile:
        csvWriter = csv.writer(outputFile, delimiter = ",", lineterminator='\r')
        csvWriter.writerow(['fileName','boolean'])
        csvWriter.writerow([csvFile,'FALSE'])
    return

def outputTrue(csvFile):
    """
    Helper method, outputs a .csv file containing csvFile file name and boolean value in the
    case that the csvFile is determined a proper csv file.
    """
    print("TRUE")
    with open(f"{csvFile[:-4]}OutputResult.csv", 'w') as outputFile:
        csvWriter = csv.writer(outputFile, delimiter = ",", lineterminator='\r')
        csvWriter.writerow(['fileName','boolean'])
        csvWriter.writerow([csvFile,'TRUE'])
    return

if __name__ == "__main__":
    CSVChecker(sys.argv[1])