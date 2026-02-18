# AIBuddy (CoM-PAS) Project Guide

Welcome to your project! Here is how to get everything running.

## 1. The Backend (The Brain)
This runs the logic and memory of your AI.

**How to run it:**
1. Open a terminal (Command Prompt or PowerShell).
2. Go to your project folder:
   ```powershell
   cd d:\AIBUDDY
   ```
3. Run the start script:
   ```powershell
   python backend/run.py
   ```
   *You should see "Uvicorn running on http://0.0.0.0:8000"*

## 2. The Frontend (The App)
This is the mobile app you see.

**Prerequisites:**
You need **Flutter** installed.
- Download it from: [flutter.dev](https://docs.flutter.dev/get-started/install/windows)
- Extract it to `C:\src\flutter` (recommended).
- Add `C:\src\flutter\bin` to your **Path** environment variable.

**How to run it:**
1. Open a **new** terminal.
2. Go to the app folder:
   ```powershell
   cd d:\AIBUDDY\mobile_app
   ```
3. Get the helper libraries:
   ```powershell
   flutter pub get
   ```
4. Start the app:
   ```powershell
   flutter run
   ```
   *Choose "Windows" or "Chrome" if asked.*

## 3. Project Structure
- `backend/`: Python code for the AI.
- `mobile_app/`: Flutter code for the UI.
- `chroma_db/`: Where your AI's memory is saved.

## Troubleshooting
**"Command not found" error?**
If you just installed Flutter, you must **restart your terminal** (close and open it again) for the changes to take effect.

