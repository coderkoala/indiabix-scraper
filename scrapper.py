from getter import rawGetter
from getter import isResponse
from bs4 import BeautifulSoup
import os
import csv

def append(tail):
    #list_questions is for questions
    #list_answer_tuple is for options
    #list_right_tuple is for correct option
    list_questions = list()
    list_answer_tuple = list()
    list_right_tuple = list()
    '''getting the requests
    '''
    i_html = rawGetter(tail)
    html = BeautifulSoup(i_html, 'html.parser')

    if(html != None):
        questions = html.find_all("td", attrs={"class": "bix-td-qtxt"})
        right = html.find_all("span", attrs={"class": "jq-hdnakqb mx-bold"})
        #checking to see if empty. If empty, skip page
        if(questions != [] and right != []):
            
            for td in questions:
                list_questions.append(td.text)

            for ans in right:
                list_right_tuple.append(ans.text)
        #to iterate through
        iteration = 0
        table = html.find_all('table', attrs={"class":"bix-tbl-container"})
        for td in table:
            #Temp var for just taking in the data
            newcsv = list()
            newcsv.append(list_questions[iteration])
            newcsv.append(list_right_tuple[iteration])
            #Praise no consistency for regex of input
            d = td.find_all("td", attrs={"class": "bix-td-option", "width":"99%"})
            for din in d:
                newcsv.append(din.text)
            print('[APPEND]: ',newcsv)
            list_scraped.append(newcsv)
            iteration = iteration + 1  
            """            
            for opt in options:
                if(count <= 4):
                    count = count + 1
                    list_answer_tuple.append(opt.text)
                else:
                    newcsv.append(list_questions[iteration])
                    newcsv.extend(list_answer_tuple)
                    newcsv.append(list_right_tuple[iteration])
                    list_scraped.append(newcsv)
                    print('[APPEND]: ',list_questions[iteration], list_answer_tuple, list_right_tuple[iteration])
                    count = 1
                    iteration = iteration + 1
                    list_answer_tuple = list()
                    newcsv = list()
                    continue"""

list_final = [['Question','Answer','Option A', 'Option B', 'Option C', 'Option D', 'Option E']]
#used to collect the objects
list_scraped = list()
latter = list()
input_file_name = input("[NAME] Output to save: ")
index = input("[PASTE] url to crawl: ")
inquiry = input("[RECURSION]Try automatic child pages? [y/n]: ")
if inquiry == "y" or inquiry == "Y":
    latter = map(str,input("[001001 001002 001003]Please enter the sub urls to crawl: \n").split())
    for ip in latter:
        append(index + ip)
else:
    append(index)
list_final.extend(list_scraped)
#write it to an spreadsheet readable format(csv)
with open(input_file_name+ '.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(list_final)
    csvFile.close()
try:
    os.system("start excel "+input_file_name+".csv && exit")
except:
    pass