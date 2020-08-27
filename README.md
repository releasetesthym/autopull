# AutoPull

## Description

Docker Hub started their new pricing plan on 2020/8/26.  
The biggest change is that Docker images which are owned by a free account not pulled or pushed by someone for 6 months will be marked as "inactive"  
The images which are marked as "inactive" will be deleted by Docker Hub.  
The new policy is known as "Inactive image retention policy", and it is ONLY applied to free accounts, pro or team accounts exceped.  
This actions fires on the first day of every month at 10:30 UTC, it will list all images of a specific Docker Hub account, pull them, and remove them.  
The script prevents images owned by free accounts from being deleted by Docker Hub.  

## Usage

Fork this repository, enable Github Actions and make a commit.