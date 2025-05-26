# Restaurant-Recommendation-System-IUP-Informatics-ITS

<div align="center">

| NRP        | Name                             |
|------------|----------------------------------|
| 5025231075 | Reino Yuris Kusumanegara         |
| 5025231082 | Muhammad Hanif Fakhriansyah      |
| 5025231161 | Muhammad Rizqy Hidayat           |

</div>

---

## Background and Problem Statement

When individuals or groups plan to eat out, there will always be debates in choosing where they want to eat due to the varying preferences of each individual. They must also consider constraints such as budget, approximate cost, travel distance, operational hours, and more. The abundance of restaurant options combined with limited time and varying preferences creates this problem.

Hence, we developed a Restaurant Recommendation System to assist people who are undecided and want to choose a restaurant based on their preferences quickly. The system uses search methodologies, such as Uninformed and Informed search.

Generally, when an individual or group wants to eat out, they often face difficulty choosing a restaurant that matches their preferences, budget, and location. This problem becomes more complex when there are multiple people with different preferences, such as:

- Available budget  
- Restaurant location  
- Ratings or reviews from previous customers  

This recommendation system aims to solve this problem by offering restaurant options that meet the preferences of multiple users in a single search.

---

## Uniqueness

1. **Distance and Time Efficiency**  
   By leveraging search algorithms like A* search, the system can prioritize nearby restaurants that minimize travel time, which is crucial for users with limited time, such as lunch breaks. It ensures that the recommendation not only fits the food preferences but also accounts for time efficiency.

2. **Quick Decision-making**  
   This recommendation system uses a combination of uninformed, informed, and local search algorithms to find optimal solutions. Algorithms like A* help find the best routes to nearby restaurants and can be used to refine restaurant choices based on the users' preferences, adjusting for cost, location, and group size. By using multiple algorithms, the system ensures both speed and accuracy in producing recommendations.

3. **Multiple User Preferences**  
   When several people are involved, each with their own food preferences, budget, and location, the system can combine and balance these multiple preferences to provide a recommendation that satisfies the majority of users. This is particularly useful for situations like family outings, group lunches, or meetings where diverse preferences must be considered. Individuals can also benefit from this system, making it adaptable for both single users and groups.


## Methodology

In this project, we implement a restaurant recommendation system using two popular search algorithms:

- **A-Star (A*) Search**
- **Breadth-First Search (BFS)**

The purpose is to recommend restaurants based on user-defined criteria, including distance, rating, and budget. We also provide visualizations of the routes and restaurants on an interactive map to enhance user experience and understanding.

## Objectives

We build a web-based that looks like this:

![image](https://github.com/user-attachments/assets/4fedee32-f50a-48e3-a115-7786c4236d09)

The user can select on rating or distance based on the preferences:

![image](https://github.com/user-attachments/assets/f60f243b-8c22-478c-b4f1-fbefeacf28c8)

Rating-priority usage example (Try using 4.5 rating with 15 km maximum 

