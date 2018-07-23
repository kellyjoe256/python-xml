import os
import xml.etree.ElementTree as ET

base_dir = os.path.abspath(os.path.dirname(__file__))
filename_path = os.path.join(base_dir, 'sample.xml')

# or ET.fromstring(string_with_xml), if xml is stored in string with xml
tree = ET.parse(filename_path)

root = tree.getroot()

countries = list(root)

directions = {'E': 'East', 'W': 'West', 'N': 'North', 'S': 'South'}

for country in countries:
    country_name = country.attrib.get('name')
    print(country_name)
    country_child_elements = list(country.iter())
    # remove first element because it's the root element [country] itself
    country_child_elements = country_child_elements[1:]
    for child_element in country_child_elements:
        if child_element.tag != 'neighbor':
            continue
        print('    {} is in the {} of {}'.format(
            child_element.attrib.get('name'),
            directions.get(child_element.attrib.get('direction'), 'unknown'),
            country_name))
    print('-' * 50)
