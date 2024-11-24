from enum import Enum

class Categories(Enum):
    GRAPHICSCARD = "Graphics Card"
    PROCESSOR = "Processor"
    STORAGE = "Storage"
    POWER_SUPPLY = "Power Supply"
    MOTHERBOARD = "Motherboard"
    MEMORY = "Memory"
    CASE = "Case"
    CPUCOOLER = "CPU Cooler"
    MONITOR = "Monitor"
    KEYBOARD = "Keyboard"
    MOUSE = "Mouse"
    HEADSET = "Headset"
    AUDIO = "Audio"
    COOLING = "Cooling"
    ACCESSORIES = "Accessories"
    LIGHTING = "Lighting"
    NETWORKING = "Networking"
    LAPTOP = "Laptop"

class Tags(Enum):
    GENERAL = "general"
    GAMING = "gaming"
    DISPLAYS = "displays"
    GRAPHICS = "graphics"
    COOLING = "cooling"
    STORAGE = "storage"
    CONNECTIVITY = "connectivity"
    POWER = "power"
    PERIPHERALS = "peripherals"
    LAPTOPS = "laptops"
    DESKS_AND_MOUNTS = "desks and mounts"
    CONTENT_CREATION = "content creation"
    MISC = "miscellaneous"


TAG_VALUES = {
    Tags.GENERAL: [
        "storage", "portable", "external", "productivity", 
        "office", "business", "professional", "mainstream", 
        "creative", "studio"
    ],
    Tags.GAMING: [
        "gaming", "mechanical", "premium", "budget", "rgb", 
        "lightweight", "tenkeyless", "compact", "ergonomic", 
        "control", "customization"
    ],
    Tags.DISPLAYS: [
        "monitor", "curved", "4k", "144hz", "hdmi2.1", 
        "ips", "eye-care", "quantum-dot", "calibration"
    ],
    Tags.GRAPHICS: [
        "nvidia", "amd", "intel", "high-end", "high-performance", 
        "rtx4090", "rtx4080", "rtx4070", "rtx4060ti", "rtx4060", 
        "rtx4050", "rtx3050", "rtx3050ti", "rx6600", "z690", 
        "ddr5", "ddr4"
    ],
    Tags.COOLING: [
        "cooling", "aio", "liquid-cooler", "case", "atx", "fans"
    ],
    Tags.STORAGE: [
        "ssd", "nvme", "hdd", "sata"
    ],
    Tags.CONNECTIVITY: [
        "wifi", "usb", "usb-c", "hdmi", "connectivity", 
        "hub", "dock"
    ],
    Tags.POWER: [
        "psu", "modular", "gold-rated", "power", 
        "protection", "surge"
    ],
    Tags.PERIPHERALS: [
        "mousepad", "desk-pad", "keyboard", "speakers", 
        "microphone", "audio", "dac", "lighting"
    ],
    Tags.LAPTOPS: [
        "laptop", "ultrabook", "convertible", "macbook", "m3"
    ],
    Tags.DESKS_AND_MOUNTS: [
        "desk", "mount"
    ],
    Tags.CONTENT_CREATION: [
        "streaming", "capture", "content-creation", "interface"
    ],
    Tags.MISC: [
        "bluetooth", "comfort", "modding"
    ]
}