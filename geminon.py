import wpparser
from sys import argv
from collections import namedtuple
from markdownify import markdownify

import re
def main(filename):
  data = wpparser.parse(filename)

  for post in data["posts"]:
    if post["content"] and post["title"] and post["status"] == "publish":
      date = post["post_date_gmt"]
      title = post["title"]

      gmi_filename = f"{date} {title}.gmi"

      gmi_content = (markdownify((post["content"])))
      gmi_content=  re.sub(r'\[(.+?)\]\((.+?)\)', r'\n=> \2 \1\n', gmi_content)
      gmi_content=  re.sub(r'\!\[\]\((.+?)\)', r'=> \n\1 (image content)\n', gmi_content)
      gmi_content = "\n".join([f"#{title}",date,gmi_content])
      fixed_title = "".join([c for c in title if c!='/'])
      print(title, fixed_title)
      with open(f"capsule/gemlog/{date} {fixed_title}.gmi", 'w') as fp:
        fp.write(gmi_content)
if __name__ == "__main__":
  filename = argv[1]
  main(filename)
