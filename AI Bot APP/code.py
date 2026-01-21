
import google.generativeai as ai # import models AI from Google
import flet as f  # library for UI 

ai.configure(api_key='API')  # api for import model ai from api ..
model = ai.GenerativeModel('gemini-1.5-flash') # include gemini-1.5-flash model
chatbot = model.start_chat()
def ui(page : f.Page):
    page.title = 'kawai'
    page.window.width = 450
    page.window.height = 800
    page.window.left = 400
    page.vertical_alignment = 'center'
    page.horizontal_alignment ='center'
    page.bgcolor = '#000000'  #f.Image(src='C:\\Users\\user\\Downloads\\rinnegan-dd-3840x2160.jpg')
    page.scroll = 'auto'
    chat_massage = f.Column(                               ################################
        controls=[], scroll='auto',
        expand=True, alignment=f.MainAxisAlignment.START
    )
    border_chat = f.Container(
    content=chat_massage, border=f.Border(
    bottom=f.BorderSide(width=3,color='#ff4f0f'),left=f.BorderSide(width=3,color='#ff4f0f')
    ,right=f.BorderSide(width=3,color='#ff4f0f'),top=f.BorderSide(width=3,color='#ff4f0f'))
    ,border_radius=5,padding=8,expand=True,height=550,width=700)
    
    chat = f.Column( controls=[border_chat],expand=True,scroll='auto')
    new_massage = f.TextField(label='search', autofocus=True,shift_enter=True,min_lines=1,max_lines=120,content_padding=10,width=300,
        filled=True,expand=True,bgcolor='black',color='#ffffff',border_color='#FF4F0F')
    
    def send_click(e):   
        user = f.Container(
              content=f.Text(new_massage.value, color='#FFFFFF'),
              bgcolor='#ff4f0f',  # لون خلفية الرسالة
              padding=10, border_radius=10,
        )
        chat_massage.controls.append(user)
        resp = chatbot.send_message(str(new_massage.value)) 
        bot = f.Container(
        content=f.Text(resp.text, color='#FFFFFF'),
        bgcolor='#333333',padding=10,border_radius=10,)
        chat_massage.controls.append(bot)
        new_massage.value = ''
        page.update()
    def open_profile(a):
        page.launch_url('https://www.instagram.com/35sql/')

    
    contact_icon = f.IconButton(
        icon=f.Icons.CONTACT_MAIL,
        icon_color="pink",
        tooltip="تواصل عبر instagram",
        on_click=open_profile
    )
    
    page.add(chat,f.Row(controls=[new_massage,
            f.ElevatedButton('Send',on_click=send_click,bgcolor='#ff4F0f',color="#FFFFFF")])) 
    page.navigation_bar = f.CupertinoNavigationBar(
        bgcolor = '#FF4f0f'
    )

    page.update()

f.app(target=ui)  # اذا تطبيق عادي
#f.app(target=ui,view=f.AppView.WEB_BROWSER) #     اذا  صفحة ويب 
