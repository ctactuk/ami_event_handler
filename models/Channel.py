from enum import Enum
import Event


class ChannelStateDesc(Enum):
    Down = "Down"
    Rsrvd = "Rsrvd"
    OffHook = "OffHook"
    Dialing = "Dialing"
    Ring = "Ring"
    Ringing = "Ringing"
    Up = "Up"
    Busy = "Busy"
    DialingOffhook = "DialingOffhook"
    PreRing = "PreRing"
    Unknown = "Unknown"


class Channel(Event):
    ChannelState: str
    ChannelStateDesc: ChannelStateDesc
    CallerIDNum: str
    CallerIDName: str
    ConnectedLineNum: str
    ConnectedLineName: str
    Language: str
    AccountCode: str
    Context: str
    Exten: str
    Priority: str
    Linkedid: str
