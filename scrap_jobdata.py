import zipfile, csv
import logging, traceback
from os.path import dirname, abspath
import pandas as pd
import numpy as np
from datetime import datetime
from pattern.en import pluralize, singularize
import inflect
import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
import logging, sys

logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# nltk.download('punkt')
# nltk.download('stopwords')

parentDir = dirname(abspath(__file__))
file_name = parentDir +'/data job posts.csv.zip'

try :
    logging.info("ETRACTING ZIPPED FILE OF DATA SOURCE")
    with zipfile.ZipFile(file_name,"r") as zip_ref:
        zip_ref.extractall("./data job posts.csv/")
    logging.info("zip file extract")
except Exception as e:
    logging.info(traceback.format_exc())

try:
    logging.info("Q2- EXTRACT DATA FROM SPECIFIED COLUMN & GENERATE NEW DATA FRAME ")
    jobs_data = parentDir + '/data job posts.csv/data job posts.csv'    
    reader = pd.read_csv(jobs_data)
    df = pd.DataFrame(reader)
    extracted_data = {"Job Post": reader["jobpost"], 
                "Position Duration": reader["Duration"], 
                "Position Location": reader["Location"],
                "Job Description": reader["JobDescription"],
                "Job Responsibilities": reader["JobRequirment"],
                "Required Qualification": reader["RequiredQual"],
                "Remuneration": reader["Salary"],
                "Application Dateline": reader["Deadline"],
                "About Company": reader["AboutC"] 
                }
    extracted_data = pd.DataFrame(extracted_data)
    try:
        extracted_data.to_csv('extracted_data.csv')
        logging.info("EXTRACTED DATA IS SAVED AS:'extracted_jobs_data.csv'")
    except Exception as e:
        logging.info(traceback.format_exc())
except Exception as e:
    logging.info(traceback.format_exc())

#--- Q3 Company with highest posting in past 2 years
try:
    logging.info("Q3- GET COMPANY WITH HIGHEST JOBPOST IN PAST 2 YEARS")
    current_year = df['Year'].max()
    past2years = df['Year'] > (current_year - 2) 
    past_2years = pd.DataFrame((df[past2years & df['Company']]))
    group_by_company = past_2years['Company'].groupby(past_2years['Year']).describe()
    print("\n",group_by_company,"\n")
except Exception as e:
    logging.info(traceback.format_exc())

#--- 4 month with highest posting over the years
try:
    logging.info("Q4- GET MONTH WITH HIGHEST JOB POSTING OVER THE YEARS")
    count_by_month = df['jobpost'].groupby([df['Year'],df['Month']]).count().sort_values().groupby(level=0).tail(1)
    print (count_by_month)
except Exception as e:
    logging.info("\n",traceback.format_exc(),"\n")

#--- 5 Clean Job Responsibilities text  - remove stop words, plural > singular
try:
    logging.info("Q5- CLEAN JOB RESPONSIBILITIES")
    logging.info("Open & Read file 'extracted_data.csv'...")
    extracted_jobs_data = pd.read_csv('extracted_data.csv')
    ed = pd.DataFrame(extracted_jobs_data)

    logging.info("Removing stop words...")
    stop_words = set(stopwords.words('english'))
    jobsResponsibilities = ed['Job Responsibilities']
    filtered_text = []
    for jr in jobsResponsibilities:
        if str(jr) != 'nan':
            word_tokens = word_tokenize(jr) 
            filtered_sentence = [w for w in word_tokens if not w in stop_words]   
            filtered_sentence = [] 
            
            for w in word_tokens: 
                if w not in stop_words: 
                    filtered_sentence.append(w)
            filtered_text.append(filtered_sentence)
        else:
            filtered_text.append(jr)
    logging.info("Singularize plural words...")
    singularized_text = []
    inflect = inflect.engine()
    for text in filtered_text:
        singular_sentence =[]
        if str(text) != 'nan':
            for word in text: 
                if type(word) == str:
                    if inflect.singular_noun(word) is False:
                        singular_sentence.append(word)
                    else:
                        singular_sentence.append(singularize(word))
            singular_sentence = ' '.join(singular_sentence)
            singularized_text.append(singular_sentence)
        else:
            singularized_text.append('-')

    # create new column, populate singularized_text into the column
    logging.info("Create new column & populate cleaned Job Responsibilities")
    ed['Cleaned Job Responsibilities'] = singularized_text
    new_dataframe = pd.DataFrame(ed)
    new_dataframe.to_csv('new_extracted_data.csv')
    logging.info("NEW COLUMN IS ADDED AND SAVED TO :'new_extracted_data.csv'")
except Exception as e:
    logging.info(traceback.format_exc())
















