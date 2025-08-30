
import socket
import time
import random
import sys

HOST = "127.0.0.1"
PORT = 9999

USERS = ["U101", "U202", "U303", "U404", "U505", "U606"]
SKUS  = ["SKU-1", "SKU-2", "SKU-3", "SKU-4", "SKU-5"]
VALUES = [9.90, 14.90, 24.90, 39.90, 54.90, 79.90]

def line_add_to_cart():
    u = random.choice(USERS)
    sku = random.choice(SKUS)
    val = random.choice(VALUES)
    return f"INFO ecommerce event=add_to_cart user={u} sku={sku} value={val:.2f}"

def line_cart_abandoned():
    u = random.choice(USERS)
    nitems = random.randint(1, 5)
    val = sum(random.choice(VALUES) for _ in range(nitems))
    return f"INFO ecommerce event=cart_abandoned user={u} items={nitems} value={val:.2f}"

def line_checkout():
    u = random.choice(USERS)
    val = random.choice(VALUES)
    return f"INFO ecommerce event=checkout_ok user={u} value={val:.2f}"

def main():
    interval = float(sys.argv[1]) if len(sys.argv) > 1 else 0.4  # seconds between messages
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as srv:
        srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        srv.bind((HOST, PORT))
        srv.listen(1)
        print(f"[server] Escuchando en {HOST}:{PORT} (enviando continuamente cada {interval}s)")
        conn, addr = srv.accept()
        print("[server] Cliente conectado:", addr)
        with conn:
            conn.sendall(b"ready\n")
            while True:
                r = random.random()
                if r < 0.20:
                    line = line_cart_abandoned()
                elif r < 0.60:
                    line = line_add_to_cart()
                else:
                    line = line_checkout()
                try:
                    conn.sendall((line + "\n").encode("utf-8"))
                except BrokenPipeError:
                    print("[server] Cliente desconectado. Esperando nuevo cliente...")
                    conn, addr = srv.accept()
                    print("[server] Cliente conectado:", addr)
                    continue
                time.sleep(interval)

if __name__ == "__main__":
    main()
