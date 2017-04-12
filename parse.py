import xml.etree.ElementTree as ET
import os

i = 1
count = 0
elog = open('./error_log', 'w')

for fname in os.listdir('./data/pubmed_xml'):
    try:
        tree = ET.parse('./data/pubmed_xml/' + fname)
        fou = open('./data/pubmed_text_only/efetch_{}.txt'.format(i), 'w')
        root = tree.getroot()
        i += 1
        for tag in root.iter('AbstractText'):
            if tag.text is not None:
                fou.write((tag.text + '\n').encode('utf-8'))
                count += 1
        fou.close()
    except Exception as e:
        elog.write(fname + str(i) + '\n')
        elog.write(str(e) + '\n')
    else:
        pass
    finally:
        pass

print(i, count) 