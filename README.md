# `navigate`
*a command line tool for navigating file directories quickly*

## What does `navigate` do?
Simply put, `navigate` allows the end user to quickly jump between directories without having to `cd` 
through a series of directories or type out the full filepath to the directory you want. How it works 
is simple: you pass `navigate` the directory you want to go to, and `navigate` will ask you which of a 
series of filepaths is the one you mean. Type `y` to instantly go to that filepath, or `n` to keep looking.
If `navigate` runs out of valid directories to show you, it will tell you so.

For example:

Say I have directory filepaths `/home/max/tufts/cs105/hw1`, `/home/max/tufts/cs116/hw1`, and `/home/max/tufts/cs135/hw1`
and I want to travel to `/home/max/tufts/cs135/hw1`. I could run `cd tufts; cd cs135; cd hw1`, or `cd /tufts/cs135/hw1`.
Or I might get sick and tired of that, and install `navigate`. Then, my command line experience might look like this:

(I am in `/home/max`)
 ```
nav hw1
Are you looking for /home/max/tufts/cs105/hw1 ? (y/n)  
Are you looking for /home/max/tufts/cs116/hw1 ? (y/n) 
Are you looking for /home/max/tufts/cs135/hw1 ? (y/n) 
```

(I am now in `/home/max/tufts/cs135/hw1`)

Fundamentally, this is only 9 key presses -- quicker than either other option for this kind of traversal.


## A few neat tricks
### The Jumptable
`navigate` is much more than just this algorithm. It also stores a jumptable of frequently used filepaths.
After the first time you use `navigate` to travel somewhere, it will store that filepath along with the associated
directory in a jumptable. The next time you ask for that directory, the first ones shown will be filepaths you've
travelled to before using that directory with `navigate`. 

Let's try another example:

Say I'm in the same directory as before (`/home/max`), and have logged back in and once again want to travel to `/home/max/tufts/cs135/hw1`.
This time, when I run the program, I get this:

```
nav hw1
| LABEL | PATH
|   a   | /home/max/tufts/cs135/hw1
Select path, or press ENTER if your path is not here:
```
I press `a`, and am now in `/home/max/tufts/cs135/hw1`

If I were to press `ENTER`, I would be prompted with a series of directories as usual. Let's say for instance I didn't press `a`, and instead
queried the directories until I went to `/home/max/tufts/cs116/hw1`. What's nice about this jumptable is subsequent entries don't boot previous
entries, they just reorder them. So, if I've used `navigate` to travel to both `/home/max/tufts/cs135/hw1` and `/home/max/tufts/cs116/hw1`, if 
I try to go to `hw1` again, I get this output first:

```
nav hw1
| LABEL | PATH
|   a   | /home/max/tufts/cs116/hw1
|   b   | /home/max/tufts/cs135/hw1
Select path, or press ENTER if your path is not here:
```
Note that the most recently visited path is the first to appear in the table.

At times, your jumptable may become cluttered and annoying. For convenience, the jumptable can be cleared by running:
```
nav /
Are you sure you want to clear the jumptable in data.json? THIS CANNOT BE UNDONE! (y/n) 
Your jumptable has been cleared.
```
### Substring Searches
Another neat feature of `navigate` is that it will look to see if your search term is a substring of any directories as well.
For example, if I have the long directories `/home/max/scans/209.85.231.104`, `/home/max/logs/020921`, and `/home/max/tufts/cs105/studentids/209` 
and I query `209`, I can expect the following output:

```
nav 209
Are you looking for /home/max/tufts/cs105/studentids/209 ? (y/n)
Are you looking for /home/max/logs/020921 ? (y/n)
Are you looking for /home/max/scans/209.85.231.104 ? (y/n)
```
Note that the exact match appears first, and directories with a common substring to the query appear afterwards.

If I had visited all of these directories before using `navigate` with the query `209` previously, I might get
the following jumptable:

```
nav 209
| LABEL | PATH
|   a   | /home/max/tufts/cs105/studentids/209
|   b   | /home/max/logs/020921
|   c   | /home/max/scans/209.85.231.104
Select path, or press ENTER if your path is not here:
```
Note the order again, with exact match appearing first. 


## Installation & Usage
### Installation
To install, clone this repo or simply download the associated files. Then, you will need to do the following:
* start by ensuring the paths listed in files `n` and `nav.py` accurately reflect the full filepath of `data.json` and `nav.py` in your system. I've used my own filepaths, but if you want to use this program across your entire computer, you will need the proper paths.
* create an alias to reference this program conveniently. `n` needs to be run as `source` to work, so run the command `alias nav="source ~/projects/navigate/n"`. Naturally, replace `~/projects/navigate/n` with whatever your filepath is. Of course, you can call this `alias` anything -- I like to use `nav`, as it is short, sweet, representative, and not used by anything else. 
* I recommend putting this `alias` command in your `~/.bashrc` or `~/.bash_aliases` file so it is run at startup and you don't have to do it manually.

### Requirements
Please see `requirements.txt`.

### Usage
To use, simply run on the command line like so: `nav <DIRECTORY NAME>`

Follow the prompts to select the directory you want. Using the jumptable, you will need to type the associated 
letter listed under label, but if not in the jumptable, a simple `y/n` to approve or disapprove a filepath will
do the trick.

To clear your jumptable, run on the command line: `nav /` and follow the associated prompts.

Feel free to use, modify, and distribute this code, with the appropriate credit.

## What's in this repo
`nav.py`: python script containing main algorithm for finding directory and managing jumptable.

`n`: shell script to wrap the main algorithm and actually change the directory. must be run as `source` to work.

`data.json`: json text file to store jumptable

`README.md`: this file

`requirements.txt`: python library requirements for `nav.py`.

## Author
This code is written entirely by Max Mitchell. Special thanks to Paul Mitchell for consulting on approaches to various
hurdles in this project. 

Please feel free to report any bugs directly on this page, or message me with questions about this software. Although I am
busy with school and work, and this is a side project, I would be more than happy to assist. 

This product is issued without warranty. Development is sporatic and only as time allows. 
