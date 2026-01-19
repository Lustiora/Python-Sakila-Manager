import psycopg2
import tkinter
from tkinter import messagebox
# import Main
from window import center_window
from window import set_focus_force

count = 3

# -- Login GUI --

def login_gui():
    login = tkinter.Tk() # 표사되는 Window(tkinter.Tk())에 변수명을 지정하여 변수명을 기준으로 속성을 추가
    login.title("Staff Login")
    center_window(login, 260, 100)

    tkinter.Label(login, text="Username").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    user_id = tkinter.Entry(login) # Entry -> 입력칸 | 입력된 값을 사용하기 위해 변수명 지정 필요
    user_id.grid(row=0, column=1, padx=10, pady=5)
    login.grid_columnconfigure(0, weight=1) # ([열],[배당 비율])
    tkinter.Label(login, text="Password").grid(row=1, column=0, padx=5, pady=5, sticky="e")
    user_pw = tkinter.Entry(login, show="*") # show="*" > 유출 방지 : 입력값 * 대체 출력
    user_pw.grid(row=1, column=1, padx=10, pady=5)
    # user_pw.bind("<Return>", #) # Enter key 입력으로 Login 모듈 동작 ("[입력키]", [모듈])
    login.grid_columnconfigure(1, weight=1)
    # login_but = tkinter.Button(login, text="Login", command=user_login)
    # login_but.grid(row=2, column=0, columnspan=2, padx=10, pady=3, sticky="ew") # command=[클릭시 동작내용] | sticky="e" > 우측 정렬
    # login_but.bind("<Return>", user_login)
    # row=[행], column=[열]) > 0행 0열 = 좌측 상단 / 행과 열이 겹치는 경우 덮어씌워짐 | padx=[좌측우측외부여백], pady=[상단하단외부여백], ipa~=[내부여백]
    # 상세 정리 : https://puliseul.tistory.com/81

    login.after(200, set_focus_force, login, user_id) # set_focus_force(login, user_id)
    login.mainloop() # root(Window)를 지속적으로 반복 실행 (종료방지)