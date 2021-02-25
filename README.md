# muffin-v-chihuahua-with-embedded-model

This repo offers some code to illustrate the following blog article <http://link to come when published>.

It aims to demonstrate one way to package with Wheel and Docker a Machine Learning application able to classify muffins and chihuahua in an image. 

This way is described as the packaging of an ML application with **"an embedded model"** in the [Continuous Delivery for Machine Learning (CD4ML)](https://martinfowler.com/articles/cd4ml.html#ModelServing) article from Martin Fowler's blog. 


This app needs 

* a pre-trained Deep Learning model,
* some images of muffins and chihuahuas, for demonstration purposes,
* some Python code.

Packaging of this Python app is done with 

* the Wheel format, with setuptools 
* and docker.

