# Vicaima Performance Dialogue Platform

## Description
This project was developed during the **Vicaima × 42 Porto Hackathon** (May 2024) as part of a team tasked with creating a web platform for Vicaima. 
The goal was to design and implement a platform to facilitate the performance evaluation process within the organization, improving its efficiency through better communication and data handling. </br> </br>

[Presentation](https://github.com/mjorgecruz/vicaima/blob/main/Vicaima%20Hackaton.pdf)
</br></br>
The platform supports three distinct roles: **Admin (HR)**, **Evaluator**, and **Evaluated**, each with its own set of features tailored to their responsibilities.


## Features
- **Admin**:
  - Mass data upload (.csv) for employees.
  - Creation and management of evaluation events.
  - Monitoring ongoing evaluations.
  - Deletion of employee data.
- **Evaluator**:
  - Access to active evaluation events.
  - View employee performance data.
  - Evaluate employees and communicate the results.
- **Evaluated**:
  - Confirmation of knowledge of evaluations.
  - View performance feedback from evaluators.

## Technologies Used
- **Backend**: Built using Django with SQLite for data storage and management.
- **Security**: Implemented role-based access control and secure data handling using Django’s security features.
- **Frontend**: A clean and user-friendly interface to mediate interaction between users and the platform. Data views are customized based on the user’s role.

## Current Status
The core functionalities of the platform have been implemented, including role-based access, performance evaluation event management, and employee data handling. 
We have developed a consistent user experience through a design system that ensures interface clarity and ease of use.

## Next Steps
1. **Short-term**: Implement a data dashboard for enhanced visualization of organizational performance data and a mechanism for evaluated users to confirm their knowledge of evaluation results.
2. **Mid-term**: Add additional features to enhance each role's capabilities.
3. **Long-term**: Continuously adapt the platform to meet Vicaima’s specific organizational needs by introducing new variables and features.


## Team
- Lucas Medeiros (lumarque)
- Luís Balsa (luide-so)
- Rui Oliveira (ruiolive)
- Teresa Chow (tchow-so)
