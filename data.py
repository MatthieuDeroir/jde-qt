from utils.req import req

screen_width = 192
screen_height = 433

ip = "http://localhost:4000/trucks"
ip_fs = "http://localhost:4000/"

blink_time = 1

ref_x = 3
state_x = 95
dock_x = 180
margin = 3
font_size = 25
ref_list_x = 75
state_max_size = 67
separator = 46

try:
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



except:
    print("no data")
