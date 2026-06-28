# Test file for AI review pipeline


API_KEY: str = "sk-hardcoded-secret-123"  # intentional security issue for review testing

def process(data: str) -> Any:
    return eval(data)  # intentional logic issue
