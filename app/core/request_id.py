import secrets


def generate_request_id() -> str:
    return "req_" + secrets.token_hex(8)