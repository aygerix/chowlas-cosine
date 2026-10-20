"""Local Lean LSP diagnostics, retaining imported environments across edits.
Usage from lean/: lake env python3 ../.research/agents/lean_next_scratch/lsp_check.py
Stop the PTY process with Ctrl-C. Final verification still uses lake build.
"""
import json, pathlib, subprocess, threading, time, sys, os
root = pathlib.Path.cwd()
scratch = root.parent / '.research/agents/lean_next_scratch'
work = scratch / 'Combined.lean'
log = scratch / 'lsp_diagnostics.json'
source_names = sys.argv[1:] or ['WindowMoments.lean', 'Averaging.lean', 'Fejer.lean', 'WindowBound.lean']
proc = subprocess.Popen(['lean', '--server'], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                        stderr=open(scratch / 'lsp_stderr.log', 'w'))
lock = threading.Lock()
request_id = 0

def send(method, params, request=False):
    global request_id
    obj = {'jsonrpc':'2.0', 'method':method, 'params':params}
    if request:
        request_id += 1
        obj['id'] = request_id
    data = json.dumps(obj).encode()
    with lock:
        proc.stdin.write(f'Content-Length: {len(data)}\r\n\r\n'.encode() + data)
        proc.stdin.flush()

def reader():
    while True:
        hdr = {}
        while True:
            line = proc.stdout.readline()
            if not line:
                return
            if line in (b'\r\n', b'\n'):
                break
            key, value = line.decode().split(':', 1)
            hdr[key.lower()] = value.strip()
        obj = json.loads(proc.stdout.read(int(hdr['content-length'])))
        if obj.get('method') == 'textDocument/publishDiagnostics':
            log.write_text(json.dumps(obj['params'], ensure_ascii=False, indent=2))
            diagnostics = obj['params']['diagnostics']
            print(json.dumps({'version': obj['params'].get('version'),
                              'errors': sum(d.get('severity') == 1 for d in diagnostics), 'count':len(diagnostics)}, ensure_ascii=False), flush=True)
        elif obj.get('method') == '$/lean/fileProgress':
            (scratch / 'lsp_progress.json').write_text(json.dumps(obj['params']))

threading.Thread(target=reader, daemon=True).start()
send('initialize', {'processId':os.getpid(),'rootUri':root.as_uri(),
                    'capabilities':{'textDocument':{'publishDiagnostics':{'versionSupport':True}}}}, True)
send('initialized', {})
previous = None
version = 0
try:
    while proc.poll() is None:
        chunks = []
        for name in source_names:
            source = (root / (name if '/' in name else 'ChowlaCosine/P31/' + name)).read_text()
            if name != source_names[0]:
                source = '\n'.join(line for line in source.splitlines()
                                   if not line.startswith('import ')) + '\n'
            chunks.append('-- SOURCE ' + name + '\n' + source)
        extra = scratch / 'lsp_extra.lean'
        if extra.exists():
            chunks.append(extra.read_text())
        text = '\n'.join(chunks)
        if text != previous:
            work.write_text(text)
            version += 1
            uri = work.as_uri()
            if previous is None:
                send('textDocument/didOpen', {'textDocument':{
                    'uri':uri,'languageId':'lean4','version':version,'text':text}})
            else:
                send('textDocument/didChange', {'textDocument':{'uri':uri,'version':version},
                                              'contentChanges':[{'text':text}]})
            previous = text
            print('Submitted version ' + str(version), flush=True)
        time.sleep(1)
finally:
    proc.terminate()
    try:
        proc.wait(timeout=5)
    except subprocess.TimeoutExpired:
        proc.kill()
