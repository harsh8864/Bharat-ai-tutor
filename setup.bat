@echo off
chcp 65001 >nul
echo 🚀 Bharat AI Tutor WhatsApp Bot - Setup Script
echo ================================================

REM Check Node.js
echo ℹ️  Checking Node.js installation...
node --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Node.js not found. Please install Node.js v16 or higher.
    echo ℹ️  Download from: https://nodejs.org/
    pause
    exit /b 1
) else (
    for /f "tokens=*" %%i in ('node --version') do set NODE_VERSION=%%i
    echo ✅ Node.js found: %NODE_VERSION%
)

REM Check Python
echo ℹ️  Checking Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python not found. Please install Python 3.7 or higher.
    echo ℹ️  Download from: https://www.python.org/downloads/
    pause
    exit /b 1
) else (
    for /f "tokens=*" %%i in ('python --version') do set PYTHON_VERSION=%%i
    echo ✅ Python found: %PYTHON_VERSION%
)

REM Check FFmpeg
echo ℹ️  Checking FFmpeg installation...
ffmpeg -version >nul 2>&1
if %errorlevel% neq 0 (
    echo ⚠️  FFmpeg not found. Audio processing features will not work.
    echo ℹ️  Install FFmpeg: Download from https://ffmpeg.org/download.html
) else (
    echo ✅ FFmpeg found
)

REM Install Node.js dependencies
echo ℹ️  Installing Node.js dependencies...
call npm install
if %errorlevel% neq 0 (
    echo ❌ Failed to install Node.js dependencies
    pause
    exit /b 1
) else (
    echo ✅ Node.js dependencies installed successfully
)

REM Install Python dependencies
echo ℹ️  Installing Python dependencies...
call python -m pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ❌ Failed to install Python dependencies
    pause
    exit /b 1
) else (
    echo ✅ Python dependencies installed successfully
)

REM Create necessary directories
echo ℹ️  Creating necessary directories...
if not exist "audio" mkdir audio
if not exist "uploads" mkdir uploads
if not exist "data" mkdir data
if not exist "sessions" mkdir sessions
echo ✅ Directories created successfully

REM Check environment file
echo ℹ️  Checking environment configuration...
if not exist ".env" (
    echo ⚠️  .env file not found. Creating template...
    (
        echo # Bharat AI Tutor WhatsApp Bot - Environment Variables
        echo # Copy this file to .env and fill in your actual values
        echo.
        echo # 🔑 REQUIRED: Gemini AI API Key (Get from https://makersuite.google.com/app/apikey)
        echo GEMINI_API_KEY=your_gemini_api_key_here
        echo.
        echo # 🐍 Python Configuration (Optional - defaults to system python)
        echo PYTHON_PATH=python
        echo.
        echo # 🔄 Retry Configuration (Optional)
        echo GEMINI_RETRY=3
        echo.
        echo # 🌐 Server Configuration (Optional)
        echo PORT=3000
        echo.
        echo # 📱 WhatsApp Session Configuration (Optional)
        echo VENOM_SESSION=bharat-ai-tutor
        echo.
        echo # 🎵 Audio Configuration (Optional)
        echo MAX_AUDIO_LENGTH=300
        echo AUDIO_QUALITY=128k
        echo.
        echo # 📊 Logging Configuration (Optional)
        echo LOG_LEVEL=info
        echo ENABLE_DEBUG=false
        echo.
        echo # 🔒 Security Configuration (Optional)
        echo ENABLE_RATE_LIMITING=true
        echo MAX_REQUESTS_PER_MINUTE=10
        echo.
        echo # 📚 Educational Configuration (Optional)
        echo DEFAULT_LANGUAGE=en
        echo ENABLE_HINDI_SUPPORT=true
        echo ENABLE_VOICE_MESSAGES=true
    ) > .env
    echo ✅ .env template created
    echo ⚠️  Please edit .env file and add your GEMINI_API_KEY
) else (
    echo ✅ .env file found
)

REM Run environment check
echo ℹ️  Running environment check...
call python check_env_and_deps.py
if %errorlevel% neq 0 (
    echo ⚠️  Environment check failed. Some features may not work properly.
) else (
    echo ✅ Environment check passed
)

echo.
echo 🎉 Setup completed successfully!
echo ================================================
echo.
echo Next steps:
echo 1. Edit .env file and add your GEMINI_API_KEY
echo 2. Run the bot: npm start
echo 3. Scan the QR code with WhatsApp
echo 4. Start chatting with the bot!
echo.
echo For help, check the README.md file
echo.
echo ✅ Setup script completed successfully!
pause 