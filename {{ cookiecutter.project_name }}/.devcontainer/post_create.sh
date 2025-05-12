#!/usr/bin/env bash
set -e  # Exit on error

echo "🔧 Installing TeX Live and LaTeX tools..."
sudo apt-get update
sudo apt-get install -y --no-install-recommends \
    texlive-latex-recommended \
    texlive-latex-extra \
    texlive-fonts-recommended \
    latexmk \
    lmodern

echo "📦 Installing uv..."
curl -LsSf https://astral.sh/uv/install.sh | sh

echo "🔁 Installing Python dependencies with uv..."
uv sync --frozen --all-extras

echo "🧹 Installing pre-commit hooks..."
uv run pre-commit install --install-hooks

echo "✅ Post-create setup complete."
echo "🚀 You can now start using your development container!"
