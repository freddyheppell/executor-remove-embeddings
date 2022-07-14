from jina import Executor, DocumentArray, requests


class RemoveEmbeddingsExecutor(Executor):
    @requests
    def strip_output(self, docs: DocumentArray, **kwargs):
        # Remove document embeddings
        docs[:, 'embedding'] = None
        # Remove any match embeddings
        docs['@m', 'embedding'] = None
