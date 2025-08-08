#!/bin/bash

echo "🚀 Starting Bharat AI Tutor..."
echo "=============================="

# Install Python dependencies if not already installed
echo "🐍 Installing Python dependencies..."
pip install -r requirements.txt

# Verify Node.js dependencies
echo "🔍 Verifying Node.js dependencies..."
node verify-deps.js

if [ $? -eq 0 ]; then
    echo "✅ All dependencies verified successfully!"
    echo "📱 Starting WhatsApp bot..."
    npm start
else
    echo "❌ Dependency verification failed!"
    echo "💡 Installing Node.js dependencies..."
    npm install
    echo "📱 Starting WhatsApp bot..."
    npm start
fi
