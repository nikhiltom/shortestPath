from chaininghashtable import ChainingHashTable
from Package import Package
import csv



# This function opens package csv file and reads row by row
def loadPackageData(filename):
    with open(filename) as packageFile:
        packages = csv.reader(packageFile, delimiter=',')
        #each column in row gets assigned to different variables
        for package in packages:
            pID = int(package[0])
            address = package[1]
            city = package[2]
            state = package[3]
            zip = package[4]
            deliverby = package[5]
            weight = package[6]
            notes = package[7]
            status = None

            #new instance of package is created
            package1 = Package(pID, address, city, state, zip,deliverby, weight, notes, status)
            #newly created package object is inserted into the hash table
            packageHashMap.insert(pID, package1)

#create package hash table
packageHashMap = ChainingHashTable()

#load package data into hash table
loadPackageData('Package_File.csv')

def getPackage(id):
    for i in range(len(packageHashMap.table)):
        if i == id:
            print(vars(packageHashMap.search(i)))


'''

with open('Package_File.csv') as packageFile:
    packageList = list (csv.reader(packageFile, delimiter=','))
    for i, row in enumerate(packageList, start=1):
        packageHashMap.insert(i, row)
       # print(row)


with open('Package_File.csv') as packageFile:
    packageList = csv.reader(packageFile, delimiter = ',')
    for row in packageList:
        print(row)
'''
with open('Distance_Table.csv') as distanceFile:
    distanceList = list (csv.reader(distanceFile, delimiter=','))
    # for row in distanceList:
    # print(row)

def getIndex(address):
    for i,row in enumerate(distanceList):
        if address in row[1]:
            return i


def getDistance(a,b):
    print(a , b, getIndex(a))
    try:
        return float (distanceList[getIndex(a)][getIndex(b)+2] )
    except:
        return float (distanceList[getIndex(b)][getIndex(a)+2] )

print(getDistance('HUB', 'Oakland'))

getPackage(30)


'''


A) Package data steps:
1-Create ChainingHashTable data structure (See C950 - Webinar-1 - Let’s Go Hashing webinar)
2-Create Package and Truck objects and have packageCSV and distanceCSV and addressCSV files ready
3-Create loadPackageData(ChainingHashTable) to 
- read packages from packageCSV file (see C950 - Webinar-2 - Getting Greedy, who moved my data  webinar) 
- update Package object
- insert Package object into ChainingHashTable with the key=PackageID and Item=Package



print("\nInsert:")
myHash.insert(addressCSV[0][0], addressCSV[0][1])  # 2nd bucket; Key=1, item="CITIZEN KANE - 1941"
print(myHash.table)

myHash.insert(bestMovies[4][0], bestMovies[4][1])
print(myHash.table)

myHash.insert(bestMovies[10][0], bestMovies[10][1])  # 2nd bucket as well; Key=11, item="STAR WARS - 1977"
print(myHash.table)

print("\nSearch:")
print(myHash.search(1))  # Key=1, item="CITIZEN KANE - 1941"
print(myHash.search(11))  # Key=11, item="STAR WARS - 1977"; so same bucket and Chainin is working

print("\nUpdate:")
myHash.insert(1, "Star Trek - 1979")  # 2nd bucket; Key=1, item="Star Trek - 1979"
print(myHash.table)

print("\nRemove:")
myHash.remove(1)  # Key=1, item="Star Trek - 1979" to remove
print(myHash.table)

myHash.remove(11)  # Key=11, item="STAR WARS - 1977" to remove
print(myHash.table)

'''