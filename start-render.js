#!/usr/bin/env node

/**
 * Robust start script for Render deployment
 */

const { spawn } = require('child_process');
const fs = require('fs');

console.log('🚀 Starting Bharat AI Tutor on Render...');

// Environment setup
process.env.PUPPETEER_SKIP_DOWNLOAD = 'true';
process.env.CHROME_BIN = '/usr/bin/google-chrome-stable';
process.env.DISPLAY = ':0';

// Create required directories
const dirs = ['temp', 'audio', 'uploads'];
dirs.forEach(dir => {
    if (!fs.existsSync(dir)) {
        fs.mkdirSync(dir);
    }
});

// Start the application
console.log('📱 Starting WhatsApp bot...');
const app = spawn('node', ['index.js'], {
    stdio: 'inherit',
    env: { ...process.env }
});

app.on('exit', (code) => {
    console.log(`⚠️ Application exited with code ${code}`);
    process.exit(code);
});
