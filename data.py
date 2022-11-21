from utils.req import req

screen_width = 192
screen_height = 433

ipv4 = "localhost"
port = ":4000"

ip = "http://"+ ipv4 + port + "/trucks"
ip_fs = "http://"+ ipv4 + port + "/files"
ip_mode = "http://"+ ipv4 + port + "/modes"
ip_sb = "http://"+ ipv4 + port + "/veille"

path_to_media = "../../server/frontend/public"

blink_time = 1

ref_x = 3
ref_width = 105
state_x = 92
dock_x = 180
dock_title_x = 1
margin = 3
font_size = 25
ref_list_x = 75
state_max_size = 80
separator = 46

line_font_size = 12
title_font_size = 10
font = "Arial"

data = [{"ref": "0123456789",
         "state": "LOADING",
         "dock": "13"
         },
        {"ref": "0123456789",
         "state": "COME",
         "dock": "13"
         },
        {"ref": "0123456789",
         "state": "LOADING",
         "dock": "13"
         },
        {"ref": "0123456789",
         "state": "COME",
         "dock": "13"
         },
        {"ref": "0123456789",
         "state": "LOADING",
         "dock": "13"
         },
        {"ref": "0123456789",
         "state": "COME",
         "dock": "13"
         },
        {"ref": "0123456789",
         "state": "WAIT",
         "dock": "13"
         },
        {"ref": "0123456789",
         "state": "WAIT",
         "dock": "13"
         },
        {"ref": "0123456789",
         "state": "WAIT",
         "dock": "13"
         },
        {"ref": "0123456789",
         "state": "WAIT",
         "dock": "13"
         },
        {"ref": "0123456789",
         "state": "WAIT",
         "dock": "13"
         },
        {"ref": "0123456789",
         "state": "WAIT",
         "dock": "13"
         }
        ]
