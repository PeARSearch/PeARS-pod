# PeARS Pod

## What and why

PeARS Pod is for people who want to 'look like a search engine', and wish to set up an online PeARS pod with a fixed URL. An example PeARS pod can be found [here](http://www.openmeaning.org/pod0/). **Note that setting up a pod with a URL is not necessary to share your Web knowledge!** PeARS also lets you share indexes with your friends via text files and images. This repo is purely for people who would like to setup a permanent online page where visitors can search their pod.

In order to use this repo, you need to have copy of [PeARS, version Orchard](https://github.com/PeARSearch/PeARS-orchard) installed on your computer, which you will specifically use to prepare your pod. If you are using PeARS for your own general purposes at the same time, we advise you to keep two copies of Orchard in two different directories. For instance, you may have one Orchard instance in your home directory for private purposes, and another install in a *your-pod-name* directory, alongside your PeARS Pod install.


## Learn to use your pod locally

#### 1. Clone this repo on your machine:

    git clone https://github.com/PeARSearch/PeARS-pod.git

#### 2. Optional step Setup a virtualenv in your directory.

    virtualenv -p python3 env && source env/bin/activate

#### 3. Install the build dependencies:

    pip3 install -r requirements.txt

#### 4. Unpack the semantic space

Head over to the app/static/spaces directory and unzip english.dm.zip.

#### 5. Tell your pod what to index.

You should save a csv file containing your pod in the *app/static/pods* folder. If you don't know yet what a csv pod is, consult <a href="https://pearsearch.org/faq.html#newpods">the documentation on PeARS Orchard</a>.

#### 6. Run it!

In the root of the repo, run:

    python3 run.py

Now, go to your browser at localhost:5000. You should see your pod running. Happy searching!

## Putting your pod online

You can setup your pod online on any server that will let you run a Flask application with a database. We provide specific instructions for use with <a href="https://www.pythonanywhere.com/">https://www.pythonanywhere.com/</a>. These can be found [on the Wiki](https://github.com/PeARSearch/PeARS-pod/wiki/Deploying-a-PeARS-pod-on-PythonAnywhere).
