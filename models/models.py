from dataclasses import dataclass
from enum import Enum


@dataclass
class Event:
    Event: str


class Status(Enum):
    Unknown = "Unknown"
    Registered = "Registered"
    Unregistered = "Unregistered"
    Rejected = "Rejected"
    Lagged = "Lagged"


@dataclass
class PeerStatus(Event):
    Event: str
    ChannelType: str
    Peer: str
    PeerStatus: Status
    Cause: str
    Address: str
    Port: int
    Time: str
