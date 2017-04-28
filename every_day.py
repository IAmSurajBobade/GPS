# -*- coding: utf-8 -*-

"""
@author: Suraj.Bobade
email: iamsurajbobade@gmail.com
"""

import os
import webbrowser
import datetime


# Variables
office_start_time = 10
office_end_time = 18
webpages_list = ["https://mail.google.com/mail/",
                 "https://outlook.live.com",
                 "https://facebook.com",
                 "https://twitter.com",
                 "https://www.quora.com/"]

# Initialisations
chrome = webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
now = datetime.datetime.now()

if office_start_time < now.hour < office_end_time:
    # start applications used in the time between 10AM to 6PM
    
    # Open Outlook app
    os.startfile("C:\Program Files (x86)\Microsoft Office\Office15\OUTLOOK.exe")
    # Open Jabber
    os.startfile("C:\\Program Files (x86)\\Cisco Systems\\Cisco Jabber\\CiscoJabber.exe")
    # Open Jira, Stash
    chrome.open("https://jira.community.com/secure/Dashboard.jspa")
    chrome.open("https://stash.com")

chrome.open("https://mail.google.com/mail/")
chrome.open("")
chrome.open("")
chrome.open("")
chrome.open("")