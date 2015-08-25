# Introduction to the Unix Shell

In this session we will look at some aspects
of the bash shell. We will look at how some
aspects of computational science can be 
automated with shell scripts and help everybody
get up to speed before we dive into version 
control after coffee.

To get started you should open a bash shell
and type:

```
cd
cd Desktop
git clone ...
cd ...
```

We will then try to work through the material
together with time set asside for the following 
exercises.

## Excercise 1

1. Create a directory for your work inside the
`data/users` directory. You should use your name
for the directory name.

2. Create a file called "aims.txt" in your new
directory which includes some text outlining 
what you want to get out of this workshop.

3. Copy all the files from `data/users/nelle/molecules`
into your new directory.

If you find this easy please help the people around
you. Once you have finished please attach the 
green sticky note to your monitor. If you get stuck 
attach the red sticky note.

## Excercise 2

Write a short pipeline to count the total number
of hydrogen atoms in all the pbd files in your
directory. You will need to use a new command 
that you have not been introduced to and take 
care to only count hydrogen atoms, not parts 
of the header that include "H".

Again, discuss this with those around you and
use the sticky notes as you finish or get
stuck.

## Exercise 3

Write a shell script that works like `wc`, 
but counts the carbon atoms in pdb files. 
For example, my version, called `count_carbon.sh`
works like this:

```
$ bash count_carbon.sh ethane.pdb methane.pdb
ethane.pdb:        2
methane.pdb:        1
Total:        3
$ bash count_carbon.sh *.pdb
cubane.pdb:        8
ethane.pdb:        2
methane.pdb:        1
octane.pdb:        8
pentane.pdb:        5
propane.pdb:        3
Total:       27
$
```

## Excercise 4

Generalise the count_carbon.sh script to take
(as the first argument) an element symbol to 
count. For example, my version works like this:

```
bash count_atom.sh H *.pdb
cubane.pdb:        8
ethane.pdb:        6
methane.pdb:        4
octane.pdb:       18
pentane.pdb:       12
propane.pdb:        8
Total:       56
```

If you get stuck, you may find it useful to 
explore how the `arguments_example.sh` 
script (in `data/solutions/`) works with different 
numbers of arguments.
