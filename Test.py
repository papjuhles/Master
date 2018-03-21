import xml.etree.cElementTree as ET
import graphviz as gv
from collections import defaultdict

tree = ET.ElementTree(file='C:/Users/Christian/Google Drive/Uni/Master/5 Wintersemester 17-18/Masterarbeit/Test Data/ETM_Configuration1.xes')
root = tree.getroot()

lst = []

for traces in root:
    if traces.tag == '{http://www.xes-standard.org/}trace':
        for events in traces:
            if events.tag == '{http://www.xes-standard.org/}event':
                for attr in events:
                    print(attr.get('value'))
                    lst.append(attr.get('value'))

print(lst[0])


print('***************************************************************************************')

traceName = []
eventName = []
traceEvent = {}
d = defaultdict(list)
i = 0

for traces in root:
    if traces.tag == '{http://www.xes-standard.org/}trace':
        for entries in traces:
            if entries.tag == '{http://www.xes-standard.org/}string':
                traceName.append(entries.get('value'))
            if entries.tag == '{http://www.xes-standard.org/}event':
                for events in entries:
                    if events.get('key') == 'concept:name':
                        eventName.append(events.get('value'))
                        #traceEvent[traceName[i]] = events.get('value')
                        d[traceName[i]].append(events.get('value'))
        i += 1

print(traceName[5])
print(eventName)
print(traceEvent)
print('***************************************************************************************')
print(d['trace 0'])
print('***************************************************************************************')

eventsTotals = {}

# Minimale Anzahl Events und Total Events per Event
for element in root:
    if element.get('key') == 'meta_concept:named_events_total':
        minEvents = element.get('value')
        for singleEvent in element:
            eventsTotals.update({singleEvent.get('key'): singleEvent.get('value')})

print(minEvents)
print(eventsTotals)

# graphical output of one specific trace
j = 0
g2 = gv.Digraph(format='svg')
for item in d['trace 0']:
    g2.node(d['trace 0'][j])
    if j+1 < len(d['trace 0']):
        g2.edge(d['trace 0'][j], d['trace 0'][j+1])
        j += 1

g2.render(filename='img/g2')