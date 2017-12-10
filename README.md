# PeARS Pod
----
## What and why

PeARS Pod is for people who want to set up a PeARS pod, to work with [PeARS, version Orchard](https://github.com/PeARSearch/PeARS-orchard). 

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



