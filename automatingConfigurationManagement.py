'''Q3. In DevOps, automating configuration management tasks is essential for maintaining consistency and managing infrastructure efficiently.

●       The program should read a configuration file (you can provide them with a sample configuration file).

●       It should extract specific key-value pairs from the configuration file.

●       The program should store the extracted information in a data structure (e.g., dictionary or list).

●       It should handle errors gracefully in case the configuration file is not found or cannot be read.

●       Finally save the output file data as JSON data in the database.

●       Create a GET request to fetch this information.

Sample Configuration file: 

[Database]
host = localhost
port = 3306
username = admin
password = secret

[Server]
address = 192.168.0.1
port = 8080
 
Sample Output: 
Configuration File Parser Results:
Database:
- host: localhost
- port: 3306
- username: admin
- password: secret

Server:
- address: 192.168.0.1
- port: 8080 '''

from backports import configparser
import json 

import configparser
try:
    #creating a obejct of configparser
    config = configparser.ConfigParser()
    # opening the file in read mode
    configFilePath = r'//home/mandar/DevOps/DevOpsBatch01/Assignments/ConfTest.conf'
    config.read(configFilePath)

except FileNotFoundError:
    print("Could not open/read file:")
    sys.exit()

except ConfigParserError:
    print("There was an error parsing the configuration file.")
    sys.exit()

#creating empty dictionary to store values
dictConf = {}
#using for loop to iterate in sections of config file
for sec in config.sections():
    #putting section as a key and empty value in dictionary
    dictConf[sec] = {}
    #using for loop to iterate in options of config file
    for opt in config.options(sec):
        #putting values in dictionary
        dictConf[sec][opt] = config.get(sec, opt)
        
print(dictConf)

#creating and opening a JSON file to write all configs in JSON file
with open("//home/mandar/DevOps/DevOpsBatch01/Assignments/ConfTest.json", "w") as JSONFile: 
    json.dump(dictConf, JSONFile)