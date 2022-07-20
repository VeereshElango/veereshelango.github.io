---
title: How did I create my automated AI-powered Tamil lyrics generator?
excerpt: "My story about transforming an idea to a working application using Google Colab and Tensorflow.js"
comments: true
categories:
    -  posts
tags:
    - nlp
    - tamil
    - lstm
    - text_generation
    - tensorflow
header:
  overlay_image: /assets/images/tamil_song_lyrics_header.jpg
  overlay_filter: "0.5"
  caption: "Photo credit: [**Pexels**](https://pexels.com)"
toc: true
toc_sticky: true
---
One fine self-quarantined day, I was trying to flatten my wife 
by singing my favourite Tamil song

>நீயும் நானும் அன்பே<br>
>கண்கள் கோர்த்துக்கொண்டு<br>
>வாழ்வின் எல்லை சென்று<br>
>ஒன்றாக வாழலாம்<br>

<cite>Penned by Kabilan Vairamuthu in Imaikkaa Nodigal movie. [Lovely song](https://www.youtube.com/watch?v=dImiR3Sr8Wo)</cite>
 {: .small}

Well she replied
> That's great! It would be even better if you could write on your own for me.


Fair claim, but that's not my cup of tea. On the other hand, I can't let down her request even without a trial.
That's where I pulled a feather from the cap of Data Science, _Text generation using recurrent neural networks_ and created an application to
generate lyrics. 
{: .text-justify}

Some might be curious to get your hands on the [code](https://cutt.ly/1t7RMno) and 
[application](https://cutt.ly/Mt7b1aD). 
For others, I will take you through my journey in transforming the idea to a working application.
{: .text-justify}

## Data Collection
The first and foremost thing is data, and it is not available ready-made in this case. I have to prepare the dataset by myself.
I couldn't find many websites where Tamil song lyrics are written in Tamil - Weird. At last, 
[tamilpaa.com](https://www.tamilpaa.com/) suited my needs. I utilized the python library
called [beautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#) to scrap the songs from tamilpaa.com.
{: .text-justify}

## Model choice
The aim was to design a model which could learn the pattern from the song lyrics and 
generate them on the trigger. The characters and words in the song lyrics
have some sort of dependency with preceding and following. Thus, Recurrent neural networks (RNN) would be a suitable choice
for this.
{: .text-justify}

<figure class="align-right">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/images/karpathy_blog.png" style="width:300px;height:200px" alt="A snapshot from Andrej Karpathy blog.">
  <figcaption>A snapshot from Andrej Karpathy blog.</figcaption>
</figure> 
It would be inappropriate if I miss out this <remarkable></remarkable> article [The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) by Andrej Karpathy where I understood the basics and effectiveness of RNN. In this article, he explains how 
RNN should be used for creating character-level language models, with the examples on top of Paul Graham' essays and
Shakespeare works. 
{: .text-justify}

<figure class="align-right">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/images/tensorflow_page.png" style="width:300px;height:200px" alt="A snapshot from Tensorflow's tutorial on Text generation with RNN">
  <!--<figcaption>A snapshot from Text generation with RNN tutorial.</figcaption>-->
</figure> 

Following his work, there is a Tensorflow's tutorial on [Text generation with RNN](https://www.tensorflow.org/tutorials/text/text_generation),
where each step is explained extensively. I 
utilized the notebook from that tutorial and modified for my purpose. Hence, I 
would take you through the interesting sections rather than repeating all technical steps. 
{: .text-justify} 

## Data preparation
The teacher presents the concept in the way that a student could learn. 
Similarly, the data has to be prepared in the way that the RNN could understand.

**Step1:** Combine all the song lyrics into one string variable.

**Step2:** Create an index for each unique character and encode the whole
string with their corresponding index

**Step3:** Divide the encoded string into sequences of length **N**+1 characters. <br>
For example, for **N**=15 the below stanza 
````
நீயும் நானும் அன்பே
கண்கள் கோர்த்துக்கொண்டு
வாழ்வின் எல்லை சென்று
ஒன்றாக வாழலாம்
````
will be divide sequences of length 16.

````
'நீயும் நானும் அன'
'்பே\nகண்கள் கோர்த'
'்துக்கொண்டு\nவாழ்'
'வின் எல்லை சென்ற'
'ு\nஒன்றாக வாழலாம்'
````

**Step4:** Each sequence is divided into input and target text with the length of **N**. <br>
For example, the above sentences will break as 
````
Sequence    : நீயும் நானும் அன
Input       : நீயும் நானும் அ
Target      : ீயும் நானும் அன
````

**Step5:** Feed in the input and target pairs in their encoded form to the model
## How model gains wisdom?
Are you wondering how the model will learn by feeding the data in this fashion?

In simple words, it boils down to the concept of probability. For example, 
following the above example model tries to learn
* the probability of <kbd>'ீ'</kbd> given the context of <kbd>'ந'</kbd>
* the probability of <kbd>'ய'</kbd> given the context of <kbd>'ந ீ''</kbd>
* the probability of <kbd>'ு'</kbd> given the context of <kbd>'ந ீ ய'</kbd>
* the probability of <kbd>'ம'</kbd> given the context of <kbd>'ந ீ ய ு''</kbd>
* ....
* the probability of <kbd>'ன'</kbd> given the context of <kbd>'ந ீ ய ு ம ் ந ா ன ு ம ் அ'</kbd>


![no-alignment]({{ site.url }}{{ site.baseurl }}/assets/images/lstm_tamil_lyric.jpg)

During test time, a character will be fed to the RNN, and it returns the distribution
of characters that are likely to come next. Sample the distribution and feed it
back to the RNN to get the next letter. Repeat this process until you're
sampling text.
{: .text-justify} 

After a few trials, I settled up with using two [Long short-term memory (LSTM)](https://en.wikipedia.org/wiki/Long_short-term_memory) layers
stacked on top of each other. These layers are uni-directional which means it has the capacity to learn from preceding 
characters only. As I sensed results with human readable, spelling mistake less and poematic structure for this initial attempt, I stopped tuning.
{: .text-justify} 

## Presentation
One of the key learning in my experience would
be the importance of iteratively developing the product from end-to-end. In other words,
Agile way of development. So, let's make it usable.
{: .text-justify} 

I utilized amazing [Tensorflow.js](https://www.tensorflow.org/js) for this purpose. It enables us
to develop and use the models directly in a browser which is perfectly suitable for my case as I will be deploying
in Github pages at the end.
{: .text-justify}   

## Results & Issues

### Sample results

````
உயிரே நீதானே நாளை நமதடா
ஆம்பளையே தெரியாதா?
அடி அழகே அழகு
நில்லும் நிலா நாதன் ஊஞ்சலா
திருத்தணி தேரினில் பி
````

````
காதல் —
இங்கே இல்லை வாழ்விலே
காலை விடிந்து போகும் வானவில் கீழே
சுக வாள் முனையே நீ வந்தாய் வாழ்விலே
கனவுகள்
````

````
கண் —
மலர்ந்திடும் இந்த பூமி மட்டும்
பக்கம் வந்து நீயும் கூட உன்னை ஓயாது திறக்கும்
வானம் வரை என்னை விட வ
````
### What works?

<figure class="align-left">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/images/success.gif" style="width:150px;height:150px" alt="success">
</figure> 
The model was able to generate **meaningful words** almost every time without spelling mistakes. Such as

இங்கே -> here <br>
காலை -> morning <br> 
பூமி -> earth <br>
கனவுகள் -> dreams

Also,**meaningful short phrases** <br>
* 'உயிரே நீதானே நாளை நமதடா' -> You are my life. Tomorrow is ours<br>
* 'காதல் — இங்கே இல்லை வாழ்விலே' -> Love is not here in life<br>
* 'வானம் வரை' -> Till cloud <br>

### What is not working?
<figure class="align-right">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/images/thinking.gif" style="width:150px;height:150px" alt="success">
</figure> 

* Not generating meaningful long phrases/stanzas
* Context switching
 
For example from first sample, <br>
It starts like woman singing about a man.<br>
உயிரே நீதானே -> You are my life <br>
நாளை நமதடா -> Tomorrow is ours <br>
ஆம்பளையே தெரியாதா?-> Don't you know this man <br>

Now, man singing about woman <br>
அடி அழகே -> Hey beautiful<br>

This line could be either from man or woman depending on future lines <br>
அழகு நில்லும் நிலா நாதன் ஊஞ்சலா -> Does the Man's/Lord Muruga's swing bed is beautiful like moon? <br>

### Future works
* Could divide the songs into different genres such as love, mother, patriotism, devotional etc., and train models per genre
* Could try with bi-directional networks as the words/characters has some connection with both preceding and following.
* It would be interesting to train model for a particular lyricist alone. Eg., for [Kannadasan](https://en.wikipedia.org/wiki/Kannadasan),
[Na.Muthukumar](https://en.wikipedia.org/wiki/Na._Muthukumar), [Vairamuthu](https://en.wikipedia.org/wiki/Vairamuthu). 

## Conclusion
> Always walk through life as if you have something new to learn, and you will.

<cite>Vernon Howard</cite>
{: .small}

Great learning & satisfaction in making a working application.

What are you waiting for?

Use this [code](https://cutt.ly/1t7RMno) to start with and build your own automated lyrics generator for your favourite language!
Let me know your story.

*Do you have any questions about this post? Was this article interesting for you?
Ask your questions/thoughts in the comments below and I will get notified.*

## Other related works

* [Lyrics Engineering by Madan Karky](http://madhankarky.blogspot.com/2009/11/lyrics-lyric-engineering.html)
* [Automatic Tamil lyric generation based on image sequence and derived tune](https://ieeexplore.ieee.org/document/7154828)
* [Automatic Tamil lyric generation based on ontological interpretation for semantics](https://www.ias.ac.in/article/fulltext/sadh/039/01/0097-0121)
* [N-Gram Based Approach to Automatic Tamil Lyric Generation by Identifying Emotion](https://link.springer.com/chapter/10.1007/978-81-322-0740-5_111)
