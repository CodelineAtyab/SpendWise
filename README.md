# SpendWise

# The Expense Tracker Application - Python/FastAPI application with MySQL

This repository contains a FastAPI application that stores and manages user expenses in a MySQL database. 

This guide will help you fork the repository, and provide you steps to manually run this application.

These manual steps can be used to write a Dockerfile for this application along with a docker-compose.yaml, and run both application and database containers locally by just using one command.

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Git](https://git-scm.com/)

## Getting Started

### 1. Fork the Repository

1. Go to the original repository: [Link of Repo](https://github.com/CodelineAtyab/SpendWise)
2. Click the `Fork` button on the top right to create your own copy of the repository.

Note: Please watch [this youtube video](https://www.youtube.com/watch?v=CML6vfKjQss) if you want to know just the submission process. Its the same as contributing to an open-source project.

### 2. Clone Your Forked Repository

1. Clone your forked repository. You can simply do it by clicking on `Code` and copying the HTTPS URL.
2. Now simply clone the repo on your PC. Command will be like `git clone [URL]` where URL is the one, you got from step 1.

### 3. Synchronize the main branch
1. Run `git status` and make sure you are on the main branch.
2. Run `git pull` to make sure the upstream origin/main has the same state as downstream main branch.

### 4. Create a New Branch
Before implementing anything, make sure you are on a new branch.

You can create a new branch and switch to it by running:
```bash
git checkout -b feature/ticket-id-short-task-name
```
Please replace `ticket-id` with your actual ticket ID from Clickup in lower case and without any spaces.
Please replace `short-task-name` with a title that is related to your ticket's title. Please keep this short and lower case without any spaces as well.

For Example:
```bash
git checkout -b feature/86ermm50c-generate-pattern
```

Note: Remember, this will make a copy of the branch we were on before we ran this command. In our case, this `86ermm50c-generate-pattern` branch will be a copy of `main` branch.

### 5. Do the work needed
Now, simply start working on the code changes or any other changes related to the project.

### 6. Push the changes to github
Run `git status` -> `git add *` -> `git commit -m "a message"` -> `git push`. 
If we are pushing the new branch for the first time, git will show a command to create an `upstream` branch. Run that command.

### 7. If needed make more changes
We can still keep updating the project files and once the application is working, we can again do:

`git status` -> `git add *` -> `git commit -m "a message"` -> `git push`

### 8. Create a PR (Pull Request)
Once the work is done and pushed, we can goto github and create a `Pull Request` for our branch `86ermm50c-generate-pattern`

### 9. Get it approved
Request the team members to review the code and give you approvals

### 10. Merge the changes back to the main branch
Once we get 3 approvals, we can simply select `Squash` as a merge strategy and then click the `Merge` button on github.

### 11. We are done
Now, for a new task, we can simply repeat steps from (4) to (10) and keep doing this.