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
