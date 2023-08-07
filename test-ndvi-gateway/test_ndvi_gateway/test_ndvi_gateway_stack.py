from aws_cdk import (
    aws_lambda as _lambda,
    aws_iam as iam,
    aws_events as events,
    aws_events_targets as targets,
    Stack,
    Duration,
)
from constructs import Construct


class TestNdivGatewayStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        common_layer = _lambda.LayerVersion(
            self, 'testing_package_layer',
            code=_lambda.Code.from_asset('dependencies/testing_package'),
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

        is_report_morning = events.Rule(
            self, "Report in the morning",
            schedule=events.Schedule.expression("cron(0 23 * * ? *)")
        )

        is_report_morning.add_target(
            targets.LambdaFunction(handler=handler))

        is_report_evening = events.Rule(
            self, "Report in the evening",
            schedule=events.Schedule.expression("cron(0 11 * * ? *)")
        )

        is_report_evening.add_target(
            targets.LambdaFunction(handler=handler))

        handler.add_to_role_policy(iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            resources=["*"],
            actions=["sqs:*"]
        ))
