#!/usr/bin/env node

/**
 * Robust start script for Render deployment
 */

const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');

console.log('🚀 Starting Bharat AI Tutor on Render...');
console.log('==========================================');

// Check if we're in production
const isProduction = process.env.NODE_ENV === 'production';
console.log(`🌍 Environment: ${isProduction ? 'Production' : 'Development'}`);

// Verify critical dependencies
console.log('🔍 Verifying dependencies...');
const criticalDeps = ['dotenv', 'express', 'venom-bot'];
let missingDeps = [];

for (const dep of criticalDeps) {
    try {
        require(dep);
        console.log(`✅ ${dep} - OK`);
    } catch (error) {
        console.log(`❌ ${dep} - MISSING`);
        missingDeps.push(dep);
    }
}

if (missingDeps.length > 0) {
    console.log('📦 Installing missing dependencies...');
    try {
        const { execSync } = require('child_process');
        execSync('npm install --production', { stdio: 'inherit' });
        console.log('✅ Dependencies installed successfully!');
    } catch (error) {
        console.error('❌ Failed to install dependencies:', error.message);
        process.exit(1);
    }
}

// Start the application with crash recovery
console.log('📱 Starting WhatsApp bot...');
let restartCount = 0;
const maxRestarts = 3;

function startApp() {
    console.log(`🔄 Starting application (attempt ${restartCount + 1}/${maxRestarts + 1})...`);
    
    const app = spawn('node', ['index.js'], {
        stdio: 'inherit',
        env: { ...process.env }
    });
    
    app.on('exit', (code) => {
        console.log(`⚠️ Application exited with code ${code}`);
        
        if (code !== 0 && restartCount < maxRestarts) {
            restartCount++;
            console.log(`🔄 Restarting application (${restartCount}/${maxRestarts})...`);
            setTimeout(startApp, 2000); // Wait 2 seconds before restart
        } else if (restartCount >= maxRestarts) {
            console.error('❌ Max restart attempts reached. Application failed.');
            process.exit(1);
        } else {
            console.log('✅ Application exited normally.');
            process.exit(code);
        }
    });
    
    app.on('error', (error) => {
        console.error('❌ Failed to start application:', error.message);
        process.exit(1);
    });
}

// Start the application
startApp();

// Handle process signals
process.on('SIGINT', () => {
    console.log('🛑 Received SIGINT, shutting down gracefully...');
    process.exit(0);
});

process.on('SIGTERM', () => {
    console.log('🛑 Received SIGTERM, shutting down gracefully...');
    process.exit(0);
});
