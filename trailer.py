from moviepy import *
import numpy as np


### VIDEO LOADING
video = VideoFileClip("./resources/bbb.mp4") 


### SCENES EXTRACTION
# extract the scenes we want to use
# First the characters
intro_clip = video.subclipped(1, 11)
bird_clip = video.subclipped(16, 20)
bunny_clip = video.subclipped(37, 55)
rodents_clip = video.subclipped("00:03:34.75", "00:03:56")
rambo_clip = video.subclipped("04:41.5", "04:44.70")

### SCENES PREVIEWING
# Now, lets have a first look at our clips
# Warning: you need ffplay installed for preview to work.
# We set a low fps so our machine can render in real time without slowing down.
intro_clip.preview(fps=10)
bird_clip.preview(fps=10)
bunny_clip.preview(fps=10)
rodents_clip.preview(fps=10)
rambo_clip.preview(fps=10)