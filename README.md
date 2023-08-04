# QA-DevOps-Project-1

## Objective

The objective for this phase 2 of the DevOps training project was to create a fully automated CI pipeline, based around the program created during project 1. 

This would involve using the tools learned since completing Project 1: Docker, Jenkins and Nexus. 


## Planning, Design and Project Tracking 

### Trello

I used Trello as my project management tool to keep track of the different tasks and divide them into To Do, Doing and Done

<img width="658" alt="Trello" src="https://github.com/jmusgrave14/QA-DevOps-Project-1/assets/139867104/f77f0857-8f88-4c42-8887-60a761bfa753">

### ERD

This basic Entity Relationship Diagram plans out the database used for the project

![ERD](https://github.com/jmusgrave14/QA-DevOps-Project-1/assets/139867104/97a99b31-b453-4d6c-856c-d8332fae20bc)

### Risk Assessment 

This is a basic initial risk assessment. As this was a training project the risks involved were low

![image](https://github.com/jmusgrave14/QA-DevOps-Project-1/assets/139867104/1269fab8-506d-4480-b425-1e80b149e5e5)


## Implementation

### Docker 

Firstly I created a new Dockerfile in my Project 1 folder

![image](https://github.com/jmusgrave14/QA-DevOps-Project-1/assets/139867104/8d55f64e-cc5a-43a6-97ff-0580e4c2d78b)

I then used this to build and run a Docker image of my Project 1 app

![image](https://github.com/jmusgrave14/QA-DevOps-Project-1/assets/139867104/e4f89e3f-6117-46f5-8cd7-ada46ad67431)

Finally I connected this image to the database I had created on MySQLWorkbench 

![image](https://github.com/jmusgrave14/QA-DevOps-Project-1/assets/139867104/545bc6de-a1eb-4563-b3b9-46d8e8afd30c)

### Nexus 

I was not very confident using Nexus due to difficulties with the teaching of it. However I followed instructions to sign in and create proxy and hosted repositiories

![image](https://github.com/jmusgrave14/QA-DevOps-Project-1/assets/139867104/2758276e-2df3-4e11-ad91-581217457378)

### Jenkins

I logged in as root in order to set up a Jenkins server 

![image](https://github.com/jmusgrave14/QA-DevOps-Project-1/assets/139867104/14461550-fb01-4493-a842-7ccbffdcefaa)

I then created a freestyle project and a pipeline, both linked to my GitHub repository 

![image](https://github.com/jmusgrave14/QA-DevOps-Project-1/assets/139867104/857687a8-ac8d-4934-9a93-883acbfd2005)

![image](https://github.com/jmusgrave14/QA-DevOps-Project-1/assets/139867104/21c7accc-0900-40c8-921b-5c4a47a778e0)

I then created a new Jenkinsfile in my GitHub repo which contained the code needed to build, push and deploy my app

![image](https://github.com/jmusgrave14/QA-DevOps-Project-1/assets/139867104/8a145010-ce09-4683-b808-a6572976724d)

I tested that the pipeline ran on Jenkins and made the necessary changes when it failed 

![image](https://github.com/jmusgrave14/QA-DevOps-Project-1/assets/139867104/183ae3ef-5e31-4c5e-adf8-dcb62aa15eba)


## Testing 

Once my app was running I tested it by changing the code and making sure it still built, and by going to the relevant localhost urls to check that the app functions of log and stat were working 

![image](https://github.com/jmusgrave14/QA-DevOps-Project-1/assets/139867104/ce1c3209-87b9-4775-80cb-081b0e99de2b)

![image](https://github.com/jmusgrave14/QA-DevOps-Project-1/assets/139867104/b80025dd-63d2-45c2-9ddd-b839de018e01)












