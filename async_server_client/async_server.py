import asyncio
import os

HTML_FILE = "hello-world.html"

async def handle_client(reader:asyncio.StreamReader, writer:asyncio.StreamWriter):
    try:
        #читання даних від клієнта
        data = await reader.read(1024)
        message = data.decode()
        #отримання першого рядку запиту
        request_line = message.splitlines()[0]
        method, path, _  = request_line.split()
        response = (
            "HTTP/1.1 404 Not Found\r\n"
            "Content-Type: text/plain\r\n"
            "\r\n"
            "Not Found\r\n"
        )
        if path == "/ping":
            response = (
                "HTTP/1.1 200 OK\r\n"
                "Content-Type: text/plain\r\n"
                "\r\n"
                "PONG"
            )
        elif path == "/hello":
            if os.path.isfile(HTML_FILE):
                with open(HTML_FILE, "r", encoding="utf-8") as file:
                    html_content = file.read()
                response = (
                    "HTTP/1.1 200 OK\r\n"
                    "Content-Type: text/html; charset=utf-8\r\n"
                    f"Content-Length: {len(html_content.encode("utf-8"))}\r\n"
                    "\r\n"
                    f"{html_content}"
                )
            else:
                response = (
                    "HTTP/1.1 500 Internal Server Error\r\n"
                    "Content-Type: text/plain\r\n"
                    "\r\n"
                    "HTML file not found"
                )
        #Відправляєм відповідь
        writer.write(response.encode("utf-8"))
        await writer.drain()
    except Exception as e:
        print("Enter handle client:",e)
    finally:
        writer.close()
        await writer.wait_closed()

async def main():
    server = await asyncio.start_server(handle_client, host="127.0.0.1", port=9000)
    addr = server.sockets[0].getsockname()
    print(f"Serving on {addr}")
    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())