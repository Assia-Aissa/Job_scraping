from bs4 import BeautifulSoup
import requests
import csv 
html_text=requests.get('https://m.timesjobs.com/mobile/jobs-search-result.html?txtKeywords=python&cboWorkExp1=-1&txtLocation=')
print(html_text.status_code) # 200 means that we have access to the page

def find_jobs(myskill):
    soup =BeautifulSoup(html_text.text,'lxml')
    jobs = soup.find_all('li')

    job_list = []  # Create an empty list to store job info
    #print(jobs) # this will give us all the jobs that are in the page
    for job in jobs :
        job_title=job.find('h3')
        company_name=job.find('span',class_='srp-comp-name')
        job_time=job.find('span',class_='posting-time')
        job_skills =job.find('div',class_='srp-keyskills')
        
        if job_title and job_time and job_skills:
            if myskill.lower() in job_skills.text.lower():
                title=job_title.text.strip() 
                time_post=job_time.text.strip()
                company=company_name.text.strip()

                skill_links=job_skills.find_all('a')
                skill_job=[link.text.strip() for link in skill_links]
                print(f"=JOB ROLE= {title} =AT= {company} =POSTED AT= {time_post}")
                print("Skills:", ', '.join(skill_job))
                print("-" * 50)

                # add job informatin to the job list
                job_list.append({'Job Title':title,
                                 'Company':company,
                                 'Time Posted':time_post,
                                 'Skills':skill_job})
    return job_list  # Return the list of jobs found
def save_to_csv_file(jobs,filename="Jobs.csv"):
    with open(filename,'w',newline='',encoding='utf-8')as file:
        fields=['Job Title','Company','Time Posted','Skills']
        writer=csv.DictWriter(file,fieldnames=fields)
        writer.writeheader()
        writer.writerows(jobs)# write all job entries to the file 
    print(f"\n file saved {len(jobs)}  jobs to {filename}")

    

def job_search():
    print("Searching for jobs...")
    print("what skill do u wanna filter for ? ")
    myskill=input("> ")
    jobs=find_jobs(myskill)
    if jobs:
        save_to_csv_file(jobs)  # Save results if any job is found
    else:
        print("No jobs found with that skill.") 
    print("Done!")
    print("Have a nice day :)")


if __name__=="__main__":
    job_search() # this will make the program run once