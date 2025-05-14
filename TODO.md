- User Authentication
    - Add user registration/login endpoints with password hashing (bcrypt).
    - Use JWT for session management.
- Note Storage
    - Create a Note model.
    - Implement create/read/delete routes for user-owned notes.
- Client-Side Encryption
    - Use the Web Crypto API to encrypt notes before sending.
    - Decrypt on read in Vue.js.
- Server-Side Encryption (Optional for comparison)
    - Add AES-GCM encryption with a per-user key stored via KDF.

---

Server:
- SAVE DB CHANGES TO LOCAL
- run:
    - cd ./server
    - python api.py

- test:
    - curl -X POST http://127.0.0.1:5000/enter -H "Content-Type: application/json" -d '{"email": "a", "password": "b"}'
