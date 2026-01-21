from screeninfo import get_monitors
def center_window(window, width, height, resizable=None, min_size=None):
    # 1. 창 정보 업데이트
    window.update_idletasks()

    target_monitor = None
    monitors = get_monitors()

    # 2. '주 모니터(Primary)'를 찾아서 고정 타겟으로 설정
    for m in monitors:
        if m.is_primary:
            target_monitor = m
            break

    # 만약 주 모니터 감지에 실패했다면(Linux 드라이버 특성 등), 무조건 첫 번째 모니터 사용
    if target_monitor is None and len(monitors) > 0:
        target_monitor = monitors[0]

    # 3. 좌표 계산 (선택된 모니터의 중앙)
    if target_monitor:
        x_pos = target_monitor.x + (target_monitor.width // 2) - (width // 2)
        y_pos = target_monitor.y + (target_monitor.height // 2) - (height // 2)
    else:
        # 정말 만약에 모니터 정보를 아예 못 가져왔을 경우 (안전장치)
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x_pos = (screen_width // 2) - (width // 2)
        y_pos = (screen_height // 2) - (height // 2)

    # 4. 적용
    window.geometry(f"{width}x{height}+{x_pos}+{y_pos}")

    # 옵션 설정 (기존과 동일)
    if resizable is not None:
        if isinstance(resizable, bool):
            window.resizable(resizable, resizable)
        else:
            window.resizable(resizable[0], resizable[1])

    if min_size is not None:
        window.minsize(min_size[0], min_size[1])

def center_window_delayed(window, width, height):
    # 기존 center_window 로직 실행 (screeninfo 사용하는 버전)
    center_window(window, width, height, resizable=None)

    # 위치를 잡은 뒤에 창을 보여줌 (deiconify)
    window.deiconify()

def set_focus_force(main, entry):  # 포커스 강제 조정
    main.lift()  # 창을 화면 맨 앞으로
    main.attributes('-topmost', True)  # 잠시동안 창을 최상위로 고정
    main.attributes('-topmost', False)  # 고정 해제 (안 그러면 다른 창이 안 덮임)
    entry.focus_force()  # [entry]입력창 강제 포커스

# from Window import set_focus_force
# login.after(200, set_focus_force, login, user_id) # set_focus_force(login, user_id)