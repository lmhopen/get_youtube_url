使用方法：

python get_youtube_url.py "YouTube视频URL" [质量]
参数说明：

第二个参数可选：best, 1080p, 720p, 480p, 360p
默认：480p
示例：

# 默认480p
python get_youtube_url.py "https://www.youtube.com/watch?v=Om6N_fFJtRY"

# 指定720p
python get_youtube_url.py "https://www.youtube.com/watch?v=Om6N_fFJtRY" 720p
程序会自动输出真实的下载链接，复制链接后可以用浏览器或IDM等工具下载。
