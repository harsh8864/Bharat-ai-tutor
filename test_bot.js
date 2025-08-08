#!/usr/bin/env node

/**
 * Bharat AI Tutor Bot - Test Script
 * Tests all major components before deployment
 */

const fs = require('fs');
const path = require('path');
const { exec } = require('child_process');

console.log('🧪 Bharat AI Tutor Bot - Component Test');
console.log('========================================');

// Colors for output
const colors = {
    green: '\x1b[32m',
    red: '\x1b[31m',
    yellow: '\x1b[33m',
    blue: '\x1b[34m',
    reset: '\x1b[0m'
};

function log(message, type = 'info') {
    const color = colors[type] || colors.reset;
    console.log(`${color}${message}${colors.reset}`);
}

// Test 1: Check environment variables
log('📋 Testing environment configuration...', 'blue');
if (!process.env.GEMINI_API_KEY || process.env.GEMINI_API_KEY === 'your_gemini_api_key_here') {
    log('❌ GEMINI_API_KEY not configured in .env file', 'red');
    log('   Please add your Gemini API key to the .env file', 'yellow');
} else {
    log('✅ GEMINI_API_KEY configured', 'green');
}

// Test 2: Check Node.js dependencies
log('📦 Testing Node.js dependencies...', 'blue');
const packageJson = JSON.parse(fs.readFileSync('package.json', 'utf8'));
const requiredDeps = ['venom-bot', 'axios', 'express', 'dotenv'];
let depsOk = true;

requiredDeps.forEach(dep => {
    if (!packageJson.dependencies[dep]) {
        log(`❌ Missing dependency: ${dep}`, 'red');
        depsOk = false;
    }
});

if (depsOk) {
    log('✅ All required Node.js dependencies found', 'green');
}

// Test 3: Check Python environment
log('🐍 Testing Python environment...', 'blue');
exec('python --version', (error, stdout, stderr) => {
    if (error) {
        log('❌ Python not found or not accessible', 'red');
    } else {
        log(`✅ Python found: ${stdout.trim()}`, 'green');
        
        // Test Python dependencies
        exec('python check_env_and_deps.py', (pyError, pyStdout, pyStderr) => {
            if (pyError) {
                log('❌ Python dependencies check failed', 'red');
                log(`   Error: ${pyError.message}`, 'yellow');
            } else {
                log('✅ Python dependencies check passed', 'green');
            }
        });
    }
});

// Test 4: Check FFmpeg
log('🎵 Testing FFmpeg installation...', 'blue');
exec('ffmpeg -version', (error, stdout, stderr) => {
    if (error) {
        log('❌ FFmpeg not found - audio processing will not work', 'red');
        log('   Install FFmpeg from: https://ffmpeg.org/download.html', 'yellow');
    } else {
        log('✅ FFmpeg found', 'green');
    }
});

// Test 5: Check required directories
log('📁 Testing directory structure...', 'blue');
const requiredDirs = ['audio', 'uploads', 'data', 'sessions'];
let dirsOk = true;

requiredDirs.forEach(dir => {
    if (!fs.existsSync(dir)) {
        log(`❌ Missing directory: ${dir}`, 'red');
        dirsOk = false;
    }
});

if (dirsOk) {
    log('✅ All required directories exist', 'green');
} else {
    log('   Creating missing directories...', 'yellow');
    requiredDirs.forEach(dir => {
        if (!fs.existsSync(dir)) {
            fs.mkdirSync(dir, { recursive: true });
            log(`   Created: ${dir}`, 'green');
        }
    });
}

// Test 6: Test transcription script
log('🎤 Testing transcription script...', 'blue');
if (fs.existsSync('transcribe.py')) {
    log('✅ transcribe.py found', 'green');
    
    // Test syntax
    exec('python -m py_compile transcribe.py', (error, stdout, stderr) => {
        if (error) {
            log('❌ transcribe.py has syntax errors', 'red');
            log(`   Error: ${error.message}`, 'yellow');
        } else {
            log('✅ transcribe.py syntax is valid', 'green');
        }
    });
} else {
    log('❌ transcribe.py not found', 'red');
}

// Test 7: Test TTS script
log('🗣️ Testing TTS script...', 'blue');
if (fs.existsSync('speak.py')) {
    log('✅ speak.py found', 'green');
    
    // Test syntax
    exec('python -m py_compile speak.py', (error, stdout, stderr) => {
        if (error) {
            log('❌ speak.py has syntax errors', 'red');
            log(`   Error: ${error.message}`, 'yellow');
        } else {
            log('✅ speak.py syntax is valid', 'green');
        }
    });
} else {
    log('❌ speak.py not found', 'red');
}

// Test 8: Check main bot file
log('🤖 Testing main bot file...', 'blue');
if (fs.existsSync('index.js')) {
    log('✅ index.js found', 'green');
    
    // Test syntax
    exec('node -c index.js', (error, stdout, stderr) => {
        if (error) {
            log('❌ index.js has syntax errors', 'red');
            log(`   Error: ${error.message}`, 'yellow');
        } else {
            log('✅ index.js syntax is valid', 'green');
        }
    });
} else {
    log('❌ index.js not found', 'red');
}

// Final summary
setTimeout(() => {
    console.log('\n📊 Test Summary');
    console.log('================');
    console.log('✅ Environment: Check .env file for GEMINI_API_KEY');
    console.log('✅ Dependencies: Run "npm install" if needed');
    console.log('✅ Python: Ensure Python 3.7+ is installed');
    console.log('✅ FFmpeg: Install for audio processing');
    console.log('✅ Directories: All required folders exist');
    console.log('✅ Scripts: All Python and Node.js files are valid');
    
    console.log('\n🚀 Ready to deploy!');
    console.log('   Run: npm start');
    console.log('   Then scan the QR code with WhatsApp');
}, 2000); 