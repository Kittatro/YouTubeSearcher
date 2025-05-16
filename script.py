import subprocess
import sys
from youtube_transcript_api import YouTubeTranscriptApi

def fetch_video_list(channel_url, content_type):
    """fetches the video list using yt-dlp."""
    print(f"\nFetching video list from: {channel_url}/{content_type}")
    command = [
        "python", "-m", "yt_dlp",
        "--flat-playlist",
        "--print", "%(title)s|%(id)s",
        f"{channel_url}/{content_type}"
    ]
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    video_list = result.stdout.strip().split("\n")
    return video_list

def search_videos_for_phrase(videos, search_phrase):
    """searches the videos for a given phrase in the transcript."""
    found_urls = []
    for line in videos:
        title, video_id = line.split("|", 1)
        try:
            # fetch transcript
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            for entry in transcript:
                text = entry['text'].lower()
                if all(word in text for word in search_phrase.lower().split()):
                    url = f"https://youtu.be/{video_id}?t={int(entry['start'])}"
                    print(f"Found match in: {url}")
                    found_urls.append(url)
                    break  # stop after the first match
        except Exception as e:
            pass  # skip if no transcript or error
    return found_urls

def main():
    # prompt for inputs
    channel_url = input("Enter the channel URL (e.g. https://www.youtube.com/@kittatro): ").strip()
    content_type = input("Do you want to scan 'videos' or 'shorts'? If invalid, 'videos' by default: ").strip().lower()
    search_phrase = input("Enter the search phrase: ").strip()

    # validate content type
    if content_type not in ["videos", "shorts"]:
        print("Invalid content type, defaulting to 'videos'")
        content_type = "videos"

    # fetch the video list
    videos = fetch_video_list(channel_url, content_type)

    # search for the phrase in the videos' transcripts
    print(f"\nSearching for '{search_phrase}' in captions...")
    found_urls = search_videos_for_phrase(videos, search_phrase)

    # save results to file
    with open("found_videos.txt", "w", encoding="utf-8") as out_file:
        out_file.write("\n".join(found_urls))

    print(f"\nDone! {len(found_urls)} matching videos saved to 'found_videos.txt'")

if __name__ == "__main__":
    main()
