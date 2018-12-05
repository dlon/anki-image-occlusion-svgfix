from xml.etree import ElementTree as ET
import re
import os


exp = re.compile('_[AQ]_[0-9]\.svg$')
rel_path = 'collection.media'

ns = {'ns0': "http://www.w3.org/2000/svg"}


def fix_file(path):
    tree = ET.parse(path)
    root = tree.getroot()
    for elem in root.iterfind('.//ns0:rect[@style]', ns):
        fill = elem.attrib['style'].split(';')[0].split(':')[1]
        elem.attrib['fill'] = '#%s' % fill
        del elem.attrib['style']
    tree.write(path, xml_declaration=False)

for file in os.listdir(rel_path):
    if exp.search(file):
        fix_file(os.path.join(rel_path, file))
