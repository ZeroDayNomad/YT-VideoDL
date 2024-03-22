#     ____                  __         ____        __           _____            __
#    / __ \____ _____  ____/ /___ _   / __ \____ _/ /_____ _   / ___/__  _______/ /____  ____ ___  _____
#   / /_/ / __ `/ __ \/ __  / __ `/  / / / / __ `/ __/ __ `/   \__ \/ / / / ___/ __/ _ \/ __ `__ \/ ___/
#  / ____/ /_/ / / / / /_/ / /_/ /  / /_/ / /_/ / /_/ /_/ /   ___/ / /_/ (__  ) /_/  __/ / / / / (__  )
# /_/    \__,_/_/ /_/\__,_/\__,_/  /_____/\__,_/\__/\__,_/   /____/\__, /____/\__/\___/_/ /_/ /_/____/
#                                                                 /____/
# Written By: Immain
# Date Created: 1/26/2023
# Version: 1.0.0
# Description: Downloads video and audio at best quality from youtube and saves it as a mp4 file with the thumbnail as a jpg file in the same directory as the script.

import pafy, re, wget, os, ffmpeg

url = input("Add YouTube Link: ")

result = pafy.new(url)

videoTitle = result.title

exp = "^.*((youtu.be\/)|(v\/)|(\/u\/\w\/)|(embed\/)|(watch\?))\??v?=?([^#&?]*).*"
s = re.findall(exp,url)[0][-1]
thumbnail = f"https://i.ytimg.com/vi/{s}/maxresdefault.jpg"
file = f"{videoTitle}.jpg"
wget.download(thumbnail)
os.rename("maxresdefault.jpg", file)
print(thumbnail)

streams = result.streams
for stream in streams:
    print(stream)

best_quality_video = result.getbestvideo(preftype="mp4")
bestaudio = result.getbestaudio(preftype="m4a")

video_stream = ffmpeg.input(best_quality_video.url)
audio_stream = ffmpeg.input(bestaudio.url)
ffmpeg.output(video_stream, audio_stream, "output.mp4").run()

filestream = f"{videoTitle}.mp4"
os.rename("output.mp4", filestream)
