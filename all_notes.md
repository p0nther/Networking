 ==============================================================================
#                 [ The Packet from the Perspective of Scapy and Python ]
  ==============================================================================

packet_structure = {

    ###[ Ethernet Layer - Layer 2 ]###
    "Ethernet": {
        "dst": "🎯 The MAC address of the device currently receiving the packet on the local network.",
        "src": "📍 The MAC address of the device currently sending the packet on the local network.",
        "type": "🌐 Tells the network card that the data inside this frame belongs to the IPv4 protocol."
    },

    ###[ IP Layer - Layer 3 ]###
    "IP": {
        "version": "🔢 The version of the Internet Protocol being used (IPv4 in this case).",
        "len": "📏 The total size of the entire IP packet (Headers + Data) in bytes.",
        "ttl": "⏳ A counter that limits how many routers the packet can pass through before it is discarded, preventing infinite loops.",
        "proto": "⚙️ Tells the IP layer that the protocol carrying the payload is TCP.",
        "chksum": "🧮 A checksum value used to verify that the IP header information has not been corrupted or modified.",
        "src": "📮 The original and final IP address of the device that initiated the connection (source).",
        "dst": "🏁 The original and final IP address of the target device (final destination)."
    },

    ###[ TCP Layer - Layer 4 ]###
    "TCP": {
        "sport": "🚪 The random source port opened by the client application to send data from.",
        "dport": "🎯 The destination port on the server (for example, challenge port 31337).",
        "seq": "🔢 The sequence number used so the server can track byte order and reassemble data correctly.",
        "ack": "🔄 The acknowledgment number that tells the other side: I successfully received your data.",
        "chksum": "🛡️ A strong checksum that ensures the TCP header and actual payload arrived without corruption.",
        "options": "🛠️ Optional TCP settings used to manage the connection (such as Maximum Segment Size)."
    },

    ###[ Raw Layer - Data Layer ]###
    "Raw": {
        "load": "💬 The actual data and message (Payload) exchanged between applications (for example, the word 'echo')."
    }
}
