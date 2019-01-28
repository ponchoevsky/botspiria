import moviepy.editor as mpe
#from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

#ffmpeg_extract_subclip("suspiria.mp4", 60, 90, targetname="sub_suspiria.mp4")
#ffmpeg_extract_subclip("song.mp3", 40, 70, targetname="sub_song.mp3")

my_clip = mpe.VideoFileClip('sub_suspiria.mp4')
audio = mpe.AudioFileClip('sub_song.mp3')
#audio.set_duration(my_clip.duration)

final_clip = my_clip.set_audio(audio)
#final_clip.write_videofile("suspiria_final.mp4", codec="libx264", audio_codec="aac")
final_clip.write_videofile("suspiria_final.mp4",  audio_codec="aac")
