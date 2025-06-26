from fastmcp import FastMCP
from fastmcp.server.auth import BearerAuthProvider
import os

# public_key = """-----BEGIN PUBLIC KEY-----
# MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEApuHurasLiK0K2GnY8C9M
# 2Cf+GgeRKwCFidrkNMKMpPfNmym4zaWiE6g3ZC0c7b3fioSds/BYv2N3Qp0f7rxQ
# YIUjf7DdPf3F8UE2emg9ElXuxEJWsovHbgUV2xPRtweVByIAmEjUPdu0iM9Pu8Vn
# nlmOYl7peBVOpMbf1/gKcbZnaN/cgcTuLloBdeaOALG2eDzifrRMfhoOz22JR80i
# E++j2hz4lsxcgIb5RIUGx4e1H2Hs50J0SCYkNj2HieEqi8LKc0SZsDb2/4kUmk52
# M5cIxvK0n2xuWW4hXsqZI2duXWTqXwVsrzCwclSZz/F6Eb/nraxL/oep1FCkFnCo
# PwIDAQAB
# -----END PUBLIC KEY-----"""

# auth = BearerAuthProvider(
#     public_key=public_key,
#     issuer="https://calculator.ubnai.kr",
#     audience="calculator"
# )

# mcp = FastMCP(name="calculator", auth=auth)
mcp = FastMCP(name="calculator")


@mcp.tool
def multiply(a: float, b: float) -> float:
    """Multiplies two numbers together."""
    print(f"원격 MCP 서버(Smithery 배포): Multiplying {a} and {b}")
    return a * b

if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        # port = int(os.getenv("PORT", 8080)),
        port = int(os.getenv("PORT", 8000)),
        path="/mcp",
        log_level="debug",
    )
