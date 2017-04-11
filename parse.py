import xml.etree.ElementTree as ET
import os

i = 1
count = 0
for fname in os.listdir('/home/catcan/Desktop/ctd_pubmed/ctd_pubmed'):
    try:
        tree = ET.parse('/home/catcan/Desktop/ctd_pubmed/ctd_pubmed/' + fname)
        fou = open('/home/catcan/Desktop/data/pubmed/efetch_{}.txt'.format(i), 'w')
        root = tree.getroot()
        i += 1
        for tag in root.iter('AbstractText'):
            fou.write((tag.text + '\n').encode('utf-8'))
            count += 1
    except Exception as e:
        print(fname, i)
        print(e)
    else:
        pass
    finally:
        pass

print(i, count) 