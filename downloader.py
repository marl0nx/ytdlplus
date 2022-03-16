import os
import pytube
from colorama import Fore as color
from pytube.exceptions import RegexMatchError
from pytube.exceptions import VideoUnavailable


def clear():
    os.system('cls')
    pass


def banner():
    print(color.RED + '''$$\     $$\ $$$$$$$$\ $$$$$$$\  $$\       $$$$$$$\  $$\                     
\$$\   $$  |\__$$  __|$$  __$$\ $$ |      $$  __$$\ $$ |                    
 \$$\ $$  /    $$ |   $$ |  $$ |$$ |      $$ |  $$ |$$ |$$\   $$\  $$$$$$$\ 
  \$$$$  /     $$ |   $$ |  $$ |$$ |      $$$$$$$  |$$ |$$ |  $$ |$$  _____|
   \$$  /      $$ |   $$ |  $$ |$$ |      $$  ____/ $$ |$$ |  $$ |\$$$$$$\  
    $$ |       $$ |   $$ |  $$ |$$ |      $$ |      $$ |$$ |  $$ | \____$$\ 
    $$ |       $$ |   $$$$$$$  |$$$$$$$$\ $$ |      $$ |\$$$$$$  |$$$$$$$  |
    \__|       \__|   \_______/ \________|\__|      \__| \______/ \_______/''')
    pass


class symbols:
    info = f'{color.WHITE}[{color.YELLOW}?{color.WHITE}] '
    success = f'{color.WHITE}[{color.GREEN}!{color.WHITE}] '
    error = f'{color.WHITE}[{color.RED}!{color.WHITE}] '
    arrow = f'{color.WHITE}[{color.RED}>{color.WHITE}] '


def downloader(url, video_type='mp3'):
    try:
        if video_type == 'mp3':
            yt = pytube.YouTube(url)
            print(symbols.info + f'Downloading {yt.title} (mp3)...')

            video = yt.streams.get_audio_only()

            out_file = video.download(output_path="output/mp3")

            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file.replace(' ', ''))
            print()
            print(symbols.success + f'Downloaded {yt.title} (mp3) successfully! Saved in output/mp3')
            print()
            input(symbols.info + 'Press [Enter] to continue.')
            start()
        elif video_type == 'mp4':
            yt = pytube.YouTube(url)
            print(symbols.info + f'Downloading {yt.title} (mp4)...')
            video = yt.streams.get_highest_resolution()
            out_file = video.download(output_path="output/mp4")

            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp4'
            os.rename(out_file, new_file.replace(' ', ''))
            print()
            print(symbols.success + f'Downloaded {yt.title} (mp4) successfully! Saved in output/mp4')
            print()
            input(symbols.info + 'Press [Enter] to continue.')
            start()
        else:
            yt = pytube.YouTube(url)
            print(symbols.info + f'Downloading {yt.title} (default: mp3)...')

            video = yt.streams.get_audio_only()

            out_file = video.download(output_path="output/mp3")

            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file.replace(' ', ''))
            print()
            print(symbols.success + f'Downloaded {yt.title} (mp3) successfully! Saved in output/mp3')
            print()
            input(symbols.info + 'Press [Enter] to continue.')
            start()
        pass
    except KeyboardInterrupt:
        exit(0)
    except RegexMatchError:
        clear()
        banner()
        print()
        print(symbols.error + 'This video does not exist!')
        print()
        print(symbols.info + 'Press [Enter] to continue.')
        input()
        start()
    except VideoUnavailable:
        clear()
        banner()
        print()
        print(symbols.error + 'This video does not exist!')
        print()
        print(symbols.info + 'Press [Enter] to continue.')
        input()
        start()


def start():
    try:
        os.system('title ')
        clear()
        banner()
        print()
        print(symbols.info + 'What type of video you wanna download? (mp3/mp4)')
        print()
        video_type = input(symbols.arrow)
        print()
        print(symbols.info + 'Please enter the YouTube Video URL:')
        print()
        url = input(symbols.arrow)
        print()
        downloader(url=url, video_type=video_type)
        pass
    except KeyboardInterrupt:
        exit(0)


start()
