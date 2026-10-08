import re, html, hashlib, json, os
ATTRS=('alt','aria-label','placeholder','title','content')
def norm(t): return re.sub(r'\s+',' ',html.unescape(t)).strip()
def key(t): return hashlib.md5(norm(t).encode()).hexdigest()[:6]
def iter_texts(src):
    out=[]
    for m in re.finditer(r'>([^<>]+)<',src):
        t=norm(m.group(1))
        if re.search(r'[A-Za-zÀ-ú]',t): out.append(t)
    for a in ATTRS:
        for m in re.finditer(r'\b%s="([^"]*)"'%a,src):
            t=norm(m.group(1))
            if re.search(r'[A-Za-zÀ-ú]{2}',t) and not t.startswith(('http','/','#')) and a!='content': out.append(t)
    return out
def translate(src,en,missing=None):
    pres=[]
    def stash(m):
        pres.append(m.group(0)); return '@@%d@@'%(len(pres)-1)
    src=re.sub(r'<pre.*?</pre>',stash,src,flags=re.S)
    def cm(m):
        t=norm(m.group(2)); k=key(t)
        if k in en: return m.group(1)+html.escape(en[k],quote=False)+m.group(3)
        if missing is not None and re.search(r'[A-Za-zÀ-ú]{2}',t): missing.add((k,t))
        return m.group(0)
    pres=[re.sub(r'(<span class="cm">)([^<]*)(</span>)',cm,b) for b in pres]
    def rep_text(m):
        raw=m.group(1); t=norm(raw)
        if not re.search(r'[A-Za-zÀ-ú]',t): return re.sub(r'(\d),(\d)',r'\1.\2',m.group(0))
        k=key(t)
        if k not in en:
            if missing is not None: missing.add((k,t))
            return m.group(0)
        lead=re.match(r'\s*',raw).group(0); trail=re.search(r'\s*$',raw).group(0)
        return '>'+lead+html.escape(en[k],quote=False)+trail+'<'
    src=re.sub(r'>([^<>]+)<',rep_text,src)
    def rep_attr(a):
        def f(m):
            t=norm(m.group(1)); k=key(t)
            if k in en: return '%s="%s"'%(a,html.escape(en[k],quote=True))
            if re.search(r'[A-Za-zÀ-ú]{2}',t) and missing is not None and not t.startswith(('http','/','#')): missing.add((k,t))
            return m.group(0)
        return f
    for a in ATTRS:
        if a=='content': continue
        src=re.sub(r'\b%s="([^"]*)"'%a,rep_attr(a),src)
    for i,b in enumerate(pres): src=src.replace('@@%d@@'%i,b)
    return src
