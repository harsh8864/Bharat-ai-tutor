#!/usr/bin/env node

/**
 * 🚀 Bharat AI Tutor - Deployment Helper
 * This script helps you deploy your bot online
 */

const fs = require('fs');
const path = require('path');

console.log('🚀 Bharat AI Tutor - Deployment Helper');
console.log('=====================================\n');

// Check if .env exists
if (!fs.existsSync('.env')) {
    console.log('❌ .env file not found!');
    console.log('📝 Creating .env file...');
    
    const envContent = `# Required
GEMINI_API_KEY=your_gemini_api_key_here

# Production settings
NODE_ENV=production
PORT=3000
VENOM_SESSION=bharat-ai-tutor
GEMINI_RETRY=3
`;
    
    fs.writeFileSync('.env', envContent);
    console.log('✅ .env file created!');
    console.log('⚠️  Please edit .env and add your GEMINI_API_KEY\n');
}

// Check if all required files exist
const requiredFiles = [
    'package.json',
    'requirements.txt',
    'index.js',
    'transcribe.py',
    'speak.py'
];

console.log('🔍 Checking required files...');
let allFilesExist = true;

requiredFiles.forEach(file => {
    if (fs.existsSync(file)) {
        console.log(`✅ ${file}`);
    } else {
        console.log(`❌ ${file} - MISSING`);
        allFilesExist = false;
    }
});

if (!allFilesExist) {
    console.log('\n❌ Some required files are missing!');
    process.exit(1);
}

console.log('\n✅ All files present!');

// Deployment options
console.log('\n🚀 Choose your deployment platform:');
console.log('1. Railway (Recommended) - Easiest, $3/month');
console.log('2. Render - Good alternative, $7/month');
console.log('3. Heroku - Classic option, $7/month');
console.log('4. Manual deployment guide');

console.log('\n📋 Quick Railway Deployment:');
console.log('1. Go to https://railway.app');
console.log('2. Sign up with GitHub');
console.log('3. Click "New Project" > "Deploy from GitHub repo"');
console.log('4. Select your repository');
console.log('5. Add environment variables:');
console.log('   - GEMINI_API_KEY=your_key_here');
console.log('   - NODE_ENV=production');
console.log('   - PORT=3000');
console.log('6. Deploy!');

console.log('\n📱 After deployment:');
console.log('- Your bot will be live at: https://your-app.railway.app');
console.log('- Users can message: +91 9011429593');
console.log('- Check logs for QR code to scan');

console.log('\n💡 Tips:');
console.log('- Railway auto-deploys when you push to GitHub');
console.log('- Check deployment logs for QR code');
console.log('- Monitor usage at railway.app/dashboard');
console.log('- Cost: ~$3/month for 24/7 operation');

console.log('\n🎉 Your bot will be accessible worldwide!');
console.log('🌍 Users can access it 24/7 without your PC running');
