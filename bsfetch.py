SELECTION = {
'OS' : [
    'AmogOS',
    'Nyarch Linux',
    'Hannah Montana Linux',
    'Justin Bieber Linux',
    'TempleOS',
    'UwUntu',
    'Red Star OS',
    'PonyOS',
    'Debian GNU/Hurd',
    'Plan 9',
    'Inferno',
    'Haiku',
    'Damn Small Linux',
    'GoboLinux',
    'Fatdog64',
    'Kiss Linux',
    'Source Mage GNU/Linux',
    'Venom Linux',
    'Arch Linux (btw)',
    'Exherbo',
    'OpenIndiana',
    'Illumos',
    'KolibriOS',
    ],
'Host' : [
    'Samsung Family Hub Smart Refrigerator',
    'Sony PlayStation 2',
    'Sony PlayStation 3',
    'Sony PlayStation 4',
    'OLPC XO-1',
    'Commodore C64x',
    'Atari VCS 800',
    'AmigaOne X5000',
    'Tadpole Viper',
    'DragonBox Pyra',
    'InFocus Kangaroo Mobile Desktop Pro',
    'Intel Compute Stick',
    'GPD Win Max',
    'Panasonic Toughbook CF-U1 Rugged',
    'Sega Dreamcast',
    'HP TouchPad',
    'Nintendo Wii',
    'Sony Vaio UX',
    'Chumby One',
    'Diebold Nixdorf Opteva ATM',
    'Sharp Zaurus SL-5500',
    'Neo FreeRunner',
    'Ben NanoNote',
    'Pepper Pad 3',
    'Archos 9 PC Tablet',
    'Microsoft Xbox',
    'Microsoft Xbox 360',
    'Cosmo Communicator',
    'Palm Foleo',
    'ClockworkPi DevTerm',
    'Xiaomi Pad 5',
    'POCO F3',
    'Linksys WRT54G Router',
    'Tesla Model 3 Infotainment Unit',
    ],
'Shell' : [
    'Fish',
    'KornShell 93',
    'Elvish',
    'Oil Shell',
    'BusyBox ash',
    'COMMAND.COM',
    'Almquist shell',
    'Loksh',
    'Heirloom Bourne Shell',
    'Scsh',
    'Ion',
    'Dash',
    'Tcsh',
    ],
'WM' : [
    'Ratpoison',
    'Blackbox',
    'Enlightenment',
    'AfterStep',
    'EvilWM',
    'Cagebreak',
    'goomwwm',
    'Sawfish',
    'Muffin',
    'Musca',
    'Notion',
    'Hikari',
    'Velox',
    'Matchbox',
    'IceWM',
],
'CPU' :[
    'Intel Itanium 2 9150M (2) @ 1.67 GHz',
    'Intel Atom N270 (1+HT) @ 1.60 GHz',
    'IBM POWER5+ (2) @ 2.20 GHz',
    'Loongson 3A2000 (4) @ 1.00 GHz',
    'VIA C3 Nehemiah (1) @ 1.20 GHz',
    'VIA Eden X2 U4200 (2) @ 1.00 GHz',
    'AMD Geode LX800 (1) @ 500 MHz',
    'Sun UltraSPARC IV (2) @ 1.50 GHz',
    'Cyrix 6x86MX PR233 (1) @ 233 MHz',
    'Transmeta Efficeon TM8800 (1) @ 1.60 GHz',
    'Transmeta Crusoe TM5800 (1) @ 1.00 GHz',
    'DEC Alpha 21264 EV67 (1) @ 667 MHz',
    'MIPS R12000 (1) @ 300 MHz',
    
],
'GPU' : [
    '3Dfx Voodoo5 9000',
    '3Dfx Voodoo Banshee',
    'NVIDIA RIVA TNT2 M64',
    'ATI Rage Fury MAXX',
    'ATI Radeon Xpress 200',
    'Matrox G400 MAX',
    'Matrox Parhelia-512',
    'S3 Savage4 Pro',
    'PowerVR KYRO II',
    'SiS Mirage 3',
    'Trident Blade 3D 9880',
    'Intel GMA X4500',
    ],
'Memory' : [
    '9 Gib / 11 GiB',
    '6 Gib / 7 GiB',
    '420 MiB / 69 Gib',
    '9001 Mib / 9000 MiB',
    '5318008 KiB / 80085 MiB',
    '7 GiB / 13 GiB',
    '666 MiB / 777 MiB',
    '3 GiB / 14 GiB',
    ],
'Locale' : [
    'zh_HK.BIG5HK@radical',
    'zh_HK.BIG5HK@stroke',
    'zh_CN.GB18030@pinyin',
    'zh_TW.EUC@zhuyin',
    'sv_SE.ISO8859-15@euro',
    'ru_RU.KOI8-R',
    'ko_KR.EUC@dict',
    'ja_JP.eucJP',
    'ku_TR.UTF-8@sorani',
    'aa_ER@saaho',
    'ca_ES@valencia',
    'gez_ER@abegede',
    'gn_PY@Latin',
    'hak_TW',
    'hr_HR',
    'ia_FR',
    'kk_KZ',
    'ayc_PE',
    'bi_TV',
    'el_CY',
    'fo_FO',
    'ff_SN',
    'hif_FJ',
    'hus_MX',
    'kab_DZ',
    'kok_IN',
    'km_KH',
    'lij_IT',
    'lo_LA',
    'mh_MH',
    'miq_NI',
    'mn_MN',
    'mnw_MM',
    'myv_RU@cyrillic',
    'nah_MX',
    'niu_NU',
    'pap_CW',
    'quy_PE',
    'sgs_LT',
    'son_ML',
    'syr',
    'the_NP',
    'tpi_PG',
    'wae_CH',
    'wal_ET',
    'yue_HK',
    'yuw_PG',
]
}

def get_user_host_name():

    from getpass import getuser
    from socket import gethostname

    return f'{getuser()}@{gethostname()}'


def get_logo(name, max_width, max_height):

    def _get_logo_path(name):

        def _filename_format(name):

            return (
                name.replace(' ', '')
                .replace('/', '')
                .replace('(', '')
                .replace(')', '')
                .lower()
            )

        filename_path = (
            join(__file__.strip(basename(__file__)), 'logo/')
            + _filename_format(name)
            + '*'
        )

        return glob(filename_path)[0]
    
    def _calculate_size(img_width, img_height, max_width, max_height):

        def _get_cell_size():
            from array import array
            from fcntl import ioctl
            from sys import stdout
            from termios import TIOCGWINSZ

            buf = array('H', [0, 0, 0, 0])
            try:
                ioctl(stdout.fileno(), TIOCGWINSZ, buf)
                rows, cols, xpixels, ypixels = buf
                if xpixels > 0 and ypixels > 0 and cols > 0 and rows > 0:
                    return xpixels / cols, ypixels / rows
            except Exception:
                pass

            # Fallback: Default terminal cell aspect ratio (1 cell is roughly 10px wide x 20px high)
            return 10.0, 20.0
    
        cell_w, cell_h = _get_cell_size()
        max_width_px = max_width * cell_w
        max_height_px = max_height * cell_h
        scale = min(max_width_px / img_width, max_height_px / img_height)
        render_w = img_width * scale
        render_h = img_height * scale
        final_width = max(1, round(render_w / cell_w))
        final_height = max(1, round(render_h / cell_h))

        return final_width, final_height
    
    from base64 import b64encode
    from io import BytesIO
    from glob import glob
    from os.path import basename, join
    from cairosvg import svg2png
    from PIL import Image
    
    name = _get_logo_path(name)

    if name[-4:].lower() == '.svg':
        png = svg2png(url=str(name))
        img = Image.open(BytesIO(png))
    else:
        img = Image.open(name)

    img = img.convert('RGBA')
    img_width, img_height = img.size

    final_width, final_height = _calculate_size(img_width, img_height, max_width, max_height)

    out = BytesIO()
    img.save(out, format='PNG')

    return b64encode(out.getvalue()).decode(), final_width, final_height

def supports_kitty_graphics():
    
    from os import read, write
    from sys import stdin, stdout
    from termios import tcgetattr, tcsetattr, TCSADRAIN
    from tty import setcbreak
    from select import select

    timeout=0.1

    if not stdout.isatty() or not stdin.isatty():
        return False

    # Kitty graphics capability query
    query = b'\033_Gi=1,a=q;\033\\'

    fd = stdin.fileno()
    old = tcgetattr(fd)

    try:
        setcbreak(fd)
        write(stdout.fileno(), query)
        stdout.flush()

        if select([stdin], [], [], timeout)[0]:
            response = read(fd, 1024)
            return b'\033_G' in response
    finally:
        tcsetattr(fd, TCSADRAIN, old)

    return False
def test():

    from random import choice
    from time import sleep
    
    TO_PRINT = {key: choice(SELECTION[key]) for key in SELECTION.keys()}
    for os in SELECTION['OS']:
        TO_PRINT['OS']= os
        username_AT_networking_host_name = get_user_host_name()
        if supports_kitty_graphics():
            max_width = 25
            max_height= 9
            logo, final_width, final_height = get_logo(TO_PRINT['OS'], max_width, max_height)
            print(f'\033_Ga=T,f=100,c={final_width},r={final_height};{logo}\033\\', end='')
            print(f'\033[{final_height}A', end='')
            PRINT_PREFIX = f'\033[{final_width+2}C'
        else:
            PRINT_PREFIX = ''
        print()
        print(PRINT_PREFIX + username_AT_networking_host_name)
        print(PRINT_PREFIX + ('-'*len(username_AT_networking_host_name)))
        for key in TO_PRINT.keys():
            print(f'{PRINT_PREFIX}{key}: {TO_PRINT[key]}')
        if TO_PRINT['OS'] != SELECTION['OS'][-1]:
            sleep(1)
def main():
    
    from random import choice

    TO_PRINT = {key: choice(SELECTION[key]) for key in SELECTION.keys()}
    username_AT_networking_host_name = get_user_host_name()
    if supports_kitty_graphics():
        max_width = 25
        max_height= 9
        logo, final_width, final_height = get_logo(TO_PRINT['OS'], max_width, max_height)
        print(f'\033_Ga=T,f=100,c={final_width},r={final_height};{logo}\033\\', end='')
        print(f'\033[{final_height}A', end='')
        PRINT_PREFIX = f'\033[{final_width+2}C'
    else:
        PRINT_PREFIX = ''
    print()
    print(PRINT_PREFIX + username_AT_networking_host_name)
    print(PRINT_PREFIX + ('-'*len(username_AT_networking_host_name)))
    for key in TO_PRINT.keys():
        print(f'{PRINT_PREFIX}{key}: {TO_PRINT[key]}')
    
if __name__ == '__main__':
    main()