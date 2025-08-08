#!/bin/bash

# Bharat AI Tutor WhatsApp Bot - Setup Script
# This script automates the installation and setup process

echo "🚀 Bharat AI Tutor WhatsApp Bot - Setup Script"
echo "================================================"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

# Check if running on Windows
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
    IS_WINDOWS=true
    print_info "Detected Windows environment"
else
    IS_WINDOWS=false
fi

# Step 1: Check Node.js
print_info "Checking Node.js installation..."
if command -v node &> /dev/null; then
    NODE_VERSION=$(node --version)
    print_status "Node.js found: $NODE_VERSION"
else
    print_error "Node.js not found. Please install Node.js v16 or higher."
    print_info "Download from: https://nodejs.org/"
    exit 1
fi

# Step 2: Check Python
print_info "Checking Python installation..."
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
else
    print_error "Python not found. Please install Python 3.7 or higher."
    print_info "Download from: https://www.python.org/downloads/"
    exit 1
fi

PYTHON_VERSION=$($PYTHON_CMD --version 2>&1)
print_status "Python found: $PYTHON_VERSION"

# Step 3: Check FFmpeg
print_info "Checking FFmpeg installation..."
if command -v ffmpeg &> /dev/null; then
    FFMPEG_VERSION=$(ffmpeg -version | head -n1)
    print_status "FFmpeg found: $FFMPEG_VERSION"
else
    print_warning "FFmpeg not found. Audio processing features will not work."
    print_info "Install FFmpeg:"
    if [[ "$IS_WINDOWS" == true ]]; then
        print_info "  Windows: Download from https://ffmpeg.org/download.html"
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        print_info "  macOS: brew install ffmpeg"
    else
        print_info "  Linux: sudo apt update && sudo apt install ffmpeg"
    fi
fi

# Step 4: Install Node.js dependencies
print_info "Installing Node.js dependencies..."
if npm install; then
    print_status "Node.js dependencies installed successfully"
else
    print_error "Failed to install Node.js dependencies"
    exit 1
fi

# Step 5: Install Python dependencies
print_info "Installing Python dependencies..."
if $PYTHON_CMD -m pip install -r requirements.txt; then
    print_status "Python dependencies installed successfully"
else
    print_error "Failed to install Python dependencies"
    exit 1
fi

# Step 6: Create necessary directories
print_info "Creating necessary directories..."
mkdir -p audio uploads data sessions
print_status "Directories created successfully"

# Step 7: Check environment file
print_info "Checking environment configuration..."
if [[ ! -f ".env" ]]; then
    print_warning ".env file not found. Creating template..."
    cat > .env << EOF
# Bharat AI Tutor WhatsApp Bot - Environment Variables
# Copy this file to .env and fill in your actual values

# 🔑 REQUIRED: Gemini AI API Key (Get from https://makersuite.google.com/app/apikey)
GEMINI_API_KEY=your_gemini_api_key_here

# 🐍 Python Configuration (Optional - defaults to system python)
PYTHON_PATH=$PYTHON_CMD

# 🔄 Retry Configuration (Optional)
GEMINI_RETRY=3

# 🌐 Server Configuration (Optional)
PORT=3000

# 📱 WhatsApp Session Configuration (Optional)
VENOM_SESSION=bharat-ai-tutor

# 🎵 Audio Configuration (Optional)
MAX_AUDIO_LENGTH=300
AUDIO_QUALITY=128k

# 📊 Logging Configuration (Optional)
LOG_LEVEL=info
ENABLE_DEBUG=false

# 🔒 Security Configuration (Optional)
ENABLE_RATE_LIMITING=true
MAX_REQUESTS_PER_MINUTE=10

# 📚 Educational Configuration (Optional)
DEFAULT_LANGUAGE=en
ENABLE_HINDI_SUPPORT=true
ENABLE_VOICE_MESSAGES=true
EOF
    print_status ".env template created"
    print_warning "Please edit .env file and add your GEMINI_API_KEY"
else
    print_status ".env file found"
fi

# Step 8: Run environment check
print_info "Running environment check..."
if $PYTHON_CMD check_env_and_deps.py; then
    print_status "Environment check passed"
else
    print_warning "Environment check failed. Some features may not work properly."
fi

# Step 9: Final instructions
echo ""
echo "🎉 Setup completed successfully!"
echo "================================================"
echo ""
echo "Next steps:"
echo "1. Edit .env file and add your GEMINI_API_KEY"
echo "2. Run the bot: npm start"
echo "3. Scan the QR code with WhatsApp"
echo "4. Start chatting with the bot!"
echo ""
echo "For help, check the README.md file"
echo ""

print_status "Setup script completed successfully!" 