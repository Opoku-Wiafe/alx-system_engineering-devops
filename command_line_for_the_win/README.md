Intoduction to advance CommandLine Commands project

***
Print all matching lines (without the filename or the file path) in all files under the current directory that start with "access.log" that contain the string "500".

Note that there are no files named access.log in the current directory, you will need to search recursively.
***
** find . -type f -name "access.log*" -exec grep "500" {} \;

17.
***
Extract all IP addresses from files that start with "access.log" printing one IP address per line.
***
** grep -ro ^[0-9.]* **/access.log*

18.
***
The file split-me.txt contains a list of numbers separated by a ; character.
Split the numbers on the ; character, one number per line.
***
**

22.
***
Print the numbers 1 to 100 separated by spaces.
***
** tr ';' '\n' < split-me.txt
