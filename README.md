# Facebook Chat Statistics

A small program written in Python that lets you see statistics of any given Facebook Messenger conversation. I used this as a Valentines day surprise for my girlfriend and it is therefore focused on only conversations between two persons, but can be modified and used for any other purpose. This project was inspired by [this](https://www.reddit.com/r/dataisbeautiful/comments/7xicua/my_girlfriend_made_a_visualization_of_all/) Reddit post.

## Features

The program fetches data such as:

* Start time
* End time
* Number of days
* Number of messages
* Number of words
* Average length of messages
* Average messages per day

It also plots using Matplotlib the following diagrams (see pictures below)

* Who texts the most
* Timeline
* Activity by day
* Activity by weekday

## Images

<img src="pics/who_texts_the_most.png"/>
<img src="pics/timeline.png">
<img src="pics/activity_by_day.png">
<img src="pics/activity_by_week.png">

## Running locally

Firstly you will need to download or clone the repository.

### Download your Facebook conversations to a .json file
Download your Facebook data by following [these](https://www.facebook.com/help/212802592074644?helpref=uf_permalink) instructions and chosing the format to be JSON. Note that you only have to download your messages in order for this program to work.

### Run it
1. First you will have to install the needed packages. The script uses Matplotlib to plot. Matplotlib can be installed by typing

```
pip install matplotlib
```

2. Edit the Python script so that it loads your parsed conversation by replacing the path below to the path of your conversation
```
data = json.load(open('message.json'))
```
You can also change the names declared in the script to your liking.

3. Run the script with
```
python MessengerStats.py
```

Enjoy!
