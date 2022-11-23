# START LAB EXERCISE 05
print('Lab Exercise 05 \n')

#SETUP

student_orgs = [
    'Organization Name | Email | Category | Description | Active',
    '1st Generation Engineers | 1stgenengin.sab@umich.edu | academic/Honors Societies | create a community of scholars with similar backgrounds | 1',
    'Association for Women in Mathematics UM Student Chapter | awm-um-exec-board@umich.edu | Academic/Honors Societies | promote equal opportunity in math | 1',
    'Active Minds | active.minds.uofm@umich.edu | Activism | raising mental health awareness | 1',
    'Healthcare and Life Sciences Club | geetikar@umich.edu | Business & Entrepreneurship | increase career opportunities | 1',
    'Ballroom Dance Club | BDC-board@umich.edu | creative & Performing Arts | promote social partner dancing | 1',
    'CMYK Design | cmykdesign@umich.edu | Creative & Performing Arts | form relationships with like-minded designers | 1',
    'Chinese Students and Scholars Association | umichcssaboard@gmail.com | cultural/Ethnic | community service, culture exchange, and campus diversity enrichment | 1',
    'Graduate Rackham International | grin.contact@umich.edu | Cultural/Ethnic | support connections and social involvement across cultures | 1',
    'Spectrum Center | spectrumcenter@umich.edu | department | enrich the campus experience through intersectional lens | 1',
    'A2 Data Dive | datadiveorganizers@umich.edu | Graduate/Professional | increase data literacy in the community | 0',
    'Michigan Chess Club | chessofficers@umich.edu | Sports Clubs & Recreation | intercollegiate chess tournaments | 1',
    'Michigan Parkour | mipk.execs@umich.edu | Sports Clubs & Recreation | relaxed, motivational community atmosphere | 1',
    'Michigan Pickleball Club | coopstev@umich.edu | sports Clubs & Recreation | safe, inclusive space for players of all skill levels | 1',
    'Books for a Benefit | bfbeboard@umich.edu | Service/Service Learning | promote a life-long appreciation for reading | 1',
    'HackBlue | hackblue-leadership@umich.edu | service/Service Learning | teach computer science to underrepresented students | 1',
    'Hindu Students Council | hsc.info@umich.edu | Religious/Spiritual | creating an atmosphere conducive to worship, education, cultural experience | 1',
    'Black@SI | blackatsiorganizers@gmail.com | Academic/Honors Societies | academic and social support network that serves Black students | 1',
    'American Library Association Student Chapter | alaofficers@umich.edu | Academic/Honors Societies | promote interest in libraries | 1',
    '58 Greene | jamiemgr@umich.edu | Cultural/Ethnic | premier multicultural, co-ed acappella group | 1',
    'Michigan Bird Club | anitayr@umich.edu | Environmental | recreational birding and bird conservation | 1',
    'Friends of the Campus Farm | farm.core@umich.edu | Environmental | create a healthy future through sustainable food education | 0'
]

# END SETUP

## PROBLEM 1 (4 points)

def split_strings(orgs):
    for i in range(len(orgs)):
        orgs[i] = orgs[i].split(' | ')
    return orgs

student_orgs_split = split_strings(student_orgs) #call function
print(f"\n1.1 Student Orgs Split: \n {student_orgs_split}")

student_org_headers = student_orgs_split[0]
print(f'\n1.2 Headers: \n {student_org_headers}')

student_org_data = student_orgs_split[1:]
print(f'\n1.3 Data: \n {student_org_data}')



## PROBLEM 2 (3 points)

def convert_to_int(org):
    org[-1] = int(org[-1])
    return org

for org in student_org_data:
    convert_to_int(org)

print(f"\n2.1 Convert Active string element to integer: \n {student_org_data}")



## PROBLEM 3 (5 points)

def get_org_email_by_active_status(orgs, active=1):
    emails = []
    for org in orgs:
        if org[-1] == active:
            emails.append(org[1])
    return emails

active_emails = get_org_email_by_active_status(student_org_data) #call function
print(f"\n3.1 Get Active Organization Emails by Active Status: \n {active_emails}")

inactive_emails = get_org_email_by_active_status(student_org_data, 0) #call function
print(f"\n3.2 Get Inactive Organization Emails by Active Status: \n {inactive_emails}")



## PROBLEM 4 (6 points)

def get_organization_by_category(orgs, category):
    org_names = []
    for org in orgs:
        if org[2].lower().startswith(category.lower()):
            org_names.append(org[0])
    return org_names

sports_orgs = get_organization_by_category(student_org_data, 'Sports')



## PROBLEM 5 (7 points)

search_terms = ('Chess', 'Coding', 'Community')
chess, coding, community = search_terms

def search_org_descriptions(orgs, search_term):
    org_names = []
    for org in orgs:
        if search_term.lower() in org[3].lower():
            org_names.append(org[0])
    return org_names

chess_orgs = search_org_descriptions(search_term=chess, orgs=student_org_data)


# END LAB EXERCISE
