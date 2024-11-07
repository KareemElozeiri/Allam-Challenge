import flet as ft
from ibm_API import get_response

def load_page6(page: ft.Page, navigate_to):
    page.clean()

    back_button = ft.ElevatedButton("رجوع", on_click=lambda _: navigate_to("الصفحة الرئيسية"), width=150)
    output_label = ft.Text("", size=20, text_align=ft.TextAlign.CENTER)

    def on_submit(e):
        base_prompt = ""
        prompt = f"اكتب لي ابياتا باللغة العربية الفصحى عن {text_box.value} .بأسلوب تقليدي وعاطفي، مستخدمًا صورًا شعرية ملونة ووصفًا حسيًا يعبر عن الموضوع. اجعل الأبيات شاعرية وأصيلة ."
        print("PRESSED")
        response = get_response(prompt=prompt)
        print(response)
        output_label.value = response
        page.update()
        page.update()

    text_box = ft.TextField(
        label="اكتب موضوعك هنا",
        text_align=ft.TextAlign.RIGHT,
        on_submit=on_submit,
        multiline=True
    )

    content_column = ft.Column(
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20,
        expand=True
    )
    
    content_column.controls.extend([
        ft.Text("ادخل موضوعا و علام سينشئ ابياتا عنه", size=30, text_align=ft.TextAlign.CENTER,font_family="Ruqaa"),
        text_box,
        ft.ElevatedButton("إرسال", on_click=on_submit),
        output_label,
        back_button
    ])

    page.add(content_column)