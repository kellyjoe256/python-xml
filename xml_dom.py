import os
from xml.dom import minidom

base_dir = os.path.abspath(os.path.dirname(__file__))
filename_path = os.path.join(base_dir, 'sample.xml')

try:
    xml_document = minidom.parse(filename_path)
except Exception as e:
    print('Error occured: {}'.format(e))
else:
    data = xml_document.documentElement
    countries = data.getElementsByTagName('country')
    directions = {'E': 'East', 'W': 'West', 'N': 'North', 'S': 'South'}

    for country in countries:
        country_name = country.getAttribute('name')
        print(country_name)
        neighbors = country.getElementsByTagName('neighbor')
        for neighbor in neighbors:
            print('    {} is in the {} of {}'.format(
                neighbor.getAttribute('name'),
                directions.get(neighbor.getAttribute('direction'), 'unknown'),
                country_name))
        print('-' * 50)
