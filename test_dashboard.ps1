Write-Host "🧪 Testing Bharat AI Tutor Dashboard..." -ForegroundColor Green
Write-Host ""

try {
    # Test 1: Landing page
    Write-Host "📄 Testing landing page..." -ForegroundColor Yellow
    $landingResponse = Invoke-WebRequest -Uri "http://localhost:3000/" -UseBasicParsing
    Write-Host "✅ Landing page accessible" -ForegroundColor Green
    
    # Test 2: Dashboard page
    Write-Host "📊 Testing dashboard page..." -ForegroundColor Yellow
    $dashboardResponse = Invoke-WebRequest -Uri "http://localhost:3000/dashboard" -UseBasicParsing
    Write-Host "✅ Dashboard page accessible" -ForegroundColor Green
    
    # Test 3: Dashboard API
    Write-Host "🔌 Testing dashboard API..." -ForegroundColor Yellow
    $apiResponse = Invoke-WebRequest -Uri "http://localhost:3000/api/dashboard" -UseBasicParsing
    $data = $apiResponse.Content | ConvertFrom-Json
    
    Write-Host "✅ Dashboard API working" -ForegroundColor Green
    Write-Host "📊 Dashboard Data:" -ForegroundColor Cyan
    Write-Host "   - Active Users: $($data.userStats.activeUsers)" -ForegroundColor White
    Write-Host "   - Voice Messages: $($data.userStats.voiceMessages)" -ForegroundColor White
    Write-Host "   - Text Messages: $($data.userStats.textMessages)" -ForegroundColor White
    Write-Host "   - Avg Streak: $($data.userStats.avgStreak)" -ForegroundColor White
    Write-Host "   - Popular Topics: $($data.popularTopics.Count)" -ForegroundColor White
    Write-Host "   - Learning Streaks: $($data.learningStreaks.Count)" -ForegroundColor White
    Write-Host "   - Feedback Items: $($data.feedback.Count)" -ForegroundColor White
    
    Write-Host ""
    Write-Host "🎉 All dashboard tests passed!" -ForegroundColor Green
    Write-Host ""
    Write-Host "📱 Dashboard Features:" -ForegroundColor Cyan
    Write-Host "   ✅ User Stats (Voice vs Text usage, active users)" -ForegroundColor Green
    Write-Host "   ✅ Popular Topics (Most asked study topics)" -ForegroundColor Green
    Write-Host "   ✅ Learning Streaks (Daily usage streak tracker)" -ForegroundColor Green
    Write-Host "   ✅ Feedback & Ratings (User feedback from WhatsApp)" -ForegroundColor Green
    Write-Host ""
    Write-Host "🌐 Access your dashboard at: http://localhost:3000/dashboard" -ForegroundColor Yellow
    
} catch {
    Write-Host "❌ Dashboard test failed: $($_.Exception.Message)" -ForegroundColor Red
    if ($_.Exception.Response) {
        Write-Host "Status: $($_.Exception.Response.StatusCode)" -ForegroundColor Red
    }
} 