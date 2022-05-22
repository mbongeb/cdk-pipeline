import aws_cdk as cdk
from constructs import Construct

from .pipeline_webinar_stack import PipelineWebinarStack

class WebServiceStage(cdk.Stage):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        service = PipelineWebinarStack(self, "WebService")

        