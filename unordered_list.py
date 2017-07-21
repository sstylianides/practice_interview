#!/usr/bin/python

'''
Q3: Write a function in Python that takes a list of strings and returns a single string that
    is an HTML unordered list (<ul>...</ul>) of those strings. You should include a brief
    explanation of your code. Then, what would you have to consider if the original list was
    provided by user input?

ANSWER:

The first thing I would do is create a function that prints <ul> in order to initialize the
unordered list.  I would then create a for loop that inserts the list of strings in between
<li></li>.  I would then make a print statement that clases the </ul>.

if the original list was a user input, then I would create an empty list to store the strings
and create a while loop that takes user input and break the loop after the user presses the
enter key.  I woould append the user input into the list then call each string on the list to
insert it between <li></li>

'''
def unorderedList(elements):
    print("<ul>")
    for s in elements:
        ul = "<li>" + str(s) + "</li>"
        print(ul)
    print("</ul>")


if __name__ == "__main__":

    string = ['mushrooms', 'peppers', 'pepperoni', 'steak', 'walnuts', 'goat cheese', 'eggplant',
    'garlic sauce']
    unorderedList(string)
