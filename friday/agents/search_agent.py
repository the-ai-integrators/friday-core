import requests

class SearchAgent:
    """A safe and simple public search agent using DuckDuckGo API."""

    def run(self, query: str):
        url = f"https://api.duckduckgo.com/?q={query}&format=json&no_redirect=1"

        try:
            response = requests.get(url, timeout=5)

            # Try decoding JSON safely
            try:
                data = response.json()
            except ValueError:
                # JSON decode failed → fallback
                return {
                    "query": query,
                    "abstract": None,
                    "error": "Invalid response from search API (non-JSON)",
                }

            return {
                "query": query,
                "abstract": data.get("AbstractText") or "No summary available",
            }

        except Exception as e:
            # Any network or unexpected error → safe fallback
            return {
                "query": query,
                "abstract": None,
                "error": f"Search request failed: {str(e)}",
            }
