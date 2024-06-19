import asyncio
import flet as ft
async def main(page: ft.Page) -> None:
    page.title="Orange Earn"
    page.theme_mode="dark"
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.fonts={"Font": "fonts/Font.ttf"}
    page.theme=ft.Theme(font_family="Font")

    async def score_up(event: ft.ContainerTapEvent) -> None:
        score.data += 1
        score.value = str(score.data)


        image.scale = 0.5
        progress_bar.value += (1 / 100)

        if score.data % 100 == 0:
            orange_coins_txt.value = str(int(orange_coins_txt.value.replace(" 🍊", "")) + 1) + " 🍊"
            progress_bar.value = 0
            page.update_async()

        await page.update_async()
        await asyncio.sleep(0.1)

        image.scale = 0.7
        await page.update_async()


    score = ft.Text(value="0", size=100, data=0)
    orange_coins_txt = ft.Text(value="0 🍊", size=20, data=0)
    image = ft.Image(src="images/Orange.png", scale=0.7 ,fit=ft.ImageFit.SCALE_DOWN, animate_scale=ft.Animation(duration=600, curve=ft.AnimationCurve.EASE))
    progress_bar = ft.ProgressBar(value=0, width=page.width - 100, bar_height=20, color=ft.colors.ORANGE_500, bgcolor=ft.colors.ORANGE_200, border_radius=10)

    await page.add_async(
        score,

        orange_coins_txt,

        ft.Container(
            content=image,
            on_click=lambda _: print(),
            on_tap_down=score_up,
            margin=ft.Margin(0, 0, 0, 5)
        ),

        ft.Container(
            content=ft.FilledButton("Listing is on 20 OF JULY", disabled=True),
            scale=1
        ),

        progress_bar

    )

ft.app(target=main, assets_dir="assets")