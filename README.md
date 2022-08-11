# Pixela GUI

A simple GUI written in Python (tkinter) for the [Pixela](https://pixe.la)'s habit tracking API.


## What is Pixela

Pixela is an API based habit tracker that allows you to create graphs like this to track your habits (if you're used to GitHub you've probably seen them before) : 

<p align="center">
   <img src="https://user-images.githubusercontent.com/52866589/180415900-09ab83c9-be79-482b-9862-757ea661d4f5.png" width=100% height=100%>
</p>


One graph corresponds to one habit and each "pixel" corresponds to one day. For exemple you can create a graph "Running" where you'll put the number of km you ran everytime you go to run. 



## Why this project ? 

This was one of my first "serious" project on my journey to learn programming. I made it a few month ago but decided only recently to put it online. 

Also as I am trying to build good long term habits I thought it would be a good idea to make two birds one stone by programming a GUI for a habit tracker.

## What did I learn ? 

* Object Oriented Programming in Python
* API call / HTTP Requests
* Build a Graphical User Interface (tkinter)
* Project structure and organisation 
* GitHub

# Requirements

- Python ≥ 3.6

# Installation

First install the required packages 

```bash
pip3 install -r requirements.txt 
```

Then you can do 

```bash
python3 main.py
```
 

## How to use the App
The interface is very basic and therefore very intuitive but I'll guide you through it anyway. 

After starting the app, you'll end up on the "Welcome Page". From here you can chose to create an Account or to Login directly if you already have one. You can also chose to Delete an existing Account


<p align="center">
   <img src="https://user-images.githubusercontent.com/52866589/180417185-d94008a2-b7ec-4533-bc6e-c90a5951aa5b.png" width=30% height=30%>
</p>


### Create an Account

Simply enter a username and a password, then click the "Create Account" button and wait for the confirmation. You must also accept the [terms of service](https://github.com/a-know/Pixela/wiki/Terms-of-Service) by checking the box. 

The username must be lowercase, with letters and numbers only.

<p align="center">
   <img src="https://user-images.githubusercontent.com/52866589/180417024-993b68ef-7fcf-4e35-a200-c5dde9da7488.png" width=30% height=30%>
</p>


### Log In

Enter your Username and Password and click the "Log in" button.

<p align="center">
   <img src="https://user-images.githubusercontent.com/52866589/180417199-c2a9a774-00d0-4f42-8d19-3f54f1298bbc.png" width=30% height=30%>
</p>


### Visit your Pixela's personal page

Once logged, you access the User Page where you can chose to create or update your graphs. 
On this page, there is also a link to your personal pixela's page where you can see all your graphs and account informations. 
Your Graphs are at the bottom of the page, click on the graph's name to open your graph and have a better view of your progress. 

<!---
--- graph_detailed image ---
<p align="center">
   <img src="https://user-images.githubusercontent.com/52866589/180415900-09ab83c9-be79-482b-9862-757ea661d4f5.png" width=30% height=30%>
</p>
-->

### Create a graph

For creating a graph, you must first chose a graph name. Then you can choose the unit with which you want to measure your habit. For exemple for the habit "Running" you can chose to measure it in km but you can also measure it in miles or in minutes.

<p align="center">
   <img src="https://user-images.githubusercontent.com/52866589/180417190-c501230a-f197-4be4-8bc3-a9214e75b091.png" width=30% height=30%>
</p>


### Update a graph

For updating a graph, you must first select a graph/habit. Then indicate how much you've done and select the date on which you've done it.  Finally, click on the "Update" button and wait for confirmation.

On this page you can also delete a graph simply by selecting the graph et click the "Delete Graph" button. 

<p align="center">
   <img src="https://user-images.githubusercontent.com/52866589/180417213-b5802b19-a4a7-4f02-a1ca-eb8a56e91fb0.png" width=30% height=30%>
</p>


## Send feedback

If you encounter a problem or want to give feedback on anything about the project, feel free to send an email at thibautp10@hotmail.fr , would be really appreciated.


