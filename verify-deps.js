#!/usr/bin/env node

/**
 * Verify all dependencies are properly installed
 */

console.log('🔍 Verifying dependencies...');

const requiredModules = [
  'dotenv',
  'express',
  'venom-bot',
  'axios',
  'body-parser',
  'multer',
  'node-cron'
];

let allGood = true;

for (const module of requiredModules) {
  try {
    require(module);
    console.log(`✅ ${module} - OK`);
  } catch (error) {
    console.log(`❌ ${module} - MISSING`);
    allGood = false;
  }
}

if (allGood) {
  console.log('\n🎉 All dependencies are properly installed!');
  process.exit(0);
} else {
  console.log('\n❌ Some dependencies are missing!');
  console.log('💡 Try running: npm install');
  process.exit(1);
}
