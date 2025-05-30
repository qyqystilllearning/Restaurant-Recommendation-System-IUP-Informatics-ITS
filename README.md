# Restaurant-Recommendation-System-IUP-Informatics-ITS

<div align="center">

| NRP        | Name                             |
|------------|----------------------------------|
| 5025231075 | Reino Yuris Kusumanegara         |
| 5025231082 | Muhammad Hanif Fakhriansyah      |
| 5025231161 | Muhammad Rizqy Hidayat           |

</div>

---

## Introduction

This web-based restaurant recommendation system helps users find the best nearby restaurants based on their location, budget, distance, and rating preferences. Users can enter their coordinates manually or use auto-detection. The system uses A* and BFS algorithms to suggest restaurants and displays results on an interactive map with routes using OSRM. It's designed to make dining decisions faster and more convenient.

## Background and Problem Statement

When individuals or groups plan to eat out, there will always be debates in choosing where they want to eat due to the varying preferences of each individual. They must also consider constraints such as budget, approximate cost, travel distance, operational hours, and more. The abundance of restaurant options combined with limited time and varying preferences creates this problem.

Hence, we developed a Restaurant Recommendation System to assist people who are undecided and want to choose a restaurant based on their preferences quickly. The system uses search methodologies, such as Uninformed and Informed search.

Generally, when an individual or group wants to eat out, they often face difficulty choosing a restaurant that matches their preferences, budget, and location. This problem becomes more complex when there are multiple people with different preferences, such as:

- Available budget  
- Restaurant location  
- Ratings or reviews from previous customers  

This recommendation system aims to solve this problem by offering restaurant options that meet the preferences of multiple users in a single search.

---

## Methodology

In this project, we implement a restaurant recommendation system using two popular search algorithms:

- **A-Star (A*) Search**
- **Breadth-First Search (BFS)**

The purpose is to recommend restaurants based on user-defined criteria, including distance, rating, and budget. We also provide visualizations of the routes and restaurants on an interactive map to enhance user experience and understanding.

## Demo Output

Please download the ```Quiz 2``` Folder. Then, run the ```app.py``` in the ```Quiz2``` folder and follow the output link on from the terminal:

![image](https://github.com/user-attachments/assets/473349f5-26cb-4d38-b9b6-1408d8d6ff56)

And then the web will looks like this:

![image](https://github.com/user-attachments/assets/a11c979b-1d42-43b6-b566-8488c59cebd3)

The user can select on rating or distance based on the preferences:

![image](https://github.com/user-attachments/assets/b380cc80-3743-4f26-bf1c-5ad59690955f)

Rating-priority usage example (Try using 4.5 rating with 15 km maximum and budget of 50.000):

![image](https://github.com/user-attachments/assets/b4570555-a010-446d-8bd1-f22e40a769fd)

The result:

![image](https://github.com/user-attachments/assets/7040bb66-7483-4067-9563-93e7941230bd)

Task Distribution:
1. Reino Yuris Kusumanegara - 33.33% : Web and app development engineer
2. Muhammad Rizqy Hidayat - 33.33% : Rating-priority algorithm development,
debugger, and github execution
3. Muhammad Hanif Fakhriansyah - 33.33% : Distance-priority algorithm development,
tester, and report maker

