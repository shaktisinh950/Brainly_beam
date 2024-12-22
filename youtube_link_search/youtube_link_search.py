from googleapiclient.discovery import build

def get_youtube_links(search_query, max_results=5):
    # Your YouTube Data API key
    API_KEY = "AIzaSyDt25T32onDzEwtLW_MyZMhz855-l2FKUE"
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"

    # Build the YouTube API client
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=API_KEY)

    # Perform the search
    search_response = youtube.search().list(
        q=search_query,
        part="id,snippet",
        maxResults=max_results,
        type="video"  # Only fetch videos
    ).execute()

    # Extract video links
    video_links = [
        f"https://www.youtube.com/watch?v={item['id']['videoId']}"
        for item in search_response.get("items", [])
        if item["id"]["kind"] == "youtube#video"
    ]

    return video_links

links = get_youtube_links(input("Search here : "), max_results=5)

print("YouTube Links:")
for link in links:
    print(link)
