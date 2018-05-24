### How the save system works
#### and how you can learn from it  
The save system works simply by reading a line from a file. If it can't find the file, there is a recovery program that can be run to restore your data (although it will be reset)
### What it does:
Python is one of the simplest languages when it comes to files. To open a file, you simply type:
```python
file = open("./fileLocation/file.txt", "r")
```
First, you have to remember that `file` is a `file object`, not a file itself. You can do things to the file by calling functions on the ```file``` file object.  
Now: What it means:  
`file`: the name of the file object. Is a variable. You can call it whatever you like.  
`open()`: The Python function to access a file.  
`"./fileLocation/file.txt"`: The directory of the file (ie C:/Users/you/python/...). Does not have to be a text file. In fact, it could even be another program!  
`"r"`: The *mode* of the file object. It is how python can interact with the file.
- `"r"` will give Python read access, but not write access (it can read the file).
- `"w"` will give Python write access, but not read access (it can change the file)
- `"a"` will give Python append access, allowing it to add on to files (but not read them)
- `"r+"` will give Python read and write.
- `"w+"` is exactly like `"w"`, except that python will create the file if it does not exist.
On to actual code!
```python
save = open("./data/save1/location.txt", "r")
loc = save.readline()
if loc == "intro":
    ...
else:
    print("An error occured")
print("FINISHED") # should not print
```
What it does is opens the file at `./data/save1/location.txt` and then reads the first line of it. The `readline()` function reads a line out of the file that it is acting on.
