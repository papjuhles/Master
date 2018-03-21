import xml.etree.cElementTree as ET
import mysql.connector

# establish connection to database
cnx = mysql.connector.connect(user='master', password='master', host='localhost', database='master')
cursor = cnx.cursor()


# read xes
tree = ET.ElementTree(file='C:/Users/Christian/Google Drive/Uni/Master/5 Wintersemester 17-18/Masterarbeit/Test Data/ETM_Configuration1.xes')
root = tree.getroot()

#get relative frequencies for each event
for traces in root:
    if traces.get('key') == 'meta_concept:named_events_average':
        for keys in traces:
            eventName = keys.get('key')
            value = keys.get('value')

            query = ("INSERT INTO frequency (event, frequency) VALUES ('{0}', '{1}')".format(eventName, value))
            cursor.execute(query)
            cnx.commit()