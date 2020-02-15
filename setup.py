import os

class GitSetup():

    def __init__(self,username):
        self.username = username
        os.system("git init")
        pass
    
    def add_origin(self,repo_name):
        command = 'git remote add origin https://github.com/'+str(self.username)+'/'+str(repo_name)+'.git'
        os.system(command)
        os.system("git push -u origin master")
        pass
    
    def git_commit(self,commit_message):
        os.system("git add .")
        os.system("git commit -m \""+str(commit_message)+"\"")
        print("Commited All change")
        pass

    def remove_git(self):
        os.system("rm -rf .git")
        print("removed git from local repository")
        pass

    def reinit(self):
        os.system("git init")
        pass


if __name__ == "__main__":

    git_object = GitSetup(input('Username: '))
    git_object.git_commit(input('Commit Message: '))
    git_object.add_origin(input('Remote repository name: '))