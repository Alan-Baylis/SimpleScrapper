#Library import
import requests
from bs4 import BeautifulSoup
import csv


# Collect first page of artists list

page = requests.get('https://www.nga.gov/collection/anZ1.htm')
# Create a BeautifulSoup object
#soup = BeautifulSoup(page.text, 'html.parser')
soup = BeatifulSoup(page.text, 'html.parser')



#Activate to enable multi page
pages = []
for i in range (1,6)
    url= 'https://www.nga.gov/collection/anZ' + str(i) + '.htm' 
    pages.append(url)
	
	
	
	
# Remove bottom links
Last_link = soup.find(class_= 'AlphaNav')
Last_link.decompose()

# Create a file to write to, add headers row
F = csv.writer(open("ScrapOut.csv", 'w'))
F.writerow(['name', 'links'])

# Pulling all text from the BodyText div
artist_name_list = soup.find(class_= 'BodyText')

# Pull text from all instances of <a> tag within BodyText div
artist_name_list_items = artist_name_list.find_all('a')



# Create for loop to print out all artists' names
for artist_name in artist_name_list_items:
    #THis print with extra data use the next to specfify
	#print(artist_name.prettify())
    name = artist_name.contents[0]
    links = 'https://www.nga.gov' + artist_name.get('href')

    print(name)
    print(links)
    F.writerow([name, links])
    


