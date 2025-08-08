#!/bin/bash

echo "🚀 Starting Bharat AI Tutor..."
echo "=============================="

# Force install Node.js dependencies first
echo "📦 Installing Node.js dependencies..."
npm install --production

# Install Python dependencies
echo "🐍 Installing Python dependencies..."
pip install -r requirements.txt

# Verify critical Node.js dependencies
echo "🔍 Verifying critical dependencies..."
node -e "
try {
    require('dotenv');
    console.log('✅ dotenv - OK');
} catch(e) {
    console.log('❌ dotenv - MISSING, reinstalling...');
    require('child_process').execSync('npm install dotenv', {stdio: 'inherit'});
}
try {
    require('express');
    console.log('✅ express - OK');
} catch(e) {
    console.log('❌ express - MISSING, reinstalling...');
    require('child_process').execSync('npm install express', {stdio: 'inherit'});
}
try {
    require('venom-bot');
    console.log('✅ venom-bot - OK');
} catch(e) {
    console.log('❌ venom-bot - MISSING, reinstalling...');
    require('child_process').execSync('npm install venom-bot', {stdio: 'inherit'});
}
console.log('🎉 All dependencies verified!');
"

# Start the application
echo "📱 Starting WhatsApp bot..."
npm start
