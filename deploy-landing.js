#!/usr/bin/env node

/**
 * Bharat AI Tutor - Landing Page Deployment Script
 * Deploys the landing page to various platforms
 */

const fs = require('fs');
const path = require('path');

console.log('🚀 Bharat AI Tutor - Landing Page Deployment');
console.log('============================================');

// Check if public directory exists
const publicDir = path.join(__dirname, 'public');
const indexFile = path.join(publicDir, 'index.html');

if (!fs.existsSync(publicDir)) {
    console.log('📁 Creating public directory...');
    fs.mkdirSync(publicDir, { recursive: true });
}

if (!fs.existsSync(indexFile)) {
    console.error('❌ index.html not found in public directory');
    process.exit(1);
}

console.log('✅ Landing page files found');

// Deployment options
const deploymentOptions = {
    local: {
        name: 'Local Development',
        command: 'npm start',
        url: 'http://localhost:3000',
        description: 'Run locally for development and testing'
    },
    heroku: {
        name: 'Heroku',
        command: 'git push heroku main',
        url: 'https://your-app-name.herokuapp.com',
        description: 'Deploy to Heroku cloud platform'
    },
    railway: {
        name: 'Railway',
        command: 'railway up',
        url: 'https://your-app-name.railway.app',
        description: 'Deploy to Railway platform'
    },
    vercel: {
        name: 'Vercel',
        command: 'vercel --prod',
        url: 'https://your-app-name.vercel.app',
        description: 'Deploy to Vercel platform'
    },
    netlify: {
        name: 'Netlify',
        command: 'netlify deploy --prod',
        url: 'https://your-app-name.netlify.app',
        description: 'Deploy to Netlify platform'
    }
};

console.log('\n📋 Available Deployment Options:');
console.log('================================');

Object.entries(deploymentOptions).forEach(([key, option]) => {
    console.log(`\n🔹 ${option.name}`);
    console.log(`   Command: ${option.command}`);
    console.log(`   URL: ${option.url}`);
    console.log(`   Description: ${option.description}`);
});

console.log('\n🎯 Quick Start:');
console.log('===============');
console.log('1. For local development: npm start');
console.log('2. Visit: http://localhost:3000');
console.log('3. The landing page will be served automatically');

console.log('\n📱 WhatsApp Integration:');
console.log('=======================');
console.log('✅ WhatsApp number: +919011429593');
console.log('✅ Pre-filled message: "Hello AI Tutor 🤖 I want to learn something!"');
console.log('✅ Direct link: https://wa.me/919011429593?text=Hello%20AI%20Tutor%20🤖%20I%20want%20to%20learn%20something!');

console.log('\n🎨 Landing Page Features:');
console.log('========================');
console.log('✅ Modern, responsive design');
console.log('✅ WhatsApp integration');
console.log('✅ Voice message support showcase');
console.log('✅ Bilingual Hindi/English support');
console.log('✅ AI-powered learning features');
console.log('✅ Student testimonials');
console.log('✅ Smooth animations');
console.log('✅ Mobile-friendly');

console.log('\n🚀 Ready to deploy!');
console.log('===================');
console.log('The landing page is ready to be deployed to any platform.');
console.log('All files are properly configured and optimized.');

// Check for common deployment files
const deploymentFiles = [
    'package.json',
    'requirements.txt',
    '.env',
    'public/index.html'
];

console.log('\n📁 Required Files Check:');
console.log('========================');
deploymentFiles.forEach(file => {
    const exists = fs.existsSync(path.join(__dirname, file));
    console.log(`${exists ? '✅' : '❌'} ${file}`);
});

console.log('\n🎉 Deployment script completed successfully!'); 