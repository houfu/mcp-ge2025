from mcp.server import FastMCP

# Initialize FastMCP server
mcp = FastMCP("SG Election MCP Server")


@mcp.resource("manifesto://{party}")
def get_manifesto(party: str) -> str:
    """
    Function to get the manifesto of a party.
    :param party: The name of the party.
    :return: A string containing the manifesto.
    """
    dictionary = {
        "People's Action Party": "PAP",
        "Workers' Party": "WP",
        "Singapore Democratic Party": "SDP",
        "Singapore People's Party": "SPP",
        "Progress Singapore Party": "PSP",
        "National Solidarity Party": "NSP",
        "Singapore Democratic Alliance": "SDA",
        "Red Dot United": "RDU",
        "People's Power Party": "PPP",
        "People's Alliance for Reform": "PAR",
    }
    party = dictionary.get(party, party)
    filepath = f"data/manifestos/{party.upper()}.md"
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return f"Manifesto for {party} not found. Please check the party name. Or they don't have a manifesto?"


if __name__ == "__main__":
    mcp.run()
