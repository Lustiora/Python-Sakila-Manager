def center_window(window, width, height): # Window 자동 중앙 정렬 모듈 (미정렬 시 좌측 상단) (tkinter)
    screen_width = window.winfo_screenwidth() # 현재 모니터의 해상도(크기)를 가져옴
    screen_height = window.winfo_screenheight()
    x_pos = (screen_width // 2) - (width // 2) # 정중앙 좌표 계산 \ (//)는 정수 나누기
    y_pos = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x_pos}+{y_pos}") # 위치 적용 (가로x세로+X좌표+Y좌표)
    window.resizable(False, False) # Window Size 변동 금지 (가로, 세로)
# 적용 > center_window([tkinter Window],[width],[height])

def set_focus_force(main, entry):  # 포커스 강제 조정
    main.lift()  # 창을 화면 맨 앞으로
    main.attributes('-topmost', True)  # 잠시동안 창을 최상위로 고정
    main.attributes('-topmost', False)  # 고정 해제 (안 그러면 다른 창이 안 덮임)
    entry.focus_force()  # [entry]입력창 강제 포커스

# from Window import set_focus_force
# login.after(200, set_focus_force, login, user_id) # set_focus_force(login, user_id)