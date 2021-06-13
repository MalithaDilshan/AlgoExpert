"""
    Download web content using the urllib and save into a specified file
"""
import urllib.request
import xmltojson
import json

url = 'https://programminghistorian.org/en/lessons/working-with-web-pages'
response = urllib.request.urlopen(url)
web_content = response.read()

# print(web_content)

file_path = 'C:\\Users\\ACER\\Desktop\\Python_projects\\pythonProject\\SpentX\\AlgoExpert\\Parallel ' \
            'Programming\\web_content.html '
f = open(file_path, 'wb')
f.write(web_content)
f.close()

# Only working for simple html files, need to find a proper way to do this
with open(file_path, 'r', encoding="utf-8") as html_file:
    html_content = html_file.read()
    _json = xmltojson.parse(str(html_content))
    print(_json)

# Resources: https://programminghistorian.org/en/lessons/working-with-web-pages
