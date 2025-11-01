import requests

response = requests.get("https://gitlab.com/api/v4/users/mark_1010/projects")
my_projects = response.json()

for project in my_projects:
    print(f"Project Name: {project['name']} \nProject URL: {project['web_url']} \n ")



'''
print(response.json())
print(type(response.json))
print(response.json()[0])

'''