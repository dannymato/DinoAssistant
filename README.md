# Dinosaur Assistant

This is a repository for testing for a miniature robot dinosaur integrating with Google's Google Assistant

The idea would be to sync sounds played by the Google Assistant API with movements of a motor controlling the mouth of a dinosaur all connected to a Raspberry Pi

This uses Google's samples for the Google Assistant API for python modified for this specific use case

## Setup

Navigate to the folder you wish to download to

```
$	git clone https://github.com/dannymato/DinoAssistant.git
$	cd DinoAssistant
```
Install virtualenv which is different for each distro

```
$	python -m venv env

$	env/bin/python -m pip install --upgrade pip setuptools wheel
$	source env/bin/activate

(env) $ 	python -m pip install --upgrade google-assistant-sdk[samples]
(env) $ 	python -m

```
Readme not complete yet
