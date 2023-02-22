import ffmpeg
import pytube
import os
import shutil


def build_video(vid, out_file, file_type=1):
    yt = pytube.YouTube(vid)
    print(vid)
    title = yt.title
    print(title)
    print('Author:', yt.author)
    print('Number of views:', yt.views)
    print('Length of video:', yt.length, 'sec')
    if file_type == 1:
        try:
            yt.streams.filter(res='1080p', progressive=False).first().download(filename='video.mp4')
            yt.streams.filter(abr='160kbps', progressive=False).first().download(filename='audio.mp3')
            audio = ffmpeg.input('audio.mp3')
            video = ffmpeg.input('video.mp4')

            video_audio = ffmpeg.concat(video, audio, v=1, a=1)

            output = ffmpeg.output(video_audio, out_file, format='mp4')
            output.run()
            clean_up(vid, title)

        except:
            yd = yt.streams.get_highest_resolution()
            yd.download('/home/andy/Desktop/downloaded_vid')

    elif file_type == 2:
        yt.streams.filter(abr='160kbps', progressive=False).first().download(filename='out.mp4')
        clean_up(vid, title)


def clean_up(vid, title):
    new_title = title.replace(" ", "_")
    print(new_title)
    dest = "/home/andy/Desktop/downloaded_vid"
    new_name = f"/home/andy/Desktop/python_projects/youtube_downloader/{new_title}"
    print(new_name)
    old_name = "/home/andy/Desktop/python_projects/youtube_downloader/out.mp4"
    os.rename(old_name, new_name)
    shutil.move(new_name, dest)
    os.remove('audio.mp3')
    os.remove('video.mp4')


video_to_down = input("What video would you like to download: ")
type_of_downloaded = int(input("Type 1 if you want video or type 2 if you just want audio: "))
build_video(video_to_down, 'out.mp4', type_of_downloaded)
