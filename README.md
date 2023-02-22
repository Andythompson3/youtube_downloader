# youtube_downloader
A simple application that allows you to download Youtube videos

With the new updates to Youtube you can no longer use .get_highest_resolution() for pytube. This is because they have changed how they store videos
that have a higher quality. They are storing video files and audio files seperatly now. This means that if you just use pytube you will maxout your 
video quality at 720p. 

Unless you use shutil to help you compile the video and audio file. 
