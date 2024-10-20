📊 Backend_Task
📝 Introduction
This project outlines a serverless application designed to monitor and retrieve exchange rate data from the European Central Bank (ECB). It uses AWS Lambda, DynamoDB, and is deployable via AWS CDK. The application ensures data is current and exposes a REST API for data retrieval.

🔑 Key Components
✅ DynamoDB Table: Primary storage for exchange rates.
🛠️ Lambda Functions: One updates exchange rates daily; another retrieves data.
🌐 API Gateway: Accesses the latest ECB exchange rates and updates.
🎯 Objectives
🔄 Automated Data Retrieval: Automatically fetches exchange rates from the ECB.
⏰ Scheduled Updates: Updates data daily at 17:00:00 UTC.
⚡ Efficient Data Storage: Uses DynamoDB for high-performance data management.
🌍 API Accessibility: REST API for accessing exchange rates.
🧪 Testing Framework: Ensures functionality and reliability.
📈 Scalable Architecture: Scales automatically according to demand.
🏗️ System Architecture
Data Source: ECB for exchange rate data.
🔄 AWS Lambda Functions:
Update Exchange Rates Lambda: Fetches and updates rates daily.
Get Exchange Rates Lambda: Retrieves current rates via the REST API.
📂 DynamoDB Table: Ensures swift data updates and retrievals.
🌐 AWS API Gateway: Provides a RESTful endpoint for accessing the latest rates.
🛠️ AWS CDK: Defines and provisions cloud resources.
🔔 AWS EventBridge: Triggers daily updates and initializes the DynamoDB table upon deployment.
🚀 Deployment Steps

Prerequisites:

Install AWS CLI and configure access.
Install AWS CDK: npm install -g aws-cdk.
Ensure Python 3.8+ is installed.
Install Python dependencies: pip install -r requirements.txt.
Repository Setup:

Clone the repository: git clone https://github.com/subhan-cod/Backend_Task.git
Navigate to the project directory: CD Back_End_Task
CDK Bootstrapping:

Bootstrap the AWS environment: cdk bootstrap.
System Deployment:

Deploy using AWS CDK: cdk deploy.
📚 Operational Guide
🌐 Accessing the API: Use the provided API Gateway endpoint to query exchange rates.
🧪 Testing the API: Use tools like curl or Postman.
📊 Monitoring and Logs: Use AWS Lambda and CloudWatch.
🗑️ Cleanup: Use cdk destroy to decommission resources.
✅ Execution Steps

Accessing the REST API: Retrieve exchange rates using the API Gateway endpoint.
Testing the API: Validate functionality using Python requests library, Postman, or curl.
Monitoring and Logging: Monitor via AWS Management Console.
Cleanup Procedure: Remove resources using cdk destroy.

🧪 Testing Protocol
Objective: Validate integrity and performance of the serverless architecture.
Execution Steps:
Install dependencies: pip install -r requirements.txt
Run tests: pytest
Review outcomes and address failures promptly.

📈 Significance of Testing
Testing ensures the application meets design specifications and operates reliably. Integrating these tests into a CI/CD pipeline ensures continuous validation of functionality and performance.