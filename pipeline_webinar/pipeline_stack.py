import aws_cdk as cdk
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep
from constructs import Construct

class PipelineStack(cdk.Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # source_artifact = aws_codepipeline.Artifact()
        # cloud_assembly_artifact = aws_codepipeline.Artifact()


        # pipelines.CdkPipeline(self, "Pipeline",
        #     cloud_assembly_artifact=cloud_assembly_artifact,
        #     pipeline_name='WebinarPipeline',
        #     source_action=aws_codepipeline_actions.GitHubSourceAction(
        #         action_name='GitHub',
        #         output=source_artifact,
        #         oauth_token=Stack.SecretValue.secret_manager('github-token'),
        #         repo='cdkpipeline',
        #         owner='mbongeb',
        #         trigger=aws_codepipeline_actions.GitHubTrigger.POLL),
        #     synth_action=pipelines.SimpleSynthAction(
        #         source_artifact=source_artifact,
        #         cloud_assembly_artifact=cloud_assembly_artifact,
        #         install_command='npm install -g aws-cdk && pip install -r requirements.txt',
        #         synth_command='cdk synth'
        #     ))


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