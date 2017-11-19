import sys
import datetime
import time
import urllib3

# Get command line parameters
output_file = sys.argv[1]
query_interval = int(sys.argv[2])
execution_time = int(sys.argv[3])

# Create output file and http pool for requests
outputFile = open(output_file, 'w')
http = urllib3.PoolManager()

# Write initial bracket and set that it is the first line. Set end time based on execution_time
outputFile.write('[\n')
firstLine = True
end_time = datetime.datetime.now() + datetime.timedelta(seconds=execution_time)

while True:
    # If execution_time is over, break while loop
    if datetime.datetime.now() >= end_time:
        break
    # If not first line, print comma before. Else, set firstLine = False to print in next iteration.
    if not firstLine:
        outputFile.write(',\n')
    else:
        firstLine = False
    # Get json data and write to file, then sleep for query_interval.
    response = http.request('GET', 'http://data.itsfactory.fi/journeys/api/1/vehicle-activity')
    outputFile.write(response.data.decode('utf-8'))
    time.sleep(query_interval)

# Write final bracket and close file.
outputFile.write('\n]')
outputFile.close()
