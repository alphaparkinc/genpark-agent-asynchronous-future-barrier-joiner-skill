"""Asynchronous Future Barrier Joiner Engine.
100% Python Standard Library.
"""

from typing import Dict, Any

class AsyncFutureBarrierJoiner:
    """Coordinates scatter-gather flows by holding barriers until all registered child agent promises resolve."""
    def __init__(self):
        self.futures: Dict[str, Dict[str, Any]] = {}

    def register_future(self, future_id: str, payload: Any = None):
        self.futures[future_id] = {"resolved": False, "payload": payload}

    def resolve_future(self, future_id: str, result: Dict[str, Any]):
        if future_id in self.futures:
            self.futures[future_id]["resolved"] = True
            self.futures[future_id]["result"] = result

    def join_all(self) -> Dict[str, Any]:
        all_resolved = all(f["resolved"] for f in self.futures.values()) if self.futures else True
        results = {fid: f.get("result") for fid, f in self.futures.items() if f["resolved"]}
        return {
            "all_resolved": all_resolved,
            "resolved_count": len(results),
            "pending_count": len(self.futures) - len(results),
            "aggregated_results": results
        }
