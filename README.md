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

### 3. Create a New Branch
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

