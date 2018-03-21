import xml.etree.cElementTree as ET

tree = ET.ElementTree(file='C:/Users/Christian/Google Drive/Uni/Master/5 Wintersemester 17-18/Masterarbeit/Test Data/ETM_Configuration1.xes')
root = tree.getroot()

log = dict()

for traces in root:
    if traces.tag == '{http://www.xes-standard.org/}trace':
        for events in traces:
            if events.get('key') == 'concept:name':

                caseID = events.get('value')
            if events.tag == '{http://www.xes-standard.org/}event':
                for entry in events:
                    if entry.get('key') == 'time:timestamp':
                        timestamp = entry.get('value')
                    if entry.get('key') == 'concept:name':
                        eventName = entry.get('value')
                    if entry.get('key') == 'lifecycle:transition':
                        transition = entry.get('value')
                if caseID not in log:
                    log[caseID] = []
                case = (timestamp, eventName, transition)
                log[caseID].append(case)

for caseID in sorted(log.keys()):
    for (timestamp, eventName, transition) in log[caseID]:
        print(caseID, timestamp, eventName, transition)

# for caseID in log:
#     for (timestamp, eventName, transition) in log[caseID]:
#         print(caseID, timestamp, eventName, transition)