from dataclasses import dataclass, asdict
from typing import Dict, Optional

from constants import DEFAULT_SETTINGS
from utils import parse_str


@dataclass
class Carbon:
    """Class that constructs the URL for the Carbon.now.sh

    Attributes:
        bg: Background.
        t: Theme.
        wt: Windows theme.
        l: Language.
        width: Width.
        ds: Drop shadow.
        dsyoff: Drop shadow offset.
        dsblur: Drop shadow blur.
        wc: Window controls.
        wa: Window adjustment.
        pv: Padding vertical.
        ph: Padding horizontal.
        ln: Line numbers.
        fl: First line number.
        fm: Font family.
        fs: Font size.
        lh: Line height.
        si: Square image.
        es: Export size.
        wm: Watermark.
    """

    bg: Optional[str] = None
    t: Optional[str] = None
    wt: Optional[str] = None
    l: Optional[str] = None
    width: Optional[str] = None
    ds: Optional[str] = None
    dsyoff: Optional[str] = None
    dsblur: Optional[str] = None
    wc: Optional[str] = None
    wa: Optional[str] = None
    pv: Optional[str] = None
    ph: Optional[str] = None
    ln: Optional[str] = None
    fl: Optional[str] = None
    fm: Optional[str] = None
    fs: Optional[str] = None
    lh: Optional[str] = None
    si: Optional[str] = None
    es: Optional[str] = None
    wm: Optional[str] = None

    def __post_init__(self) -> None:
        for key, value in DEFAULT_SETTINGS.items():
            if not getattr(self, key):
                if key == "bg":
                    value = parse_str(value)
                setattr(self, key, value)

    def build_query(self) -> str:
        query = ""
        for key, value in self.parameters().items():
            if key == "bg":
                value = parse_str(value)
            query += f"{key}={value}&"
        return query[:-1]

    def parameters(self) -> Dict[str, str]:
        return asdict(self)
