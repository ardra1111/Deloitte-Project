import json, unittest, datetime

with open("./data-1.json","r") as f:
    jsonData1=json.load(f)
with open("./data-2.json","r") as f:
    jsonData2 = json.load(f)
with open("./data-result.json","r") as f:
    jsonExpectedResult = json.load(f)

# Convert Json data from format 1 to a unified format


def convertFromFormat1 (jsonObject):

# Split the location files using '/' as the delimiter

    locationParts=jsonObject['location'].split('/')

# Create a dictioary for the unified format
   
    result= {
        "deviceID": jsonObject['deviceID'],       #Extract the deviceID
        "deviceType": jsonObject['deviceType'],   #Extract the deviceType
        "timestamp": jsonObject['timestamp'],     #Extract the timestamp
        "location": {
            "country": locationParts[0], #Extract the country from location
            "city": locationParts[1],    #Extarct the city from location
            "area": locationParts[2],    #Extract teh area from location
            "factory": locationParts[3], #Extact teh factory from location
            "section": locationParts[4]  #Extract the section from location
        },
        "data": {
            "status" : jsonObject['operationStatus'],  #Copy the operations as status 
            "temperature" : jsonObject['temp']          # Copy the temprature
        }
    }

    return result

#Convert Json data from format 2 to the unified format 

def convertFromFormat2 (jsonObject):

    #Convert the ISO timestap to milliseconds
    date = datetime.datetime.strptime(jsonObject['timestamp'],
                                      '%Y-%m-%dT%H:%M:%S.%fZ')  #ISO Timestamp format
    
    # In convertFromFormat2 function:
timestamp = round((date - datetime.datetime(1970, 1, 1)).total_seconds() * 1000)
 # convert to milliseconds

    # Create a dictionary in the unified format 

    result= {
        "deviceID": jsonObject['device']['id'],    #Extract the deviceID
        "deviceType":jsonObject['device']['type'], #Extract the deviceType
        "timestamp": timestamp,                    # Copy the timestamp 
        "location": {
            "country": jsonObject['country'], #Extract country 
            "city": jsonObject['city'],       #Extarct city 
            "area": jsonObject['area'],       #Extract area 
            "factory": jsonObject['factory'], #Extact factory
            "section": jsonObject['section']  #Extract section 
        },
        "data": jsonObject['data']
    }



    return result

#Main conversion function
#This function takes a Json object as input and determines which onversion function to use based on the presence of teh device field.
#If the device field is not present it means the data is in the first format so it calls covert from format 1.
#If the device fielsd is present it means the data is in the second format so it calls covert from format 2.

def main (jsonObject):

    result = {}

    if (jsonObject.get('device') == None):
        result = convertFromFormat1(jsonObject)
    else:
        result = convertFromFormat2(jsonObject)

    return result


class TestSolution(unittest.TestCase):  #The codes defines a test class called test solutions that inherits from unitus.test
#Includes 3 test methods
    def test_sanity(self):   # test sanity ensures that the conversion results matches the expected result.

        result = json.loads(json.dumps(jsonExpectedResult))
        self.assertEqual(
            result,
            jsonExpectedResult
        )

    def test_dataType1(self): # test_dataType1 tests the conversion from the first format using Json data 1.

        result = main (jsonData1)
        self.assertEqual(
            result,
            jsonExpectedResult,
            'Converting from Type 1 failed'
        )

    def test_dataType2(self):  #test_dataType2 tests teh conversion from the second format using Json data 2.

        result = main (jsonData2)
        self.assertEqual(
            result,
            jsonExpectedResult,
            'Converting from Type 2 failed'
        )

if __name__ == '__main__':
    unittest.main()
#the code checks if the script is being run as teh main program
# if it is it runs the tests using unitus.main  which verifies teh correctness of conversion finctions 
#  key line "if __name__ == '__main__':" is a conditional statement taht checks whether the script is being run as the main program.
# if it is the code vlock intended under thsi condition will be executed  