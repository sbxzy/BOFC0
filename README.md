# BOFC0
## 修仙学士：前传 的开放资源
## Open resources for the game BOFC: a Prelude


#### Requirments 前置条件：
numpy
hashlib
binascii
pygame
pygame-menu
requests
yaml
lxml
inputs
pyautogui

and most importantly:
Panda3D development version. (You can try pip3 install --pre --extra-index-url https://archive.panda3d.org/ panda3d)

After that, switch to the ‘game’ directory and run
python3 BOFC.py

You may need to install more packages that are reported missing.

### 手册Manual
在game文件夹下，查看和修改’keys.txt’来控制游戏按键。游戏中经常用j键打开查看玩法提示。如果您有多个显卡，请设置采用高性能GPU运行。游戏作弊码(通过回车键激活)如下表：
Keys are configured in ‘keys.txt’ under the ‘game’ directory. In the game, if you don’t know what to do, always press ‘j’ to see hints. If you have multiple video cards, please set it to run with high performance GPU.
Press Enter can invoke console for cheats.
Cheat code:
Code	Function
additem [0|1|2|3|4|5]	Drop random item
place {NPC name} {plot name}	Activate plot on NPC
move {NPC name} {x,y,z}	Move NPC to position (x,y,z)

NPC names and plot names can be seen from console outputs if you are running the game from cmd.

For non-Chinese players: All plots are in the form of xml files under the ‘game\levels’ directory, you can translate and modify those Chinese characters. But please do not add any punctuations apart from , and .

音乐音量大小在game文件夹下的music_volume.txt设置。Music volume can be changed by modify the file music_volume.txt under the game folder.


### License: 
Free to use but restricted. Please, do not decrypt the encrypted py files. If you want to use these encrypted resources and egg model (animation) files, contact the author at sbxzy@foxmail.com or can [buy](https://www.microsoft.com/store/productId/9N82ZJHM81WJ) a windows version at Microsoft appstore, and send me the bill information through the email. I will reply with zipped code that run the complete game. After recieving the pack, simply unzip and overwrite all py files and folders.

This game includes files from several CC series copyrighted.
Under the directories ‘musics/peace’ and ‘0addata’ under the game directory. All ogg files are from this project:
https://play0ad.com/
They are distributed under this license. 
 
Under the ‘animation’ directory, models and animations are created by Makehuman software and Blender 2.79. Resources created by Makehuman users and are used, these used resources are distributed under CC-BY license and CC0 license.
Links of these resources are:
https://www.blender.org/
http://www.makehumancommunity.org/
https://download.blender.org/demo/test/pabellon_barcelona_v1.scene_.zip
http://www.makehumancommunity.org/content/user_contributed_assets.html
http://www.makehumancommunity.org/clothes/elvs_clubdress_2.html
http://www.makehumancommunity.org/clothes/elvs_long_halterdress1.html
http://www.makehumancommunity.org/clothes/ghandi_gown.html
http://www.makehumancommunity.org/clothes/elvs_daisy_hair1.html
http://www.makehumancommunity.org/clothes/french_braid_01_variation.html
http://www.makehumancommunity.org/clothes/leather_boots.html
http://www.makehumancommunity.org/clothes/armored_corset_wonder_woman.html
http://www.makehumancommunity.org/clothes/vambraces_wonder_woman.html
http://www.makehumancommunity.org/clothes/armored_boots_wonder_woman.html
http://www.makehumancommunity.org/clothes/bracelet_wonder_woman.html
http://www.makehumancommunity.org/skin/stonebuddha.html

And there are of course the PANDA3D software (www.panda3d.org) and tobspr’s render pipeline:
https://github.com/tobspr/RenderPipeline

RenderPipeline include following files (under the ‘game’ directory):
 

The libs folder contains a minimal Python environment that runs the game. It is distributed under the python software foundation license.
Apart from files mentioned above, other files and codes are copyrighted to the game author (email sbxzy@foxmail.com). Please contact the author if any of your arts are not listed above. If you want to use models, sounds or other code stuff created by the author in your own projects, also contact sbxzy@foxmail.com.
2020-08-04

