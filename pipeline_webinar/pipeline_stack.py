import aws_cdk as cdk
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep
from constructs import Construct

from .webservice_stage import WebServiceStage

class PipelineStack(cdk.Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)


        pipeline = CodePipeline(self, "Pipeline",
                    pipeline_name="webinarcd",
                    synth=ShellStep("Synth",
                        input=CodePipelineSource.git_hub("mbongeb/cdk-pipeline", 
                            "main", authentication=cdk.SecretValue.secrets_manager("github-token")),
                        
                        commands=["npm install -g aws-cdk",
                                "python -m pip install -r requirements.txt",
                                "cdk synth"]
                    )
                )

        pipeline.add_stage(WebServiceStage(self, 'Pre-Prod', env=cdk.Environment(account="213911150042", region="us-west-2")))