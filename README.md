## Seattle Humane Society Scraper

#### This script scrapes the Seattle Humane Society adoptable dogs page and returns a data frame containing information about the dogs that are available for adoption.

The general process is as follows:

* Retrieve data from the webpage using Mechanize Browser

* Follow the link for each adoptable dogs

* Extract information about each dog (name, age, breed etc) and store it in a dictionary

* Convert the dictionary into a dataframe and display the results
