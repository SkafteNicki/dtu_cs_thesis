#!/usr/bin/env bash
set -e  # Exit on error

echo "🔧 Installing TeX Live and LaTeX tools..."
# The base image ships a Yarn apt source whose signing key has expired, which
# makes `apt-get update` fail. Yarn is not needed here, so drop the source.
sudo rm -f /etc/apt/sources.list.d/yarn.list
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
uvx pre-commit install --install-hooks

echo "✅ Post-create setup complete."
echo "🚀 You can now start using your development container!"
