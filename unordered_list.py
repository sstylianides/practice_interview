#!/usr/bin/python

'''
Q3: Write a function in Python that takes a list of strings and returns a single string that
    is an HTML unordered list (<ul>...</ul>) of those strings. You should include a brief
    explanation of your code. Then, what would you have to consider if the original list was
    provided by user input?

'''
def unorderedList(elements):
    print("<ul>")
    for s in elements:
        ul = "<li>" + str(s) + "</li>"
        print(ul)
    print("</ul>")


if __name__ == "__main__":

    string = ['mushrooms', 'peppers', 'pepparoni', 'steak', 'walnuts', 'goat cheese', 'eggplant',
    'garlic sauce']
    unorderedList(string)