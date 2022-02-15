# -*- coding: utf-8 -*-
#! /usr/bin/python3
"""
An interactive dictionary in Python
"""
import pyautogui
from random import choice
#grab matching library and data
from difflib import get_close_matches
from json import load
data = load(open("data.json", 'r'))

def translate(w): 
    #finds definition for output[0] input word and returns the word and definition.
    #the word is returned because it is used as the window title and may change during the function.
    #if word empty, return a random word
    if w == "":
        rand = choice(list(data.items()))
        return(rand[0], rand[1])
    #make sure case is not an issue, check if word exists
    if w.lower() in data:
        return[w, data[w.lower()]]
    else: 
        #if word doesn't exist, prompt user with a potential match
        matches = get_close_matches(w, data.keys())
        if len(matches) > 0:
            yn = pyautogui.confirm("Did you mean " + matches[0] + " instead?", word, ["Yes", "No"])
            if yn == "Yes":
                return[matches[0], (data[matches[0]])]
            #if all else fails, return nonexistent word message
            else:
                return["Error", "The word doesn't exist. Please double check it."]
        else:
            return["Error", "The word doesn't exist. Please double check it."]
while True:
    #run program repeatedly until user exits by pressing cancel
    word = pyautogui.prompt("Welcome to the Dictionary. Enter a word: ", "Dictionary", "")
    
    #cancelling a pyautogui prompt returns None
    if word == None:
        break
    #under normal conditions, translate the word and split the output into a word and definition
    else:    
        output = translate(word)
        word = output[0]
        definition = output[1]

    #convert definition into a single string and show an alert box with the info
    ans = ""
    if type(definition) == list:
        for item in definition:
            ans = ans + "\n" + item
    else:
        ans = definition
    pyautogui.alert(ans, word, "OK")