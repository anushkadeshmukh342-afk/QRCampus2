#!/bin/bash

# Kill previous Flask & ngrok if running
lsof -ti :5001 | xargs kill -9 2>/dev/null
pkill ngrok 2>/dev/null

# Activate venv
source venv/bin/activate

# Start Flask
echo "🚀 Starting Flask server..."
python3 app.py &

# Wait for server
sleep 3

# Start Ngrok
echo "🌐 Launching Ngrok..."
NGROK_URL=$(ngrok http 5001 --log=stdout | grep -o 'https://[a-z0-9]*\.ngrok-free\.app' | head -n 1)

# Copy to clipboard
if [[ $NGROK_URL != "" ]]; then
  echo "✅ Ngrok URL: $NGROK_URL"
  echo "$NGROK_URL" | pbcopy
  echo "📋 Copied to clipboard!"
else
  echo "❌ Failed to retrieve Ngrok URL"
fi