# Standard:
https://softwareengineering.stackexchange.com/questions/165725/git-branching-and-tagging-best-practices
https://nvie.com/posts/a-successful-git-branching-model/
# --------------------------------------------------------------------------------

# Change Branch
git checkout <branch_name>

# discard all files
git checkout -- .
git checkout -- main.py

# Show remote repo (lists)
git remote -v

# checkout the correct version
git tag  # shows the tagged versions
git checkout latest-tag-found-above
# --------------------------------------------------------------------------------

#--------------
# GIT TAGS  https://www.youtube.com/watch?v=govmXpDGLpo
#--------------
# Step 1:
Checkout the branch where you want to create the tag
git checkout "branch name"
example : git checkout master
________________________________________________________

# Step 2:
Create tag with some name
git tag "tag name"
example : git tag v1.0
git tag -a v1.1 -m "tag for release ver 1.1"  (to create annotated tags)
________________________________________________________

# Step 3:
Display or Show tags
git tag
git show v1.0
git tag -l “v1.*”
________________________________________________________

# Step 4:
Push tags to remote
git push origin v1.0
git push origin --tags
git push --tags
(to push all tags at once)
________________________________________________________

# Step 5:
Delete tags (if required only)
to delete tags from local :
git tag -d v1.0
git tag --delete v1.0

# to delete tags from remote :
git push origin -d v1.0
git push origin --delete v1.0
git push origin :v1.0

# to delete multiple tags at once:
git tag -d v1.0 v1.1 (local)
git push origin -d v1.0 v1.1 (remote)
________________________________________________________

# Checking out TAGS
We cannot checkout tags in git
We can create a branch from a tag and checkout the branch
git checkout -b "branch name" "tag name"
example : git checkout -b ReleaseVer1 v1.0
________________________________________________________

# Creating TAGS from past commits
git tag "tag name" "reference of commit"
example : git tag v1.2 5fcdb03
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
