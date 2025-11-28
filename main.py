# from fastmcp import FastMCP
from mcp.server.fastmcp import FastMCP
import requests
from dotenv import load_dotenv
import os
from datetime import datetime
from ytmusicapi import YTMusic
import webbrowser



load_dotenv()
mcp = FastMCP(name="ymt_server")
ytmusic = YTMusic()


@mcp.tool()
def brave_web_search(query: str, count: int = 5) -> str:
    """Search the web using Brave Search API.
    
    Args:
        query: The search query
        count: Number of results to return (default 5, max 20)
    """
    try:
        api_key = os.environ.get("BRAVE_API_KEY")
        if not api_key:
            return "Error: BRAVE_API_KEY not set in environment variables"
        
        url = "https://api.search.brave.com/res/v1/web/search"
        headers = {
            "X-Subscription-Token": api_key,
            "Accept": "application/json"
        }
        params = {
            "q": query,
            "count": count
        }
        
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        
        data = response.json()
        
        # Extract web results
        results = []
        if "web" in data and "results" in data["web"]:
            for result in data["web"]["results"]:
                title = result.get("title", "No title")
                url = result.get("url", "No URL")
                description = result.get("description", "No description")
                results.append(f"**{title}**\n{url}\n{description}\n")
        
        if results:
            return "Search results:\n\n" + "\n".join(results)
        else:
            return "No results found"
            
    except Exception as e:
        return f"Error performing search: {str(e)}"
    

@mcp.tool()
def search_youtube_music(query: str, search_type: str = "songs") -> str:
    """Search YouTube Music for songs, artists, albums, or playlists.
    
    Args:
        query: The search query (song name, artist, or genre)
        search_type: Type of search - 'songs', 'artists', 'albums', or 'playlists'
    """
    try:
        results = ytmusic.search(query, filter=search_type, limit=5)
        
        output = []
        if search_type == "songs":
            for song in results:
                title = song.get('title', 'Unknown')
                artists = ', '.join([a['name'] for a in song.get('artists', [])])
                video_id = song.get('videoId', '')
                duration = song.get('duration', 'Unknown')
                output.append(f"{title} by {artists} ({duration}) - ID: {video_id}")
        
        elif search_type == "artists":
            for artist in results:
                name = artist.get('artist', 'Unknown')
                browse_id = artist.get('browseId', '')
                output.append(f"{name} - ID: {browse_id}")
        
        elif search_type == "albums":
            for album in results:
                title = album.get('title', 'Unknown')
                artists = ', '.join([a['name'] for a in album.get('artists', [])])
                year = album.get('year', 'Unknown')
                output.append(f"{title} by {artists} ({year})")
        
        return f"YouTube Music search results:\n" + "\n".join(output) if output else "No results found"
    
    except Exception as e:
        return f"Error searching YouTube Music: {str(e)}"

@mcp.tool()
def get_song_details(video_id: str) -> str:
    """Get detailed information about a specific song on YouTube Music.
    
    Args:
        video_id: The YouTube Music video ID of the song
    """
    try:
        song = ytmusic.get_song(video_id)
        
        title = song['videoDetails'].get('title', 'Unknown')
        author = song['videoDetails'].get('author', 'Unknown')
        length = song['videoDetails'].get('lengthSeconds', 'Unknown')
        view_count = song['videoDetails'].get('viewCount', 'Unknown')
        
        return f"Song: {title}\nArtist: {author}\nDuration: {length}s\nViews: {view_count}"
    
    except Exception as e:
        return f"Error getting song details: {str(e)}"


@mcp.tool()
def play_in_browser(video_id: str) -> str:
    """Open a YouTube Music song in the default web browser.
    
    Args:
        video_id: The YouTube Music video ID
    """
    try:
        url = f"https://music.youtube.com/watch?v={video_id}"
        webbrowser.open(url)
        return f"Opened YouTube Music in browser: {url}"
    except Exception as e:
        return f"Error opening browser: {str(e)}"

@mcp.tool()
def get_current_date() -> str:
    """Get the current local date and time."""
    now = datetime.now()
    return now.strftime("%A, %B %d, %Y")







if __name__ == "__main__":
    mcp.run()
