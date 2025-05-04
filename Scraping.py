from bs4 import BeautifulSoup

# to import data from test.html we have to work with file objects 
##########################
#import html file content
##########################
with open ('test.html','r') as myfile:
    content = myfile.read()
    #just to test if we really have acces to the contnet 
    #print(content)
    #create instance of beautifulsoup
    soup=BeautifulSoup(content,'lxml')
    '''
    #grab information 
    tags=soup.find('h5')
    print(tags)  #this will give as result : <h5 class="card-title">Python for beginners</h5>
    link=soup.find('a') 
    print(link) # and this one : <a class="btn btn-primary" href="#">Start for 20$</a>

# find method search just for the first element because there is 3 tags of h5 and 3 links <a> 

# so we use find_all method to solve that 
    all_course_tags=soup.find_all('h5')
    print("________________________")
    print(all_course_tags)
    #[<h5 class="card-title">Python for beginners</h5>, 
    # <h5 class="card-title">Python Web Development</h5>, 
    # <h5 class="card-title">Python Machine Learning</h5>]
    for course in all_course_tags:
        print(course.text)
    '''
    ##################################################################
    ##################################################################
    #find the div tag with filter of class that they have 
    course_cards=soup.find_all('div',class_='card')
    for course in course_cards:
        course_name=course.h5.text
        course_price=course.a.text.split()[-1]

        print(f"{course_name} costs ==>{course_price}")

         