import enum
from supabase import create_client
import os

from parlant.core.tools import ToolResult

supabase_url=os.environ["SUPABASE_URL"]
supabase_anon=os.environ["SUPABASE_ANON_KEY"]
supabase = create_client(supabase_url, supabase_anon)

def check_vegetable_price(vegetable: str) -> ToolResult:
    return ToolResult(f"1 kg of {vegetable} costs 3$")


class ProductCategory(enum.Enum):
    LAPTOPS = "laptops"
    PERIPHERALS = "peripherals"


def available_products_by_category(category: ProductCategory) -> ToolResult:
    products_by_category = {
        ProductCategory.LAPTOPS: ["Lenovo", "Dell"],
        ProductCategory.PERIPHERALS: ["Razer Keyboard", "Logitech Mouse"],
    }

    return ToolResult(products_by_category[category])


class Categories(enum.Enum):
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
    


# verify if product category is in stock
def get_in_stock(category: Categories) -> ToolResult:
    all_db = (
        supabase.table("products")
        .select("id, title, variant_inventory_qty")
        .eq("type", category.value)
        .execute()
    )

    in_stock_count = sum(1 for item in all_db.data if item["variant_inventory_qty"] > 2)
    return ToolResult(in_stock_count > 2)

# fetch products by tags
def get_products_by_tags(category: Categories, tags: str) -> ToolResult:
    tags_list = tags.split(",")
    unique_products = {}
    
    for tag in tags_list:
        item_db = (
            supabase.table("products")
            .select(
                "id, title, variant_inventory_qty, variant_price, tags, body_html"
            )
            .eq("type", category.value)
            .contains("tags", [tag])
            .execute()
        )
        if item_db and item_db.data:
            for product in item_db.data:
                unique_products[product["id"]] = product

    return ToolResult(list(unique_products.values()))
