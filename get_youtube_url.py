#!/usr/bin/env python3
"""
获得youtube视频真实下载地址
第二个参数可选：best, 1080p, 720p, 480p, 360p
默认：480p
用法
python get_youtube_url.py "https://www.youtube.com/watch?v=Om6N_fFJtRY"
如果想指定720p
python get_youtube_url.py "https://www.youtube.com/watch?v=Om6N_fFJtRY" 720p
"""
import sys
import subprocess

def get_video_url(youtube_url, quality="480p"):
    quality_map = {
        "best": "best",
        "1080p": "bestvideo[height<=1080]+bestaudio/best[height<=1080]",
        "720p": "bestvideo[height<=720]+bestaudio/best[height<=720]",
        "480p": "best[height<=480]",
        "360p": "best[height<=360]",
    }
    
    fmt = quality_map.get(quality, quality_map["480p"])
    
    try:
        cmd = ["yt-dlp", "-f", fmt, "--get-url", "--no-playlist", youtube_url]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            print(f"Error: {result.stderr}")
            return None
            
    except Exception as e:
        print(f"Failed: {e}")
        return None

def main():
    if len(sys.argv) < 2:
        print("=" * 50)
        print("YouTube Video URL Extractor")
        print("=" * 50)
        print("Usage: python get_youtube_url.py <YouTube_URL> [quality]")
        print("")
        print("Quality: best, 1080p, 720p, 480p, 360p")
        print("Default: 480p")
        print("")
        print("Examples:")
        print('  python get_youtube_url.py "https://www.youtube.com/watch?v=xxxx"')
        print('  python get_youtube_url.py "https://www.youtube.com/watch?v=xxxx" 720p')
        return
    
    youtube_url = sys.argv[1]
    quality = sys.argv[2] if len(sys.argv) > 2 else "480p"
    
    print(f"Fetching {youtube_url} ({quality})...")
    print("-" * 50)
    
    url = get_video_url(youtube_url, quality)
    
    if url:
        print("Download URL:")
        print(url)
        print("-" * 50)
        print("Note: URL has expiration, download soon")
    else:
        print("Failed to get URL")

if __name__ == "__main__":
    main()
