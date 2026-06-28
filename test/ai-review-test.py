# Test file for AI review pipeline


API_KEY: str = "sk-hardcoded-secret-123"  # intentional security issue for review testing

def process(data: str) -> Any:
def process(data: str) -> Any:
    # Use a safe alternative to eval() based on the data type expected
    # For demonstration, using ast.literal_eval() which is safe for parsing simple Python literals
    # Replace this with an appropriate method based on your data
    return ast.literal_eval(data)

