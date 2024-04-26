# Molly
Molly is a voice assistant AI based on google Geminin pro.

What molly can do :
+ Molly can save the chat history(logs) in a text file on your computer, where it saves one file for each day you talk to her.
+ Molly can tells you jokes or whatever you want to hear.
+ Molly can answer all your questions by responding with a reasonable answers.

#### for now, molly doesn't have a fascinating user interface yet, but it will later as soon as possible.


### To use molly:
+ you have to download python and whatever IDE you prefer(VS code + python plugins) on your local machine
+ ou must install the necessary libraries to operate molly (you will find it in the first lines of the code)
+ Whenever you want to start a conversation with her you must call her (by saying "hello molly" or anything alike)
+ you may need to get your own google_api key from geminin and put it in a .env file on your local machine (Don't worry about that I'll provide a link for this)

  
*youtube video to show how to get API key* : https://youtu.be/6aj5a7qGcb4?si=OzWfRRRUliQbPam8 .


After getting the API key you need to set it as environment variable (.env), here are the steps to do this :
  + right click on this pc
  + click on properties
  + click on advanced system setteings from top rights menu (for windows 10)
  + click on environment variable
  + in variable name write : GOOGLE_API_KEY , in variable value : paste the key you have got
  + click ok


After that you need to set a new .env by applying the same steps, but for the variabe name : PYGAME_HIDE_SUPPORT_PROMPT and for variable value : hide
