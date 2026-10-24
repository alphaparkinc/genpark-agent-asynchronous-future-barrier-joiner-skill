from client import AsyncFutureBarrierJoiner

joiner = AsyncFutureBarrierJoiner()
joiner.register_future("sub_agent_search")
joiner.register_future("sub_agent_code_analysis")

joiner.resolve_future("sub_agent_search", {"citations_found": 8})
status_partial = joiner.join_all()
print("Partial Join:", status_partial["all_resolved"], f"(Pending: {status_partial['pending_count']})")

joiner.resolve_future("sub_agent_code_analysis", {"ast_nodes": 450})
status_complete = joiner.join_all()
print("Complete Join:", status_complete["all_resolved"], f"(Resolved: {status_complete['resolved_count']})")
