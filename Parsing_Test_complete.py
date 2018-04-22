import xml.etree.cElementTree as ET

tree = ET.ElementTree(file='C:/Users/Christian/Google Drive/Uni/Master/5 Wintersemester 17-18/Masterarbeit/BPI Challenge 2017/Data/Application Event Log/BPI Challenge 2017/BPI Challenge 2017.xes')
root = tree.getroot()

eventsTot = {}

def totalEvents():
    for entry in root:
        if entry.get('key') == 'meta_concept:named_events_total':
            test = entry.get('value')
            return test

def totalPerEvent():
    for entry in root:
        if entry.get('key') == 'meta_concept:named_events_total':
            for line in entry:
                eventsTot[line.get('key')] = line.get('value')
            return eventsTot

if __name__ == '__main__':
    print(totalPerEvent())
