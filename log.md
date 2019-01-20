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


### Day 20: November 19, 2018

**Today's Progress** User authentication is now implemented! Login is
required to see any information on the app now, which is a major step
for the app because we can now start thinking about pointing a domain
toward it and actually using it.

**Thoughts** Authentication was tricky to wrap my head around at first,
but Django does all the hard stuff, you just have to tell it what you
want in the right way. I'm burning thorugh my to-do list on this app.
It's awesome.

**Link to work** Since there's a login wall, I can now share the link -
https://garnereng-222619.appspot.com. But if you don't have a login, you
won't be able to check out the rest of the app.


### Day 21: November 27, 2018

**Today's Progress** I took a week off coding for the Thanksgiving
holiday. Guests started arriving last Tuesday and then yesterday after
everyone left I was sick.

I'm back at it today. Making some small updates and refamiliarizing
myself with the garnereng app. Also going to try to implement the Feedly
dev digest application as a command line app in python.

**Thoughts** I went down a rabbit hole reading articles about data
science today. It's interesting and I think I'd be good at it. However,
it seems like the barriers to entry are much higher than in web
development - particularly when it comes to degree requirements.

**Link to work** garner-eng updated and new commits in dev-feed on my
github


### Day 22: November 28, 2018

**Today's Progress** My little Feedly aggregator is working to connect
to feedly and get articles from a sample feed. I also have
authentication working, so in theory all that's left is to add some
params to the API Get request and I should be able to grab my unread
articles.

**Thoughts** I'm sure using the Feedly API makes total sense to
developers who have been doing this for a while, but it was a challenge
figuring out how to construct URLs and resource IDs. A missing trailing
`/` halted my progress for quite a while and I had to gradually work
backward until I could figure out where the 404 error was coming from.

**Link to work** Commits in the `dev-feed` repository.


### Day 23: November 29, 2018

**Today's Progress** It's working as a command line python program! The
program uses the python requests module to connect to the feedly API. It
authenticates using an OAuth key that I have saved in a secrets file.

I first had to get my user aricle stream working. It took a little 
massaging of endpoints and resource IDs before I reliably got back what 
I needed. Then, I spent a while learning about the encoding of the 
response and how to parse and prettify JSONs. Now, the app exports an 
indented UTF-8 .json file to the output folder!

**Thoughts** One limitation: Feedly only allows 250 API requests per
day. I'm not sure how that's measured. Right now, I'm capping my article
stream requests at 20 articles by default.

Now that I have the API connection working, I need to figure out what
I'm going to build with it. Ideally, I can somehow filter, sort, and
then save articles over time so I have a backlog of usable articles for
the dev digest.

**Link to work** Commits are in `dev_feed`


### Day 24: November 30, 2018

**Today's Progress** There was a bug in garner-eng when I tried to show
it to Max last night, so I found and fixed that bug. To guard against
future bugs, I'm learning about testing and I spent today writing my
first few Django tests. Luckily the Django testing suite uses similar
syntax to Python's unittest module, so most of what I learned today
should be transferrable.

**Thoughts** I listened to a podcast at the gym this morning on
test-driven development. I'm familiar with the concept, but I've never
tried it. I'm interested to try to use it with a simple project like
dev-feed that I'm working on.

**Link to work** Commits in `garner-eng`


### Day 25: December 2, 2018

**Today's Progress** Brief coding session today. I updated the
formattting of the digest output file in the dev-feed

**Thoughts** Taking it chill this weekend, but still got a little bit
done on the dev-feed. I want to work on writing tests for the app, and
next I need to add more content to the API call and work on filtering
and sorting the results.

**Link to work** Commit in `dev-feed`


### Day 26: December 3, 2018

**Today's Progress** Dev feed app is taking shape. It now all runs
inside one application. I initially had the API call in one .py file and
the formatting in another. But now they're together and happen all at
once. The output is a markdown text file. Next step, sorting and
filtering results.

**Thoughts** Happy with the brief progress I've made today. I also think
I'm going to move more toward data-focused work. Analytics stuff. See
how I like that.

**Link to work** Commits in `dev-feed`


### Day 27: December 4, 2018

**Today's Progress** Before I got to sorting and filtering, I wanted to
make the application more flexible, so I broke everything into separate
functions and added command line options when I run the program.

**Thoughts** This new structure will make the application much more
modular, and it allows me to run variations of the program on the fly.
It will also make testing parts of my code easier. This is a best
practice that I've read about and used before. I want to make it more
second nature when I'm creating from scratch.

I also added docstrings and comments for all my new functions.

**Link to work** 5 commits in `dev-feed`


### Day 28: December 6, 2018

**Today's Progress** I'm happy with `dev-feed` at the moment since I
broke it into separate smaller feeds. Feedly's built-in sorting is
working fine, at least in the samples I've run. We'll see how it does
the next time I make the dev digest and actually use it!

I'm interested in algorithms and data manipulation, so I'm moving back
to C and working on the Project Euler problems. I'm already scratching
my head over the first one. I think it should be possible to do it in
constant time O(1).

**Thoughts** Ohhh my C is a little rusty, but it's quickly coming back
to me. I kind of like static typing and actually thinking about what's
going on in memory when you write something. My first attempt at solving
the problem worked up to a point before breaking down.

Obviously, there's the straightforward solution of iterating through the
numbers and adding them in linear time O(n), but I really feel like I
can do better and I though I had a solution but it breaks down.

**Link to work** New repository `euler`


### Day 29: December 7, 2018

**Today's Progress** I solved Euler #2 but forgot to write my daily log.
It was a brief coding session in the morning.

**Thoughts** Solution works in log(n) time, since the Fibonacci series
grows in n^1.6 until it reaches the upper bound of the algorithm. Start
with the straightforward solution, get it working, and then optimize it
once you have your head around the problem and the variables/functions
defined.

**Link to work** Commits in `euler`


### Day 30: December 8, 2018

**Today's Progress** Euler #3 and #4 today. #3 iterates through numbers
until it finds a factor or reaches the square root of the input.

 #4 goes through a double for-loop, so worst case it's quadratic, but it
 has a break statement to make it run much faster on average.

**Thoughts** I like working on these puzzles. I can feel myself getting
more fluent with C and the intricacies of data manipulation.

I'm learning to like testing, but with some of these challenges it's
tough to write tests because I don't know the answer ahead of time. I'll
need to work on writing smaller tests.

I think my documentation is getting better, and I'm also improving
making small commits in git insead of all the changes in a single
commit daily.

**Link to work** Commits in `euler`


### Day 31: December 10, 2018

**Today's Progress** Euler #5 and #6 today. Both were straightforward
and felt somewhat easy, especially with the foundation of the first few
problems. I'm sure they'll get harder soon though.

**Thoughts** Did some good research today on data engineering.
Interested in starting a project with lots of data, but not sure if I
can do it without having to pay for it. Storing lots of data and
spinning up multiple machines to process non-relational data seems like
it can't possibly be free.

**Link to work** Commits in `euler`


### Day 32: December 11, 2018

**Today's Progress** Implemented Problem 7 of Project Euler, calculating
the 10,000 prime. My solution uses a hard coded array of possible prime
factors to calculate the 10,000th in O(n log n) time.

**Thoughts** I wrote a whole blog post about why I like Project Euler so
much. It's really challenging my algorithmic thinking and forcing me to
work on fundamentals.

**Link to work** Commits in `euler`


### Day 33: December 13, 2018

**Today's Progress** Another Project Euler problem in the books. This
one was pretty straightforward once I got everything set up. I'm waiting
for them to get sneaky hard and require me to do all kinds of
optimizations but none so far.

**Thoughts** I've been doing a lot on Medium recently. It's nice to see
people reading what I have to say about code and technology. Trying to
build an audience there. Seems like having a community that I write for
could be a powerful motivator and a great networking tool when it comes
time for the job search.

Speaking of the job search, I've been reading articles online that
basically say you should start applying for jobs whenever you can build
something. I've built a lot of things at this point, including web apps
from the ground-up and my feedly Dev Digest tool. I don't think I
actually want a job right now, though. One thing I keep thinking about
is doing Italy again next summer, and I'm happy at the moment with my
writing workload as well. It's nice that there's no rush to get a job
and I can really learn things well and follow my interests.

**Link to work** Commits in `euler`


### Day 34: December 14, 2018

**Today's Progress** Project Euler #9 implemented in C today. Felt good
about this one too. I had to play around with type casting a little bit
going from a float to an int, and I learned a handy trick for seeing if
a float has decimal values:

```C
float i;

if (i == (int) i) {
    then the float is a round number
}
else {
    the float has decimal values
}
```

**Thoughts** I've been getting a little fatigued the past few days. I
find I don't want to work on code at the end of the day. Once I get into
a problem, I'm motivated. But it's the getting started that has been
hard recently.

I think it has something to do with how much time I've started spending
on writing, especially on Medium. I need to find a happy place of
writing enough without wearing myself out. Maybe I'll do code first
thing in the morning and leave writing to later in the day.

**Link to work** Commits in `euler`


### Day 35: December 15, 2018

**Today's Progress** I implemented a few Euler solutions in Python that
I've already completed in C. At first, I was wondering, "Is that it?"
because the Python solutions seemed to be so musch easier to write.

I didn't look at the C implementations when I wrote the Python code, but
structure of the solutions are still fresh in my mind. I also didn't do
any unit testing in the Python solutions, so that makes things slightly
easier too. Perhaps I'll add tests later.

**Thoughts** Still plugging along on my Medium writing as well. Another
post out today. My post advocating the Project Euler problems that I
published on December 11 got shared and has 1.4K views, 833 reads, 59
fans, and 334 claps. So, that's exciting and driving traffic. Currently
at 272 followers.

**Link to work** Commits in `euler`


### Day 36: December 17, 2018

**Today's Progress** I used the `dev-feed` application for the first
time in production today! I had to create new dev digests for Intertech,
so I ran the Feedly script aaaaand...

THERE WERE BUGS, of course.

Firstly, my API token had expired. Easy fix, but need to implement an
easier way to signal that from the command line so you know exactly
what's wrong when something is wrong. Learned about the 401 Unauthorized
status code.

Next, I had some broken links in the output digest. This is because
Feedly's API is inconsistent where it stores the proper URL for the
article. I wrote a Try/Except statement to catch KeyErrors and fix most
links. There are still some bad links slipping through, but coverage is
much better now -- acceptable level for my needs.

Finallly, I created a new repository where I can view the output
markdown files without cluttering up the application repository.
Involved a little bit of sneaky git work using gitignore and then
creating a new .git file within the existing repository. They're
together in the same directory on my machine, but the repositories are
separate on GitHub.

**Thoughts** I'm actually really happy with the results. This was the
fastest I've ever written the dev digest. The program allows me to grab
only what I need and review it quickly in plaintext, instead of waiting
for feedly to load images and stuff.

I could implement it as a web application that stores a database of past
articles, too maybe. Then, every article ever included in a dev digest
would be in one place.

**Link to work** Commits in `dev-feed` and `digests`


### Day 37: December 18, 2018

**Today's Progress** Another Project Euler problem down. I implemented
today's problem in C. Lots of tricky work with primes.

I learned about returning arrays from a function in C in order to
complete the solution with it broken up into one function doing only one
thing.

**Thoughts** They're starting to get more complicated. It's not that the
problem was super hard to solve, I just had to juggle a lot of moving
parts in my mind the way I implemented my solution.

**Link to work** Commits in `euler/c/p10`


### Day 38: December 19, 2018

**Today's Progress** I used dev-feed in production again today! Pat
needed a few more links and I was able to generate them for him in less
than 20 minutes. The dev digest is a breeze to create now!

I also reimplemented my bashrc from scratch. There were things annoying
me about how cluttered my prompt was getting and I didn't have a symlink
set up to keep my bashrc in source control. I fixed all that and now
have a simple bashrc where I understand every line.

**Thoughts** The Pragmatic Programer talks a lot about thinking about
how you work. Adding aliases and other shortcuts to my bashrc makes a
lot of sense to make me a faster developer. Now I just need to use them
and get used to them.

**Link to work** Commits in `digests` and `hello-world/bash`


### Day 39: December 20, 2018

**Today's Progress** Project Euler #11 implemented in C. The solution
was fairly straightforward again. Took me a little while to code it up
because I was feeling distracted, but by the end it worked. Happy with
my linear time solution.

**Thoughts** The problem involved a grid, but implemented it as a simple
array and used modulo to iterate over "rows." Solutions came fairly
quickly.

Side note: I'm really happy with the aliases I created in my bashrc
yesterday. They're making directory navigation so much easier now.

**Link to work** Commits in `euler/c`


### Day 40: December 21, 2018

**Today's Progress** It's my birthday, and yes I coded today!

I did another Project Euler challenge. That makes 12 completed in C.
Another tricky brain twister, but I feel good about how I did.

**Thoughts** Wow, this Medium writing is catching fire. A post I wrote
is currently #1 on Medium. It's a great feeling that so many people like
my writing. Currently over 10k views. Another post is also trending. I'm
up to 449 followers, which is the real metric I want to track moving
forward because it impacts how many people will see my future posts.

**Link to work** Commits in `euler/c`. My popular Medium post is about
[Project
Euler](https://blog.usejournal.com/consider-yourself-a-developer-you-should-solve-the-project-euler-problems-ed8d13397c9c).


### Day 41: December 24, 2018

**Today's Progress** Worked on a Python Project Euler problem. Something
easy and quick, just to get some code in today on Christmas Eve.

It's amazing how much cleaner my Python implementation looks than the
original C code. Both in terms of the language's syntax and my variable
naming and commenting.

**Thoughts** The past two days I've been with family and haven't coded.
We'll see how much I get done over Christmas and New Year's. I'm fine
not commiting code this week. I'm making my own rules for this 100 days
challenge.

**Link to work** Commits in `euler/c`


### Day 42: December 27, 2018

**Today's Progress** Started a new project today! I want to automate my
Twitter likes and retweets, especially on people who share my articles.
I implemented a barebones Tweepy bot in Python and got the repository
all set up.

**Thoughts** I'm coming up with all kinds of ideas for problems to solve
with code. Here they are so I can reference them later:

- Balderdash as a mobile app that multiple people can play
- Garner Engineering mobile app that ties into the database
- Sudoku solver
- Medium bot (idk if this is possible via the Medium API)

**Link to work** Commits in a new repository `twitter-bot`


### Day 43: December 28, 2018

**Today's Progress** Got the Twitter bot working to favorite all tweets
that mention my article.

Uses the format `url:ed8d13397c9c` as Twitter's unique URL identifier

**Thoughts** Next step is to create a list of the urls of my articles
and create a loop so that the bot favorites all tweets related to all my
articles.

**Link to work** Commits in `twitter-bot`


### Day 44: December 29, 2018

**Today's Progress** Made some updates to my bashrc to add more aliases
for setting up virtualenv quickly and setting environment variables to
print UTF-8 to the console

Also added a loop that allows me to add multiple article URLs to the
Twitter bot and favorite all the mentions of my articles at once

**Thoughts** Happy with my progress on this Twitter app so far. It has
been pretty easy, actually. I gotta think up some ideas for more
funtionality I'd like it to automate.

**Link to work** Commits in `hello-world/bash` and `twitter-bot`


### Day 45: December 30, 2018

**Today's Progress** Project Euler problem 4 is now implemented in
Python. Didn't take too long to get the solution working and it runs
quite fast. Also now extendible to values larger than 999.

**Thoughts** I worked on this from the parking lot while the family was
at church. I need to remember to push these commits when I get back on
wifi later today.

**Link to work** Commits in `euler/python`


### Day 46: December 31, 2018

**Today's Progress** New functionality added to `twitter-bot` to reply
to tweets in addition to favoriting them when they mention my articles.

Read a lot of the Tweepy docs and the Twitter API docs to get things
working with crafting reply tweets.

Also broke the program down into constituent functions and added
comments/docstrings.

**Thoughts** Feeling quite confident in my abilities at the moment. The
limiting factor on this project has been thinking of functionality I
actually want to implement and how I want it to work. Writing the code
has been fairly easy.

**Link to work** Commits in `twitter-bot`


### Day 47: January 1, 2018

**Today's Progress** Brief coding session today with New Years stuff. I
added funtionality to `twitter-bot` that also looks for any mentions of
me (@bennettgarner) and automatically likes those tweets as well.

**Thoughts** Reading the Tweepy and API docs is a little confusing. Idk
what I'd do without Stack Overflow. It's challenging b/c the docs DO
provide everything you need, but it's often buried or doesn't include
any example code of how it actually works.

**Links** Commits in `twitter-bot`


### Day 48: January 2, 2018

**Today's Progress** Back at it today and I'm working on a fun little 
project where I build a Sudoku solver. Trying to learn a little graph 
theory and get a working solution, even if it's a little messy at first.

**Thoughts** I'm not really sure how I'm going to make this Sudoku
solver work. Checking all the possible permutations of 81 squares is not
really feasible. I think the answer is to somehow create a list of
possible values for each square. Then, reduce the possible values
horizontally, vertically, and within the 3x3 boxes.

That still may not get every logical solution, though. I'm going to try
to solve this without any outside help. Luckily, there are sudoku
solvers already out there with source code available if I get REALLY
stuck. But I'm working without their guidance on this as long a
possible.

**Link to work** New repository `sudoku-solver`. Also made changes in
`bashrc` to add aliases and upgrade my version of Python to one that
supports f-strings.


### Day 49: January 3, 2018

**Today's Progress** Sudoku solver is getting tricky but I think I'm
setting myself up for success. I'm using object-oriented programming to
create and update the various grids I'll need to solve a Sudoku.

**Thoughts** This is my first time creating an OOP project from scratch.
I've had a little exposure to OOP with data structures like linked lists
etc. I've also used class-based stuff in Django. But creating it from
scratch has a learning curve.

**Link to work** Commits in `sudoku-solver`


### Day 50: January 4, 2018

**Today's Progress** `get_user_grid` is implemented, allowing me to
repeatedly prompt the user to input their sudoku grid. Not the best UI,
but it's working for now and I can change it to a graphical interface
later.

**Thoughts** As part of one of my functions, I define and return a
dictionary. I got confused for a second when the function returned
values in a different order than I supplied them. Then, I remembered
Python sorts keys in a dictionary.

Coding feels good right now. There are still hiccups and challenges, but
nothing I can't figure out and address within a few minutes of
debugging.

**Link to work** Commits in `sudoku-solver`


### Day 51: January 5, 2018

**Today's Progress** Implemented `get_possibilities` today which goes
through the user's grid and creates a mirror grid listing the possible
values for each square. Right now, it only eliminates the values
currently in the square.

Next up, I need to implement horizontal, vertical, and box elimination
for each value.

**Thoughts** Today's coding spun my head in circles for a while. First,
I had trouble conceptualizing how I'd iterate through the 81 squares in
the sudoku grid. (I'd just woken from a nap and nothing was making
sense.) Second, I ran into a confusing bug where my code went into
negative indexes of a list, adding values I expected at the front of the
list to the end instead.

All's well that ends well, I suppose, but I'm not even into the meat of
the problem solving a Sudoku.

**Link to work** Commits in `sudoku-solver`


### Day 52: January 6, 2018

**Today's Progress** Small addition to `twitter-bot` today. Added a
feature that follows back anybody who follows me or tweets my articles.

Pretty straightforward implementation

**Thoughts** I've done some digging into the Tweepy source code. It
looks like they could use some maintainers/contributors. I might try to
make Tweepy my open source project of choice to work on and get some
good contributions. The repository has over 5000 stars, but the Discord
is pretty quiet in terms of support and there are 300+ open issues.

**Link to work** Commits in `twitter-bot`


### Day 53: January 7, 2018

**Today's Progress** More work on `sudoku-solver`. I got stumped by a
problem in one of my functions right before the Clemson-Alabama game
is going to come on, so I'll start coding tomorrow with a problem.

**Thoughts** Long, frustrating, but all-consuming coding session today.
I restructured the app a little more to move the initialization of the
possibilities grid into a different function from checking horizontal
matches.

**Link to work** Commits in `sudoku-solver`


### Day 54: January 8, 2018

**Today's Progress** Figured out my problem in the `check_horizontal`
function in `sudoku-solver`. `.remove()` gets rid of the value in place
without needing to put or return anything.

Also added to my bashrc.

**Thoughts** My bigger question, that I'm still stumped on, is why
modifying the `p_rows` variable also modifies `p` directly. I need to do
some more learning about Python scope. It's working, nevertheless.

**Link to work** Commits in `sudoku-solver`


### Day 55: January 9, 2018

**Today's Progress** I got rid of the `get_rows` method for the Grid
class. It wasn't doing anything for me that I couldn't do already, so I
refactored the code.

I also started thinking this whole project would be easier if each data
point were a node connected to it's column and row. So I'm working on a
new implementation (starting from scratch...) that uses Nodes in a
graph, which I realize I should have done from the beginning.

**Thoughts** This is a good learning exercise and I'm glad I'm figuring
out these challenges rather than on a job or something. It's messing
with my brain, but I'm getting more comfortable with stuff.

**Link to work** Commits in `sudoku-solver` in `solver.py` and
`nodal.py`


### Day 56: January 10, 2018

**Today's Progress** The new object-oriented Grid/Node classes are
working, as are their methods! I can now accept user input to build the
grid as well.

One nice thing about using custom objects is I don't have to keep two
separate grids--one for answers and the other for possiblities--anymore.
Instead, it's all wrapped into the variables associated with each Node.

I also worked on my Twitter bot today to add some nice progress bars
using a new package I discovered called tqdm.

**Thoughts** I kind of had to scrap my old code, which stinks. But some
of it I can refactor to work under the new architecture. I'll delete
archive.py once I'm past the point where I was with the old version.

**Link to work** Commits in `sudoku-solver` and `twitter-bot`


### Day 57: January 11, 2018

**Today's Progress** I'm really pleased with my progress narrowing down
possibilities. Vertical, horizontal, and box based elimination are now
implemented.

**Thoughts** I tried to input a whole sudoku test puzzle today to try it
out for the first time and see how far it gets. The problem is the user
experience is horrible. I'm going to need to refactor the code to accept
text files instead.

**Link to work** Commits in `sudoku-solver`


### Day 58: January 12, 2018

**Today's Progress**

**Thoughts**

**Link to work** Commits in `sudoku-solver`


### Day 59: January 13, 2018

**Today's Progress** My sudoku solver works! At least to solve simple
puzzles. Idk if there are some logically-correct sudokus that my solver
couldn't eventually find the answer to.

User experience is much better now too, bc I used an input txt file to
add the puzzle.

**Thoughts** I feel good having this project completed. It took me a
while, but I feel like it pushed me to learn new stuff, and I feel
comfortable with classes and OOP in a way I didn't before.

**Link to work** Commits in `sudoku-solver`


### Day 60: January 14, 2018

**Today's Progress** I started on a React app today. I've decided to
take the plunge on full-stack web dev. Much more interested in the
backend stuff than the front end, but I think I'll be surprised how much
logic is involved in building React components, too.

**Thoughts** This is simultaneously working on JavaScript, Node.js, and
React for me -- all things that are either new or far removed from what
I've worked on recently. I'm excited about it. The tutorial makes sense
so far and everything is working on my local machine.

**Link to work** Commits in `react-hello`


### Day 61: January 15, 2018

**Today's Progress** Finished the official React tutorial, building a
Tic Tac Toe game.

**Thoughts** I felt really good about my grasp of the concepts
until I tried to do some of the extra challenges. I think I just don't
understand how React renders components. Bolding and adding loops into
the render process I couldn't get it to compile.

**Link to work** Commits in `react-hello`


### Day 62: January 16, 2018

**Today's Progress** Watched some videos and feeling better about my
understanding of React. Going to start building some things from scratch
now.

I started playing around with it, but got stuck when I attempted to
install Bootstrap as a dependency. Babel is having trouble with the
build.

Also wrote about variable names on Medium and worked on the variable
names in my Twitter bot.

**Thoughts** I think I'll have a pretty solid stack if I've got
experience with Postgres/MySQL, Django/Node.js, and React + Bootstrap,
all deployed to Google Cloud.

I'll want some more experience with vanilla JavaScript. Docker is
another place to get experience.

**Link to work** Commits in `twitter-bot` - didn't have internet to push
my react commits but also worked on `react-hello`


### Day 63: January 17, 2018

**Today's Progress** I've learned a little bit more about rendering
React components. Now I know how to render a table using a for loop in a
helper function.

**Thoughts** Gonna try again with Bootstrap in this React app. Maybe I
can get it working better this time.

**Link to work** Commits in `react-hello`


### Day 64: January 18, 2018

**Today's Progress** Bootstrap is working and I have my Tic Tac Toe
application looking nice, including conditional formatting. Getting more
comfortable with React and reacquainted with Bootstrap.

**Thoughts** I'm excited to start putting this together into a full
stack app. Something running on Google Cloud with a Django controller
and React view.

Maybe I can even refactor Garner Eng with React components.

**Link to work** Commits in `react-hello`


### Day 65: January 19, 2018

**Today's Progress** I deployed a react app to google app engine today
and I messed around with dependencies and customizations of a React
portfolio app.

**Thoughts** Confirmed: I don't enjoy web design. I can
appreciate good designs, but dealing with the CSS on my portfolio was
getting me super frustrated. I was constantly going back and revising
things or deleting my progress altogether. Maybe I'm going about it the
wrong way, though. In any case, I much prefer tricky logic, routing,
tracking down problems with dependencies, etc.

**Link to work** Commits in `portfolio` which are deployed to
[Google App Engine](https://portfolio39.appspot.com)


### Day 66: January 20, 2018

**Today's Progress** A bunch of random stuff. Added icons to portfolio.
Fixed some stuff in my vimrc. Wrote a promposal into TicTacToe that I
didn't commit to GitHub.

**Thoughts** Went to Hacker Hours today, and I'm buzzing from the
conversations I had. I met an experienced developer, Brian Kelly, and
was able to keep up with the stuff he was talking about. I wanna work
with him on SongPro, an application he has developed for rendering
guitar tabs.

I also was able to help two people with the coding projects they were
working on. One just needed to update one of his dependencies to get his
build working. The other I helped him untangle a Django API mess he had
gotten into.

**Link to work** Commits in `portfolio`, `guitar-tabs`, and `vimrc`


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
