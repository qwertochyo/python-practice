import os
import random
import csv
from concurrent.futures import ThreadPoolExecutor

FILES_NAMES = ["first.csv", "second.csv", "third.csv", "fourth.csv", "fifth.csv"]
CATEGORIES = ["A", "B", "C", "D"]
FOLDER = "data"
RECORDS_AMOUNT = 50

def generationFiles():
    for filename in FILES_NAMES:
        filepath = os.path.join(FOLDER, filename)

        with open(filepath, "w", newline="") as file:
            writer = csv.writer(file)

            for _ in range(RECORDS_AMOUNT):
                writer.writerow([random.choice(CATEGORIES), random.uniform(0, 10.0)])

def printStruct(data):
    if isinstance(data, dict):
        for key, value in data.items():
            print(f"{key}: {value}")
    elif isinstance(data, list):
        for item in data:
            for key, value in item.items():
                print(f"{key}: {value}")
            print()

def readDataFromFile(filename):
    data = {}
    filepath = os.path.join(FOLDER, filename)

    with open(filepath, "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            if (row[0] in CATEGORIES):
                key = row[0]
                value = float(row[1])
                if key not in data:
                    data[key] = []
                data[key].append(value)

    return data

def solveMedian(valuesArray):
    valuesArray = sorted(valuesArray)
    length = len(valuesArray)

    if length % 2 == 0:
        mid1 = valuesArray[length // 2 - 1]
        mid2 = valuesArray[length // 2]
        result = (mid1 + mid2) / 2
    else:
        result = valuesArray[length // 2]
    
    return result

def solveMeanDeviation(valuesArray):
    length = len(valuesArray)

    mean = sum(valuesArray) / length
    meanDeviation = 0

    for x in valuesArray:
        meanDeviation += abs(x - mean)

    meanDeviation /= length
    return meanDeviation


generationFiles()

with ThreadPoolExecutor() as executor:
    inputValues = list(executor.map(readDataFromFile, FILES_NAMES))

arrayOutputValues = []
mapResultValues = {}
mapFinalResults = {}

meanDeviation = 0
medianValue = 0

print()
print("====== Medians and Mean Deviation ======")
print()

for item in inputValues:
    mapOutputValues = {}
    for key, value in item.items():
        medianValue = solveMedian(value)
        meanDeviation = solveMeanDeviation(value)
        mapOutputValues[key] = [medianValue, meanDeviation]
    arrayOutputValues.append(mapOutputValues)

printStruct(arrayOutputValues)

print("====== Median of medians ======")
print()

for item in arrayOutputValues:
    for key, value in item.items():
        if key not in mapResultValues:
            mapResultValues[key] = []
        mapResultValues[key].append(value[0])

for key, values in mapResultValues.items():
    medianValue = solveMedian(values)
    meanDeviation = solveMeanDeviation(values)
    mapFinalResults[key] = [medianValue, meanDeviation]

printStruct(mapFinalResults )
