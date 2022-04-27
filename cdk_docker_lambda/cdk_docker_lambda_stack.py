from aws_cdk import (
    # Duration,
    Stack,
    aws_lambda as _lambda
)
from constructs import Construct

class CdkDockerLambdaStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.prediction_lambda = _lambda.DockerImageFunction(
            scope=self,
            id="ExampleDockerLambda",
            # Function name on AWS
            function_name="ExampleDockerLambda",
            # Use aws_cdk.aws_lambda.DockerImageCode.from_image_asset to build
            # a docker image on deployment
            code=_lambda.DockerImageCode.from_image_asset(
                # Directory relative to where you execute cdk deploy
                # that contains a Dockerfile with build instructions
                directory="cdk_docker_lambda/ExampleDockerLambda"
            ),
        )

        self.prediction_lambda.add_function_url(
            auth_type=_lambda.FunctionUrlAuthType.NONE
        )