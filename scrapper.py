from getter import rawGetter
from getter import isResponse
from bs4 import BeautifulSoup
import csv

string = [ \
    '001001','001001','001001','001001','001001', \
    '002001','002001','002001','002001','002001', \
    '003001','003001','003001','003001','003001', \
    '004001','004001','004001','004001','004001', \
    '005001','005001','005001','005001','005001' \
]

input_file_name = input("[NAME] Output to save: ")
index = input("[PASTE] url to crawl: ")
recursive = input("[RECURSION]Try automatic child pages? [y/n]: ")
if recursive != 'y' or recursive != 'Y':
    string = '/'
list_scraped = list()
list_final = [['Question','Option A', 'Option B', 'Option C', 'Option D', 'Answer'],]

for i in string:
    '''Initializing the vars
    ''' 
    list_questions = list()
    list_answer_tuple = list()
    list_right_tuple = list()
    newcsv = list()  
    '''getting the requests
    '''
    i_html = rawGetter(index + i)
    html = BeautifulSoup(i_html, 'html.parser')
    if(html != None):
        options = html.find_all("td", attrs={"class": "bix-td-option", "width":"99%"})
        questions = html.find_all("td", attrs={"class": "bix-td-qtxt"})
        right = html.find_all("span", attrs={"class": "jq-hdnakqb mx-bold"})
        if(questions != [] and right != [] and options != []):
            for td in questions:
                list_questions.append(td.text)

            for ans in right:
                list_right_tuple.append(ans.text)
                
            count = 1
            iteration = 0
            for opt in options:
                if(count < 4):
                    count = count + 1
                    list_answer_tuple.append(opt.text)
                else:
                    newcsv.append(list_questions[iteration])
                    newcsv.extend(list_answer_tuple)
                    newcsv.append(list_right_tuple[iteration])
                    list_scraped.append(newcsv)
                    print('[APPEND]: ',list_questions[iteration], list_answer_tuple, list_right_tuple[iteration])
                    count = 0
                    iteration = iteration + 1
                    list_answer_tuple = list()
                    newcsv = list()
                    continue
list_final.extend(list_scraped)
with open(input_file_name+ '.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(list_final)
    csvFile.close()
