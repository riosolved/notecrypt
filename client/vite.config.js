
import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import vueDevTools from 'vite-plugin-vue-devtools';

// NOTE : https://vite.dev/config/
export default defineConfig({
    root: './src',
    plugins: [
        vue(),
        // vueDevTools()
    ],
    build: {
        outDir: '../dist'
    },
    // server: {
    //     host: true
    // }
    server: {
        host: '0.0.0.0',  // Allow access from other containers (not just localhost)
        port: 5173,
        hmr: {
            protocol: 'wss',  // Use secure WebSocket protocol for HTTPS
            host: 'localhost',  // The host of your application
            port: 5173,  // The port for WebSocket
        },
    },
});
