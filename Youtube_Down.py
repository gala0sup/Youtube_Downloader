import os


def down_vid(url):
    os.system("youtube-dl.exe -x " +
              "--audio-format mp3 " +
              "--audio-quality 0 " +
              "--no-playlist " +
              "--prefer-ffmpeg " +
              "--embed-thumbnail " +
              "-o %(title)s.%(ext)s " +
              '"{}"'.format(url))
    
    
def init():
    # type: () -> object
    print("Enter Video link :- ")
    link = raw_input()  # type: str
    os.chdir('C:\\Users\\\<username>\\Downloads\\!SONGS')
    print ("\nSong Will be downloded in "+os.getcwd())
    return link


vid_url = init()
down_vid(vid_url)
down_more_vids = True

while down_more_vids:
    more = raw_input("\nDownload more videos [Y/N] ")
    if more == "y" or more == "Y":
        vid_url = init()
        down_vid(vid_url)
    elif more == "N" or more == "n":
        down_more_vids = False
        print('\n')
    else:
        pass


os.system('pause')
