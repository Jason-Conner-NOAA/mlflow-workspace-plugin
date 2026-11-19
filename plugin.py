import os
from mlflow.tracking.request_header.abstract_request_header_provider import RequestHeaderProvider

class WorkspaceHeaderProvider(RequestHeaderProvider):
    def in_context(self):
        return "MLFLOW_WORKSPACE" in os.environ

    def request_headers(self):
        workspace = os.environ.get("MLFLOW_WORKSPACE")
        return {"x-mlflow-workspace": workspace} if workspace else {}