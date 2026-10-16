// rust_servers/serverfile1.rs
use std::net::{TcpListener, TcpStream};
use std::io::{Read, Write};
use std::thread;

fn handle_client(mut stream: TcpStream) {
    let mut buffer = [0; 1024];
    match stream.read(&mut buffer) {
        Ok(size) if size > 0 => {
            let request = String::from_utf8_lossy(&buffer[..size]);
            println!("[Server 1 - Gateway] Received student request: {}", request.lines().next().unwrap_or(""));

            let response = "HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n{\"status\":\"active\",\"gateway\":\"Rust Server 1 connected\"}";
            let _ = stream.write_all(response.as_bytes());
        }
        _ => {}
    }
}

fn main() {
    let listener = TcpListener::bind("127.0.0.1:8081").expect("Failed to bind Server 1");
    println!("🚀 [Rust Server 1] Gateway running on port 8081...");

    for stream in listener.incoming() {
        match stream {
            Ok(stream) => {
                thread::spawn(|| {
                    handle_client(stream);
                });
            }
            Err(e) => eprintln!("Connection failed: {}", e),
        }
    }
}
