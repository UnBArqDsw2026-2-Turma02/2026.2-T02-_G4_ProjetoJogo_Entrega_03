const http = require('node:http');
const fs = require('node:fs');
const path = require('node:path');

const root = path.join(__dirname, 'docs');
const port = Number(process.env.PORT || 8000);
const types = { '.html': 'text/html', '.md': 'text/markdown', '.css': 'text/css', '.js': 'text/javascript', '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.svg': 'image/svg+xml' };

http.createServer((request, response) => {
  let pathname;
  try { pathname = decodeURIComponent(new URL(request.url, 'http://localhost').pathname); }
  catch { response.writeHead(400).end(); return; }
  const file = path.resolve(root, `.${pathname === '/' ? '/index.html' : pathname}`);
  if (file !== root && !file.startsWith(root + path.sep)) { response.writeHead(403).end(); return; }
  fs.readFile(file, (error, body) => {
    if (error) { response.writeHead(error.code === 'ENOENT' ? 404 : 500).end(); return; }
    response.writeHead(200, { 'Content-Type': `${types[path.extname(file).toLowerCase()] || 'application/octet-stream'}; charset=utf-8` });
    response.end(body);
  });
}).listen(port, '127.0.0.1', () => console.log(`Docs: http://localhost:${port}`));
