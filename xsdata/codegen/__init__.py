from urllib.request import build_opener

from xsdata import __version__

opener = build_opener()
opener.addheaders = [("User-agent", f"xsdata/{__version__}")]
