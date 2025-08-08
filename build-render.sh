#!/bin/bash

echo "🚀 Starting Bharat AI Tutor Build for Render..."
echo "=============================================="

# Install Node.js dependencies
echo "📦 Installing Node.js dependencies..."
npm install --production
if [ $? -ne 0 ]; then
    echo "❌ Failed to install Node.js dependencies"
    exit 1
fi
echo "✅ Node.js dependencies installed successfully!"

# Install Python dependencies with error handling
echo "🐍 Installing Python dependencies..."
pip install --no-cache-dir --upgrade pip

# Try minimal requirements first
echo "📦 Trying minimal requirements..."
pip install --no-cache-dir -r requirements-minimal.txt
if [ $? -ne 0 ]; then
    echo "⚠️  Minimal requirements failed, trying essential packages only..."
    pip install --no-cache-dir requests python-dotenv pydub numpy
    if [ $? -ne 0 ]; then
        echo "❌ Failed to install essential Python dependencies"
        exit 1
    fi
    echo "✅ Essential Python dependencies installed"
else
    echo "✅ Minimal Python dependencies installed successfully!"
fi

# Verify critical Node.js dependencies
echo "🔍 Verifying Node.js dependencies..."
node -e "
const deps = ['dotenv', 'express', 'venom-bot', 'axios', 'body-parser', 'multer', 'node-cron'];
let allGood = true;
for (const dep of deps) {
    try {
        require(dep);
        console.log(\`✅ \${dep} - OK\`);
    } catch (e) {
        console.log(\`❌ \${dep} - MISSING\`);
        allGood = false;
    }
}
if (!allGood) {
    console.log('❌ Critical dependencies missing!');
    process.exit(1);
}
console.log('🎉 All Node.js dependencies verified!');
"

if [ $? -ne 0 ]; then
    echo "❌ Node.js dependency verification failed"
    exit 1
fi

echo "🎉 Build completed successfully!"
echo "🚀 Ready to start the application..."
