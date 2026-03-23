import threading
import os
import yt_dlp
from kivy.config import Config

# تثبيت الإعدادات الأساسية للواجهة
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')

from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.clock import Clock
from kivy.utils import platform
from kivymd.uix.screen import MDScreen
from kivymd.uix.menu import MDDropdownMenu

# الكود الخاص بالواجهة (KV Language) كما هو مع تحسينات طفيفة
KV = '''
<MenuCard@MDCard>:
    icon: ""
    text: ""
    on_release: app.change_screen(self.text.lower())
    orientation: "vertical"
    padding: dp(15)
    spacing: dp(10)
    radius: [20,]
    md_bg_color: 0.1, 0.1, 0.1, 1
    elevation: 4
    MDIcon:
        icon: root.icon
        halign: "center"
        font_size: dp(40)
        theme_text_color: "Custom"
        text_color: 1, 0.84, 0, 1
    MDLabel:
        text: root.text
        halign: "center"
        bold: True
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1

<DownloaderScreen@MDScreen>:
    platform_name: ""
    platform_color: [1, 1, 1, 1]
    MDBoxLayout:
        orientation: "vertical"
        padding: dp(20)
        spacing: dp(15)
        
        MDBoxLayout:
            size_hint_y: None
            height: dp(50)
            MDIconButton:
                icon: "arrow-left"
                on_release: app.change_screen("main")
            MDLabel:
                text: root.platform_name + " DOWNLOADER"
                bold: True
                theme_text_color: "Custom"
                text_color: root.platform_color
        
        MDProgressBar:
            id: progress_bar
            value: 0
            max: 100
            size_hint_y: None
            height: dp(2)
            opacity: 0
            color: root.platform_color
            
        MDTextField:
            id: link_input
            hint_text: "Paste URL here..."
            mode: "rectangle"
            fill_color_normal: 0.1, 0.1, 0.1, 1
            hint_text_color_focus: root.platform_color 
            line_color_focus: root.platform_color 
            text_color_normal: 1, 1, 1, 1 
            
        MDRaisedButton:
            id: quality_btn
            text: "Quality: Best (Auto)"
            size_hint_x: 1
            md_bg_color: 0.15, 0.15, 0.15, 1
            on_release: app.open_quality_menu(self)

        MDRaisedButton:
            text: "START DOWNLOAD"
            size_hint_x: 1
            md_bg_color: 1, 0.84, 0, 1
            text_color: 0, 0, 0, 1
            on_release: app.start_download(root.name, root.ids.link_input.text)
            
        MDLabel:
            id: status_label
            text: "Status: Idle"
            halign: "center"
            font_style: "Caption"
            theme_text_color: "Secondary"
        Widget:

ScreenManager:
    MDScreen:
        name: "main"
        md_bg_color: 0, 0, 0, 1
        MDBoxLayout:
            orientation: "vertical"
            padding: dp(20)
            MDLabel:
                text: "Y-DOWNLOADER PRO"
                halign: "center"
                font_style: "H5"
                bold: True
                theme_text_color: "Custom"
                text_color: 1, 0.84, 0, 1
                size_hint_y: None
                height: dp(80)
            MDGridLayout:
                cols: 2
                spacing: dp(20)
                MenuCard:
                    icon: "youtube"
                    text: "YouTube"
                MenuCard:
                    icon: "facebook"
                    text: "Facebook"
                MenuCard:
                    icon: "instagram"
                    text: "Instagram"
                MenuCard:
                    icon: "cog"
                    text: "Settings"
            Widget:
    DownloaderScreen:
        name: "youtube"
        platform_name: "YOUTUBE"
        platform_color: 1, 0, 0, 1
    DownloaderScreen:
        name: "facebook"
        platform_name: "FACEBOOK"
        platform_color: 0.1, 0.4, 0.9, 1
    DownloaderScreen:
        name: "instagram"
        platform_name: "INSTAGRAM"
        platform_color: 0.9, 0.1, 0.4, 1
    MDScreen:
        name: "settings"
        md_bg_color: 0, 0, 0, 1
        MDLabel:
            text: "Settings Screen - Path: /sdcard/Download"
            halign: "center"
            MDIconButton:
                icon: "arrow-left"
                pos_hint: {"top": 1}
                on_release: app.change_screen("main")
'''

class YDownloaderPro(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.selected_quality = "best"
        self.quality_menu = None
        self.base_path = ""

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Amber" # اللون الذهبي الذي تفضله
        
        if platform == 'android':
            try:
                # طلب صلاحيات التخزين الحديثة المتوافقة مع أندرويد 13+
                from android.permissions import request_permissions, Permission
                request_permissions([
                    Permission.WRITE_EXTERNAL_STORAGE, 
                    Permission.READ_EXTERNAL_STORAGE,
                    # صلاحيات إضافية للنسخ الحديثة
                    "android.permission.MANAGE_EXTERNAL_STORAGE" 
                ])
                from android.storage import primary_external_storage_path
                self.base_path = os.path.join(primary_external_storage_path(), "Download")
            except:
                self.base_path = "/sdcard/Download"
        else:
            self.base_path = "./Downloads"
            
        return Builder.load_string(KV)

    def open_quality_menu(self, button):
        items = [{"text": "Best", "on_release": lambda x="best": self.set_q(x, button)},
                 {"text": "720p", "on_release": lambda x="best[height<=720]": self.set_q(x, button)},
                 {"text": "480p", "on_release": lambda x="best[height<=480]": self.set_q(x, button)},
                 {"text": "MP3", "on_release": lambda x="bestaudio": self.set_q(x, button)}]
        self.quality_menu = MDDropdownMenu(caller=button, items=items, width_mult=3)
        self.quality_menu.open()

    def set_q(self, q, btn):
        self.selected_quality = q
        btn.text = f"Quality: {q}"
        self.quality_menu.dismiss()

    def change_screen(self, name):
        self.root.current = name

    def update_ui(self, sn, text, prog=0, op=1):
        def _update(dt):
            screen = self.root.get_screen(sn)
            screen.ids.status_label.text = text
            screen.ids.progress_bar.value = prog
            screen.ids.progress_bar.opacity = op
        Clock.schedule_once(_update)

    def start_download(self, sn, url):
        if not url.strip(): return
        self.update_ui(sn, "Connecting...")
        threading.Thread(target=self.safe_engine, args=(url, sn), daemon=True).start()

    def safe_engine(self, url, sn):
        try:
            # التأكد من وجود المجلد
            path = os.path.join(self.base_path, "YDownloader")
            if not os.path.exists(path):
                os.makedirs(path, exist_ok=True)
            
            opts = {
                'format': self.selected_quality,
                'outtmpl': f'{path}/%(title)s.%(ext)s',
                'nocheckcertificate': True,
                'quiet': True,
                'no_warnings': True,
                'cachedir': False,
                'progress_hooks': [lambda d: self.hook(d, sn)],
                'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
                'referer': 'https://www.google.com/',
                'extractor_args': {
                    'youtube': {
                        'player_client': ['web', 'mweb', 'android'],
                        'player_skip': ['configs', 'webpage']
                    }
                },
            }
            
            with yt_dlp.YoutubeDL(opts) as ydl:
                ydl.download([url])
            self.update_ui(sn, "Success! Check Downloads/YDownloader", 100, 0)
        except Exception as e:
            self.update_ui(sn, f"Error: {str(e)[:30]}", 0, 0)

    def hook(self, d, sn):
        if d['status'] == 'downloading':
            try:
                p_str = d.get('_percent_str', '0%').replace('%','').strip()
                p_float = float(p_str)
                self.update_ui(sn, f"Downloading: {p_str}%", p_float, 1)
            except: pass

if __name__ == '__main__':
    YDownloaderPro().run()
    
