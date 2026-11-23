## 1. Navigation & Directory Commands

- **`pwd`**: **P**rint **W**orking **D**irectory (shows exactly where you are).
- **`ls`**: **L**i**s**t the contents of the current directory.
- `ls -l`: Long format (shows permissions, owner, date, size).
- `ls -r`: Reverse alphabetical order.
- `ls -lr`: Combine flags (long format + reverse order).
- `ls --help`: Short summary of options.
- `man ls`: Opens the full **man**ual page (press `q` to quit).
- **`cd`**: **C**hange **D**irectory.
- `cd Documents`: Move into the `Documents` folder.
- `cd /`: Move to the absolute root directory.
- `cd ..`: Move up one directory level.
- Use the **Tab** key to auto-complete file/folder names.
- **`sudo`**: **S**uper**U**ser **DO**; runs a command with administrator privileges.

## 2. File Management & Permissions

### Basic File Operations

- **`cat filename`**: Print the contents of a file.
- **`echo "text"`**: Print text to the screen.
- `echo "text" > file.txt`: Overwrite a file.
- `echo "text" >> file.txt`: Append to a file.
- **`mv file.txt /path/`**: Move a file; also renames files (`mv old.txt new.txt`).
- **`cp file.txt copy.txt`**: Copy a file.
- **`rm file.txt`**: Remove (delete) a file.

### Understanding `ls -l` Permissions

Example: `-rwxr-xr-x 1 devasc devasc 1095 Mar 30 21:24 script.sh`

- The first character is the file type: `-` = regular file, `d` = directory.
- The next three characters are the **owner** permissions.
- The next three characters are the **group** permissions.
- The last three characters are the **others** permissions.
- The first `devasc` is the owner; the second `devasc` is the group.

### Changing Permissions & Ownership

- **`chmod +x script.sh`**: Add executable permission so the script can run with `./script.sh`.
- **`sudo chown root file.txt`**: Change the owner to `root`.

## 3. Regular Expressions with `grep`

`grep` searches for patterns within text files. It is case-sensitive by default.

- **`grep word /etc/passwd`**: Find lines containing `word`.
- **`grep '^root' /etc/passwd`**: `^` anchors the search to the beginning of a line.
- **`grep 'false$' /etc/passwd`**: `$` anchors the search to the end of a line.
- **`grep 'd..m' /etc/passwd`**: `.` matches any single character.
- **`grep '[8-9]' /etc/passwd`**: `[ ]` matches one character from the range.
- **`grep '[,]' /etc/passwd`**: Find lines containing a literal comma.
- **`grep 'new*' /etc/passwd`**: `*` matches zero or more occurrences of the preceding character.

## 4. System Administration

- **`ip address`**: View network configuration, including IP and MAC addresses.
- **`date`**: Check the current system date and time.
- `shutdown now`: Shut down immediately.
- `shutdown +1 "Message"`: Shut down in one minute with a message.
- `shutdown -c`: Cancel a scheduled shutdown.

## 5. The `vi` (or `vim`) Text Editor

1. **`vi filename.txt`**: Open or create a file.
2. **`i`**: Enter Insert mode.
3. **`Esc`**: Return to Command mode.
4. **`:w`**: Write (save) the file.
5. **`:q`**: Quit the editor.
6. **`:wq`**: Write and quit.

## 6. Git Version Control

## 6.1 Initial Setup

Before you start using Git, you need to tell it who you are. This information is attached to every commit you make.

```bash
# Set your name and email globally
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Verify your settings
git config --list
```

## 6.2 Starting a Repository

A repository (repo) is a folder that Git is tracking.

```bash
# Initialize a brand new Git repo in your current folder
git init

# Clone (download) an existing repo from GitHub
git clone https://github.com/username/repo-name.git
```

## 6.3 The Basic Workflow (Stage & Commit)

Git has a staging area where you put files before you save them permanently.

```bash
# Check the status of your files (red = untracked/modified, green = staged)
git status

# Stage a specific file
git add filename.py

# Stage ALL changed files
git add .

# Commit your staged files with a descriptive message
git commit -m "Added new script for parsing JSON"

# Stage and commit all tracked files at once (skips the `git add` step)
git commit -am "Updated logic in parsing script"
```

## 6.4 Branching & Merging

Branches allow you to work on features without messing up the main code.

```bash
# List all local branches (the * indicates your current branch)
git branch

# Create a new branch
git branch feature-branch

# Switch to a branch
git checkout feature-branch

# Create AND switch to a new branch in one command
git checkout -b feature-branch

# Merge another branch INTO your current branch
# (e.g., you are on `main` and want to pull in changes from `feature`)
git merge feature-branch

# Delete a branch (only after it's merged)
git branch -d feature-branch
```

## 6.5 Working with Remotes (GitHub)

Sending your code to the cloud and getting other people's changes.

```bash
# See where your remote (GitHub) is pointing
git remote -v

# Push your local commits to the remote repository
git push origin main

# Pull the latest changes from the remote into your local machine
git pull origin main

# Fetch changes to see what others did WITHOUT merging them into your code yet
git fetch origin
```

## 6.6 Viewing History

```bash
# See a list of all commits (newest at the top)
git log

# See a short, one-line summary of each commit
git log --oneline

# See what changes you made since your last commit
git diff
```

## 6.7 Undoing Things (Emergency Commands)

*Be careful with these!*

```bash
# Unstage a file (keeps your changes, just removes it from the staging area)
git restore --staged filename.py

# Discard changes in a file (WARNING: your recent edits to that file will be lost)
git restore filename.py

# Undo the last commit, but keep the changes in your working directory
git reset --soft HEAD~1

# Completely undo the last commit and delete the changes (DANGEROUS)
git reset --hard HEAD~1
```

## 6.8 The Golden Rule of `git pull`

If you get an error that says `failed to push some refs` or `rejected`, it means someone else pushed to GitHub while you were working.

**Never use `git push --force`.**

Always run `git pull origin main` first to merge their changes with yours, resolve any conflicts, and *then* push.
