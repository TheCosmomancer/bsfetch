TO_PRINT = {
'OS' : [
    'OS: AmogOS',
    'OS: Windows 9 Professional',
    'OS: Nyarch Linux',
    'OS: Hannah Montana Linux',
    'OS: Justin Bieber Linux',
    'OS: TempleOS',
    'OS: UwUntu',
    'OS: Red Star OS',
    'OS: Suicide Linux',
    'OS: PonyOS',
    'OS: Debian GNU/Hurd',
    'OS: Collapse OS',
    'OS: Plan 9',
    'OS: Inferno',
    'OS: Haiku',
    'OS: Damn Small Linux',
    'OS: GoboLinux',
    'OS: Fatdog64',
    'OS: Kiss Linux',
    'OS: Source Mage GNU/Linux',
    'OS: Venom Linux',
    'OS: Arch Linux (btw)',
    'OS: Exherbo',
    'OS: OpenIndiana',
    'OS: Illumos',
    'OS: KolibriOS',
    ],
'Host' : [
    'Host: Grandma\'s Computer',
    'Host: Potato',
    ],
'Uptime' : [
    'Uptime: Been Up For a While...',
    'Uptime: Up all night to get lucky',
    'Uptime: 14 Billion Years',
    ],
'Shell' : [
    'Shell: Fish',
    'Shell: KornShell 93',
    'Shell: Elvish',
    'Shell: Oil Shell',
    'Shell: BusyBox ash',
    'Shell: COMMAND.COM',
    'Shell: Almquist shell',
    'Shell: Loksh',
    'Shell: Heirloom Bourne Shell',
    'Shell: Scsh',
    'Shell: Ion',
    'Shell: Dash',
    'Shell: Tcsh',
    ],
# 'WM' : [],
# 'CPU' :[],
'GPU' : [
    'GPU0: HAVA Graphics @ 2.25 GHz [Integrated]\nGPU1: HAVA NICEDAY 6090 1024GB',
    ],
'Memory' : [
    'Memory: Memory of a Goldfish',
    'Memory: 9 Gib / 11 GiB',
    ],
}
if __name__ == '__main__':
    from random import choice
    # username_AT_networking_host_name = ...
    # print(username_AT_networking_host_name)
    # print('-'*len(username_AT_networking_host_name))
    for key in TO_PRINT.keys():
        print(choice(TO_PRINT[key]))