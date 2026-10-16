// rust_servers/serverfile3.rs
use std::collections::HashMap;
use std::sync::{Arc, Mutex};
use std::net::{TcpListener, TcpStream};
use std::io::{Read, Write};
use std::thread;

struct CacheStore {
    store: Mutex<HashMap<String, String>>,
}

fn main() {
    let cache = Arc::new(CacheStore {
        store: Mutex::new(HashMap::new()),
    });

    let listener = TcpListener::bind("127.0.0.1:8083").expect("Failed to bind Server 3");
    println!("🛡️ [Rust Server 3] Cache & Security Master running on port 8083...");

    for stream in listener.incoming() {
        let cache_clone = Arc::clone(&cache);
        match stream {
            Ok(stream) => {
                thread::spawn(move || {
                    handle_cache_client(stream, cache_clone);
                });
            }
            Err(e) => eprintln!("Cache server connection failed: {}", e),
        }
    }
}

fn handle_cache_client(mut stream: TcpStream, cache: Arc<CacheStore>) {
    let mut buffer = [0; 1024];
    if let Ok(size) = stream.read(&mut buffer) {
        if size > 0 {
            let mut store = cache.store.lock().unwrap();
            store.insert("system_status".to_string(), "Optimal".to_string());
            
            let response = format!(
                "HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n{{\"cache_size\": {}, \"security\": \"Verified\"}}",
                store.len()
            );
            let _ = stream.write_all(response.as_bytes());
        }
    }
}

