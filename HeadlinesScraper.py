from bs4 import BeautifulSoup
import requests
import re

url_list=["https://www.hindustantimes.com/","https://indianexpress.com/","https://www.thehindu.com/"]
newspaper =int(input("1 -> hindustantimes.com\n2 -> indianexpress.com\n3 -> thehindu.com"))
response = requests.get(url_list[newspaper])
print(f"Status Code : {response.status_code}")

soup = BeautifulSoup(response.content,"html.parser")

print("\n\n -----------------Get-Headlines--------------\n\n")
index=1
links_list=[]
for i in range (1,7):
    tag = f"h{i}"
    print(f"\n\nh{i} Headings \n\n")
    count = 1
    for  heading in soup.find_all(tag):
        print(f"[{index}] {count}) ",heading.text.strip())
        link_tag=heading.find_all('a')
        for links in link_tag:
            links_list.append(links['href'])
            break
        count+=1
        index+=1
user_input=int(input("\nEnter the link you want to access : "))
print(links_list[user_input])