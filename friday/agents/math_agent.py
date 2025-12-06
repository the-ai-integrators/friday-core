class MathAgent:
    """A tiny math agent — simple, safe, educational."""
    
    def run(self, expression: str) -> str:
        try:
            result = eval(expression)
            return f"Result: {result}"
        except Exception:
            return "Invalid expression"
