from moviepy import *
import numpy as np


### VIDEO LOADING
video = VideoFileClip("./resources/bbb.mp4") 


### SCENES EXTRACTION
# extract the scenes we want to use
# First the characters
intro_clip = video.subclipped(1, 11)
bird_clip = video.subclipped(16, 10)
bunny_clip = video.subclipped(37, 55)
rodents_clip = video.subclipped("00:03:34.75", "00:03:56")
rambo_clip = video.subclipped("04:41.5", "04:44.70")

### SCENES PREVIEWING
# Now, lets have a first look at our clips
# Warning: you need ffplay installed for preview to work.
# We set a low fps so our machine can render in real time without slowing down.
# intro_clip.preview(fps=10)
# bird_clip.preview(fps=10)
# bunny_clip.preview(fps=10)
# rodents_clip.preview(fps=10)
# rambo_clip.preview(fps=10)

# TODO: preview encounter AttributeError:
# AttributeError: 'FFPLAY_AudioPreviewer' object has no attribute 'logfile'
# but did not affect the previewing of the clips.
# TODO: preview also has no sound, I think the video should have sound.


# CLIPS MODIFICATION CUTTING
# remove the clip the part between 00:06:00 to 00:10:00 of the clip
# rodents_clip = rodents_clip.with_section_cut_out(start_time=4, end_time=10)
# rodents_clip.preview(fps=10)

# ?: what is a text clip?
### TEXT/LOGO CLIPS CREATION
# Create the texts to put between the clips
font = "./resources/font/font.ttf"
intro_text = TextClip(
    font=font,
    text="The Blender Foundation and\nPeach Project presents",
    font_size=50,
    color="#fff",
    text_align="center",
)
bird_text = TextClip(font=font, text="An unlucky bird", font_size=50, color="#fff")
bunny_text = TextClip(font=font, text="A (slightly overweight) bunny", font_size=50, color="#fff")
rodents_text = TextClip(font=font, text="And three rodent pests", font_size=50, color="#fff")
revenge_text = TextClip(font=font, text="Revenge is coming...", font_size=50, color="#fff")
made_with_text = TextClip(font=font, text="Made with", font_size=50, color="#fff")

# Also need the big buck bunny logo, lets load it and resize it
logo_clip = ImageClip("./resources/logo_bbb.png").resized(width=400)
moviepy_clip = ImageClip("./resources/logo_moviepy.png").resized(width=300)