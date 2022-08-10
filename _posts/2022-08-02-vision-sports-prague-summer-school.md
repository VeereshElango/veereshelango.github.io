---
title: Vision and Sports Summer School 2022
excerpt: "a short summary about the summer school and my takeaways"
comments: true
classes: wide
categories:
    -  posts
tags:
    - summer-school    
header:
  overlay_image: /assets/images/posts/summer-school/group_picture.jpg
  overlay_filter: "0.5"  
---

> கற்றலின், கேட்டலே நன்று.<br>
> Listening is Better than Learning <br>

<cite> from [Pazhamozhi Naanooru](https://en.wikipedia.org/wiki/Pa%E1%B8%BBamo%E1%B8%BBi_N%C4%81%E1%B9%89%C5%AB%E1%B9%9Fu) from literature [Pathinen Keezhkanakku](https://en.wikipedia.org/wiki/Eighteen_Lesser_Texts)</cite>
 {: .small}

Explanation : It is better to hear knowledgeable things from learned men (experienced) than self-learning.

## Summer School & my experience

This [Vision and Sports summer school](http://cmp.felk.cvut.cz/summerschool2022/index.html) was conducted at Czech Technical University, Prague between 25-30th July, 2022. It is  sponsored by Google and endorsed by [ELLIS society](https://ellis.eu/events/vision-and-sports-summer-school-2022-in-prague) and [ELISE Consortium](https://www.elise-ai.eu/).

The summer school had speakers from academic as well as industries such as Google, Facebook and Valeo, covering several sub-fields of computer vision. There were nearly 50 to 60 students all over from Europe, varying from yet-to-start PhD to final year of their PhD. The uniqueness of this summer school was the fusion of (intense) sports activities at the end of everyday lecture so that every student was assigned with one sport as per their wishlist (as much as possible). This helped us to mingle and socialize.The sports activities drained the energy at the end of the day but it didn't stop us from mingling and enjoying the night life of Prague. 

I would highly recommend this summer school if you are into computer vision and like to get good insights current trends on different sub-fields of computer vision at a beautiful city.
 
If you are curious to get some short gist about different sessions of summer school, feel free to continue. 

## Lectures & Exercise
### [Ondrej Chum](http://cmp.felk.cvut.cz/~chum/), Czech Technical University
***Large scale Image Retrieval and Specific Object Search***

This lecture started with similar image search in large scale followed by methods to gather features from images and strategies to match them. Then the challenges associated with image retrieval and techniques to solve them were explained. Finally wrapped up by talking about reconstructing 3D reconstruction from single image and querying with night image.

###  [Christoph Lampert](http://pub.ist.ac.at/~chl/), IST Austria
***Best Practice in Machine Learning for Computer Vision*** 
<figure class="align-right" style="width: 400px">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/images/posts/summer-school/chris-takeaway.jpg" alt="a slide from Christoph Lampert lecture">
  <figcaption>a slide from Christoph Lampert lecture</figcaption>
</figure> 
The lecture started with message of computer vision is not about winning Kaggle competitions but should perform interesting or relevant tasks. The best practices to follow on   solving a computer vision task was explained using five steps: sanity checks, defining the problem, collect and annotate data, model training and model evaluation. Also the best practices to follow on scientific scrutiny was also discussed. Finally wrapped with nice take home messages which I like.



###  [Patrick Pérez](https://ptrckprz.github.io/), Valeo.ai
***CV/ML for the real world - robustness, confidence, uncertainity, out-of-distribution, domain adaptation and generalization*** 

The lecture starts with the introduction about mad progress of the community in producing high performance models on popular datasets such MS-COCO, Pascal-VOC-2012, etc., but not accounting the distribution shift, brittleness towards adverserial attacks and absurd predictions in real-world systems. It was interesting to hear about the effect of using different type of data augumentation and domain adaptation techniques to tackle the robustness of the model. Also, the importance to evaluate the model more than single metric was insightful. 

###  [Hilde Kuehne](https://hildekuehne.github.io/), Goethe University
***Self-Supervised learning, Contrastive learning, Vision Language models, Multi-modal Learning***

<figure class="align-right" style="width: 400px">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/images/posts/summer-school/multimodallearning.jpg" alt="a slide from Hilde Kuehne lecture">
  <figcaption>a slide from Hilde Kuehne lecture</figcaption>
</figure> 
This is my favourite lecture of the summer school as the topics were highly interesting as well as enlightening. The lecture started with types of self-supervised learning such as by colorization, context structure, jigsaw puzzle and clustering. Then moved on to contrastive learning where topics like ranking loss, pairwise/contrastive loss, distance metrics were discussed along with how contrastive loss could be used for self-supervised learning. Then the techniques, importance and latest SOTA on vision language models were briefly talked through. "Multi-modal Learning - the watercooler of AI (speech, vision, nlp, ml theory)" fun and interesting way to introduce this topic. It was interesting to hear how multi-modal learning help us to learn feature representation without human annotated data and several applications of them in cross-modal learning. 

### [Vittorio Ferrari](https://research.google/people/105461/), Google Research
***3D Deep Learning***

This lecture started with talk about classical 3D reconstruction system by taking several images of a scene. A nice introduction to image formulation helped me to get some basics about the 3D reconstruction area. Then it discussed about single image to depth map using auto-encoders, then evolution of single image to single object reconstruction from voxels to point cloud to meshes. Also, good overview about single/ multiple images / videos to multiple object reconstruction. Finally, interesting discussion about NeRF (one of the interesting breakthrough in 3D domain).

###  [David Novotny](https://d-novotny.github.io/), Meta AI Research
***3D Deep Learning***

This lecture started with difference between multi-view geometry and 3D learning followed by advantages of implicit shape reconstruction. The details of NeRF model was discussed in deep followed by its challenges and improvements. The datasets such as ShapeNet, Objectron and CO3D were discussed to show the importance of quality datasets for 3D reconstruction. Followed by, interesting marriage between NeRF and transformers.

###  [Jiri Matas](http://cmp.felk.cvut.cz/~matas/), Czech Technical University
***Visual Tracking***

Another interesting lecture started with difference between correspondence search and segmentation in the domain of visual tracking. The applications of this field in tracking transparent objects, humans, animals, multiple objects, coins were interesting.  Then we went through classical and fundamental methods such as KLT tracker, Discriminative Tracker, MOSSE tracker, KCF tracker. The challenges and methods for fast moving object tracking was disscussed at end of the lecture.

### [Dmytro Mishkin](http://cmp.felk.cvut.cz/~mishkdmy/), Czech Technical University & Hover Inc.
***Lab session***

This was a practical lab exercise session which started with some interesting tips on jupyter notebook, then an image classification challenge to distinguish between beer and tradelnik, followed by task to train a image colorization network. The artifacts are available [here](https://github.com/ducha-aiki/vs3-cnn-labs).

On the last day, we had three sessions were Hilde, Vittorio and Patrick took us through their latest work.

That's it from me. Feel free to share your comments. 