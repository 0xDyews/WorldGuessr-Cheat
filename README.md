# 🌍 WorldGuessr Cheat

This is a small Python script using [mitmproxy](https://mitmproxy.org/) to intercept and extract coordinates from Google Maps image search requests.

Whenever a matching request is detected, it automatically opens the exact location in Google Maps but zoomed out so you can see the general area (like country level).

---

## 🚀 What It Does

- Listens for specific internal Google Maps API requests.
- Parses the request data to extract latitude and longitude.
- Opens the coordinates in your default browser on Google Maps.

---

## 🛠 Setup Instructions

### 1. Install mitmproxy

```bash
pip install -r requirements.txt
```

### 2. Set up Proxy in Firefox/Chrome
Use an extension like FoxyProxy and configure it to:

- Host: 127.0.0.1
- Port: 8888
- Proxy Type: HTTP

Then activate the proxy.


### 3. Install mitmproxy's CA Certificate
To see HTTPS traffic (like Google Maps), you need to install mitmproxy’s certificate:

- Visit http://mitm.it in the proxied browser.
- Download and install the certificate for your platform.
- Follow the prompts for your OS/browser to trust it.


### 4. Run mitmproxy with the script

```bash
mitmproxy --listen-port 8888 -s main.py
```

### 5. Enjoy!
<3
