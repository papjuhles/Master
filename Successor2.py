import xml.etree.cElementTree as ET
import mysql.connector

# establish connection to database
cnx = mysql.connector.connect(user='master', password='master', host='localhost', database='master')
cursor = cnx.cursor()

# read xes
tree = ET.ElementTree(file='C:/Users/Christian/Google Drive/Uni/Master/5 Wintersemester 17-18/Masterarbeit/Test Data/ETM_Configuration1.xes')
root = tree.getroot()

log = dict()

# Events in dictionary speichern
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

# Ausgabe aller Events sortiert
# for caseID in sorted(log.keys()):
#     for (timestamp, eventName, transition) in log[caseID]:
#         print(caseID, timestamp, eventName, transition)

# Speichere mögliche Eventnamen in Liste
eventNames = ['A+complete', 'B+complete', 'C+complete', 'D+complete', 'E+complete', 'F+complete', 'G+complete']

# for traces in root:
#     if traces.get('key') == 'meta_concept:named_events_total':
#         for events in traces:
#             eventNames.append(events.get('key'))
# print(eventNames)

# Anzahl verschiedene Folgeevents
sequence = []
i = 0
j = 0
successors_dict = {}
successor = []
counter = 0
restart = True
for traces in root:
    if traces.get('key') == 'meta_general:classifiers':
        for keys in traces:
            if keys.get('key') == 'MXML Legacy Classifier':
                while restart:
                    restart = False
                    for elements in keys:
                        if elements.get('key') == 'meta_general:different_traces':
                            counter = 0
                            for entries in elements:
                                sequence = entries.get('key')
                                seqsplit = sequence.split(';')
                                print(seqsplit)

                                # successor.append('A+complete')
                                # for events in seqsplit:
                                #     if events == 'A+complete':
                                #             try:
                                #                 if seqsplit[j+1] not in successor:
                                #                     successor.append(seqsplit[j+1])
                                #                     j += 1
                                #             except:
                                #                 pass
                                try:
                                    if eventNames[i] not in successor:
                                        successor.append(eventNames[i])
                                    if seqsplit[i+1] not in successor:
                                        successor.append(seqsplit[i+1])
                                        counter += 1
                                except:
                                    pass
                            query = ("INSERT INTO successor (event, followingEvents) VALUES ('A+complete', '{0}')".format(counter))
                            cursor.execute(query)
                            cnx.commit()
                            successor = []
                            sequence = ""
                            seqsplit = []
                            i += 1
                            if i == 6:
                                restart = False
                                break
                            if i < 6:
                                restart = True
                                break



print(successor)