import urllib.request
import re
with urllib.request.urlopen('https://www.monster.com/career-advice/article/college-resume-template') as response:
   html = response.read().decode('utf-8')
   print("E-Mail is: ",re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",html))
