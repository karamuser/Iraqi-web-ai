// rust_servers/serverfile2.rs
use std::io::{Read, Write};
use std::net::{TcpListener, TcpStream};
use std::thread;

fn process_curriculum_query(query: &str) -> String {
    format!(
        "{{\"processed_query\": \"{}\", \"curriculum\": \"Iraqi National Curriculum\", \"validation\": \"Strict Explanation First\"}}",
        query
    )
}

fn handle_client(mut stream: TcpStream) {
    let mut buffer = [0; 2048];
    match stream.read(&mut buffer) {
        Ok(size) if size > 0 => {
            let payload = String::from_utf8_lossy(&buffer[..size]);
            println!("[Server 2 - Processor] Processing educational payload...");

            let json_response = process_curriculum_query(&payload);
            let response = format!(
                "HTTP/1.1 200 OK\r\nContent-Type: application/json\r\nContent-Length: {}\r\n\r\n{}",
                json_response.len(),
                json_response
            );
            let _ = stream.write_all(response.as_bytes());
        }
        _ => {}
    }
}

fn main() {
    let listener = TcpListener::bind("127.0.0.1:8082").expect("Failed to bind Server 2");
    println!("⚙️ [Rust Server 2] Context Processor running on port 8082...");

    for stream in listener.incoming() {
        match stream {
            Ok(stream) => {
                thread::spawn(|| {
                    handle_client(stream);
                });
            }
            Err(e) => eprintln!("Processor connection failed: {}", e),
        }
    }
}
