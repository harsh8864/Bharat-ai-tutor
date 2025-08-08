#!/bin/bash

echo "🚀 Starting Bharat AI Tutor Build Process..."
echo "=========================================="

echo "📦 Installing Node.js dependencies..."
npm install

if [ $? -eq 0 ]; then
    echo "✅ Node.js dependencies installed successfully!"
else
    echo "❌ Failed to install Node.js dependencies"
    exit 1
fi

echo "🐍 Installing Python dependencies..."
pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ Python dependencies installed successfully!"
else
    echo "❌ Failed to install Python dependencies"
    exit 1
fi

echo "🔍 Verifying key dependencies..."
node -e "
try {
    require('dotenv');
    console.log('✅ dotenv module found');
} catch(e) {
    console.log('❌ dotenv module not found');
    process.exit(1);
}

try {
    require('express');
    console.log('✅ express module found');
} catch(e) {
    console.log('❌ express module not found');
    process.exit(1);
}

try {
    require('venom-bot');
    console.log('✅ venom-bot module found');
} catch(e) {
    console.log('❌ venom-bot module not found');
    process.exit(1);
}
"

echo "🎉 Build completed successfully!"
echo "🚀 Ready to start the application..."
