# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 16:03:36 2019

@author: Shiva
"""

import pyttsx3
engine = pyttsx3.init('sapi5',False)
engine.setProperty('rate', 120)
engine.setProperty('volume',1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

