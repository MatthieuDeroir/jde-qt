from utils.req import req

screen_width = 192
screen_height = 433

ip = "http://localhost:4000/trucks"
ip_fs = "http://localhost:4000/"
ip_mode = "http://localhost:4000/modes"

blink_time = 1

ref_x = 3
ref_width = 105
state_x = 92
dock_x = 180
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
