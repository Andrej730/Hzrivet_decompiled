This repository contains script HZrivet for Maya, with fix for Maya version that use Python 3.  

Previously it was throwing indescriptive errors like `Error: SyntaxError: file C:\Program Files\Autodesk\Maya2022\Python37\lib\site-packages\shiboken2\files.dir\shiboken\support__feature__.py line 142: invalid syntax` when you would do `python("import HZrivet.UI;HZrivet.UI.UI()")` in MEL.  
If someone find this repository by the error message above - it's general message that doesn't really mean anything.  
The way to solve it was to check imported modules for syntax issues.  
The real issue was that during `import HZrivet.UI` there was import of `HZrivet.convert` that was containing `print` statement that were not using braces (Python 2 style).

Original script can be found here - https://www.highend3d.com/maya/script/hzrivet-for-maya

Original intro:
```
created by HuangZhen 20110107

my custom rivet scrip wrote by python.
more flexible & controllable

20110519
	add new version for 2010 and 2012
20131112
	add support for maya 2014

about me :http://www.ani-Q.com
qeejihz@gmail.com


install:
	copy 'HZrivet' to your script folder >>>"<your path>\maya\2009\scripts\"
	then use this command for sourcing
	mel>>>>>"python("import HZrivet.UI;HZrivet.UI.UI()");"
	python: "import HZrivet.UI;HZrivet.UI.UI()"
```
