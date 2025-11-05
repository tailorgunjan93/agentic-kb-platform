from db.async_pool import get_conncetion,release_conncetion
from models.AgentState import AgentState

async def memory_node(state:AgentState)->AgentState:
    conn = await get_conncetion()
    await conn.execute(
            """INSERT INTO agent_memory (agent_id,query,intent,summary)
                VALUES ($1,$2,$3,$4)
""",state.agent_id,state.query,state.intent,state.summary
    )

    print(f"[Memory] Logged query for agent_id={state.agent_id}")
    return state

