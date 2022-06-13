from tkinter import *
from moviepy.editor import *
from pytube import YouTube

# Set Your Colours
bgColour = '#fdf8b0'
fgColour = '#3E3DC2'
buttonColour = '#b9f6e7'

root = Tk()
root.geometry('500x300')
root.resizable(0, 0)
root.title("Corvo Codes - YouTube Downloader")
root.configure(bg=bgColour)

Label(root,
      text='Youtube Video Downloader',
      font='Lucida 20',
      bg=bgColour,
      fg=fgColour
      ).pack()

link = StringVar()
Label(root,
      text='Paste YouTube Link Here:',
      font='Lucida 15',
      bg=bgColour
      ).place(x=130, y=60)

link_enter = Entry(root, width=50, textvariable=link).place(x=95, y=90)


def downloader():
    # Set your video download folder/location
    mp4Location = "C:\\Users\\corvo\\IdeaProjects\\YouTube Downloader\\YouTube-Downloads"

    url = YouTube(str(link.get()))
    video = url.streams[1]
    video.download(mp4Location)
    Label(root,
          text='DOWNLOADED',
          font='Lucida 15 bold',
          bg=bgColour,
          fg=fgColour
          ).place(x=180, y=120)
    return video.download(mp4Location)


def converter():
    # Set your mp3 download folder/location
    mp3_file = "C:\\Users\\corvo\\IdeaProjects\\YouTube Downloader\\YouTube-Downloads\\MP3\\Converted-MP4.mp3"

    mp4_file = downloader()
    videoclip = VideoFileClip(mp4_file)
    audioclip = videoclip.audio
    audioclip.write_audiofile(mp3_file)
    audioclip.close()
    videoclip.close()
    Label(root,
          text='CONVERTED',
          font='Lucida 15 bold',
          bg=bgColour,
          fg=fgColour
          ).place(x=180, y=120)

    # Download button
download_mp4 = Button(root,
                      text='DOWNLOAD',
                      font='Lucida 15',
                      bg=buttonColour,
                      padx=2,
                      command=downloader,
                      fg=fgColour
                      ).place(x=180, y=160)

    # Converter button
converter_mp4 = Button(root,
                       text='Convert to mp3',
                       font='Lucida 15',
                       bg=buttonColour,
                       padx=2,
                       command=converter,
                       fg=fgColour
                       ).place(x=172, y=220)

root.mainloop()
