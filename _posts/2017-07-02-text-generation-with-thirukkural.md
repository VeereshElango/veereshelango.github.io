---
layout: post
title: Can Machine write Thirukkural ?
excerpt: "Character level LSTM Model trained to learn Thirukkural literature and fed with single word to write more kural."
categories: [LSTM]
comments: true
image:
  feature: https://images.unsplash.com/photo-1440635592348-167b1b30296f?crop=entropy&dpr=2&fit=crop&fm=jpg&h=475&ixjsv=2.1.0&ixlib=rb-0.3.5&q=50&w=1250
  credit: thomas shellberg
  creditlink: https://unsplash.com/photos/Ki0dpxd3LGc
---


Inspired by Andrej Karpathy's blog post [The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/), I was super excited to apply the LSTM and see the results on a different dataset.

Before we dive in I thought to give a simple intro to RNN and LSTM. 

## Short intro about RNN and LSTM 
Recurrent Neural Network is a neural network model in which each hidden layer receives both input from the previous layer and 
input from itself at each step. This enables it to hold information across inputs which can be thought as a memory.

The problem of Recurrent Neural Network is that its memory is very short term.
This is solved in Long Short Term Memory networks (LSTM).

Long Short Term Memory (LSTM) networks are capable of learning long-term dependencies. 
LSTM has a cell state which runs through all the modules of the neural network.
The cell state is very easy for the information to flow along it unchanged.
There are four gates which regulate the addition and removal of information from the cell state.

For further understanding about this neural networks, check the [references](#references).


## About Dataset - Thriukkural
[Thirukkural](https://en.wikipedia.org/wiki/Tirukku%E1%B9%9Ba%E1%B8%B7) is one of the most prominent and celebrated works in Tamil Literature. It is also one of the
most widely translated non-religious works in the world.
It is written by the poet [Thiruvalluvar](https://en.wikipedia.org/wiki/Thiruvalluvar) who lived in the 6th century. It is a unique ethical guide which delivers code of 
 conduct to the mankind to follow for all time to come. 
In total, there are 1330 couplets which are divided into 133 sections with 10 couplets each.
Each couplet has exactly 7 words, 4 in one line and 3 in next.

## Why this dataset?
Since childhood, I was admired how he expresses great morals in just 7 words.
 He wrote only 1330 couplets which almost delivers all the essential morals
   for a person to lead a successful life.
This provoked the curiosity within me to know how it would be if Thiruvalluvar has written more Thirukkural.
   Crazy thought !! 

## About the model
The model is built using Keras framework. It is a simple model with single LSTM layer with 128 neurons. It is fed with very small
data of 1330 couplets with each of 7 words, in total 9310 words. 
The model is trained for 20 iterations. 

## Results

The results definitely show Thiruvalluvar cannot be replaced by Machine anytime soon. But if you notice the results, astonishedly the 
machine (LSTM) has learnt to produce sensible Tamil words with punctuations. I was also amazed that how this 
  simple model learn the syntax of Thirukkural such as nearly four words in the first line and three words in the 
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

## References 
#### RNN/LSTM
* [The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/)
* [Understanding LSTM Networks](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)
* [Anyone Can Learn To Code an LSTM-RNN in Python (Part 1: RNN)](https://iamtrask.github.io/2015/11/15/anyone-can-code-lstm/)
* [Understanding LSTM and its diagrams](https://medium.com/@shiyan/understanding-lstm-and-its-diagrams-37e2f46f1714)
* [Composing Music With Recurrent Neural Networks](http://www.hexahedria.com/2015/08/03/composing-music-with-recurrent-neural-networks/)

