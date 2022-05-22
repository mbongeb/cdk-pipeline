import aws_cdk as core
import aws_cdk.assertions as assertions

from pipeline_webinar.pipeline_webinar_stack import PipelineWebinarStack

# example tests. To run these tests, uncomment this file along with the example
# resource in pipeline_webinar/pipeline_webinar_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = PipelineWebinarStack(app, "pipeline-webinar")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
