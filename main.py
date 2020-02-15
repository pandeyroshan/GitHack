import os


def commit_git():
    print(os.system("git init"))
    print(os.system("git add ."))
    print(os.system("git commit -m \"Initial Commit\""))
    print(os.system("git remote add origin https://github.com/pandeyroshan/GitHack.git"))
    print(os.system("git push -u origin master"))
    pass

if __name__=="__main__":
    commit_git()