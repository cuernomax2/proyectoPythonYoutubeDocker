from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=_XHjMf2i7rE")

print("Title: ", yt.title)

print("Number of views: ", yt.views)

print("Length of the video: ", yt.length, "seconds")

print("Description: ", yt.description)

print("Rating: ", yt.rating)
