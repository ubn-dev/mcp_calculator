from fastmcp import FastMCP
from fastmcp.server.auth import BearerAuthProvider
# import os

public_key = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA/H/+6x8AajIQWXdfQ4nJ
ujOM+kUh25mgynJJ/GtyP86ABiAN0VyQSMrFpe82Utf+ZkrGqOwDuWt6o6J2M5NA
9m4GPZEvzUwehGlqpwXX8/12yUDbde7cvUbfFAlRnvcde6LIR5NV1ABzcNwYeyKT
UJOXT0tv5VehjcW4vrrVDI+5JGeMOQ/LIHz4nYL7S6Kf/KNQWw1lozYzx9PTOGym
/oPde+6yDda+1V91bwEgNOPtTcfZLpW6+uxCZ93wTUevYlQafWhSZjKMFyj0LHCC
Ziqjs+FMm50wiSn1i38fLIVx4/r8nRzx3gswJ6FuNSpJliLglYxKgyRbJ2X++wGG
ZwIDAQAB
-----END PUBLIC KEY-----"""

auth = BearerAuthProvider(
    public_key=public_key,
    issuer="https://calculator.ubnai.kr",
    audience="calculator"
)

# mcp = FastMCP(name="calculator", auth=auth)
mcp = FastMCP(name="calculator")


@mcp.tool
def multiply(a: float, b: float) -> float:
    """Multiplies two numbers together."""
    print(f"원격 MCP 서버(Smithery): Multiplying {a} and {b}")
    return a * b

if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=8000,
        path="/",
        log_level="debug",
    )
