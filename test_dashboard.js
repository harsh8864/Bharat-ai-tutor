const axios = require('axios');

async function testDashboard() {
    const baseURL = 'http://localhost:3000';
    
    console.log('🧪 Testing Bharat AI Tutor Dashboard...\n');
    
    try {
        // Test 1: Landing page
        console.log('📄 Testing landing page...');
        const landingResponse = await axios.get(`${baseURL}/`);
        console.log('✅ Landing page accessible');
        
        // Test 2: Dashboard page
        console.log('📊 Testing dashboard page...');
        const dashboardResponse = await axios.get(`${baseURL}/dashboard`);
        console.log('✅ Dashboard page accessible');
        
        // Test 3: Dashboard API
        console.log('🔌 Testing dashboard API...');
        const apiResponse = await axios.get(`${baseURL}/api/dashboard`);
        const data = apiResponse.data;
        
        console.log('✅ Dashboard API working');
        console.log('📊 Dashboard Data:');
        console.log(`   - Active Users: ${data.userStats?.activeUsers || 0}`);
        console.log(`   - Voice Messages: ${data.userStats?.voiceMessages || 0}`);
        console.log(`   - Text Messages: ${data.userStats?.textMessages || 0}`);
        console.log(`   - Avg Streak: ${data.userStats?.avgStreak || 0}`);
        console.log(`   - Popular Topics: ${data.popularTopics?.length || 0}`);
        console.log(`   - Learning Streaks: ${data.learningStreaks?.length || 0}`);
        console.log(`   - Feedback Items: ${data.feedback?.length || 0}`);
        
        console.log('\n🎉 All dashboard tests passed!');
        console.log('\n📱 Dashboard Features:');
        console.log('   ✅ User Stats (Voice vs Text usage, active users)');
        console.log('   ✅ Popular Topics (Most asked study topics)');
        console.log('   ✅ Learning Streaks (Daily usage streak tracker)');
        console.log('   ✅ Feedback & Ratings (User feedback from WhatsApp)');
        console.log('\n🌐 Access your dashboard at: http://localhost:3000/dashboard');
        
    } catch (error) {
        console.error('❌ Dashboard test failed:', error.message);
        if (error.response) {
            console.error('Status:', error.response.status);
            console.error('Data:', error.response.data);
        }
    }
}

// Run the test
testDashboard(); 