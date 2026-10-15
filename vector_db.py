from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct

class QdrantStorage:
    def __init__(self, url="", collection="docs", dim=3072):
        self.client = QdrantClient(url=url, timeout=30)
        self.collection = collection
        if not self.client.collection_exists(self.collection):
            self.client.create_collection(
                collection_name = self.collection,
                vectors_config=VectorParams(size=dim, distance=Distance.COSINE)
            )

    def upsert(self, ids, vectors, payloads):
        points = [PointStruct(id=ids[i], vector=vectors[i], payload=payloads[i]) for i in range(len(ids))]
        self.client.upsert(self.collection, points=points)

    def search(self, query_vector, top_k=5):
        print("DEBUG: Collection:", self.collection)
        print("DEBUG: Query vector length:", len(query_vector))
        results = self.client.query_points(
            collection_name = self.collection,
            query=query_vector,
            with_payload=True,
            limit=top_k
        ).points

        for point in results:
            print("DEBUG: Score:", point.score)
            print("DEBUG: Payload:", point.payload)

        contexts=[]
        sources=set()

        for r in results:
            payload = getattr(r, "payload", None) or {}
            text = payload.get("text", "")
            source=payload.get("source", "")
            if text:
                contexts.append(text)
                sources.add(source)

        return {"contexts": contexts, "sources": sources}