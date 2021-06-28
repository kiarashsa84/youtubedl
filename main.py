from pytube import YouTube
from pytube.cli import on_progress
import io
import re
import os
import sys


def getsound():
    ls = yt.streams.filter(only_audio=True)
    # print(ls)
    itag = ls.itag_index
    itag = list(itag)
    itag = itag[0]
    stream = yt.streams.get_by_itag(itag)
    stream.download()
    subch = input('Do you want caption ? ')
    subch = subch.capitalize()
    if subch[0] == 'Y':
        l_caption = yt.captions
        print(l_caption)
        caption = yt.captions.get_by_language_code('en')
        caption = caption.generate_srt_captions()
        name = yt.title
        namef = name + '.txt'
        f = io.open(namef, 'w', encoding='utf-8')
        f.write(caption)
        file = namef
        base = os.path.splitext(file)[0]
        f.close()
        os.rename(file, base + '.srt')
    else:
        pass


def getvideo():
    res: list = []
    reso: list = []
    ls = yt.streams.filter(adaptive=True, type='video')
    cnt = ls.count()
    for i in range(0, cnt):
        repitation = ls[i].resolution
        res.append(repitation)
        reso.append(repitation)

    res = dict.fromkeys(res)
    res = list(res)
    cnt_q = len(res)
    itag_v = list(ls.itag_index)
    qu_ch = input('Which quality do you want ? (Enter just the number of quality) \n{} \n :'.format(res))

    if qu_ch.isnumeric():
        qu_ch = int(qu_ch)

        cap_che = input('Do you want caption ? ')
        cap_che = cap_che.capitalize()
        cap_che = cap_che[0]

        if cap_che:  # get caption
            l_caption = yt.captions
            print(l_caption)
            caption = yt.captions.get_by_language_code('en')
            caption = caption.generate_srt_captions()
            name = yt.title
            if name.count('|') != 0:
                name = name.replace('|', '')

            namef = name + '.txt'
            f = io.open(namef, 'w', encoding='utf-8')
            f.write(caption)
            file = namef
            base = os.path.splitext(file)[0]
            f.close()
            os.rename(file, base + '.srt')
        else:
            pass


        lst = str(ls)

        if qu_ch == 2160:

            if '2160p' in res:
                loc = list(re.search('2160p', lst).span())
                loc[0] = loc[0] - 32
                loc[1] = loc[1] - 34
                tag = eval(lst[loc[0]:loc[1]])
                stream = yt.streams.get_by_itag(tag)
                stream.download()
            else:
                sys.exit()

        elif qu_ch == 1440:

            if '1440p' in res:
                loc = list(re.search('1440p', lst).span())
                loc[0] = loc[0] - 32
                loc[1] = loc[1] - 34
                tag = eval(lst[loc[0]:loc[1]])
                stream = yt.streams.get_by_itag(tag)
                stream.download()
            else:

                 sys.exit()

        elif qu_ch == 1080:
            if '1080p' in res:
                loc = list(re.search('1080p', lst).span())
                loc[0] = loc[0] - 32
                loc[1] = loc[1] - 34
                tag = eval(lst[loc[0]:loc[1]])
                stream = yt.streams.get_by_itag(tag)
                stream.download()
            else:
                sys.exit()
        elif qu_ch == 720:

            if '720p' in res:
                loc = list(re.search('720p', lst).span())
                loc[0] = loc[0] - 32
                loc[1] = loc[1] - 33
                tag = eval(lst[loc[0]:loc[1]])
                stream = yt.streams.get_by_itag(tag)
                stream.download()
            else:
                sys.exit()
        elif qu_ch == 480:
            if '480p' in res:
                loc = list(re.search('480p', lst).span())
                loc[0] = loc[0] - 32
                loc[1] = loc[1] - 33
                tag = eval(lst[loc[0]:loc[1]])
                stream = yt.streams.get_by_itag(tag)
                stream.download()
            else:
                sys.exit()

        elif qu_ch == 360:

            if '360p' in res:
                loc = list(re.search('360p', lst).span())
                loc[0] = loc[0] - 32
                loc[1] = loc[1] - 33
                tag = eval(lst[loc[0]:loc[1]])
                stream = yt.streams.get_by_itag(tag)
                stream.download()
        elif qu_ch == 240:

            if '244p' in res:
                loc = list(re.search('244p', lst).span())
                loc[0] = loc[0] - 32
                loc[1] = loc[1] - 33
                tag = eval(lst[loc[0]:loc[1]])
                stream = yt.streams.get_by_itag(tag)
                stream.download()
            else:
                sys.exit()

        elif qu_ch == 144:
            if '144p' in res:
                loc = list(re.search('144p', lst).span())
                loc[0] = loc[0] - 32
                loc[1] = loc[1] - 33
                tag = eval(lst[loc[0]:loc[1]])
                stream = yt.streams.get_by_itag(tag)
                stream.download()
            else:
                sys.exit()




    else:
        try:
            float(qu_ch)
        except ValueError:
            print('!!Please enter a number!!')


def get_video_sound():
    res = []
    reso = []
    ls = yt.streams.filter(progressive=True)
    cnt = ls.count()
    for i in range(0, cnt):
        rept = ls[i].resolution
        res.append(rept)
        reso.append(rept)
    qu = input()

    res = dict.fromkeys(res)
    res = list(res)
    print(res)
    cnt_q = len(res)
    itag_v = list(ls.itag_index)
    qu_ch = eval(input('Which quality do you want ? 1.highest, 2.lowest \n:'))
    cap_che = input('Do you want caption ? ')
    cap_che = cap_che.capitalize()
    cap_che = cap_che[0]

    if cap_che:  # get caption
        l_caption = yt.captions
        print(l_caption)
        caption = yt.captions.get_by_language_code('en')
        caption = caption.generate_srt_captions()
        name = yt.title
        if name.count('|') != 0:
            name = name.replace('|', '')

        namef = name + '.txt'
        f = io.open(namef, 'w', encoding='utf-8')
        f.write(caption)
        file = namef
        base = os.path.splitext(file)[0]
        f.close()
        os.rename(file, base + '.srt')
    else:
        pass
    if qu_ch == 1:
        stream = yt.streams.get_highest_resolution()
        stream.download()
    elif qu_ch == 0:
        stream = yt.streams.get_lowest_resolution()
        stream.download()
    else:
        print('enter a valid number')


url = "http://youtube.com/watch?v=2lAe1cqCOXo"
# url = input('Enter your video or music url: ')
yt = YouTube(url, on_progress_callback=on_progress)

state = input('Which state do you want ? 1.Just sound, 2.Just video, 3.both sound and video :  ')

try:
    state = int(state)
except ValueError:
    try:
        state = float(state)
    except ValueError:
        print('!!Please enter a number!!')

if state == 1:
    getsound()

elif state == 2:
    getvideo()

elif state == 3:
    get_video_sound()
