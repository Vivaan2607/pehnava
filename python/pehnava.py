import random

casual_events= ["beach", "brunch", "trip", "club", "dinner"]
formal_events= ["business", "meeting", "interview", "office"]
traditional_events = ["wedding", "baby_shower", "engagement"]


# cloth_sec = []
# item_sec = []
# occassion = []

casual_light_shirts=["white_plain_tshirt","baby_pink_hoodie","checkered_shirt"]
casual_light_jeans=["blue_ripped_jeans","red_shorts","white trousers"]
casual_dark_shirts=["black_shirt","blue_denim_shirt","darkblue_tshirt"]
casual_dark_jeans=["black_trousers","black_faded_jeans","dark_blue_jeans"]
casual_shoes=["Sneakers","Sports_shoes","crocs"]
casual_accessories=["watch","black_cap","black_bracelet"]

formal_light_shirts=["white_shirt","blue_shirt","beige_shirt"]
formal_light_jeans=["blue_jeans","grey_jeans"]
formal_dark_shirts=["blue_shirt","black_shirt","green_shirt"]
formal_dark_jeans=["blue_jeans","black_jeans","brown_jeans"]
formal_shoes=["blaclleather_shoes","brownleather_shoes"]
formal_accessories=["watch","black_belt","brown_belt","tie"]

traditional_light_shirts = ["long_kurti","short_Kurti","suit"]
traditional_light_jeans = ["long_skirts","palazzo","pants"]
traditional_dark_shirts = ["kurti","suit","sharara"]
traditional_dark_jeans = ["skirt","jaipuri_pants","saree"]
traditional_shoes = ["heels","flats","juttis"]
traditional_accessories = ["earrings","bangles","necklaces"]


# cloth_type = input("Enter the cloth type (top/bottom/shoe/accessories): ")
# item_name = input("Enter the item name (description): ")
# occassion = input("Enter the occasssion (casual_light/casual_dark/formal_light/formal_dark/traditional_light/traditional_dark): ")



event = input("Enter the event type (club/beach/trip/dinner/brunch/traditional/wedding/baby_shower/engagement/formal/meeting/interview/office): ")
color = input("Enter the color theme(dark/light): ")

res_arr = []

v1 = random.randint(0,2)
v2 = random.randint(0,2)
v3 = random.randint(0,2)
v4 = random.randint(0,2)

if(event == 'club' or event == 'beach' or event == 'trip' or event == 'dinner' or event == 'brunch'):
  if (color=="light"):
    res_arr.append(casual_light_shirts[v1])
    res_arr.append(casual_light_jeans[v2])
    res_arr.append(casual_shoes[v3])
    res_arr.append(casual_accessories[v4])

    for i in res_arr:
      print(i)
  elif(color == "dark"):
    res_arr.append(casual_dark_shirts[v1])
    res_arr.append(casual_dark_jeans[v2])
    res_arr.append(casual_shoes[v3])
    res_arr.append(casual_accessories[v4])

    for i in res_arr:
      print(i)

elif(event == 'traditional' or event == 'wedding' or event == 'baby_shower' or event == 'engagement'):
  if (color=="light"):
    res_arr.append(traditional_light_shirts[v1])
    res_arr.append(traditional_light_jeans[v2])
    res_arr.append(traditional_shoes[v3])
    res_arr.append(traditional_accessories[v4])

    for i in res_arr:
      print(i)
  elif(color == "dark"):
    res_arr.append(traditional_dark_shirts[v1])
    res_arr.append(traditional_dark_jeans[v2])
    res_arr.append(traditional_shoes[v3])
    res_arr.append(traditional_accessories[v4])

    for i in res_arr:
      print(i)
  

elif(event == 'formal' or event == 'meeting' or event == 'interview' or event == 'office'):
  if (color=="light"):
    res_arr.append(formal_light_shirts[v1])
    res_arr.append(formal_light_jeans[v2])
    res_arr.append(formal_shoes[v3])
    res_arr.append(formal_accessories[v4])

    for i in res_arr:
      print(i)
  elif(color == "dark"):
    res_arr.append(formal_dark_shirts[v1])
    res_arr.append(formal_dark_jeans[v2])
    res_arr.append(formal_shoes[v3])
    res_arr.append(formal_accessories[v4])

    for i in res_arr:
      print(i)