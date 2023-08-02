from aws_cdk import (
    aws_lambda as _lambda,
    aws_iam as iam,
    Stack,
    Duration,
)
from constructs import Construct


class TestNdivGatewayStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        common_layer = _lambda.LayerVersion(
            self, 'common_package_layer',
            code=_lambda.Code.from_asset('dependencies/common'),
            compatible_runtimes=[_lambda.Runtime.PYTHON_3_9],
            compatible_architectures=[_lambda.Architecture.X86_64]
        )

        handler = _lambda.Function(
            self, 'test-ndvi-gateway',
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.from_asset('_lambda'),
            handler='main.lambda_handler',
            timeout=Duration.minutes(15),
            memory_size=256,
            layers=[common_layer],
        )

        handler.add_to_role_policy(iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            resources=["*"],
            actions=["sqs:*"]
        ))
