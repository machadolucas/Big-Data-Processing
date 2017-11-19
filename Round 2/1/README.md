Place your Python code into a file named **csv2xml.py**. In addition return a file **population.xml** created by your program (from the provided test data).

In order to make data generally easy to (re)use, the data should be stored in a format that is commonly supported by various programs and programming libraries.  [XML](https://en.wikipedia.org/wiki/XML), [JSON](https://en.wikipedia.org/wiki/JSON) and [CSV](https://en.wikipedia.org/wiki/Comma-separated_values) are three examples of widely used data formats. In this question we concentrate on the first and last of these three: XML and CSV.

Write a Python program that reads a CSV file that describes population in Finland's municipalities and writes the same information into an XML file. The input and output filenames are specified by the first two command line parameters, respectively.

#### Input format

The input file contains comma-separated value lines of form

```
name;year;total;males;females
```

where the field **name** refers to the name of the municipality, **total** is the  size of the population, and the last two fields **males** and **females** tell how the total population is divided into males and females. In addition to such lines of data, the beginning of the file contains a comment line (describes the data), an empty line, a header line (describes the different columns of the CSV data), and a summary line for the whole of Finland ("KOKO MAA" = whole country). These latter types of lines should be skipped; your program may simply start to process the data from row 5 onwards.

#### Output format

The information described by the input file should be output in XML format in such manner, that the data is enclosed within a root element named "populationdata", and the data for each single municipality is enclosed in an element named "municipality". Therefore the data should have the following form:

```xml
<?xml version="1.0" encoding="utf-8"?>
<populationdata>
 <municipality>
  <name>
   Akaa
  </name>
  <year>
   2014
  </year>
  <total>
   17052
  </total>
  <males>
   8477
  </males>
  <females>
   8575
  </females>
 </municipality>
 <municipality>
  ... data for the next municipality, and so on ...
</populationdata>
```

Do not produce the XML by creating the elements manually with string operations: use some XML library available in Anaconda Python, such as [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) or Python standard library's [ElementTree XML API](https://docs.python.org/3.6/library/xml.etree.elementtree.html).  Print the data in a "prettified" format where nested elements are indented, as shown above.

#### Test data

Test your program with the input file **population.csv** that holds information about the population of Finland's municipalities in the year 2014\. The file uses UTF-8 encoding.