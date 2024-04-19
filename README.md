# FLET-PDF

## Run App

```
python -m venv .venv
.venv\Scripts\activate
pip install flet
flet --version
```
```
flet run
```

> If Windows does not allow the script to run, run the following command in PowerShell from the project root:
```
Set-ExecutionPolicy RemoteSigned -Scope Process
```

## Code Snippets for Potential Use
```python
shadow = ft.BoxShadow(blur_radius=300, color=ft.colors.CYAN, offset=(0, 0), blur_style="outer"),

ft.Card(
    content=ft.Container(
        content=ft.IconButton(
            icon=ft.icons.PAUSE_CIRCLE_FILLED_ROUNDED,
            icon_color="blue400",
            icon_size=20,
            tooltip="Pause record",
            splash_radius=1,
        ),
    ),
    width=60,
    height=60,
),

ft.ElevatedButton(
    content=ft.Container(
        content=ft.Icon(name=ft.icons.CHECK_ROUNDED, color=ft.colors.BLUE),
        padding=10,
    ),
    on_click=lambda e: print("Button clicked"),
    style=ft.ButtonStyle(
        shape=ft.RoundedRectangleBorder(radius=10),
    ),
),

page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
page.auto_scroll = True
page.scroll = ft.ScrollMode.HIDDEN
page.appbar
```

## Useful Links
- [Framework Documentation](https://flet.dev/docs/)
- [Icons Flet](https://gallery.flet.dev/icons-browser/)
- [Project Video in Flet](https://www.youtube.com/watch?v=kGNp24U5Oyo)
- [Example Code Project in Flet_01](https://github.com/flet-dev/examples/blob/main/python/tutorials/calc/calc.py)
- [Example Code Project in Flet_02](https://github.com/flet-dev/examples/blob/main/python/tutorials/chat/chat.py)
