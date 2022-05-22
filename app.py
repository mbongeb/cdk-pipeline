#!/usr/bin/env python3
import os

import aws_cdk as cdk

from pipeline_webinar.pipeline_stack import PipelineStack

app = cdk.App()
PipelineStack(app, "PipelineStack", env=cdk.Environment(account="213911150042", region="us-west-2"))
app.synth()
