#!/bin/bash
# Script to run Hunyuan3D with HF-mirror.com endpoint

# Unset any proxy variables
unset http_proxy https_proxy HTTP_PROXY HTTPS_PROXY no_proxy NO_PROXY proxy_ip

# Set HF_ENDPOINT to use hf-mirror.com
export HF_ENDPOINT=https://hf-mirror.com

# Run the application with the specified arguments
# You can modify these arguments as needed
python gradio_app.py "$@"
