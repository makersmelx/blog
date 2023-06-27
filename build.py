import os
import httpx
import re
import urllib.parse
import datetime

def fetch_ci_time(filePath):
    # entries = httpx.get("https://api.github.com/repos/tw93/weekly/commits?path=" + filePath + "&page=1&per_page=1")
    # ciTime= entries.json()[0]["commit"]["committer"]["date"].split("T")[0]
    # return ciTime
    # return datetime.datetime.strptime(ciTime,"%Y-%m-%d")
    return 0

if __name__ == "__main__":
  readmefile=open('README.md','w')
  readmefile.write("# 随便写写的个人博客 (credit. https://github.com/tw93/weekly)\n\n")

  for root, dirs, filenames in os.walk('./src/pages/posts'):
    filenames = sorted(filenames, key=lambda x:float(re.findall("(\d+)",x)[0]), reverse=True)

  for index, name in enumerate(filenames):
      if name.endswith('.md'):
        filepath = urllib.parse.quote(name)
        oldTitle = name.split('.md')[0]
        url   = 'https://jiayao.me/blogs/posts/' + oldTitle
        readmeMd= '* [{}]({})\n'.format(oldTitle, url)
        readmefile.write(readmeMd)

  readmefile.close()
