# Vicaima Performance Dialogue Platform

## Description
This project was developed during the **Vicaima × 42 Porto Hackathon** (May 2024) as part of a team tasked with creating a web platform for Vicaima. 
The Vicaima Hackathon aims to create an online application to streamline the process of performance evaluation through data collection and analysis. The main objective is to convert a largely manual task into a more automated process, enhancing efficiency and accuracy.</br> </br>

---

[Presentation](https://github.com/mjorgecruz/vicaima/blob/main/Vicaima%20Hackaton.pdf)

---

</br></br>

## Objectives

- **Develop an Online Application:** Build a platform that facilitates performance evaluation through automated data collection.
- **Automation of Manual Tasks:** Transform manual evaluation processes into a more automated workflow.

## Features
The platform supports three distinct roles: **Admin (HR)**, **User**, each with its own set of features tailored to their responsibilities.

- **Admin**:
  - Add collaborators to the system.
  - Import users from a CSV file for easy onboarding.
  - Creation and management of evaluation events.
  - Monitoring ongoing evaluations.
  - Deletion of employee data.
- **User**:
  - Access to active evaluation events.
  - View employee performance data.
  - Evaluate employees and communicate the results.
  - View performance feedback from evaluators.



## Technologies Used
- **Backend**: Built using Django with SQLite for data storage and management.
- **Frontend**: A clean and user-friendly interface to mediate interaction between users and the platform. Data views are customized based on the user’s role.

## Current Status
The core functionalities of the platform have been implemented, including role-based access, performance evaluation event management, and employee data handling. 

## Next Steps
1. **Short-term**:
     - Implement a data dashboard for enhanced visualization of organizational performance data and a mechanism for evaluated users to confirm their knowledge of evaluation results.
     - Editable evaluation forms tailored to specific needs.
     - Use cookies for persistent sessions, ensuring a seamless user experience. Implement role-based access control and secure data handling using Django’s security features.
3. **Mid-term**:
     - Add additional features to enhance each role's capabilities.
5. **Long-term**:
     - Continuously adapt the platform to meet Vicaima’s specific organizational needs by introducing new variables and features.
     - Deploy the application using Docker for consistent environment management.
     - Implement a notification system for updates and reminders.

### Team Members

- **Bruno Lopes** (`brpereir`)
- **Ebenézer Marquezine** (`ebmarque`)
- **João Alves** (`joaoalme`)
- **Jorge Cruz** (`masoares`)
