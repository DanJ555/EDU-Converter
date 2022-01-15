# Medieval2-EDU-Editor
A simple python script that can read and write. Very barebones for now, will just read and write a new file.
Edit main() to create any mass changes desired. Plans for a shell and GUI coming soon (tm) and making it work for RTW and its remaster.

*************
KNOWN ISSUES
*************

The vanilla EDU file will create an error due to every single elephant lacking a space after
a comma in the formations line. I will make it so that's a non issue later but for now just manually
space out those data entries.

Medieval 2 is actually incapable of accepting any file this script is currently capable of producing. However,
if the contents of an EDU generated from this script is copy and pasted onto the original EDU or one of its 
copies it actually will work. No idea why. the generated file and the overwritten file had a size difference
of 12 kilobytes when I tested it. This might be a linux specific issue?

Adding a property to a unit that necessitates a new line will off set the commented_out data and will
make it comment out incorrect lines. Already thinking of how to deal with that.
