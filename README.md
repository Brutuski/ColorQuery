![maintained](https://img.shields.io/badge/Maintained-Yes-brightgreen) ![made_with](https://img.shields.io/badge/Made%20with-Python3-1f425f.svg) [![license](https://img.shields.io/badge/License-MIT-green)](https://github.com/Brutuski/ColorQuery/blob/master/LICENSE) ![version](https://img.shields.io/badge/Version-BETA%200.1-red)
# ColorQuery
A small python CLI to fetch details about the entered RGB of HEX Values. <\br>
This tool can be helpful to users who have to look up colors often, like developers working on new color schemes or users ricing their linux build.

## API
This CLI relies on [The Color API](https://www.thecolorapi.com/)

## Known Issues
+ Yet to add error catching
+ HEX Codes should be entered *without #*
+ RGB Values entered should be *separated by commas*

## Requirements
+ [Console-Menu](https://github.com/aegirhall/console-menu)

## Output
Depending on what the user enter, HEX or RGB Values, the output is as follows
+ RGB or HEX Values
+ HSL Values
+ HSV Values
+ CYMK Values
+ Closest named Color and it's HEX Code

## How to run
+ `git clone https://github.com/Brutuski/ColorQuery.git`
+ `cd ColorQuery`
+ `chmod +x query.py`
+ `./query.py`

## Screenshots
Menu:<img src="https://raw.githubusercontent.com/Brutuski/ColorQuery/master/Screenshots/Menu.png"/>
Sample Output:<img src="https://raw.githubusercontent.com/Brutuski/ColorQuery/master/Screenshots/SampleOutput.png" />

## To Do
+ Add error catching
+ Add exporting options
+ Add a simple GUI
+ Optimize the code, make it more compact

## Changelog
+ 23/05/2020 Initial Commit
