import requests

response=requests.get("https://gitlab.com/api/v4/users/GeetSharma/projects")
# response=requests.get("https://gitlab.com/api/v4/users/nanuchi/projects")

my_projects = response.json()

for project in my_projects:
    print("Project Name: {project['name']} \n Project URL: {project['web_url']}\n")