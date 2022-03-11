from dataclasses import dataclass
from typing import Optional, List, Any
from enum import Enum, auto
import inspect


@dataclass
class Attachment:
    title: str
    snapshot: Optional[bool]
    mimeType: Optional[bool]
    url: Optional[str]
    proxy: Optional[bool]


@dataclass
class Note:
    title: Optional[str]
    note: str


class CreatorType(Enum):
    artist = auto()
    contributor = auto()
    performer = auto()
    composer = auto()
    words_by = auto()
    sponsor = auto()
    cosponsor = auto()
    author = auto()
    commenter = auto()
    editor = auto()
    translator = auto()
    series_editor = auto()
    book_author = auto()
    counsel = auto()
    programmer = auto()
    reviewed_author = auto()
    recipient = auto()
    director = auto()
    scriptwriter = auto()
    producer = auto()
    interviewee = auto()
    interviewer = auto()
    cartographer = auto()
    inventor = auto()
    attorney_agent = auto()
    podcaster = auto()
    guest = auto()
    presenter = auto()
    cast_member = auto()


@dataclass
class Creator:
    creator_type: str
    last_name: Optional[str] = None
    first_name: Optional[str] = None
    field_mode: Optional[str] = None
    name: Optional[str] = None


class ItemType(Enum):
    annotation = auto()
    artwork = auto()
    attachment = auto()
    audio_recording = auto()
    bill = auto()
    blog_post = auto()
    book = auto()
    book_section = auto()
    case = auto()
    computer_program = auto()
    conference_paper = auto()
    dictionary_entry = auto()
    document = auto()
    email = auto()
    encyclopedia_article = auto()
    film = auto()
    forum_post = auto()
    hearing = auto()
    instant_message = auto()
    interview = auto()
    journal_article = auto()
    letter = auto()
    magazine_article = auto()
    manuscript = auto()
    map = auto()
    newspaper_article = auto()
    note = auto()
    patent = auto()
    podcast = auto()
    presentation = auto()
    radio_broadcast = auto()
    report = auto()
    statute = auto()
    thesis = auto()
    tv_broadcast = auto()
    video_recording = auto()
    webpage = auto()


class ItemMeta(type):
    __itemtypes__ = dict()

    def __new__(cls, name, bases, dct):
        kls = super().__new__(cls, name, bases, dct)
        if item_type := dct.get("itemType"):
            cls.__itemtypes__[item_type] = kls
        return kls


@dataclass
class Item(metaclass=ItemMeta):
    key: str
    version: str

    @classmethod
    def init(cls, item_type: str):
        return cls.__itemtypes__[item_type]

    @classmethod
    def to_dict(cls):
        print(inspect.signature(cls).parameters)

    @classmethod
    def from_dict(cls, env):
        return cls(
            **{k: v for k, v in env.items() if k in inspect.signature(cls).parameters}
        )

    def __getattr__(self, name: str) -> Any:
        try:
            return super().__getattribute__(name)
        except AttributeError:
            return None

    creators: List[Creator] = []
    attachments: List[Attachment] = []
    notes: List[Note] = []
    seeAlso: List[str] = []


@dataclass
class ArtworkItem(Item):
    item_type: ItemType = ItemType.artwork
    title: Optional[str] = None
    abstract_note: Optional[str] = None
    artwork_medium: Optional[str] = None
    artwork_size: Optional[str] = None
    date: Optional[str] = None
    language: Optional[str] = None
    short_title: Optional[str] = None
    archive: Optional[str] = None
    archive_location: Optional[str] = None
    library_catalog: Optional[str] = None
    call_number: Optional[str] = None
    url: Optional[str] = None
    access_date: Optional[str] = None
    rights: Optional[str] = None
    extra: Optional[str] = None


@dataclass
class EncyclopediaArticleItem(Item):
    item_type: ItemType = ItemType.encyclopedia_article
    title: Optional[str] = None
    abstract_note: Optional[str] = None
    encyclopedia_title: Optional[str] = None
    series: Optional[str] = None
    series_number: Optional[str] = None
    volume: Optional[str] = None
    number_of_volumes: Optional[str] = None
    edition: Optional[str] = None
    place: Optional[str] = None
    publisher: Optional[str] = None
    date: Optional[str] = None
    pages: Optional[str] = None
    ISBN: Optional[str] = None
    short_title: Optional[str] = None
    url: Optional[str] = None
    access_date: Optional[str] = None
    language: Optional[str] = None
    archive: Optional[str] = None
    archive_location: Optional[str] = None
    library_catalog: Optional[str] = None
    call_number: Optional[str] = None
    rights: Optional[str] = None
    extra: Optional[str] = None


@dataclass
class JournalArticleItem(Item):
    item_type: ItemType = ItemType.journal_article
    title: Optional[str] = None
    abstract_note: Optional[str] = None
    publication_title: Optional[str] = None
    volume: Optional[str] = None
    issue: Optional[str] = None
    pages: Optional[str] = None
    date: Optional[str] = None
    series: Optional[str] = None
    series_title: Optional[str] = None
    series_text: Optional[str] = None
    journal_abbreviation: Optional[str] = None
    language: Optional[str] = None
    DOI: Optional[str] = None
    ISSN: Optional[str] = None
    short_title: Optional[str] = None
    url: Optional[str] = None
    access_date: Optional[str] = None
    archive: Optional[str] = None
    archive_location: Optional[str] = None
    library_catalog: Optional[str] = None
    call_number: Optional[str] = None
    rights: Optional[str] = None
    extra: Optional[str] = None


@dataclass
class MagazineArticleItem(Item):
    item_type: ItemType = ItemType.magazine_article
    title: Optional[str] = None
    abstract_note: Optional[str] = None
    publication_title: Optional[str] = None
    volume: Optional[str] = None
    issue: Optional[str] = None
    date: Optional[str] = None
    pages: Optional[str] = None
    language: Optional[str] = None
    ISSN: Optional[str] = None
    short_title: Optional[str] = None
    url: Optional[str] = None
    access_date: Optional[str] = None
    archive: Optional[str] = None
    archive_location: Optional[str] = None
    library_catalog: Optional[str] = None
    call_number: Optional[str] = None
    rights: Optional[str] = None
    extra: Optional[str] = None


@dataclass
class NewspaperArticleItem(Item):
    item_type: ItemType = ItemType.newspaper_article
    title: Optional[str] = None
    abstract_note: Optional[str] = None
    publication_title: Optional[str] = None
    place: Optional[str] = None
    edition: Optional[str] = None
    date: Optional[str] = None
    section: Optional[str] = None
    pages: Optional[str] = None
    language: Optional[str] = None
    short_title: Optional[str] = None
    ISSN: Optional[str] = None
    url: Optional[str] = None
    access_date: Optional[str] = None
    archive: Optional[str] = None
    archive_location: Optional[str] = None
    library_catalog: Optional[str] = None
    call_number: Optional[str] = None
    rights: Optional[str] = None
    extra: Optional[str] = None


@dataclass
class BookSectionItem(Item):
    item_type: ItemType = ItemType.book_section
    title: Optional[str] = None
    abstract_note: Optional[str] = None
    book_title: Optional[str] = None
    series: Optional[str] = None
    series_number: Optional[str] = None
    volume: Optional[str] = None
    number_of_volumes: Optional[str] = None
    edition: Optional[str] = None
    place: Optional[str] = None
    publisher: Optional[str] = None
    date: Optional[str] = None
    pages: Optional[str] = None
    language: Optional[str] = None
    ISBN: Optional[str] = None
    short_title: Optional[str] = None
    url: Optional[str] = None
    access_date: Optional[str] = None
    archive: Optional[str] = None
    archive_location: Optional[str] = None
    library_catalog: Optional[str] = None
    call_number: Optional[str] = None
    rights: Optional[str] = None
    extra: Optional[str] = None


@dataclass
class BookItem(Item):
    item_type: ItemType = ItemType.book
    title: Optional[str] = None
    abstract_note: Optional[str] = None
    series: Optional[str] = None
    series_number: Optional[str] = None
    volume: Optional[str] = None
    number_of_volumes: Optional[str] = None
    edition: Optional[str] = None
    place: Optional[str] = None
    publisher: Optional[str] = None
    date: Optional[str] = None
    num_pages: Optional[str] = None
    language: Optional[str] = None
    ISBN: Optional[str] = None
    short_title: Optional[str] = None
    url: Optional[str] = None
    access_date: Optional[str] = None
    archive: Optional[str] = None
    archive_location: Optional[str] = None
    library_catalog: Optional[str] = None
    call_number: Optional[str] = None
    rights: Optional[str] = None
    extra: Optional[str] = None
