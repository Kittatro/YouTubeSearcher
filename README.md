# YouTube Searcher

This tool allows you to search YouTube videos for specific phrases and outputs matching video URLs with timestamps. It only supports searching through all the videos or shorts from a YouTube channel but you can easily edit the code to search in a certain playlist.

---

## Installation

### Step 1: Install Python

If you haven't installed Python, download and install it.

### Step 2: Clone the Repository

Clone this repository:

```bash
git clone https://github.com/Kittatro/YouTubeSearcher.git
cd YouTubeSearcher
```

### Step 3: Install Dependencies

Make sure `yt-dlp` and `youtube-transcript-api` are installed. You can install these using `pip`:

```bash
pip install yt-dlp youtube-transcript-api
```

---

## Usage

To run the script, open your terminal or command prompt in the script's folder and execute the following:

```bash
python script.py
```

You will be asked for the following inputs:

1. **Enter the YouTube channel URL**: For example: `https://www.youtube.com/@kittatro`
2. **Do you want to scan `videos` or `shorts`?**: Type `videos` or `shorts` based on what you want to search through.
3. **Enter the search phrase**: The phrase you want to search for in the video captions.

After the script finishes, you will see the results in the `found_videos.txt` file.