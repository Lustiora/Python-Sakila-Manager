#!/bin/bash
cd "$(dirname "$0")"
if [ -f ".venv/bin/activate" ]; then
    source .venv/bin/activate
else
    echo "❌ Error: .venv/bin/activate not found."
    exit 1
fi

echo "---------------------------------------------------"
echo "🚀 Flet Hot Reload Mode Starting..."
echo "[Web Mode] http://localhost:34636"
echo "[Exit] Ctrl + C"
echo "---------------------------------------------------"

flet run -r -w -v -p 34636 test_main_window.py

echo ""
read -p "Press Enter to exit..."