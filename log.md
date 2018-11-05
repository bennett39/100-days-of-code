# 100 Days Of Code - Log

### Day 0: October 29, 2018

**Today's Progress**: Implemented "Recent Transactions" on the Dashboard page of my budget app. Had some fun implementing and iterating over dictionary keys and values. Fairly straightforward implementation, though. I feel like I'm past the hard part on this project now that I have the API set up and all the database calls working.

**Thoughts:** I'm using this project as a way to learn Vim (the text editor), as well. Man is it difficult. I spend a lot of time in insert mode, using the editor like I would any other. But there are brief moments where I use Vim to quickly 'delete inner paragraph' or find and change something where I can see the editor's value. I'm going to spend a little more time learning and getting comfortable with the basics. Maybe in a week or two, I'll take off the traning wheels and turn on hard mode (no arrow keys, mouse, or backspace)

**Link to work:** 4 commits today on `budget` - https://github.com/bennett39/budget. One fun, fake code snippet `100-days.py` in
this 100-days-of-code repo.


### Day 1: October 30, 2018

**Today's Progress**: Implemented `/categorize` in my budget app. It allows the user to set a category for each transaction. Used some Jinja for and if logic to display categories if they've already been chosen or display prompt if not. Database UPDATE/WHERE queries to save the user form input.

**Thoughts** Making serious progress, though I can see how feature creep happens in software. There are so many times when I think "It'd be nice if..." I gotta be careful, though, or I'm never going to get this project finished and move on to the next one.

**Link to work** 5 commits on `budget` (see above for link)


### Day 2: October 31, 2018

**Today's Progress** Spent a lot of time today playing around with python's datetime module to get `monthly` working, so manipulating time, specifically `strftime` and `strptime` is now in my skillset. Also worked a lot with nested for loops to fill in a table with data from three different variables. Feeling confident in my basic Python abilities.

**Thoughts** Last night I tried to go back and code something in C for the first time in a while. I struggled to remember all the syntax. Since I'm interested in efficiency and big data, that'll be something to revisit - not in C, but in C++. I also ordered an algorithm design book. Perhaps I'll try coding all of the solutions in both Python and C++.

**Link to work** 2 commits on `budget`


### Day 3: November 1, 2018

**Today's Progress** The first version of the budget app is done!!! I can use it to keep my budget instead of manually updating Google Sheets, now! There are more features I'd like to implement, and it could be designed prettier. But for now I'm tired of looking at this code, and I'm going to leave it.

**Thoughts** I need to deploy it to production now so it's always available - maybe as a subdomain on bennettgarner.com - that will likely be a whole different challenge to actually building the thing. My first migration to production, oh goodie!

**Link to work** 3 commits on `budget`


### Day 4: November 2, 2018

**Today's Progress** Ah, the joys of moving from a fun little app developed in an IDE to a standalone Heroku web server. First challenge today: Sort out dependencies from the IDE, then install those on my local Linux machine to get the app running locally. Since I'm running Ubuntu Xenial 16.04, I have Python 2.7 by default. I set up a pyenv to upgrade to Python 3.6 for my dependencies. Next, set up Heroku CLI and git push the local version to Heroku - it works! Now, currently working on creating PostgreSQL database for my app, since I can't use the SQLite database I've been using. After a lot of time on the command line, I finally have pgadmin4 working in server mode. I just have to create my database/tables/schema, and then add that to the repository and therefore the Heroku app... In theory, it'll be that easy.

**Thoughts** Today was a lot of problem solving of obscure dependencies/environments on the command line. I got a sense for what actual deployment and testing feels like, and I have to say I kind of liked the frustrating problem-solving nature of the whole thing. Twice today I got the most amazing happy feeling when my Heroku app finally worked online correctly, and when I finally got pgadmin to launch successfully.

**Link to work** 13 commits on `budget` and a ton of command line stuff that isn't saved anywhere...


### Day 5: November 3, 2018

**Today's Progress** Found a new guide for my Heroku migration. Its steps didn't work fully either, but I'm on the right track. The PostgreSQL database now exists and contains all my data. However my Heroku app isn't talking to the database correctly. At first, it was a problem with dependencies - the psycopg2 module wasn't installed. Now, I'm not sure what the problem is but I'm working on it.

I also started using firecode.io to practice algorithms and data structures and gain greater fluency in Python. I might do the same for C++ as well when I'm ready to start learning it.

**Thoughts** This Heroku migration is starting to get frustrating, but I make small bits of progress that indicate I'm moving in a good direction. I enjoyed firecode last night, too. I think that will be a good resource.

**Link to work** `budget` 4 commits on `master` and 10 commits on `development`


### Day 6: November 4, 2018

**Today's Progress** Today I spent a lot of time on algorithms this afternoon. So, no code written, per se, but a lot learned. I'm using Udi Manber's book to learn. I did problem sets on paper, so there's no link to my work today but trust me I have pages of exercises and notes

**Thoughts** This is the part that excites me. I'm not really interested in becoming a web developer, and front end work isn't very appealing to me. However, crunching the numbers and solving complicated problems is fun and rewarding. I just finished some proof by induction exercises and I love the way they stretched my brain to comprehend something I didn't comprehend just a few hours ago.

**Link to work** No link, just pages of paper algorithms notes today.


### Day 7: November 5, 2018

**Today's Progress** The budget app is working on Heroku!!!!!!! There's a lot of error testing and optimizing left to do, but I think I'll take a break from this project for a while.  It was enough porting a Sqlite database to a PostgreSQL database in production. There's also a problem with session permanence if I use gunicorn, so this app is primed to break if anyone pushes its corner cases. Ultimately, refactoring it will require implementing Redis session management and rewriting a few database queries, none of which I'm interested in right now.

**Thoughts** It feels good to have this app working, but I'm mostly just glad to have it done for the moment. I need to decide on my next project, now. Probably something with a lot of data or complex algorithms. I'm going to Google around for available datasets to build a new project atop.

Another thought: I should add some dummy data to the budget database so that people can log in and at least see how it works.

**Link to work** 3 commits today on `budget`


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**


### Day : , 2018

**Today's Progress**

**Thoughts**

**Link to work**
