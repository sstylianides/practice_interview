'''
Q1: What is the most influential book or blog post you’ve read regarding web development?

Answer:

The two most influential books that I've read is "Learn Python the Hard Way" and "Learn More
Python the Hard Way" by Zed Shaw.  Although not entirely about web development, I chose these
two books because this is what gave me the foundation to dive deeper into web development and
sharpen my Python skills. These two books definitely gave me the opportunity to get a solid
understanding of programming in order to become a web developer.




Q2: Tell me about a web application you have built. Why did you choose to build it? What did
    you learn? What challenges did you face and how did you overcome them?

Answer:

One of my first web applications that I built was a map of Orange County with interesting places
to visit using the Google Maps JavaScript API.  I chose to build this application because I wanted
to familiarize myself with the Google Maps API and I also wanted to get a better understanding of
JavaScript.  Many of my projects up until that point had mainly been with Python and C.  I wanted
to challenge myself by building an application in a language that is necessary for a web developer
to be fluent in since JavaScript is the de facto language of a web browser. The greatest challenge
that I faced was not only making a functional application, but creating a beautiful, user friendly
application.  Paying attention to detail and creating an excellent user experience was my ultimate
goal.




Q3: Write a function in Python that takes a list of strings and returns a single string that
    is an HTML unordered list (<ul>...</ul>) of those strings. You should include a brief
    explanation of your code. Then, what would you have to consider if the original list was
    provided by user input?

Answer:

please refer to unordered_list.py in the Github repository.




Q4: List 2-3 attacks that web applications are vulnerable to. How do these attacks work?
    How can we prevent those attacks?

Answer:

Three types of attacks that come to mind is SQL injection attacks, cross-site scripting and
brute force attacks. SQL injection attacks is when a hacker/attacker inputs a string using
SQL in a search box, login forms or into a URL in order to extract data from the applications
database. I think the first line of defense is to encrypt the data by storing it as a salted
hash.  the second line of defense is to incorporate the principle of least privilege so only
certain users have permission to access the data.

Cross-site scripting is when attackers insert JavaScript in pages of a website in order to alter
the contents of the website or send sensitive information to a different server.  I think the best
way to prevent this is to escape before inserting untrusted data into JavaScript data values and
escape before unserting untrusted data into URL parameters.

The third type of attack that I mentioned is brute force attacks. Brute force is a trial and
error strategy that attackers use to decode encrypted data and/or passwords. It's a time
consuming process because the program is attempting to input all possible character combinations
in order to "crack the code".  I think the two easiest solutions to this problem is using CAPTCHA
to distinguish between a computer and a human and to lock out accounts after X number of attempted
logins.




Q5: Below is some starter code for a Flask Web Application. Expand on that and include a
    route that simulates rolling two dice and returns the result in JSON. You should include
    a brief explanation of your code.

Answer:

please refer to rolling_dice.py in the Github repository.




Q6. If you were to start your full-stack developer position today, what would be your goals
    a year from now?

Answer:

Looking ahead a year into being a web developer, I'd like to be doing what I'm doing now which is
to always adhere to the continuous improvement model that I was taught while obtaining my bachelors
degree in Business Administration.  Whether it's a product or service, I'm always looking for ways
to improve myself in order to deliver the best possible experience to the end user.  In terms of
being a developer, this means keeping up with the latest technologies in web dev, learning new
languages, frameworks and libraries in order to build the best web applications. I think whether
someone is brand new to programming or a seasoned developer, there is always room to learn and to
keep updating your skillset.

'''
