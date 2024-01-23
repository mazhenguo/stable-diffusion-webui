import os
os.chdir(f"/home/xlab-app-center")
os.system(f"git clone -b v2.6 https://github.com/mazhenguo/stable-diffusion-webui /home/xlab-app-center/stable-diffusion-webui")
os.chdir(f"/home/xlab-app-center/stable-diffusion-webui")
os.system(f"git lfs install")
os.system(f"git reset --hard")
os.system(f"sed -i -e '/demo:/r /home/xlab-app-center/header.py' /home/xlab-app-center/stable-diffusion-webui/modules/ui.py")
os.system(f"sed -i -e '253,258d' /home/xlab-app-center/stable-diffusion-webui/modules/ui_settings.py")
os.system(f"sed -i -e '186,228d' /home/xlab-app-center/stable-diffusion-webui/modules/ui_settings.py")
os.system(f"sed -i -e '171,178d' /home/xlab-app-center/stable-diffusion-webui/modules/ui_settings.py")
os.system(f"sed -i -e '108,113d' /home/xlab-app-center/stable-diffusion-webui/modules/ui_settings.py")
os.system(f"sed -i -e '225,227d' /home/xlab-app-center/stable-diffusion-webui/modules/ui_loadsave.py")
os.system(f"sed -i -e '214,217d' /home/xlab-app-center/stable-diffusion-webui/modules/ui_loadsave.py")

