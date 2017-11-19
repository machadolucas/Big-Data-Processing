Place your Python code into a file named **busdata.py**. In addition return a file named **busdata.zip** that contains, in zipped form, a bus data file **busdata.json** collected by your program. It is enough that your program produces **busdata.json**; you can create the zip file with some external zip compressing tool.

Write a Python program that records a series of location data about the buses of the Tampere public transportation network. Such data can be retrieved easily from the [Journeys API](http://wiki.itsfactory.fi/index.php/Journeys_API) offered by [ITS Factory](http://arkisto.hermiagroup.fi/its-factory/).

The program receives three command line parameters:

1.  The name of the file into which it should store the information.
2.  The time interval (in seconds) between successive data retrievals from the Journeys API.
    *   E.g. if this parameter is 10, then new data is retrieved every 10 seconds.
    *   In practice: call [**time.sleep(10)**](https://docs.python.org/3.6/library/time.html#time.sleep) between each successive rounds of downloading data.
3.  The time (in seconds) how long the program should keep recording the information.
    *   E.g. if this parameter is 3600, then the program should continue to retrieve and store the data for one hour. If the time interval specified by the preceding parameter would be 10, then this would mean that the program would retrieve roughly 3600/10 = 360 pieces of data during its execution.
    *   Use e.g. [the datetime module](https://docs.python.org/3.6/library/datetime.html) in order to keep track of time.

For example the command **python busdata.py busdata.json 10 3600** would keep reading bus data every 10 seconds for one hour and store all received data into the file **busdata.json**.

**Note:**<span style="font-size: 14px;"> When you test your program, do not give a value smaller than 10 for the interval between successive data retrievals. We do not wish to cause unnecessary load to the Journeys API server. Retrieving data every 10 seconds is often enough for our purposes.</span>

The Journeys API is very simple to use: simply visiting the address [http://data.itsfactory.fi/journeys/api/1/vehicle-activity](http://data.itsfactory.fi/journeys/api/1/vehicle-activity) returns information about all currently active buses within the Tampere public transportation network in JSON format.

**Caution:** do not simply write each received JSON data one after another into the output file. JSON format requires that a list of JSON data objects are enclosed in a list. For example {key: value}{key2: value2} is illegal JSON: the correct format is [{key: value}, {key2: value2}]. Therefore first write the opening bracket, and whenever you write a new JSON object into the result file, first write a preceding comma unless it is the first object. Finally write the trailing square bracket.

**Note:** The data returned by **d = requestl.urlopen(url).read()** is in bytes format. You may turn the bytes result object **d** into a string **s** by doing **s = str(d, "utf-8")**.

Once your progam works, record one hour of bus data with it using the 10 second interval and save the results into a file named **busdata.json**.

The data downloaded in this question will be used in question 6, so do this question in advance.