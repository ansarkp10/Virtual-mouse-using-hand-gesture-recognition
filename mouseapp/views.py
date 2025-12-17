from django.shortcuts import render
import subprocess
import sys
import os

# global process variable
process = None

def index(request):
    global process

    if request.method == "POST":
        action = request.POST.get("action")

        if action == "start":
            if process is None:
                process = subprocess.Popen(
                    [sys.executable, "run_mouse.py"],
                    cwd=os.getcwd()
                )

        elif action == "stop":
            if process is not None:
                process.terminate()
                process = None

    # ✅ DEFINE is_running HERE (THIS WAS MISSING BEFORE)
    is_running = process is not None

    return render(request, "index.html", {
        "is_running": is_running
    })
