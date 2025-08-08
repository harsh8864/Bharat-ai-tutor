// test-venom.js - Test script for Venom Bot integration
const venom = require('venom-bot');

console.log('🧪 Testing Venom Bot Integration...\n');

// Main async function to run the bot
async function testVenomBot() {
    let client;
    try {
        console.log('🔄 Initializing Venom Bot (this may take a moment)...');
        console.log('A Chromium browser window will open for QR code scanning.');

        client = await venom.create({
            session: 'test-session',
            multidevice: true,
            headless: false,
            logQR: true,
            useChrome: true
        });

        // After successful connection, start the bot logic
        await start(client);
    } catch (err) {
        console.error('❌ An error occurred during Venom Bot initialization:', err);
        process.exit(1);
    }
}

// This function runs once the client is successfully connected
async function start(client) {
    console.log('\n✅ WhatsApp client connected successfully!');

    try {
        // Fix 1: Await the host device info
        const hostDevice = await client.getHostDevice();
        console.log('📱 Host device info:', hostDevice);

        // Fix 2: Extract the correct phone number format
        const myNumber = `${hostDevice.id.user}@c.us`;
        console.log(`\n📤 Sending a test message to your own number (${myNumber})...`);
        
        // Fix 3: Add proper error handling for message sending
        try {
            await client.sendText(myNumber, 'Hello from Venom Bot! venom-bot test successful. ✅');
            console.log('👍 Test message sent successfully!');
        } catch (error) {
            console.error('❌ Error sending test message:', error);
        }
    } catch (error) {
        console.error('❌ Error getting host device info:', error);
    }

    // Fix 4: Improved message handling
    console.log('\n👂 Now listening for incoming messages...');
    console.log('Send "ping" to this number from any chat to test the listener.');

    client.onMessage(async (message) => {
        // Fix 5: Better message validation
        if (!message || message.isStatus || message.isGroupMsg) {
            return;
        }

        console.log(`\n📩 Message received from: ${message.from}`);
        // Fix 6: Safe message body access
        console.log(`💬 Body: ${message.body || ''}`);

        if (message.body && message.body.toLowerCase().trim() === 'ping') {
            try {
                console.log(`➡️ Replying "pong" to ${message.from}...`);
                await client.sendText(message.from, 'pong 🏓');
            } catch (error) {
                console.error(`❌ Error replying to ${message.from}:`, error);
            }
        }
    });
}

// Fix 7: Move SIGINT handler to the correct scope
let client;
process.on('SIGINT', async () => {
    console.log('\n🔴 Shutting down client...');
    if (client) {
        try {
            await client.close();
        } catch (error) {
            console.error('Error during shutdown:', error);
        }
    }
    process.exit(0);
});

// Run the main function
testVenomBot();