# #13547a
# #80d0c7
# #0f172a s-9
# #475569 s-6
from datetime import datetime
import pyperclip
import re
import clipboard
import requests
import flet as flet
from flet import (
    Page,
    Column,
    Row,
    alignment,
    padding,
    ResponsiveRow,
    Container,
    Text,
    LinearGradient,
    CircleAvatar,
    TextField,
    TextButton,
    InputBorder,
    TextStyle,
    UserControl,
    ClipBehavior,
    CrossAxisAlignment,
)

class TiktokDownload(UserControl):
    def __int__(self):
        super().__int__()

    #
    def download_video(self, e):
        url = "https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/vid/index"
        video_url = self.url_tiktok_textField.value

        querystring = {"url": video_url}

        headers = {
            "X-RapidAPI-Key": "c222310903mshb5d1b8c262a58c6p16a432jsn6a46191623eb",
            "X-RapidAPI-Host": "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring, allow_redirects=True)

        data = response.text
        video = data.replace('[', '')
        link = re.findall(r'{"video":"([^"]+)"', video)
        url_video = ''.join(link)

        now = datetime.now()
        name = f'tiktok_{now.strftime("%Y%m%d%H%M%S")}.mp4'

        r = requests.get(url_video)
        open(name, "wb").write(r.content)

    #
    def paste_click(self, e):
        url_tiktok = pyperclip.paste()
        self.url_tiktok_textField.value = url_tiktok
        self.update()

    #
    def delete_click(self, e):
        self.url_tiktok_textField.value = ""
        self.update()

    #
    def on_button(self, e):
        str_input = str(self.url_tiktok_textField.value)

        if str_input == "":
            self.url_paste.visible = True
            self.url_paste.update()
            self.url_delete.visible = False
            self.url_delete.update()
        else:
            self.url_paste.visible = False
            self.url_paste.update()
            self.url_delete.visible = True
            self.url_delete.update()

        return self.on_button

    def build(self):
        _nav = Container(
            ResponsiveRow([
                Column(col={"xs": 12, "sm": 12, "md": 12, "xl": 12},
                       controls=[
                           Container(
                               padding=20,
                               bgcolor="#DEDEDE",
                               content=Row([
                                   CircleAvatar(
                                       width=60,
                                       height=60,
                                       bgcolor="white",
                                       content=
                                       Text("TD",
                                            size=30,
                                            weight="w900",
                                            color="black",
                                            text_align="center",
                                            ),
                                   ),
                               ], alignment="spaceBetween")
                           )
                       ]
                       )
            ]),
        )

        # titles
        _title = ResponsiveRow(
            alignment="center",
            controls=[
                Container(
                    col={"xs": 12, "sm": 10, "md": 10, "xl": 12},
                    alignment=alignment.top_center,
                    padding=30,
                    content=Text('Tải Video TikTok Miễn Phí.',
                                 size=40,
                                 weight="w600",
                                 text_align="center",
                                 ),
                )
            ],
        )

        #
        url_tiktok_textField = TextField(
            border=InputBorder.NONE,
            content_padding=padding.only(
                top=0, bottom=0, right=20, left=20),
            hint_style=TextStyle(
                size=16, color='#9DB2BF'
            ),
            text_style=TextStyle(
                size=18,
                color='black',
            ),
            hint_text='Dán liên kết Tiktok vào đây',
            cursor_color='black',
            width=386,
            height=50,
            col={"sm": 8, "md": 12, "lg": 10, "xl": 12},
        )

        #
        url_paste = Container(
            # col={"sm": 2, "md": 2, "lg": 2, "xl": 2},
            visible=True,
            height=49,
            width=70,
            bgcolor="blue600",
            border_radius=10,
            padding=0,
            content=TextButton("Paste", on_click=self.paste_click, height=50),
        )
        url_delete = Container(
            visible=False,
            height=49,
            width=70,
            bgcolor="blue600",
            border_radius=10,
            content=TextButton("Delete", on_click=self.delete_click, height=50)
        )
        url_download = Container(
            # col={"sm": 10, "md": 8, "lg": 1, "xl": 1},
            visible=True,
            height=50,
            width=90,
            bgcolor="blue600",
            border_radius=10,
            padding=0,
            content=TextButton("Download", on_click=self.download_video, height=50, width=70),
        )

        # 7/6/23
        self._item = [url_paste, url_delete]
        self._item_row = ResponsiveRow(alignment="center")

        _container_input = Container(
            alignment=alignment.center,

            bgcolor="white",
            padding=2,
            border_radius=10,
            col={"sm": 10, "md": 10, "lg": 6, "xl": 5},
            content=Row([
                url_tiktok_textField,
                url_paste,
                url_delete,
            ], alignment="spaceBetween"),
            on_hover=self.on_button,
        )

        #
        _container_download = Container(
            # alignment=alignment.center,
            bgcolor="white",
            padding=2,
            border_radius=10,
            col={"sm": 10, "md": 10, "lg": 1.2, "xl": 1},
            content=url_download
        )

        _container_item = Container(
            alignment=alignment.center,
            padding=20,
            content=self._item_row
        )

        self._item_row.controls.append(_container_input)
        self._item_row.controls.append(_container_download)

        # main column
        self._main_col = Column(horizontal_alignment="center", scroll="auto")
        self._main_col.controls.append(_nav)
        self._main_col.controls.append(Container(padding=padding.only(top=75)))
        self._main_col.controls.append(_title)
        self._main_col.controls.append(_container_item)
        return self._main_col


def main(page: Page):

    _main = Container(
        # height=self.page.height,
        expand=True,
        margin=-10,
        gradient=LinearGradient(
            begin=alignment.bottom_left,
            end=alignment.top_right,
            colors=["#13547a", "#0f172a"],
        ),
        clip_behavior=ClipBehavior.HARD_EDGE,

        content=Column(
            scroll=None,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            controls=[
                TiktokDownload(),
            ]
        ),
    )
    page.add(_main)
    page.update()

if __name__ == "__main__":
    flet.app(target=main, view=flet.WEB_BROWSER)