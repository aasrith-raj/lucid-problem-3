Problem Statement: Log Analysis

You are given a file containing system logs in the format: timestamp, user_id, action 
Example: 
10:01,user1,login
10:03,user2,search
10:05,user1,purchase
10:07,user2,search
10:10,user3,login 

Task Write a program to comput are the most active user (user with highest number of actions) and the most common action 

So first we read the excal file and store it in the 'file_log'.

Then we created 2 dictionaries one for user_id and the other for actions the user made. 