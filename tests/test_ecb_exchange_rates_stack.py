"""
Description: Unit tests for validating the ECB Exchange Rates CDK stack.
Ensures essential resources such as DynamoDB tables, Lambda functions, and API Gateway are correctly configured.

Creator: Subhan Malik 
Date: 10/20/24
Email: subhan.sm74@gmail.com
"""

import aws_cdk as core
import aws_cdk.assertions as assertions
from app import ECBExchangeRatesStack


def create_stack():
    """Creates and returns an instance of ECBExchangeRatesStack."""
    app = core.App()
    return ECBExchangeRatesStack(app, 'ecb-exchange-rates')


def test_dynamodb_table_created():
    """Verify if the DynamoDB table is correctly created with proper schema and deletion policy."""
    stack = create_stack()
    template = assertions.Template.from_stack(stack)
    template.has_resource_properties('AWS::DynamoDB::Table', {
        'KeySchema': [{'AttributeName': 'id', 'KeyType': 'HASH'}],
        'AttributeDefinitions': [{'AttributeName': 'id', 'AttributeType': 'S'}]
    })
    template.has_resource('AWS::DynamoDB::Table', {'DeletionPolicy': 'Delete'})


def test_update_lambda_created():
    """Tests if the update Lambda function is created with correct configuration."""
    stack = create_stack()
    template = assertions.Template.from_stack(stack)
    template.has_resource_properties('AWS::Lambda::Function', {
        'Handler': 'update_ecb_exchange_rates.handler',
        'Runtime': 'python3.9',
        'Timeout': 360,
        'Environment': {'Variables': {'DYNAMO_TABLE_NAME': {}}}
    })


def test_read_lambda_created():
    """Tests if the read Lambda function is created with correct configuration."""
    stack = create_stack()
    template = assertions.Template.from_stack(stack)
    template.has_resource_properties('AWS::Lambda::Function', {
        'Handler': 'get_ecb_exchange_rates.handler',
        'Runtime': 'python3.9',
        'Timeout': 60,
        'Environment': {'Variables': {'DYNAMO_TABLE_NAME': {}}}
    })


def test_eventbridge_rule_created():
    """Tests if the EventBridge rule is created with correct schedule."""
    stack = create_stack()
    template = assertions.Template.from_stack(stack)
    template.has_resource_properties('AWS::Events::Rule', {
        'ScheduleExpression': 'cron(0 17 * * ? *)'
    })


def test_rest_api_created():
    """Tests if the REST API is created and configured correctly."""
    stack = create_stack()
    template = assertions.Template.from_stack(stack)
    template.has_resource_properties('AWS::ApiGateway::RestApi', {'Name': 'api-ecb-exchange-rates'})
    template.has_resource_properties('AWS::ApiGateway::Method', {
        'HttpMethod': 'GET',
        'AuthorizationType': 'NONE'
    })


def test_iam_role_created():
    """Tests if the IAM Role is created with appropriate policies."""
    stack = create_stack()
    template = assertions.Template.from_stack(stack)
    template.has_resource_properties('AWS::IAM::Role', {
        'AssumeRolePolicyDocument': {
            'Statement': [{'Effect': 'Allow', 'Principal': {'Service': 'cloudformation.amazonaws.com'}}]
        }
    })
