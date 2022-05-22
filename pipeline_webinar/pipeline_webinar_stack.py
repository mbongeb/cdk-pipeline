from cgitb import handler
from aws_cdk import (
    # Duration,
    Stack,
    aws_lambda,
    aws_apigateway,
    # aws_sqs as sqs,
)
from constructs import Construct

class PipelineWebinarStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        function = aws_lambda.Function(self, "Backend",
            runtime=aws_lambda.Runtime.PYTHON_3_7,
            handler="handler.main",
            code=aws_lambda.Code.from_asset("./lambda")
            )

        api = aws_apigateway.LambdaRestApi(self, "API",
            handler=function)