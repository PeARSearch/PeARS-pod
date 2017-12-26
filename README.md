# PeARS Pod
----
## What and why

PeARS Pod is for people who want to set up a PeARS pod, to work with [PeARS, version Orchard](https://github.com/PeARSearch/PeARS-orchard). In order to use this repo, you need to have copy of PeARS Orchard installed on your computer, which you will specifically use to prepare your pod. If you are using PeARS for your own general purposes at the same time, we advise you to keep two copies of Orchard in two different directories. For instance, you may have one Orchard instance in your home directory for private purposes, and another install in a *your-pod-name* directory, alongside your PeARS Pod install.

**AT THIS POINT, THIS REPO IS UNDER CONSTRUCTION. CHECK BACK HERE SOON!**

----
## Usage

1. Clone this repo on your machine:

    git clone https://github.com/PeARSearch/PeARS-pod.git


2. Setup a virtualenv in your directory (**this step is optional**):

    virtualenv -p python3 env && source env/bin/activate

3. Install the build dependencies:

    pip3 install -r requirements.txt

4. Head over to the app/static/spaces directory and unzip english.dm.zip.

5. In the root of the repo, run:

    python3 run.py

Now, go to your browser at localhost:5000. You should see a template front page for your pod. You don't have any pages indexed yet, so [instructions coming soon...] 



