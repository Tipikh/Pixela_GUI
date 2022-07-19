# Pixela GUI

A simple GUI written in Python (tkinter) for the [Pixela](https://pixe.la)'s habit tracking API.


## What is Pixela

Pixela is an API based habit tracker that allows you to create graphs like this to track your habits (if you're used to GitHub you've probably seen them before) : 

--- sample_graph image ---

One graph corresponds to one habit. For exemple you can create a graph "Running" where you'll put the number of km you ran everytime you go to run. 



## Why this project ? 

This was one of my first "serious" project on my journey to learn programming. I made it a few month ago but decided only recently to put it online. 

Also as I am trying to build good long term habits I thought it would be a good idea to make two birds one stone by programming a GUI for a habit tracker.

## What did I learned ? 

* Object Oriented Programming in Python
* API call / HTTP Requests
* Build a Graphical User Interface (tkinter)
* Project structure and organisation 
* GitHub

 

## How to use the App
The interface is very basic and therefore very intuitive but I'll guide you through it anyway. 

After starting the app, you'll end up on the "Welcome Page". From here you can chose to create an Account or to Login directly if you already have one. You can also chose to Delete an existing Account

--- welcome_page image ---

### Create an Account

Simply enter a username and a password, then click the "Create Account" button and wait for the confirmation. You must also accept the [terms of service](https://github.com/a-know/Pixela/wiki/Terms-of-Service) by checking the box. 

The username must be lowercase, with letters and numbers only.

--- create_account image  ---     

### Log In

Enter your Username and Password and click the "Log in" button.

--- log_in image ---


### Visit your Pixela's personal page

Once logged, you access the User Page where you can chose to create or update your graphs. 
On this page, there is also a link to your personal pixela's page where you can see all your graphs and account informations. 
Your Graphs are at the bottom of the page, click on the graph's name to open your graph and have a better view of your progress. 

--- graph_detailed image ---

### Create a graph

For creating a graph, you must first chose a graph name. Then you can choose the unit with which you want to measure your habit. For exemple for the habit "Running" you can chose to measure it in km but you can also measure it in miles or in minutes.

--- create_graph image ---

### Update a graph

For updating a graph, you must first select a graph/habit. Then indicate how much you've done and select the date on which you've done it.  Finally, click on the "Update" button and wait for confirmation.

On this page you can also delete a graph simply by selecting the graph et click the "Delete Graph" button. 

--- update_graph image ----

## Send feedback

If you encounter a problem or want to give feedback on anything about the project, feel free to send an email at thibautp10@hotmail.fr , would be really appreciated.


