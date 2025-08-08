# 🚀 **ONLINE DEPLOYMENT GUIDE - Bharat AI Tutor Bot**

## **Quick Deploy Options**

### **Option 1: Railway (Recommended - 5 minutes)**

1. **Sign up for Railway:**
   - Go to [railway.app](https://railway.app)
   - Sign up with GitHub

2. **Deploy your bot:**
   ```bash
   # Install Railway CLI
   npm install -g @railway/cli
   
   # Login to Railway
   railway login
   
   # Deploy your project
   railway init
   railway up
   ```

3. **Set Environment Variables:**
   - Go to your Railway dashboard
   - Add these environment variables:
   ```
   GEMINI_API_KEY=your_gemini_api_key_here
   NODE_ENV=production
   PORT=3000
   VENOM_SESSION=bharat-ai-tutor
   ```

4. **Get your live URL:**
   - Railway will give you a URL like: `https://your-app.railway.app`
   - Your bot will be live at this URL!

### **Option 2: Render (Alternative)**

1. **Sign up for Render:**
   - Go to [render.com](https://render.com)
   - Sign up with GitHub

2. **Connect your repository:**
   - Connect your GitHub repo
   - Choose "Web Service"
   - Set build command: `npm install && pip install -r requirements.txt`
   - Set start command: `npm start`

3. **Set Environment Variables:**
   ```
   GEMINI_API_KEY=your_gemini_api_key_here
   NODE_ENV=production
   PORT=3000
   VENOM_SESSION=bharat-ai-tutor
   ```

4. **Deploy:**
   - Click "Create Web Service"
   - Your bot will be live in 5-10 minutes!

### **Option 3: Heroku (Classic)**

1. **Install Heroku CLI:**
   ```bash
   # Download from heroku.com
   heroku login
   ```

2. **Deploy:**
   ```bash
   heroku create your-bot-name
   git add .
   git commit -m "Deploy to Heroku"
   git push heroku main
   ```

3. **Set environment variables:**
   ```bash
   heroku config:set GEMINI_API_KEY=your_key_here
   heroku config:set NODE_ENV=production
   ```

## **🔧 Production Optimizations**

### **1. Update your .env file:**
```env
# Required
GEMINI_API_KEY=your_gemini_api_key_here

# Production settings
NODE_ENV=production
PORT=3000
VENOM_SESSION=bharat-ai-tutor
GEMINI_RETRY=3
```

### **2. WhatsApp QR Code for Production:**
- In production, the QR code will appear in logs
- Check your deployment logs to scan the QR code
- Once scanned, it will stay connected

### **3. Test your deployed bot:**
```bash
# Test the API endpoints
curl https://your-app.railway.app/
curl https://your-app.railway.app/stats
```

## **📱 User Access**

### **After Deployment:**

1. **Your bot will be available at:**
   - `https://your-app.railway.app` (or your deployment URL)

2. **Users can access via:**
   - WhatsApp: Send message to your bot number
   - Web: Visit your deployment URL
   - Direct link: `https://wa.me/919011429593?text=Hello%20AI%20Tutor`

3. **Share with users:**
   ```
   🤖 Bharat AI Tutor Bot is now LIVE!
   
   📱 WhatsApp: +91 9011429593
   🌐 Web: https://your-app.railway.app
   
   🎓 Features:
   - Ask questions in Hindi/English
   - Voice message support
   - Educational content
   - Free to use!
   ```

## **🔍 Monitoring & Maintenance**

### **Check your bot status:**
```bash
# View logs
railway logs

# Check stats
curl https://your-app.railway.app/stats

# Monitor WhatsApp connection
curl https://your-app.railway.app/whatsapp-status
```

### **Update your bot:**
```bash
# Make changes locally
git add .
git commit -m "Update bot"
git push

# Railway/Render will auto-deploy
# Or manually deploy:
railway up
```

## **💰 Cost Estimation**

### **Railway:**
- Free tier: $5/month credit
- Your bot: ~$2-3/month
- **Total: ~$3/month**

### **Render:**
- Free tier: 750 hours/month
- Your bot: ~$7/month
- **Total: ~$7/month**

### **Heroku:**
- Free tier: Discontinued
- Basic dyno: $7/month
- **Total: ~$7/month**

## **🚀 Recommended: Railway**

**Why Railway is best:**
- ✅ Easiest deployment
- ✅ Good free tier
- ✅ Auto-deploys from GitHub
- ✅ Built-in monitoring
- ✅ Fast setup

**Deploy now:**
1. Go to [railway.app](https://railway.app)
2. Connect your GitHub repo
3. Set environment variables
4. Deploy in 5 minutes!

Your bot will be live and accessible to users worldwide! 🌍 