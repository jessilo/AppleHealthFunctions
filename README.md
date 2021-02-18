# AppleHealthFunctions
Python functions to process Apple Health exports into BigQuery and dashboards in Google Cloud (GCP).

Background: The increasing usage of smart health devices has meant that the amount of personal health data created is rapidly expanding, presenting new challenges for researchers looking to use this data. 70 percent of clinical trials are projected to incorporate sensors by 2025. The usage of wearables devices in clinical research has increased exponentially every year since 2008, especially in recent large-scale COVID-19 studies.

Challenge: There are two main issues facing clinical researchers looking to use wearables data. First, researchers must manually create their own data pipeline each time, which is tedious and error-prone. Also, complex data and computation regulations require researchers to take on a wide-range of non-scientific computational skills with limited guidance

Solution: My solution is a GCP-based ETL tool that consolidates wearables data from multiple smart health devices for researchers to access and analyze easily together in a dashboard. This can be used as a low-cost, cloud-based, lightweight accelerator for biomedical research, and clinical trials. It should:
- Scalable: A single, scalable tool that can be set up easily with multiple clients
- Cost-Effective: Save researchers hundreds of hours and thousands of dollars in setup, configuration, and engineering
- Collaborative and Efficient: Built on modern, managed cloud infrastructure
- Comprehensive: Able to process wearables data from all study participants
- Flexible: Browse, compare, and analyze data individually or altogether
- Extensible: Expanded and extended to support other research data alongside wearables

Architecture: 

![Architecture Diagram](https://github.com/jessilo/AppleHealthFunctions/blob/main/Wearables%20Architecture%20.png)

Project Scope: Apple Watch data from multiple users will be transformed using an automated pipeline to make data available for analysis in a variety of ways, including a dashboard view. All data can be updated through the upload new Apple Watch files.

