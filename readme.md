A system for translating a puppet show script to a real time control of a complete robotic puppet show

Areas of control -  mouth movement. single servo
Additional motion - stage and curtain control

components of system 

1- A Libreoffice spreadsheet template to write out the script and sequences of the 
theatre play
2- pysimplegui User interface for setting up the script
3- output of controls for ESP32 - for preloading on ESP32

use pyserial for real time control (in the first version this is not used). 
or use subsystem call to load the file using the arduino ide.

Use UDP multicast to start / pause / rewind the script on all the ESP32s in sync.

Convert the text to International Phonetics using the english-to-ipa library
then convert the phonetics symbols to motor movements. 


Nuances of system. 

Words - some "basic" words are programmed in as canned cycles
letters - all other words are programmed in as individual letters 

https://smartlaboratory.org/ravdess/

an interesting project with 13 servos that is open source
http://keenbots.com/Fritz/gallery.php

https://aws.amazon.com/polly/  - text to speech. supports lexicons and SSML

expressions - each line of text can have an associated expression 
awkward
neutral
sinister
sleepy
sneaky
sulk
calm
happy
sad
angry
fearful
surprised
careful
subtle
disgusted
whisper

laughing
crying 
sneezing


SSML tags for the TTS:

break
emphasis 1-3
pause
breathing sound
softly
timbre

prosody:
strength - 1-6
rate 1-5
pitch 1-5
volume 1-6


in the user interface allow up to 5 parallel threads for robots and curtain motor controls
The user interface for compiling the Puppet script is in a LibreOffice Template for now




Select the voice for the puppet (from the Amazon list, currently limited to English)
![Alt text](spreadsheet_interface_2.png?raw=true "Spreadsheet")


For each line you can set the prosody, and other SSML nuances for each robot. this is also reflected in the way the mouth moves.

![Alt text](spreadsheet_interface.png?raw=true "Spreadsheet")



Once the script is ready. Save it as a CSV file.

Open the TheatreProcessing.exe or py file.

Import the CSV file

Then click to process it. The processing does the following: 
1- Converts the text to IPA
2- Upload to the Text to speech system and retrieves the audio file
3- Converts the IPA text to individual motor movements for the robot mouths / stages / curtains
4- uploads the Code to the ESP-32 controllers


![Alt text](ProcessingAndRunning.png?raw=true "Processing")


Once the processing is complete the theatre can be "started". 
Starting sends a signal by Multicast to all the ESP32s as well as beginning the Audio Playback on the computer. 




===========IPA=====================

### English to IPA (eng_to_ipa)


This Python program utilizes the Carnegie-Mellon University Pronouncing Dictionary to convert English text into the [International Phonetic Alphabet](https://en.wikipedia.org/wiki/International_Phonetic_Alphabet).


The `convert` function is used to take English text and convert it to IPA, like so:

```Python
>>> import eng_to_ipa as ipa
>>> ipa.convert("The quick brown fox jumped over the lazy dog.")
'ðə kwɪk braʊn fɑks ʤəmpt ˈoʊvər ðə ˈlezi dɔg.'
``` 

Note that words that cannot be found in the CMU dictionary are simply reprinted with an asterisk.

#### `convert` parameters

* **text** : *string* - The input string of English text to be converted to IPA notation.

* **keep_punct** : *boolean, optional (default=True)* - Determines whether or not the punctuation marks from the input string
should be retained or not.

* **retrieve_all** : *boolean, optional (default=False)* - Given that some words might have more than one transcription,
this parameter determines whether or not a list of all possible combinations of transcriptions should be returned (True)
 or just the string of one transcription (False).
 
* **stress_marks** : *string, optional (default='both')* - Determines whether or not the primary and secondary stress 
markings (ˈ, ˌ) should be retained. Understood arguments are:
   * "primary" - retains primary stress only 
   * "secondary" - retains secondary stress only
   * "both" - to keep both primary and secondary stress markers. 
   
* **mode** : *string, optional (default='sql')* - Accepts "sql" or "json", depending on which version of the database you'd like to use.
 As another option for JSON users, simply use the function `jonvert` instead of `convert`. 
   
The `ipa_list` function returns a list of each word as a list of all its possible transcriptions. It has all the same
optional `stress_marks` and `keep_punct` parameters as `convert`.
```Python
>>> ipa.ipa_list("The record was expensive.")
[['ði', 'ðə'], ['rəˈkɔrd', 'rɪˈkɔrd', 'ˈrɛkərd'], ['wɑz'], ['ɪkˈspɛnsɪv.']]
```

The `isin_cmu` function takes a word (or list of words) and checks if it is in the CMU pronouncing dictionary (returns 
`True` or `False`). If a list of words is provided, then `True` will only be returned if *every* provided word is in the dictionary.

```Python
>>> ipa.isin_cmu("The dentist opened a new practice.")
True
>>> ipa.isin_cmu("emoji")
False
```

The `get_rhymes` function returns a list of rhymes for a word or set of words. 
```Python
>>> ipa.get_rhymes("rhyming function")
[['climbing', 'diming', 'liming', 'priming', 'timing'], ['compunction', 'conjunction', 'dysfunction', 'injunction', 'junction', 'malfunction']]
```
*Use the `jhymes` function instead to force usage of the JSON database.*
   
The `syllable_count` function returns an integer, corresponding to the number of syllables in a word. Returns a list of 
syllable counts if more than one word is provided in the input string.

```Python
>>> ipa.syllable_count("computer programming")
[3, 3]
```

For another Python package that offers support for rhyming and syllable counts (as well as other cool things), see [pronouncingpy](https://github.com/aparrish/pronouncingpy).

Note: I'd like to make this project easily available/installable from pip, but I don't know how. Looking for help!

