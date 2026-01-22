from tkinter import messagebox
import sys
import os
import subprocess

def connect_test(conn, status, main, target_file):
    try:
        # print("Test Connected 5s") # 디버깅용
        with conn.cursor() as cursor:
            cursor.execute("select 1")
        # print("DB Connect Test : Connected")
        status.config(text="Connected", fg="#2ecc71")  # 녹색
    except Exception as e:
        status.config(text="Disconnected", fg="#e74c3c")  # 빨간색
        print(f"Error: {e}")
        if messagebox.askokcancel("Error", "Disconnected\nProgram Restart?"):
            main.destroy()
            current_dir = os.path.dirname(os.path.abspath(__file__))
            if not target_file:
                target_file = os.path.join(current_dir, "db_connect.py")
            my_env = os.environ.copy() # 환경변수 설정 (리눅스용)
            if "PYTHONPATH" in my_env:
                my_env["PYTHONPATH"] = current_dir + os.pathsep + my_env["PYTHONPATH"]
            else:
                my_env["PYTHONPATH"] = current_dir
            print("Restarting Process...")
            if sys.platform == 'win32': # [Windows]
                if getattr(sys, 'frozen', False):
                    # 1. EXE 배포 환경 (Windows)
                    print("Restarting Executable (Frozen)...")
                    subprocess.Popen([sys.executable], cwd=current_dir)
                else:
                    print("Restarting via os.system...")
                    os.chdir(current_dir)
                    os.system("python db_connect.py")
                sys.exit()  # 현재 프로세스 종료
            else: # [Linux / Mac]
                os.environ.update(my_env)
                if getattr(sys, 'frozen', False):
                    print("Restarting Executable (Linux Frozen)...")
                    os.execv(sys.executable, [sys.executable])
                else:
                    print("Restarting Python Script (Linux)...")
                    os.execv(sys.executable, [sys.executable, target_file])
        return  # 재시작 로직 진입 시 함수 종료
    if main.winfo_exists():
        main.after(5000, lambda: connect_test(conn, status, main, target_file))