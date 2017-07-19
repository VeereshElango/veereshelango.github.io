---
layout: post
title: Can a Machine write Thirukkural ?
excerpt: "A Character level LSTM Model has been trained to learn Thirukkural literature and write poem with a given starting word."
categories: [LSTM]
comments: true
tags: keras tamil lstm rnn 
image:
  feature: https://unsplash.it/1250/475?image=1073
  credit: patrick tomasso
  creditlink: https://unsplash.com/@impatrickt
---


Inspired by Andrej Karpathy's blog post [The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/), I was super excited to apply the LSTM and see the results on a different dataset.
Finally, I chose the poem [Thirukkural]((https://en.wikipedia.org/wiki/Tirukku%E1%B9%9Ba%E1%B8%B7)) from one of the oldest surviving languages called [Tamil](https://en.wikipedia.org/wiki/Tamil_language).

The goal of this attempt is to create a neural network model which learns the style of Thirukkural
poem and writes the poem following the same style for a given starting word. 
This is achieved using popular LSTM (Long Short Term Memory) neural network model.

Nowadays, Machine Learning creates a huge buzz and drums up the enthusiasm within everyone to know about it. But for the amateurs, knowledge
of neural network algorithms are a hurdle to admire the power of Machine Learning.

Keeping that in mind, I thought to give a brief layman introduction followed by a technical introduction
 to RNN and LSTM neural network models.
  
## Layman intro about RNN and LSTM

The brain functionalities are the inspiration for most of the neural network algorithms.
To understand this model, we have to recollect how we learned alphabets and numbers.

For example, we will start to learn pronunciation of first four alphabets (A,B,C,D) individually, then 
  we will again try to say from A to D. Then we will learn next four alphabets (E, F, G, H), then we will again try to 
  say from A to H. If you notice, we were looping from the first alphabet everytime whenever we learn new 
  alphabets. Through this, we not only learn alphabets but also their sequence.
  
This is the logic behind Recurrent neural networks. It uses what it has learned from the previous 
  inputs while learning the new input. It has a problem with very long input which was blown-away by LSTM.

## Technical intro about RNN and LSTM 
Recurrent Neural Network is a neural network model in which each hidden layer receives both input from the previous layer and 
input from itself at each step. This enables it to hold information across inputs which can be thought as a memory.

The problem of Recurrent Neural Network is that its memory is very short term.
This is solved in Long Short Term Memory networks (LSTM).

Long Short Term Memory (LSTM) network is kind of recurrent neural network which are capable of learning long-term dependencies. 
LSTM has a cell state which runs through all the modules of the neural network.
The cell state is convenient for the information to flow along it unchanged.
There are four gates which regulate the addition and removal of information from the cell state.

As LSTM holds the information for long term, it can be trained with text file at character level as input, so that it learns to predict the next character in the sequence.
 The other interesting applications of this RNN/LSTM model are music generation, image captioning, language translator and even writing The Bible.

For further understanding about this neural networks, check the [references](#references).


## About Dataset - Thirukkural
[Thirukkural](https://en.wikipedia.org/wiki/Tirukku%E1%B9%9Ba%E1%B8%B7) is one of the most prominent and celebrated works in Tamil Literature. It is also one of the
most widely translated non-religious works in the world.
It is written by the poet [Thiruvalluvar](https://en.wikipedia.org/wiki/Thiruvalluvar) who lived in the 6th century. It is a unique ethical guide which delivers code of 
 conduct to the mankind to follow for all time to come. 
In total, there are 1330 couplets (two lines joined by rhyme) which are divided into 133 sections with 10 couplets each.
Each couplet has exactly 7 words, 4 in one line and 3 in next.

Example couplet from Thirukkural (no : 78)
```
அன்பகத் தில்லா உயிர்வாழ்க்கை வன்பாற்கண்
வற்றல் மரந்தளிர்த் தற்று
```
Explanation in English would be 
```
 Without love in the heart, 
 Life is like a sapless tree in a barren desert. 

```
## Why this dataset?
Since childhood, I admired how he expresses great morals in just 7 words.
 He wrote only 1330 couplets which almost delivers all the essential morals
   for a person to lead a successful life.
This provoked the curiosity within me to know how it would be if Thiruvalluvar has written more Thirukkural.
   Crazy thought !! 

## About the model
The first step is to create the dataset. I found a Thirukkural literature in json format. I parsed the json file
 and created a text file with 1330 couplets alone.
 
The next step is to feed this file as input to LSTM model. I took the sample
[code](https://github.com/fchollet/keras/blob/master/examples/lstm_text_generation.py) from Keras Github repository and made changes to adapt to this dataset.
It is a simple model with single LSTM layer with 128 neurons. It is fed with very small
data of 1330 couplets with each of 7 words, in total 9310 words. 
The model is trained for 20 iterations. 

The code is available [here](https://github.com/VeereshElango/text_generation_thirukkural).

## Results

The results definitely show Thiruvalluvar cannot be replaced by Machine anytime soon. But if you notice the results, astonishingly the 
machine (LSTM) has learnt to produce sensible Tamil words with punctuations. I was also amazed that how this 
  simple model learnt the syntax of Thirukkural such as nearly four words in the first line and three words in the 
  second line. 

Start Word : "சாதலின் "
```
சாதலின் இல்லாய் நினிபன் பெருந்தகை 
சிலையார் யாணென்னும் பயர்.
```
```
சாதலின்ற் பொருட்செல்வம் தாண்டற்றும் மருந்து 
கேணல் சிறப்பின் இரந்து.
```
Start Word : "   காதல்"
```
காதல்ல்லாது செய்யார் முன்றி தீயும் 
அருவியல் போர் கேது.
```
```
காதல்டு யாதெனின் நெஞ்சத்தான் கண்ணுடையார் க
ேதலிற் கொள்வாரோட்க்கு விருந்து.
```
Start Word : "  காமம் "
```
காமம்ன்தும் இடும்பை பஇடைச் சிறப்பின் இரவுருமாடு 
ஒரிவது குறவினும் பெறும்.
```
```
காமம்ணிடும் பெறுப்சின் செய்யும் அவர்தென்பீர் 
கண்ட செல்வம் தரும்.
```

Start Word : " இறைவன் "
```
இறைவன் பத் தலையபின் துணையாகை 
நீக்கிக் காமந்த நூர்.
```
```
இறைவன் முன்றினும் உய்வாத்தல் இருவறுப் 
துணையாது விழைந்து விடல்.
```

Start Word : "  ஒழுக்க"
```
ஒழுக்கத் தலையபின் துணையாது நீங்கி 
விருமுங்க்கல்ல செய்யார் மாத்து.
```

Start Word : " உயர்ந்த"
```
உயர்ந்த தஒழில் தூழ்கச் சிறப்பின் 
இரந்தவற்று விகர்முடியார் அனைத்து.
```
```
உயர்ந்த யஇருள் நோக்கெச் சுடைத்து வேநீால் 
வடிவார் என்றார் அனைத்து.
```

Start Word : " பெருமை "
```
பெருமை எய்தார் முற்றியது எண்ணிக் 
கூடியமை என்னும் செருக்கு.
```
```
பெருமை கூற்றம் காதல் அல்லசெய்தல் 
இன்னை அருமாப் படும்.
```

## Take away
* LSTM is capable of holding information for long term, hence we can say it has memory 
* LSTM networks are capable of modelling temporal aspects of data and hence have been used widely for text, videos, and time-series


## References 
#### RNN/LSTM
* [The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/)
* [Understanding LSTM Networks](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)
* [Anyone Can Learn To Code an LSTM-RNN in Python (Part 1: RNN)](https://iamtrask.github.io/2015/11/15/anyone-can-code-lstm/)
* [Understanding LSTM and its diagrams](https://medium.com/@shiyan/understanding-lstm-and-its-diagrams-37e2f46f1714)
* [Composing Music With Recurrent Neural Networks](http://www.hexahedria.com/2015/08/03/composing-music-with-recurrent-neural-networks/)

#### Thirukkural
* [Thirukkural - by Britannica](https://www.britannica.com/topic/Tirukkural)
* [Thirukkural - by Wikipedia](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=2&cad=rja&uact=8&sqi=2&ved=0ahUKEwic78TMjfLUAhXLfRoKHUSHDmgQFggxMAE&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FTirukku%25E1%25B9%259Ba%25E1%25B8%25B7&usg=AFQjCNHgAu5JoMvimy5DIy6LL3p1Wl10Lg)

**Note:** *If you liked this article, and would like to see more like this, all you have to do is to press the little heart button at the bottom, and I’ll know :)*