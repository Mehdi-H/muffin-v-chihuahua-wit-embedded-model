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

## How can I run the packaging of this muffin_v_chihuahua ML app

### Download some images

You can run `make datasets` at the root of this repo.

This command will populate the `muffin_v_chihuahua/data/chihuahua/` folder with a dataset of chihuahua images and `muffin_v_chihuahua/data/muffin/` with muffin images.

Those images are downloaded from <http://image-net.org/>.

### Download a pre-trained model

To avoid training an ad-hoc model for this computer vision task, we can download a pre-trained model with `make model`.

This command will download the InceptionV3 model [listed on Keras website](https://keras.io/api/applications/).

This model is downloaded from François Chollet [deep-learning-models](https://github.com/fchollet/deep-learning-models/) repository, in which the official InceptionV3 model is exposed as an artefact in [release v0.5](https://github.com/fchollet/deep-learning-models/releases/tag/v0.5).