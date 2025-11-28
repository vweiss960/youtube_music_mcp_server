# youtube_music_mcp_server

MCP Server for interacting with YouTube Music. This server provides tools to search, play, and get information about songs on YouTube Music.

## Features

- Search YouTube Music for songs, artists, albums, and playlists
- Get detailed song information
- Play songs directly in your browser
- Web search using Brave Search API
- Get current date and time

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- Git

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/youtube_music_mcp_server.git
   cd youtube_music_mcp_server
   ```

2. **Create a virtual environment:**

   **Windows:**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

   **macOS/Linux:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **(Optional) Set up environment variables:**

   If you want to use the Brave Search API, create a `.env` file in the root directory:
   ```
   BRAVE_API_KEY=your_api_key_here
   ```

### Running the MCP Server

You can run the server in two ways:

#### Option 1: Direct execution
```bash
python main.py
```

#### Option 2: Configure with Claude Desktop

1. Open your Claude Desktop configuration file:
   - **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`
   - **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
   - **Linux:** `~/.config/Claude/claude_desktop_config.json`

2. Add the following configuration (adjust paths as needed):

   **Windows:**
   ```json
   {
     "mcpServers": {
       "youtube-music": {
         "command": "C:\\path\\to\\youtube_music_mcp_server\\venv\\Scripts\\python.exe",
         "args": ["C:\\path\\to\\youtube_music_mcp_server\\main.py"]
       }
     }
   }
   ```

   **macOS/Linux:**
   ```json
   {
     "mcpServers": {
       "youtube-music": {
         "command": "/path/to/youtube_music_mcp_server/venv/bin/python",
         "args": ["/path/to/youtube_music_mcp_server/main.py"]
       }
     }
   }
   ```

3. Restart Claude Desktop to load the MCP server.

## Available Tools

- **search_youtube_music** - Search for songs, artists, albums, or playlists
- **get_song_details** - Get information about a specific song
- **play_in_browser** - Open a song in YouTube Music in your default browser
- **brave_web_search** - Perform web searches (requires BRAVE_API_KEY)
- **get_current_date** - Get the current date and time

## Troubleshooting

- **Module not found errors:** Make sure you've activated the virtual environment and installed dependencies with `pip install -r requirements.txt`
- **YouTube Music API errors:** The ytmusicapi may require authentication. Check the [ytmusicapi documentation](https://ytmusicapi.readthedocs.io/) for more details.
- **Brave Search not working:** Ensure your `BRAVE_API_KEY` is set correctly in the `.env` file.
