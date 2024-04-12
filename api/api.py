import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)
response_dict = r.json()

print(response_dict.keys())
print("Total repositories:", response_dict['total_count'])

repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

repo_dict = repo_dicts[0]
print("\nKeys:", len(repo_dict))
for key in sorted(repo_dict.keys()):
 print(key)
print("\nSelected information about each repository:")
names, stars = [], []
for repo_dict in repo_dicts:
 names.append(repo_dict['name'])
 stars.append(repo_dict['stargazers_count'])
 print('\nName:', repo_dict['name'])
 print('Owner:', repo_dict['owner']['login'])
 print('Stars:', repo_dict['stargazers_count'])
 print('Repository:', repo_dict['html_url'])
 print('Description:', repo_dict['description'])


my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names
chart.add('', stars)
chart.render_to_file('python_repos.svg')