#!/bin/bash
# Setup script for web job scraper dependencies

set -e

echo "Setting up Python virtual environment..."

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install playwright
echo "Installing Playwright..."
pip install --upgrade pip
pip install playwright

# Install Chromium browser
echo "Installing Chromium browser..."
playwright install chromium

echo ""
echo "Setup complete! You can now run:"
echo "  source venv/bin/activate"
echo "  python skills/web_job_scraper.py"
echo ""
echo "Or run the scraper directly with:"
echo "  ./setup.sh && source venv/bin/activate && python skills/web_job_scraper.py"
