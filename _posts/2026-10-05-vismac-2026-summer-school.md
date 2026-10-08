---
title: "VISMAC 2026: A Week of Machine Vision in Siena"
excerpt: "Highlights and takeaways from VISMAC 2026, a machine vision summer school in Siena covering 3D vision, video, physical AI and trustworthy AI."
description: "My takeaways from VISMAC 2026 in Siena, Italy: machine vision lectures on 3D vision, video understanding, physical AI, generative models and trustworthy AI."
comments: true
classes: wide
categories:
  - posts
tags:
  - summer-school
  - machine-vision
  - computer-vision
header:
  overlay_image: /assets/images/posts/vismac-2026/SienaTower.jpg
  overlay_filter: "0.5"
---

> கேடில் விழுச்செல்வம் கல்வி ஒருவற்கு<br>
> மாடல்ல மற்றை யவை.<br>
> Learning is a person's imperishable treasure; other riches are not true wealth.

<cite>Thirukkural 400, from [Thirukkural](https://en.wikipedia.org/wiki/Kural)</cite>
{: .small}

## Summer School & my experience

The [International Summer School on Machine Vision (VISMAC 2026)](https://vismac2026.github.io/) took place at the [Santa Chiara Lab](https://www.santachiaralab.unisi.it/), University of Siena, Italy, from 21 to 25 September 2026. It was organised by the Italian Association for Computer Vision, Pattern Recognition and Machine Learning (CVPL), affiliated with the [International Association for Pattern Recognition (IAPR)](https://www.iapr.org/).

The programme brought together PhD students and young researchers for a week of lectures covering a wide range of computer vision topics. Alongside the lectures, there was a startup panel, a startup demo and a poster session, giving participants a chance to share research and exchange ideas. I found it especially interesting to see how different areas of machine vision connect to broader questions about how models learn, generate, and interact with the world.

Here are some of the ideas that stood out to me from the sessions.

## Lectures & takeaways

### Human motion, 3D vision and video understanding

**[Gül Varol](https://gulvarol.github.io/) — Language-guided human motion generation**

Gül Varol spoke about using language not only to describe human motion, but also to generate and edit it. The lecture covered compositional instructions, hand motion and interactions with objects. It was interesting to see how a short text prompt can represent a complex movement, and why the generated motion needs to remain coherent over time and physically plausible.

**[Matteo Poggi](https://mattpoggi.github.io/) — Depth estimation and 3D vision**

Matteo Poggi traced the progression from stereo and monocular depth estimation to multi-view methods and 3D foundation models. These models offer exciting possibilities, but the lecture also highlighted the challenges of adapting them to new domains and using them under real deployment constraints.

**[Dima Damen](https://dimadamen.github.io/) — Egocentric video understanding**

Dima Damen focused on understanding video recorded from a first-person perspective. Unlike short, carefully selected clips, everyday video is long, continuous and multimodal. Datasets such as [Ego4D](https://ego4d-data.org/) and [EPIC-KITCHENS](https://epic-kitchens.github.io/) offer examples of this kind of naturalistic first-person video. This makes memory and context important: a system needs to understand what is happening across time, not just recognize something in one frame.

### From prediction to action

**[Lamberto Ballan](https://www.lambertoballan.net/) — Trajectory prediction and embodied navigation**

Lamberto Ballan connected human-trajectory prediction to embodied navigation. A robot or agent must do more than predict what might happen; it needs to perceive its surroundings, interpret instructions, remember useful context and choose actions that make sense in the environment.

**[Efstratios Gavves](https://www.egavves.com/) — Physical AI and world models**

Efstratios Gavves introduced physical AI and the use of world models and digital twins. Projects such as [DreMa](https://dreamtomanipulate.github.io/) explore how compositional world models can support robot imitation learning, while the [MORPHEUS benchmark](https://physics-from-video.github.io/morpheus-bench/) tests the physical reasoning of video-generation models. One idea I took away was the difference between a generated scene that looks realistic and one that obeys the mechanics of the real world. Evaluating physical consistency is essential if these models are to support simulation and robotics.

**[Davide Scaramuzza](https://rpg.ifi.uzh.ch/people_scaramuzza.html) — Low-latency robotics with event cameras**

Davide Scaramuzza showed how event cameras can help robots respond to fast motion. Instead of capturing complete images at fixed intervals, these cameras record changes in brightness as they happen. This can reduce latency and motion blur, which is particularly useful for agile robots and drones.

### Generation, creativity and model composition

**[Marina Paolanti](https://docenti.unimc.it/marina.paolanti) — Creative AI for heritage and fashion**

Marina Paolanti explored applications of AI in cultural heritage and fashion. Along with the technical opportunities, the lecture raised important questions about authenticity, rights, cultural diversity and the role of human oversight. These are important considerations when AI becomes part of creative work.

**[Tomaso Fontanini](https://personale.unipr.it/ugovdocenti/person/199302) — Joint multimodal generation**

Tomaso Fontanini discussed generative models that work across modalities such as text, images, audio and video. Generating each modality well is only part of the problem; the outputs also need to make sense together. For example, audio and video should be aligned and synchronized.

**[Simone Calderara](https://aimagelab-legacy.ing.unimore.it/imagelab/person.asp?idpersona=38) — Task arithmetic and model merging**

Simone Calderara introduced task vectors as a way to combine or modify learned capabilities by working with model updates. This idea is explored in the paper [Editing Models with Task Arithmetic](https://arxiv.org/abs/2212.04089). The idea is appealing, but merging models is not as simple as adding their skills together. Alignment and interference affect whether the resulting model works as intended.

### Robustness, privacy and trust

**[Vittorio Murino](https://www.vittoriomurino.com/) — Dataset bias and robustness**

Vittorio Murino showed how a model can learn shortcuts from its training data and then struggle when those patterns change. The paper [Distributionally Robust Neural Networks for Group Shifts](https://openreview.net/forum?id=ryxGuJrFvS) is one example of research into performance under these shifts. A high score on familiar data does not necessarily mean a model will work well in a new setting. Testing across different groups and conditions is an important part of evaluating robustness.

**[Lacopo Masi](https://iacopomasi.github.io/) — Robust classifiers and energy-based models**

Iacopo Masi connected adversarial robustness with energy-based views of classifiers. The lecture explored how this perspective can link classification with inversion, generation and ways of examining model predictions. It offered an interesting way to think about what a model considers plausible, beyond simply looking at its final label.

**[Massimiliano Mancini](https://mancinimassimiliano.github.io/) — Memorization and machine unlearning**

Massimiliano Mancini discussed how models can memorize examples from their training data, and what it means to remove that information through machine unlearning. The challenge is not only to update a model, but also to measure whether information has actually been forgotten.

**[Lorenzo Seidenari](https://www.micc.unifi.it/seidenari/) — Privacy-preserving adversarial machine learning**

Lorenzo Seidenari presented adversarial machine learning from a defensive perspective: carefully designed changes to images may help limit unwanted recognition, editing or location inference. These protections need to be tested against realistic transformations, such as resizing and compression, as well as different models.

**[Luisa Verdoliva](https://www.grip.unina.it/members/verdoliva) — Synthetic-media forensics**

Luisa Verdoliva focused on identifying generated or manipulated media. Visual clues can be useful, but they become less reliable as generation methods improve. Research such as [Noiseprint](https://ieeexplore.ieee.org/document/8891446) studies forensic traces in images, while [zero-shot detection of AI-generated images](https://arxiv.org/abs/2303.15903) addresses generalization to generators beyond those used for training. A central challenge is making detectors generalize to new generators and image-processing pipelines rather than only recognizing examples similar to those seen during training.

## What connected the talks

Although the lectures covered very different topics, a few ideas kept coming back. Larger models and more data can expand what is possible, but they do not remove the need for good evaluation. Models still have to cope with changing domains, incomplete context, physical constraints and new forms of misuse.

I also found it valuable that the programme went beyond recognition. Many sessions looked at systems that generate content, remember and reason over time, navigate environments or interact with the physical world. In all these cases, it is not enough for a result to look convincing: it needs to be reliable for the task it is meant to perform.

## Final thoughts

VISMAC 2026 was a great opportunity to hear about current directions in machine vision from researchers working across different areas. I would recommend this summer school to PhD students and young researchers who want a broad view of the field, together with a chance to discuss their work with other participants.

That’s it from me. The week left me with plenty of ideas to think about, and a clearer sense of how much careful evaluation matters as vision systems become more capable.
