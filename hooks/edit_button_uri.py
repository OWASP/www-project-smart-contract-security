import logging

log = logging.getLogger('mkdocs')

def get_edit_url(src_path, edit_url_SCSTG, edit_url_SCSVS):
    if src_path.startswith("SCSVS"):
        edit_url = f"{edit_url_SCSVS}{src_path}"
        edit_url = edit_url.replace("master/SCSVS/controls", "master/controls/")
        edit_url = edit_url.replace("master/SCSVS/", "master/Document/")
    elif src_path.startswith("SCSTG"):
        edit_url = f"{edit_url_SCSTG}{src_path}"
        edit_url = edit_url.replace("master/SCSTG/0x", "master/Document/0x")
        edit_url = edit_url.replace("master/SCSTG/", "master/")
    elif src_path.startswith("scwe"):
        edit_url = f"{edit_url_SCSTG}{src_path}"
        edit_url = edit_url.replace("master/scwe/", "master/weaknesses/")
    elif src_path.startswith(("contributing", "donate")):
        edit_url = f"{edit_url_SCSTG}{src_path}"
        edit_url = edit_url.replace("master/", "master/docs/")
    else:
        edit_url = ""
    
    return edit_url

def on_pre_page(page, config, files):
    try:
        edit_url_SCSTG = "https://github.com/OWASP/owasp-scstg/edit/master/"
        edit_url_SCSVS = "https://github.com/OWASP/owasp-scsvs/edit/master/"
    except KeyError:
        return page
    
    src_path = page.file.src_path

    if src_path.startswith(("SCSTG", "SCSVS", "scwe", "contributing", "donate")):
        edit_url = get_edit_url(src_path, edit_url_SCSTG, edit_url_SCSVS)
        if edit_url.endswith("/index.md"):
            page.edit_url = ""
        else:
            page.edit_url = edit_url
    else:
        page.edit_url = ""
 
    return page