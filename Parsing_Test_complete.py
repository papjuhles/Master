import xml.etree.cElementTree as ET

tree = ET.ElementTree(file='C:\Users\Christian\Google Drive\Uni\Master\5 Wintersemester 17-18\Masterarbeit\BPI Challenge 2017\Data\Application Event Log\BPI Challenge 2017.xes')
root = tree.getroot()

for entry in root:
    if entry.get('key') == 'meta_concept:named_events_total':
        test = entry.get('value')

print(test)