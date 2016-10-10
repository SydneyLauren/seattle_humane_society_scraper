import pandas as pd
from mechanize import Browser
from bs4 import BeautifulSoup
from collections import defaultdict


def open_browser(url):
    '''
    INPUT: string containing url to open
    OUTPUT: browser object
    open the requested page and return a browser object
    '''
    br = Browser()  # Initialize browser object
    br.addheaders = [('User-agent', 'Firefox')]
    br.open(url)  # Retrieve the requested page
    br.select_form(nr=0)
    return br


def get_petango_links(links):
    '''
    INPUT: all links in browser
    OUTPUT: list of links to petango pet profiles
    get a list of the links to petango pet profiles
    '''
    return [link for link in links if 'petango' in str(link)]


def parse_unicode(string):
    '''
    INPUT: string containing non-ascii characters
    OUTPUT: string cleaned of non-ascii, spaces, and newline characters
    clean up unicode string
    '''
    string = string.text.strip()
    return string.encode('ascii', 'ignore').split('\n')


def list_to_dict(dictionary, keys, lst):
    '''
    INPUT: dictionary as defaultdict, dictionary keys, list of data
    OUTPUT: updated dictionary
    take a dictionary and append it with new data
    '''
    for k, v in zip(keys, lst):
        dictionary[k].append(v)
    return dictionary


url = 'http://www.seattlehumane.org/adoption/dogs'  # Seattle humane society adoptable dogs page
br = open_browser(url)  # call open_browser to get browser object
petango_links = get_petango_links(br.links())  # identify links to petango pages

columns = ['Name', 'ID', 'Species', 'Gender', 'Breed', 'Age']  # choose column names for dataframe
dog_dict = defaultdict(list)  # initialize a dictionary for temporary data storage

for link in petango_links:  # loop through each of the petango links
    petango_data = br.follow_link(link)  # click the link
    soup = BeautifulSoup(petango_data, 'lxml')  # record the data as soup
    details = soup.findAll('div', {'class': 'list-animal-info-block'})  # get the details about each dog
    for detail in details:  # loop through the details
        detail_list = parse_unicode(detail)  # clean up the text
        dog_dict = list_to_dict(dog_dict, columns, detail_list)  # store in dictionary

print '\nAdoptable Dogs at the Seattle Humane Society'
print pd.DataFrame.from_dict(dog_dict, orient='columns', dtype=None), '\n'
