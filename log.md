# 100 Days Of Code - Log

### Day 0: October 29, 2018

**Today's Progress**: Implemented "Recent Transactions" on the Dashboard page of my budget app. Had some fun implementing and iterating over dictionary keys and values. Fairly straightforward implementation, though. I feel like I'm past the hard part on this project now that I have the API set up and all the database calls working.

**Thoughts:** I'm using this project as a way to learn Vim (the text editor), as well. Man is it difficult. I spend a lot of time in insert mode, using the editor like I would any other. But there are brief moments where I use Vim to quickly 'delete inner paragraph' or find and change something where I can see the editor's value. I'm going to spend a little more time learning and getting comfortable with the basics. Maybe in a week or two, I'll take off the traning wheels and turn on hard mode (no arrow keys, mouse, or backspace)

**Link to work:** 4 commits today on `budget` - https://github.com/bennett39/budget. One fun, fake code snippet `100-days.py` in this 100-days-of-code repo.


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

**Today's Progress** Today I spent a lot of time on algorithms this afternoon. So, no code written, per se, but a lot learned. I'm using Udi Manber's book to learn. I did problem sets on paper, so there's no link to my work today but trust me I have pages of exercises and notes.

**Thoughts** This is the part that excites me. I'm not really interested in becoming a web developer, and front end work isn't very appealing to me. However, crunching the numbers and solving complicated problems is fun and rewarding. I just finished some proof by induction exercises and I love the way they stretched my brain to comprehend something I didn't comprehend just a few hours ago.

**Link to work** No link, just pages of paper algorithms notes today.


### Day 7: November 5, 2018

**Today's Progress** The budget app is working on Heroku!!!!!!! There's a lot of error testing and optimizing left to do, but I think I'll take a break from this project for a while.  It was enough porting a Sqlite local database to a PostgreSQL database in production. There's also a problem with session permanence if I use gunicorn, so this app is primed to break if anyone pushes its corner cases. Ultimately, refactoring it will require implementing Redis session management and rewriting a few database queries, none of which I'm interested in right now. I'm cross-eyed from staring at this codebase.

**Thoughts** It feels good to have this app working, but I'm mostly just glad to have it done for the moment. I need to decide on my next project, now. Probably something with a lot of data or complex algorithms. I'm going to Google around for available datasets to build a new project atop.

Another thought: I should add some dummy data to the budget database so that people can log in and at least see how it works.

**Link to work** 3 commits today on `budget` bennett39-budget.herokuapp.com


### Day 8: November 6, 2018

**Today's Progress** Today I dabbled in a couple different things, trying to find a new project. I'm learning shell scripting, so I'm cutstomizing my dotfiles to make me more efficient on the command line and automate some tasks.

I've also settled on building an application and API that can basically automate the work of building Intertech's dev digest. I've read up on feedly's API a little, and I've got my access token working to get new data.

**Thoughts** This is the hard part of learning to code, because I'm in the intermediate area where there are no tutorials to tell you what to do next. You just have to decide on a new project and commit to it for a while. I might take this new feedly project as an opportunity to learn Django.

**Link to work** New repository called `dev-feed` - I'm not sharing my dotfile publicly bc it has an access token in it right now, but here's a snippet of my Git CLI shortcuts in action:

```
~/workspace/tracking/100-days-of-code/ (master) $ ga
On branch master
Your branch is up-to-date with 'origin/master'.

Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        modified:   log.md

~/workspace/tracking/100-days-of-code/ (master) $ gc "Add daily log"
[master ac4221d] Add daily log
 1 file changed, 7 insertions(+), 5 deletions(-)
~/workspace/tracking/100-days-of-code/ (master) $ gh
Warning: Permanently added 'github.com,192.30.253.113' (RSA) to the list of known hosts.
Counting objects: 3, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 860 bytes | 860.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To github.com:bennett39/100-days-of-code.git
   edef332..ac4221d  master -> master
```


### Day 9: November 7, 2018

**Today's Progress** I have a PostgreSQL server running on my machine! I'm trying to make a move to coding in Ubuntu and not in the IDE anymore. Setting up database support was among the first priorities for that transition. It took me a few hours, but I'm learning a lot about bash by using it. I also have a better understanding of how postgres works.

**Thoughts** I'm excited for what's next. I find myself settling into a workflow now. I'm going to tackle Django next and try to launch my next app using Django.

**Link to work** I wrote a blog post about what I had to do today to get my Postgres server running. https://www.bennettgarner.com/launching-your-first-postgresql-server-on-ubuntu-16-04-a-guide-from-a-novice-for-beginners/


### Day 10: November 8, 2018

**Today's Progress** Today, I got Django running on my machine! It's a very barebones application with only a single route, but it's working great and connected to my PostgreSQL server on 127.0.0.1. Last night, after I wrote yesterday's log, I continued to work on Stanford's Algorithms and Data Structures and Udi Manber's Intro to Algorithms textbook. Both are very good. 

**Thoughts** Coding projects in the morning and learning theoretical stuff in the evening is working out great. Each uses my brain differently so I feel like I'm learning a lot from both sides. 

**Link to work** New `django` directory in the `learning` repository.


### Day 11: November 9, 2018

**Today's Progress** I worked through CS50's Django tutorial and I now feel like I have a basic understanding of how Django works. I also realize how powerful it is. I'm excited to learn more and build more complicated applications.

**Thoughts** Literally everything is online. Even if I want to do data and algorithms stuff, I'm going to need some grounding in web technologies to display and share the results. Django seems like a great option for learning web frameworks. Especially with a lot of data science happening in Python, it makes sense to learn Django as part of my stack.

**Link to work** A bunch of new files - 1 commit (I know I should do microcommits, but I was following a tutorial) - in `learning/django`


### Day 12: November 10, 2018

**Today's Progress** Did a nice amount of learning bash and vim at Pel's Pies (coffee shop) today. Great way to spend a chilly Saturday. And now I have built out bashrc and vimrc files with some basic settings that will make me more efficient.

**Thoughts** While today wasn't technically coding on a project, I'm counting it because I learned a good bit about bash, vimscript, and vim plugins. Tomorrow, I'm headed to my first meetup with other developers, so I'll be sure to work on stuff there.

**Link to work** My bashrc and vimrc files are in the `hello-world` repository.


### Day 13: Novermber 11, 2018

**Today's Progress** I've switched ideas for a Django implementation,
just to push my database abilities and really see how far Django can
stretch. I'm going to build dad's field reports entry forms as a Django
app. Today I got the database (models) set up. Next, I'll write the
views and add login/authentication.

**Thoughts** I'm writing this from my first meetup - Hacker Hours. I've
met Max, Susan, Robyn, and Aaron here. It has been fun, and I had a
really good conversation with Max, so hopefully I've got a coding buddy
to work with.

**Link to work** A ton of commits in `learning/django` on the
`garnereng` project.


### Day 14: November 12, 2018

**Today's Progress** A short coding session this morning since I have a
lot of other work to get done. But I have the views working on
garner-eng and I've created a repository for it. Going to Hacker Hours
again this evening (different meetup in Manhattan) so I'll code some
more then as well.

UPDATE: I'm at Hacker Hours and I have the basic `client` view working
now.

**Thoughts** I'd like to get my barebones Django app running on Heroku
so I can see how this whole puzzle is going to fit together. That might
be my next project. Alternatively maybe I can figure out how to sudo
directly into Bluehost.

**Link to work** New repository `garner-eng` for this project.


### Day 15: November 13, 2018

**Today's Progress** The index, client, project, and site pages are all
linking to one another now dynamically. It's pretty cool. Tried to call
dad to tell him I'm doing this and show it to him, but he didn't pick
up...

**Thoughts** I can tell Django is really powerful and I'm only
scratching the surface. Right now, everything is super basic and I
don't have any styling. I've also still got a lot to learn about logging
users in and handling changes/post requests.

**Link to work** More commits in the `garner-eng` repository.


### Day 16: November 14, 2018

**Today's Progress** After a phone call with dad this morning, the
garner-eng project is officially the most complicated application I've
built to date. But it's cool how easy Django makes it to add a lot of
new models to the database and link those models dynamically. I now have
a working database that should be able to do everything dad wants it to
do.

**Thoughts** Dad says Garner Engineering will pay me for the development
work I'm doing, so I'm gonna keep working heavily on this project to
make it ultra-usable for dad long term. Keeping a database of all Garner
Engineering's projects is going to be key to internal record keeping but
also to selling the company when the time comes in the next 5-10 years.

**Link to work** 2 commits in `garner-eng`


### Day 17: November 15, 2018

**Today's Progress** Today, I switched things up to do work in the
morning and development in the afternoon. It worked out well, and I got
a lot of work done on garner-eng. Specifically, I started learning how
to deploy to Google Cloud Platform's App Engine. I deployed a tutorial
app first and then started working on getting garnereng deployed.

**Thoughts** I wasn't able to fully deploy garnereng today because I
went to a Django NYC meetup at Stack Overflow's offices downtown. There
were crazy presentations about asynchronous listening servers, using and
automating vue.js deployment on Django, and creating custom blocks in
the Wagtail Django CMS. I met Matt who spoke about the asynchronous
channel servers (his application listened for IRC chats instead of HTTP
requests). He's having a baby soon, but he said to get in touch if I try
to use any of his source code for a future app.

**Link to work** Couple commits on `garnereng`


### Day 18: November 16, 2018

**Today's Progress** The garnereng app is fully launched on Google App
Engine! I should probably do a write up on what all it took to get a
Django app to work on App Engine. Maybe I'll do that now, so that I
remember in the future.

Also, I went through and added comments to by source code so far and
made some elements in my templates conditionally display. I have a call
with dad this afternoon to see what he thinks and map some next steps.

**Thoughts** This is exciting to have an app deployed to production.
Perhaps I'll go back and change my budget app from Heroku to Google App
Engine as well. Though that seems like it might be more trouble than
it's worth.

**Link to work** I won't link to the app here since it has Garner
Engineering's proprietary information - but the commits are on GitHub


### Day 19: November 18, 2018

**Today's Progress** I didn't code much yesterday, so I'm not counting
it in my 100 Days. Officially my first skipped day.

But with the amount of progress I made today on the garnereng app, it's
almost like two days worth of work. Bootstrap templates are now fully
implemented across the app, and I added several pages for viewing more
information. It's really starting to feel robust, now.

**Thoughts** I've got a lot more I want to implement, so this project is
by no means over, but it's going to be a great learning experience in a
lot of different areas moving forward. Yet to implement:

- Interactive editing, database updates
- Search bar
- Breadcrumbs
- Dashboard with data viz
- Authentication/login

**Link to work** A lot of commits on `garnereng`


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
