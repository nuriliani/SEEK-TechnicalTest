# SEEK-TechnicalTest
This repository consists of two python script that download and scrap data from an online source. 
download_jobdata.py : work as web crawler to download online job posting data from this website https://www.kaggle.com/madhab/jobposts/ 
scrap_jobdata.py : this script mainly works to extract data from .csv file downloaded. 
                      The extracted data are :
                      1-
                        i) Job Post 
                        ii) Position Duration 
                        iii) Position Location
                        iv) Job Description
                        v) Job Responsibilities
                        vi) Required Qualification
                        vii) Remuneration
                        vii) Application Dateline
                        ix) About Company
                      2- Companies with highest job posting in recent 2 years
                      3- Month with most number of posting over the years
                      4- Text cleaning and pretifying
Execution sequence - run download_jobdata.py first then scrap_data.py, 1 and 4 is store in saperate .csv output file, while 2 and 3 is printed on console.
Programming langugage - Python3
Libry used - Selenium, Pandas, NLTK, Numpy


                      
