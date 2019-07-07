# KivyCalculator
Creating a calculator application in Python using Kivy.

The initial versions will be created to test various functionality of non conventional methods. The later versions will be more streamlined and have easier to read code with comments.

Version 0.1 Notes : 

Tried using exec() to process strings for the equations given to the calculator whilst it works it comes with its own security flaws. Made the inputs Readonly to prevent certain types of errors that the user can produce.

Am aware of various issues the application still has, that will be improved upon in the upcoming version that will use a far better system.

+Would only allow 1 decimal 
+Unable to differential between float and int
+Limited Prevention of non logical calculation


Version 0.2 Notes : 
Corrected several issues that were occuring within the application and also used a much sensible module for hanlding our calculations rather than the previous experimental version.
Existing code will require to be cleaned up and commented for ease of use and understanding. 

+ Multiple decimals can be added (1 per numeric value) that's seperated by a numeric operator.
+ Identifies weather a number is a int or float 
+ Improved control to prevent operations that would cause errors or crashes. 
