import glob
import os
import pprint

# https://www.makeuseof.com/tag/mac-terminal-commands-cheat-sheet/
print(glob.glob("/Users/yupingcui/IdeaProjects/ashleytutorial1/*"))
print(glob.glob("/Users/yupingcui/*.m4r"))
# print(os.environ['HOME'])  # mac
# print(os.environ['USER'])
pprint.pprint(dict(os.environ), width=1)


# sys.stdout, sys.err, sys stdin redirect
