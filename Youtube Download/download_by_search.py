'''
  Dependencies : youtube-dl
'''

from subprocess import call

name = input('Enter the name of video : ')
search = ["ytsearch:" + name]

command = ['youtube-dl', '-o', '/home/umang/Videos/NewVideos/%(title)s.%(ext)s+']
command.extend(search)

call(command)
