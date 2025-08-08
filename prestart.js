#!/usr/bin/env node

/**
 * Pre-start script to ensure all dependencies are installed
 */

const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

console.log('🔧 Pre-start dependency check...');

// Check if node_modules exists
if (!fs.existsSync(path.join(__dirname, 'node_modules'))) {
    console.log('📦 node_modules not found, installing dependencies...');
    try {
        execSync('npm install --production', { stdio: 'inherit' });
        console.log('✅ Dependencies installed successfully!');
    } catch (error) {
        console.error('❌ Failed to install dependencies:', error.message);
        process.exit(1);
    }
}

// Check critical dependencies
const criticalDeps = ['dotenv', 'express', 'venom-bot', 'axios', 'body-parser', 'multer', 'node-cron'];

for (const dep of criticalDeps) {
    try {
        require(dep);
        console.log(`✅ ${dep} - OK`);
    } catch (error) {
        console.log(`❌ ${dep} - MISSING, installing...`);
        try {
            execSync(`npm install ${dep}`, { stdio: 'inherit' });
            console.log(`✅ ${dep} - INSTALLED`);
        } catch (installError) {
            console.error(`❌ Failed to install ${dep}:`, installError.message);
            process.exit(1);
        }
    }
}

console.log('🎉 All dependencies are ready!');
console.log('🚀 Starting application...');
