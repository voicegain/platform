#!/usr/bin/env python3
"""
Simple webhook receiver.

Usage:
    python webhook_receiver.py      # listens on 0.0.0.0:8000
"""

import http.server
import logging


class WebhookHandler(http.server.BaseHTTPRequestHandler):
    # Silence default logging (optional—remove if you want the default log lines)
    def log_message(self, format, *args):  # noqa: N802
        return

    def do_POST(self):  # noqa: N802
        """Handle every incoming POST request."""
        # Read the raw body
        content_length = int(self.headers.get("Content-Length", 0))
        body_bytes = self.rfile.read(content_length) if content_length else b""

        # Print URL, headers, and body
        logging.info("URL: %s", self.path)
        logging.info("Headers:")
        for k, v in self.headers.items():
            logging.info("  %s: %s", k, v)
        logging.info("Body:\n%s", body_bytes.decode(errors="replace"))

        # Respond with 200 OK
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK\n")


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    server_address = ("0.0.0.0", 8000)
    httpd = http.server.HTTPServer(server_address, WebhookHandler)
    logging.info("Webhook receiver listening on http://%s:%s", *server_address)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        logging.info("\nShutting down.")


if __name__ == "__main__":
    main()
