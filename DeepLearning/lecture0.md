% Lecture 0: Introduction
% Author CS
% Date March 


# Learning with Unstructured Data

Lecture 0: Introduction

<br><br>
Prof. Claudia Soares<br>
[claudia.soares@fct.unl.pt](mailto:claudia.soares@fct.unl.pt)

---

# Today

- Course outline
- Introduction to deep learning
- Fundamentals of machine learning

---

# Outline

- Lecture 1.1: Introduction
- Lecture 1.2: Fundamentals of machine learning
- Lecture 2.1: Multi-layer perceptron
- Lecture 2.2: Training neural networks
- Lecture 3.1: Computer Vision
- Lecture 3.2: Convolutional neural networks
- Lecture 4: Attention and transformer networks
- Lecture 5: Graph Neural Networks
- Lecture 6: Natural Language Processing

---

# Main Reference

:::::::::::::: {.columns}
::: {.column width="40%"}

- Good balance of theory and practice
- Covers almost all topics; Will be added more references, as adequate
- Online book [dl2.ai](https://d2l.ai/)

:::
::: {.column width="60%"}

<p class="stretch"><img src="https://d2l.ai/_images/front.png" width="60%" height="60%"></p>

:::
::::::::::::::


---


## My mission

By the end of this course, you will have acquired a solid and detailed understanding of the field of deep learning. 

You will have learned how to design deep neural networks for a wide range of advanced probabilistic inference tasks and how to train them.

These models seen in the course apply to a wide variety of artificial intelligence problems, with plenty of applications in engineering and science.

---


# Why learning?

---

<p class="stretch"><img src="https://upload.wikimedia.org/wikipedia/commons/9/98/Adolphe_Millot_champignon.jpg" width="60%" height="60%"></p>

---

![What do you see?](https://upload.wikimedia.org/wikipedia/commons/9/98/Adolphe_Millot_champignon.jpg)


???

.italic[How do you do that?]

---

class: middle

.center[
.width-70[![](figures/lec0/dog1.jpg)]

Sheepdog or mop?
]

.footnote[Credits: [Karen Zack](https://twitter.com/teenybiscuit), 2016.]

---

class: middle

.center[
.width-70[![](figures/lec0/dog2.jpg)]

Chihuahua or muffin?
]

.footnote[Credits: [Karen Zack](https://twitter.com/teenybiscuit). 2016.]

---

class: middle

The (human) brain is so good at interpreting visual information that the **gap** between raw
data and its semantic interpretation is difficult to assess intuitively:

<br>
.center[
![](figures/lec0/mushroom-small.png)

This is a mushroom.
]

---

class: middle, center

.width-70[![](figures/lec0/mushroom-big.png)]

This is a mushroom.

---

class: middle, center

.width-30[![](figures/lec0/mushroom-rgb0.png)] +
.width-30[![](figures/lec0/mushroom-rgb1.png)] +
.width-30[![](figures/lec0/mushroom-rgb2.png)]


This is a mushroom.

---

class: middle, center

.width-80[![](figures/lec0/mushroom-small-nb.png)]

This is a mushroom.

---

class: middle, center

Writing a computer program that sees?

---

class: middle

.center.width-60[![](figures/lec0/cat1.png)]

---

count: false
class: black-slide

.center.width-60[![](figures/lec0/cat2.png)]

---

count: false
class: black-slide, middle

.center.width-80[![](figures/lec0/cat3.png)]

---

count: false
class: black-slide, middle

.center.width-80[![](figures/lec0/cat4.png)]

---

class: middle

Extracting semantic information requires models of **high complexity**, which cannot be designed by hand.

However, one can write a program that *learns* the task of extracting semantic information.

---

class: middle, black-slide

.center.width-70[![](figures/lec0/console.jpg)]

The common approach used in practice consists of:
- defining a parametric model with high capacity,
- optimizing its parameters, by "making it work" on the training data.

---

class: middle, center, black-slide

class: middle, black-slide

.center[
<video loop controls preload="auto" height="500" width="600">
  <source src="./figures/lec0/yann-dl.mp4" type="video/mp4">
</video>
]

---

class: middle

# Applications and successes

---

class: middle, center, black-slide

<iframe width="600" height="450" src="https://www.youtube.com/embed/5kpsZoKjPgQ" frameborder="0" allowfullscreen></iframe>

Object detection, pose estimation, segmentation (2019)

---

class: middle, center, black-slide

<iframe width="600" height="450" src="https://www.youtube.com/embed/V1eYniJ0Rnk" frameborder="0" allowfullscreen></iframe>

Reinforcement learning (Mnih et al, 2014)

---

exclude: true
class: middle, center, black-slide

<iframe width="600" height="450" src="https://www.youtube.com/embed/HcZ48JDamyk" frameborder="0" allowfullscreen></iframe>

Strategy games (Deepmind, 2016-2018)

---

class: middle, center, black-slide

<iframe width="600" height="450" src="https://www.youtube.com/embed/qhUvQiKec2U" frameborder="0" allowfullscreen></iframe>

Autonomous cars (NVIDIA, 2016)

---

class: middle, center, black-slide

<iframe width="600" height="450" src="https://www.youtube.com/embed/hA_-MkU0Nfw" frameborder="0" allowfullscreen></iframe>

Autonomous cars (Waymo, 2022)

---

exclude: true
class: middle, black-slide

.center[
<video loop controls preload="auto" height="400" width="600">
  <source src="./figures/lec7/physics-simulation.mp4" type="video/mp4">
</video>

Physics simulation (Sanchez-Gonzalez et al, 2020)

]

---

class: middle, black-slide, center

<iframe width="600" height="450" src="https://www.youtube.com/embed/gg7WjuFs8F4" frameborder="0" allowfullscreen></iframe>

AI for Science (Deepmind, AlphaFold, 2020)

---

class: middle, center, black-slide

<iframe width="600" height="450" src="https://www.youtube.com/embed/7gh6_U7Nfjs" frameborder="0" allowfullscreen></iframe>

Speech synthesis and question answering (Google, 2018)

---

class: middle, center, black-slide

<iframe width="600" height="450" src="https://www.youtube.com/embed/qTgPSKKjfVg" frameborder="0" allowfullscreen></iframe>

Image generation and AI art (OpenAI, 2022)

---

class: middle, center, black-slide

<iframe width="600" height="450" src="https://www.youtube.com/embed/Zm9B-DvwOgw" frameborder="0" allowfullscreen></iframe>

Write computer code (OpenAI, 2021)

---

class: middle, center, black-slide

.center.width-100[![](figures/lec0/ChatGPT.png)]

Answer all your questions (OpenAI, 2022)

---

exclude: true
class: middle, center, black-slide

<iframe width="600" height="450" src="https://www.youtube.com/embed/BIDaxl4xqJ4" frameborder="0" allowfullscreen></iframe>

Dali Lives (2019)

---

class: middle, center

.width-70[![](figures/lec0/turing-award.png)]

.italic["ACM named .bold[Yoshua Bengio], .bold[Geoffrey Hinton], and .bold[Yann LeCun] recipients of the .bold[2018 ACM A.M. Turing Award] for conceptual and engineering breakthroughs that have made deep neural networks a critical component of computing."]

---

# Why does it work now?

.center.grid[
.kol-1-2[
Algorithms (old and new)<br><br>
.width-90[![](figures/lec0/skip-connection.png)]
]
.center.kol-1-2[
More data<br><br>
.width-50[![](figures/lec0/imagenet.jpeg)]
]
]

.center.grid[
.kol-1-2[
Software<br>
.width-90[![](figures/lec0/software.png)]
]
.kol-1-2[
Faster compute engines<br><br>
.width-50[![](figures/lec0/titan.jpg)]
]
]

???

The success of deep learning is multi-factorial...

---

class: middle

## Building on the shoulders of giants

Five decades of research in machine learning provided
- a taxonomy of ML concepts (classification, generative models, clustering, kernels, linear embeddings, etc.),
- a sound statistical formalization (Bayesian estimation, PAC),
- a clear picture of fundamental issues (bias/variance dilemma, VC
dimension, generalization bounds, etc.),
- a good understanding of optimization issues,
- efficient large-scale algorithms.

.footnote[Credits: Francois Fleuret, [EE559 Deep Learning](https://fleuret.org/ee559/), EPFL.]

---

class: middle

## Deep learning

From a practical perspective, deep learning
- lessens the need for a deep mathematical grasp,
- makes the design of large learning architectures a system/software development task,
- allows to leverage modern hardware (clusters of GPUs),
- does not plateau when using more data,
- makes large trained networks a commodity.

.footnote[Credits: Francois Fleuret, [EE559 Deep Learning](https://fleuret.org/ee559/), EPFL.]

---

class: middle

.center.circle.width-30[![](figures/lec0/bishop.jpg)]

.italic[For the last forty years we have programmed computers; for the next forty years we will train them.]

.pull-right[Chris Bishop, 2020.]


---

class: end-slide, center
count: false

The end.
