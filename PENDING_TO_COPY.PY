############################################### HELP ##################################################

def open_url(url):
        webbrowser.open(url)

def help_label(options_frame):
        label_option = ctk.CTkLabel(options_frame, text='Help', justify='center', font=ctk.CTkFont(size=13, weight="bold"))
        label_option.pack(padx=(10,10), pady=(10,10))

def help_label_explain(options_frame):
        label_explain_1 = ctk.CTkLabel(options_frame, text='You can see a demo tutorial if you do click on the image', justify='center')
        label_explain_1.pack(padx=(10,10), pady=(10,10))

def help_image(options_frame):
        youtube_image = ctk.CTkImage(light_image=Image.open("GraphicUI/images/Tutorial_youtube_light.png"),
                                dark_image=Image.open("GraphicUI/images/Tutorial_youtube_dark.png"),
                                size=(200, 75))

        youtube_image = ctk.CTkButton(options_frame, corner_radius=0, height=40, border_spacing=10, text="",
                                                fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                image=youtube_image, anchor="w", command=lambda:open_url("https://youtube.com"))
        youtube_image.pack(padx=(10,10), pady=(10,10))

def help_label_explain_2(options_frame):
        label_explain_2 = ctk.CTkLabel(options_frame, text='You can download a pdf tutorial if you do click on the document', justify='center')
        label_explain_2.pack(padx=(10,10), pady=(10,10))

def help_button_pdf_image(options_frame):
        pdf_image = ctk.CTkImage(light_image=Image.open("GraphicUI/images/pdf.png"),
                                dark_image=Image.open("GraphicUI/images/pdf.png"),
                                size=(20, 20))
        label_button_explain_2 = ctk.CTkButton(options_frame, corner_radius=0, height=40, border_spacing=10, text="Demo botnet twitter.pdf",
                                                fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                image=pdf_image, anchor="w", command=lambda:open_url("https://google.com"))
        label_button_explain_2.pack(padx=(10,10), pady=(10,10))

# no sé si ha cambiado algo 
popup_comment_window_button = ctk.CTkButton(scrollable_popup_frame, text='Go!', command=lambda:[twitter_popup_comment_go_button(scrollable_frame_entries), twitter_give_comment(entry_twitter_url, button_entry, twitter_label_accounts, twitter_checkbox_follow, twitter_checkbox_like, twitter_checkbox_rt, twitter_checkbox_cmnt, twitter_button_action), close_comment_window(popup_comment_window)], state="disabled")
        popup_comment_window_button.grid(row=entry_value, column=0)

def close_comment_window(popup_comment_window):
        popup_comment_window.destroy()