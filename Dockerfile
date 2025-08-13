FROM node:18.18.0-slim

# Install Chrome dependencies
RUN apt-get update && apt-get install -y \
    chromium \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true
ENV CHROME_BIN=/usr/bin/chromium

# Create app directory
WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy project files
COPY . .

# Install Python requirements
RUN pip3 install -r requirements.txt

# Create necessary directories
RUN mkdir -p temp audio uploads

# Expose port
EXPOSE 3000

# Start command
CMD ["npm", "start"]