from sqlalchemy import Column, Integer, String, Float, ForeignKey, LargeBinary
from sqlalchemy.orm import relationship
from MusicApp.settings import Base, engine


class Album(Base):
    __tablename__ = "albums"

    id = Column(
        Integer,
        primary_key=True,
    )

    album_name = Column(
        String(30),
        nullable=False,
        unique=True,
    )

    image_url = Column(
        String(250),
        nullable=False,
    )

    price = Column(
        Float,
        nullable=False,
    )

    songs = relationship(
        "Song",
        back_populates="album",
        cascade="all, delete-orphan",
    )


class Song(Base):
    __tablename__ = "songs"

    id = Column(
        Integer,
        primary_key=True,
    )

    song_name = Column(
        String(100),
        nullable=False,
    )

    music_file_data = Column(
        LargeBinary,
    )

    album_id = Column(
        Integer,
        ForeignKey("albums.id"),
        nullable=False,
    )

    album = relationship(
        "Album",
        back_populates="songs"
    )
