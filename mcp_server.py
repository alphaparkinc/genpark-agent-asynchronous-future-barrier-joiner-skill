import sys
import json
from client import AsyncFutureBarrierJoiner

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "check_barrier",
                        "description": "Checks barrier synchronization status across registered future handles.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "join_type": {"type": "string"}
                            }
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        joiner = AsyncFutureBarrierJoiner()
        res = joiner.join_all()
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "content": [{"type": "text", "text": json.dumps(res, indent=2)}]
            }
        }
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

def main():
    joiner = AsyncFutureBarrierJoiner()
    print(json.dumps(joiner.join_all(), indent=2))

if __name__ == "__main__":
    main()
