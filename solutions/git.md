### Committing files
Which command(s) below would save the changes of myfile.txt to my local Git repository?
```
1. $ git commit -m "my recent changes"

3. $ git add myfile.txt
   $ git commit -m "my recent changes"

```
1 would work if myfile.txt has already been added to the staging area. 3 adds the file to the staging area and then saves the changes.

### Biography
Create a new Git repository on your computer called bio. Write a three-line biography for yourself in a file called me.txt, commit your changes, then modify one line, add a fourth line, and display the differences between its updated state and its original state.

### Old versions
Jennifer has made changes to the Python script that she has been working on for weeks, and the modifications she made this morning “broke” the script and it no longer runs. She has spent ~ 1hr trying to fix it, with no luck…

Luckily, she has been keeping track of her project’s versions using Git! Which commands below will let her recover the last committed version of her Python script called data_cruncher.py?
```

2. $ git checkout HEAD data_cruncher.py


4. $ git checkout <unique ID of last commit> data_cruncher.py

5. Both 2 & 4
```
