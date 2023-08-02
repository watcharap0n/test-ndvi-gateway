import aws_cdk as core
import aws_cdk.assertions as assertions

from test_ndiv_gateway.test_ndiv_gateway_stack import TestNdivGatewayStack

# example tests. To run these tests, uncomment this file along with the example
# resource in test_ndiv_gateway/test_ndiv_gateway_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = TestNdivGatewayStack(app, "test-ndiv-gateway")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
