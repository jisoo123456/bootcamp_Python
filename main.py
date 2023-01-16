#5.1(m으로 시작하는 단어를 대문자로)

song="""when an eel grabs your arm,
...And it causes great harm,
...That's a moray!"""

song_list=song.split()
song_list[13]=(song_list[13]).title()
Song=' '.join(song_list)
print(Song)