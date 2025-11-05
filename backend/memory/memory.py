from dotenv import load_dotenv
import os
import redis
import json
from typing import Dict,List,Optional

load_dotenv(override=True)
redis_port = os.getenv("REDIS_PORT")
redis_host = os.getenv("REDIS_HOST")

class MemoryManager():
    def __init__(self):
        self.client = redis.Redis(
            host = os.getenv("REDIS_HOST"),
            port = int(os.getenv("REDIS_PORT"))
        )
    def ping(self)->bool:
        try:
            return self.client.ping()
        except redis.exceptions.ConnectionError:
            return False

    def save_state(self,agent_id:str,state:dict):
        self.client.set(f"agent:{agent_id}:state",json.dumps(state))
    def gt_state(self,agent_id:str) ->Dict:
        raw = self.client.get(f"agent:{agent_id}:state")
        return json.loads(raw) if raw else {}
    def save_summary(self,agent_id:str,summary:str):
        self.client.set(f"agent:{agent_id}:summary",summary)
    def get_summary(self,agent_id)->Optional[str]:
        raw = self.client.get(f"agent:{agent_id}:summary")
        return raw
    def save_query(self,agent_id:str,query:str):
        self.client.set(f"agent:{agent_id}:query",query)
    def query_history(self,agent_id:str,limit:int=10)-> List:
        raw = self.client.get(f"agent:{agent_id}:query",-limit,-1)
        return raw
    def set_intent(self, agent_id: str, intent: str):
        self.client.set(f"agent:{agent_id}:{intent}", intent)

    def get_intent(self, agent_id: str) -> Optional[str]:
        return self.client.get(f"agent:{agent_id}:intent")


