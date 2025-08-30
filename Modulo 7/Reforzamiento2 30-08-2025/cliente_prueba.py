
import socket
import argparse
from pathlib import Path

def read_lines(sock, max_lines):
    """Yield complete lines (\n-delimited) from a TCP socket."""
    buf = b""
    lines_read = 0
    while max_lines is None or lines_read < max_lines:
        chunk = sock.recv(4096)
        if not chunk:
            break
        buf += chunk
        while b"\n" in buf:
            line, buf = buf.split(b"\n", 1)
            yield line.decode("utf-8", errors="replace")
            lines_read += 1
            if max_lines is not None and lines_read >= max_lines:
                return

def main():
    parser = argparse.ArgumentParser(description="Cliente de prueba para leer JSON por socket (líneas con \n).")
    parser.add_argument("--host", default="127.0.0.1", help="Host del servidor (default: 127.0.0.1)")
    parser.add_argument("--port", type=int, default=9999, help="Puerto del servidor (default: 9999)")
    parser.add_argument("--lines", type=int, default=20, help="Número de líneas a leer antes de terminar (0 = infinito)")
    parser.add_argument("--out", type=str, default=None, help="Ruta de archivo para guardar lo recibido (opcional)")
    args = parser.parse_args()

    target_lines = None if args.lines == 0 else args.lines

    out_fh = None
    if args.out:
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        out_fh = open(args.out, "a", encoding="utf-8")
        print(f"[i] Guardando en: {args.out}")

    print(f"[i] Conectando a {args.host}:{args.port} ...")
    with socket.create_connection((args.host, args.port)) as s:
        print("[i] Conectado. Leyendo líneas...\n")
        for line in read_lines(s, target_lines):
            print(line)
            if out_fh:
                out_fh.write(line + "\n")

    if out_fh:
        out_fh.close()
        print(f"\n[i] Guardado en: {args.out}")

if __name__ == "__main__":
    main()
