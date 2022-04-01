###############################################
# Constants | Logo and help messages
###############################################
VERSION = 'v2.3.0'
USAGE = 'Usage: %prog [options] arg'
EPILOG = 'Example: dripper -s tcp://192.168.0.1:80 -t 100'

LOGO_COLOR = f'''[deep_sky_blue1]
██████╗ ██████═╗██╗██████╗ ██████╗ ███████╗██████═╗
██╔══██╗██╔══██║██║██╔══██╗██╔══██╗██╔════╝██╔══██║
██║  ██║██████╔╝██║██████╔╝██████╔╝█████╗  ██████╔╝[bright_yellow]
██║  ██║██╔══██╗██║██╔═══╝ ██╔═══╝ ██╔══╝  ██╔══██╗
██████╔╝██║  ██║██║██║     ██║     ███████╗██║  ██║
╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝     ╚═╝     ╚══════╝╚═╝  ╚═╝
                                           [green]{VERSION}
[grey53]
It is the end user's responsibility to obey all applicable laws.
It is just like a server testing script and Your IP is visible.
Please, make sure you are ANONYMOUS!

[u blue link=https://github.com/alexmon1989/russia_ddos]https://github.com/alexmon1989/russia_ddos
'''

LOGO_NOCOLOR = f'''
██████╗ ██████═╗██╗██████╗ ██████╗ ███████╗██████═╗
██╔══██╗██╔══██║██║██╔══██╗██╔══██╗██╔════╝██╔══██║
██║  ██║██████╔╝██║██████╔╝██████╔╝█████╗  ██████╔╝
██║  ██║██╔══██╗██║██╔═══╝ ██╔═══╝ ██╔══╝  ██╔══██╗
██████╔╝██║  ██║██║██║     ██║     ███████╗██║  ██║
╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝     ╚═╝     ╚══════╝╚═╝  ╚═╝
                                           {VERSION}

It is the end user's responsibility to obey all applicable laws.
It is just like a server testing script and Your IP is visible.
Please, make sure you are ANONYMOUS!

https://github.com/alexmon1989/russia_ddos
'''

BANNER = '\n\n[r][deep_sky_blue1]#StandWith[bright_yellow]Ukraine\n'


# ==== Error messages ====
GETTING_SERVER_IP_ERROR_MSG = 'Can\'t get server IP. Packet sending failed. Check your VPN.'
YOUR_IP_WAS_CHANGED = 'Your IP was changed!!! Check VPN connection.'
NO_MORE_PROXIES_MSG = 'There are no more operational proxies to work with host.'
DEFAULT_CURRENT_IP_VALUE = '...detecting'
HOST_IN_PROGRESS_STATUS = 'HOST_IN_PROGRESS'
HOST_FAILED_STATUS = 'HOST_FAILED'
HOST_SUCCESS_STATUS = 'HOST_SUCCESS'


# ==== Formats and Constants
DATE_TIME_FULL = '%Y-%m-%d %H:%M:%S'
DATE_TIME_SHORT = '%H:%M:%S'


# ==== Defaults for Input ARGS ===
ARGS_DEFAULT_PORT = 80
ARGS_DEFAULT_THREADS = 100
ARGS_DEFAULT_RND_PACKET_LEN = 1
ARGS_DEFAULT_MAX_RND_PACKET_LEN = 1024
ARGS_DEFAULT_HEALTH_CHECK = 1
ARGS_DEFAULT_HTTP_ATTACK_METHOD = 'GET'
ARGS_DEFAULT_HTTP_REQUEST_PATH = '/'
ARGS_DEFAULT_SOCK_TIMEOUT = 1
ARGS_DEFAULT_PROXY_TYPE = 'socks5'


# ==== Defaults ====
GEOIP_NOT_DEFINED = '--'
CONNECT_TO_HOST_MAX_RETRY = 5
MIN_SCREEN_WIDTH = 90
MIN_UPDATE_HOST_STATUSES_TIMEOUT = 120
SUCCESSFUL_CONNECTIONS_CHECK_PERIOD_SEC = 120
NO_SUCCESSFUL_CONNECTIONS_DIE_PERIOD_SEC = 180
HTTP_STATUS_CODE_CHECK_PERIOD_SEC = 10
UPDATE_CURRENT_IP_CHECK_PERIOD_SEC = 60

# ==== Sockets ====
PROXY_MAX_FAILURE_RATIO = 0.8
PROXY_MIN_VALIDATION_REQUESTS = 8
