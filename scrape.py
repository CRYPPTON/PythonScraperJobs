from bs4 import BeautifulSoup
import requests
import time

# https://www.timesjobs.com/ URL from search jobs
url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation='

print('Put some skill that you are not familiar with')
unfamiliar_skill = input('>')
print(f"filtering out {unfamiliar_skill}")

def find_jobs():
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")
    for index, job in enumerate(jobs):
        job_published_data  = job.find('span', class_ = 'sim-posted').span.text
        if 'few' in job_published_data:
            company_name = job.find("h3", class_  = "joblist-comp-name" ).text.replace(' ','')
            skills = job.find("span", class_ ="srp-skills").text.replace(' ','')
            more_info = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f"Company Name : {company_name.strip()} \n")
                    f.write(f"Require Skills: {skills.strip()} \n")
                    f.write(f"More Info: {more_info} \n")
                print(f'File saved: {index}')


# Run script every 10 minutes
if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f"Waiting {time_wait} minutes...")
        time.sleep(60 * time_wait)