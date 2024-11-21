import asyncio
from parlant.core.services.tools.plugins import PluginServer, tool
from parlant.core.tools import ToolContext, ToolResult
from supabase import create_client
from dotenv import load_dotenv
import os
from enum import Enum

load_dotenv()
supabase_url = os.environ["SUPABASE_URL"]
supabase_anon = os.environ["SUPABASE_ANON_KEY"]
supabase = create_client(supabase_url, supabase_anon)


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


# class Tags(Enum):


async def main():
    # fetch all the products from the db
    @tool(id="get_products_all")
    async def get_products_all(context: ToolContext) -> ToolResult:
        all_db = supabase.table("products").select("tags").execute()
        return ToolResult(all_db.data)

    # verify if product category is in stock
    @tool(id="get_in_stock")
    async def get_in_stock(context: ToolContext, category: Categories) -> ToolResult:
        in_stock = []
        all_db = (
            supabase.table("products")
            .select("id, title, variant_inventory_qty")
            .eq("type", category.value)
            .execute()
        )

        for item in all_db.data:
            if item["variant_inventory_qty"] > 2:
                in_stock.append(item["variant_inventory_qty"])

        return ToolResult(len(in_stock) > 2)

    # fetch products by tags
    @tool(id="get_products_by_tags")
    async def get_products_by_tags(
        context: ToolContext, category: Categories, tags: str
    ) -> ToolResult:
        tags_list = tags.split(",")
        products = []  # This will store unique products
        unique_ids = set()  # To track added product IDs

        for item in tags_list:
            item_db = (
                supabase.table("products")
                .select(
                    "id, title, variant_inventory_qty, variant_price, tags, body_html"
                )
                .eq("type", category.value)
                .contains("tags", [item])
                .execute()
            )
            if item_db and item_db.data:
                for product in item_db.data:
                    if product["id"] not in unique_ids:
                        unique_ids.add(product["id"])
                        products.append(product)

        return ToolResult(products)

    async with PluginServer(
        tools=[get_products_all, get_in_stock, get_products_by_tags]
    ):
        pass


asyncio.run(main())
