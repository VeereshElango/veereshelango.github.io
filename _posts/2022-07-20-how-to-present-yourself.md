---
title: How to present yourself?
classes: wide
excerpt: "an alternative way to present yourself in a visully rich and engaging timeline method"
comments: true
categories:
    -  posts
tags:
    - data-visualization
    - story-telling
    - timeline
header:
  overlay_image: /assets/images/timeline-snapshot.JPG
  overlay_filter: "0.5"
---

A personal blog gives people a chance to get to know a person and their work. It made me think about how to better present myself to the world. Typically, we would do this by creating an about page where we would explain our experience, education, and life experiences. To put it another way, we present data about ourselves as text, images, and videos. As a reader, I find it hard to stay engaged if I am reading a lot of texts that are not engaging.

To enhance the reader's experience, we have to think from their shoes. Depending on the about page, the reader could be interested in academic work, professional experience, accomplishments or all. In my opinion, most of the readers could benefit from a good overview of education, experience and life events. So what are better ways to do that?

> Once you are a data scientist, you are always a data scientist!

This a challenge that calls for data visualization and storytelling from a data scientist perspective. An interesting way to convey a person's or organization's story is through a timeline. Therefore, I chose to make a timeline of my life story. After some research, I found [Timeline.js](http://timeline.knightlab.com/), which is one of the best timeline javascript library. To look at the result, check [here](https://veereshelango.github.io/timeline/).

<figure class="align-center" >
    <a href="{{ site.url }}{{ site.baseurl }}/timeline">
    <img src="{{ site.url }}{{ site.baseurl }}/assets/images/timeline-snapshot.JPG" style="box-shadow: 10px 10px 5px #ccc;      -moz-box-shadow: 10px 10px 5px #ccc;      -webkit-box-shadow: 10px 10px 5px #ccc;   -khtml-box-shadow: 10px 10px 5px #ccc;" alt="a snapshot of my timeline"></a>
    <figcaption>a snapshot of my timeline</figcaption>
</figure> 


This library not only offers an aesthetically appealing user interface, but it also makes it simple for anyone to make a timeline. The data is entered into a Google spreadsheet template and made publicly available. The url of this spreadsheet is used as a parameter to create the TL.Timeline object inside the html page. There are couple of other ways to use this library which can be found [here](http://timeline.knightlab.com/docs/). 

This type of visualization presents similar data in a interactable fashion and also enables the reader to interpret from a spatial perspective. Although timeline needs some improvement to make it better, I thought to share that there is an alternative way to present yourself in blogs or interviews.

If you have tried something similar or different methods to present yourself, feel free share with me in the comment section. 