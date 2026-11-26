# Football Match Tracking Application

## Overview

The aim of this project was to design and develop a football match tracking application, enabling users to record, manage, sort and analyse information relating to the football matches they have attended. The objective was to use Python to create both a text-based and graphical user interface (using Tkinter) version of the application, enabling users to add, store, view, sort, search, edit, delete match records as well as generate useful statistics to provide useful insights for the user. It focuses on allowing individual supporters to keep a record of their attendance by storing information such as the teams involved, match scores, stadiums visited, distances travelled, the result and personal team performance ratings. 

The application was designed using a modular structure to improve maintainability, readability and code reusability. There are 3 main modules, Football_Match_Tracker.py for the text-based application, Football_Match_Tracker_GUI.py for the GUI version, and the shared module matchLib.py containing all the core functionality. The application uses a custom Match class to store all the information for each match, while using lists and dictionaries to store retrieved match records ready for sorting, searching and more. Algorithms such as linear searching, Python's in built sort functionality and custom statistical calculations were implemented throughout the application. Additionally, the text-based version was designed using a numbered menu system, requiring users to select the number of the function they wished to perform. On the other hand, the GUI version was developed using buttons, labels and scrollable text areas to provide a more user-friendly experience. 

The shared module was used to implement the core functionality of the application including file handling, match record formatting, searching, sorting and statistical calculations. The functionality enabled both versions of the application to provide identical features whilst maintaining consistent behaviour and results. As a result, users are able to manage their match records efficiently regardless of whether they chose to use the text-based or graphical version of the application.

The completed application provides football supporters with a comprehensive tool for recording and analysing their attendance history. Through a combination of record management, searching, sorting and statistical analysis features, user are able to build a personalised digital diary of the matches they have attended whilst gaining useful insights from the data collected.

## Features

The Football Match Tracker provides a comprehensive set of record management features, allowing users to create and maintain a personal history of football matches attended. Match records can be added, viewed, edited and deleted, enabling users to keep their data accurate and up to date. All records are stored within an external text file, ensuring that information persists between application sessions.

In addition to record management, the application includes a range of tools designed to help users analyse and organise their data. Sorting functions can arrange records by date, team performance rating and distance travelled, whilst search functionality allows users to quickly locate specific records. The application also generates statistical information from the stored records, providing users with insights into their attendance history, stadium visits, travel distances and team performance. 

The combination of these features helps transform the application from a simple data storage system into a personal football attendance tracking tool.


### Key Features
- Add match records
- Store records in an external file
- View match records
- Sort matches
- Search matches 
- Generate statistics
- Edit records
- Delete records
- Available in both text-based and GUI versions

## Structure

### Football_Match_Tracker.py: 
The text-based implementation of the application. It provides a menu-driven interface through which users can add, view, sort, search, edit and delete match records as well as generate statistics.

### Football_Match_Tracker_GUI.py: 
The graphical user interface implementation of the application, developed using Tkinter. It provides the same functionality as the text-based version through buttons, labels, text entry fields and display areas.

### matchLib.py: 
The shared module containing the application's core functionality, including file handling, searching, sorting, formatting, statistical calculations and data validation. This module is imported by both application interfaces.

### matches_Tracker.txt: 
External text file used to store match records entered by the user. Data persists between sessions, allowing records to be viewed, edited and analysed after the application has been closed.


## Installation and Running the Application

The application was developed using Python 3. The graphical user interface was created using the Tkinter module, which is included as part of the standard Python installation and therefore does not require any additional installation.

### Running the text version: 
python Football_Match_Tracker.py

### Running the GUI version: 
python Football_Match_Tracker_GUI.py

## Screenshots

(include some screenshots, maybe some of the ones from the report)

## GitHub Development

(mention how commits were done, branches used and the general workflow)
