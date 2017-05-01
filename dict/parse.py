import xml.etree.ElementTree as ET

i = 1
count = 0
try:
    tree = ET.parse('/home/catcan/Desktop/dict/CTD_diseases.xml')
    fou = open('/home/catcan/Desktop/dict/CTD_diseases', 'w')
    root = tree.getroot()
    i += 1
    for tag in root.iter('DiseaseName'):
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