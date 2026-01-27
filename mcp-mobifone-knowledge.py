from mcp.server.fastmcp import FastMCP
import json
import os
from typing import Dict, List, Any, Tuple
import numpy as np
from sentence_transformers import SentenceTransformer
import pickle

# Initialize the FastMCP server
mcp = FastMCP("MobiFone RAG Server")

# Paths
DATA_FILE_PATH = r"d:\windifybot\mcp-english-tutor\mcp-english-tutor\mobifone_introduce.json"
EMBEDDINGS_FILE_PATH = r"d:\windifybot\mcp-english-tutor\mcp-english-tutor\embeddings.pkl"

# Initialize embedding model (free multilingual model)
# This model works well with Vietnamese text
embedding_model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

class ServiceEmbeddings:
    def __init__(self):
        self.services: Dict[str, Dict[str, Any]] = {}
        self.embeddings: Dict[str, np.ndarray] = {}
        self.service_texts: Dict[str, str] = {}
        
    def load_data(self) -> Dict[str, Any]:
        """Loads the MobiFone data from the JSON file."""
        if not os.path.exists(DATA_FILE_PATH):
            return {}
        try:
            with open(DATA_FILE_PATH, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            return {"error": str(e)}
    
    def _flatten_services(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Helper to flatten the service structure."""
        services = {}
        root = data.get("Tài liệu giới thiệu hệ sinh thái giải pháp số MobiFone", {})
        
        for chapter_name, chapter_content in root.items():
            if isinstance(chapter_content, dict) and chapter_name not in ["Mục lục", "Thông tin liên hệ"]:
                for service_name, service_details in chapter_content.items():
                    if isinstance(service_details, dict):
                        services[service_name] = service_details
                        services[service_name]['_chapter'] = chapter_name
        return services
    
    def _service_to_text(self, service_name: str, service_details: Dict[str, Any]) -> str:
        """Convert service details to searchable text."""
        text_parts = [f"Tên dịch vụ: {service_name}"]
        
        # Add all text content from the service
        for key, value in service_details.items():
            if key == '_chapter':
                text_parts.append(f"Chương: {value}")
            elif isinstance(value, str):
                text_parts.append(f"{key}: {value}")
            elif isinstance(value, list):
                text_parts.append(f"{key}: {' '.join(str(v) for v in value)}")
            elif isinstance(value, dict):
                # Handle nested dicts
                dict_text = ' '.join(f"{k}: {v}" for k, v in value.items() if isinstance(v, (str, int, float)))
                text_parts.append(f"{key}: {dict_text}")
        
        return "\n".join(text_parts)
    
    def build_embeddings(self):
        """Build embeddings for all services."""
        print("Loading data...")
        data = self.load_data()
        
        print("Flattening services...")
        self.services = self._flatten_services(data)
        
        print(f"Found {len(self.services)} services")
        print("Creating text representations...")
        
        # Create text representation for each service
        for service_name, service_details in self.services.items():
            self.service_texts[service_name] = self._service_to_text(service_name, service_details)
        
        print("Generating embeddings...")
        # Generate embeddings
        texts = list(self.service_texts.values())
        names = list(self.service_texts.keys())
        
        embeddings = embedding_model.encode(texts, show_progress_bar=True)
        
        # Store embeddings
        for name, embedding in zip(names, embeddings):
            self.embeddings[name] = embedding
        
        print("Saving embeddings...")
        self.save_embeddings()
        print("Done!")
    
    def save_embeddings(self):
        """Save embeddings to file."""
        data_to_save = {
            'embeddings': self.embeddings,
            'service_texts': self.service_texts,
            'services': self.services
        }
        with open(EMBEDDINGS_FILE_PATH, 'wb') as f:
            pickle.dump(data_to_save, f)
    
    def load_embeddings(self):
        """Load embeddings from file."""
        if not os.path.exists(EMBEDDINGS_FILE_PATH):
            print("Embeddings file not found. Building embeddings...")
            self.build_embeddings()
            return
        
        print("Loading embeddings from file...")
        with open(EMBEDDINGS_FILE_PATH, 'rb') as f:
            data = pickle.load(f)
            self.embeddings = data['embeddings']
            self.service_texts = data['service_texts']
            self.services = data['services']
        print(f"Loaded {len(self.embeddings)} service embeddings")
    
    def search(self, query: str, top_k: int = 3) -> List[Tuple[str, float, Dict[str, Any]]]:
        """Search for most relevant services using cosine similarity."""
        # Generate query embedding
        query_embedding = embedding_model.encode([query])[0]
        
        # Calculate cosine similarity with all service embeddings
        similarities = {}
        for service_name, service_embedding in self.embeddings.items():
            # Cosine similarity
            similarity = np.dot(query_embedding, service_embedding) / (
                np.linalg.norm(query_embedding) * np.linalg.norm(service_embedding)
            )
            similarities[service_name] = similarity
        
        # Sort by similarity
        sorted_services = sorted(similarities.items(), key=lambda x: x[1], reverse=True)
        
        # Return top k results
        results = []
        for service_name, score in sorted_services[:top_k]:
            results.append((service_name, float(score), self.services[service_name]))
        
        return results

# Initialize the embeddings system
service_embeddings = ServiceEmbeddings()

@mcp.tool()
def search_services(query: str, top_k: int = 1) -> str:
    """
    Tool này dùng để tìm kiếm thông tin chi tiết về các dịch vụ hoặc giải pháp số của mobifone.

    query: dịch vụ mà khách hàng muốn biết
    top_k: mặc định bằng 1

    Trả về: 1 json chứa thông tin về dịch vụ mà khách hàng muốn biết
    """
    if top_k > 1:
        top_k = 1
    
    try:
        results = service_embeddings.search(query, top_k)
        
        output = {
            "query": query,
            "results": []
        }
        
        for service_name, score, service_details in results:
            output["results"].append({
                "service_name": service_name,
                "relevance_score": round(score, 4),
                "details": service_details
            })
        
        return json.dumps(output, ensure_ascii=False, indent=2)
    
    except Exception as e:
        return json.dumps({
            "error": str(e),
            "query": query
        }, ensure_ascii=False, indent=2)
    
if __name__ == "__main__":
    service_embeddings.load_embeddings()
    # test_query = "Phần mềm kế toán MobiFone Accounting Solution"
    # result = search_services(test_query, top_k=1)
    # with open("output.txt", "w", encoding="utf-8") as f:
    #     f.write(result)
    mcp.run(transport="stdio")