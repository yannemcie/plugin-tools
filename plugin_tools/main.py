import asyncio
from parlant.core.services.tools.plugins import PluginServer, tool
from parlant.core.tools import ToolContext, ToolResult
from supabase import create_client
from dotenv import load_dotenv
import os
from plugin_tools.store import Categories, Tags, TAG_VALUES
# from store import Categories, Tags, TAG_VALUES

load_dotenv()
supabase_url = os.environ["SUPABASE_URL"]
supabase_anon = os.environ["SUPABASE_ANON_KEY"]
supabase = create_client(supabase_url, supabase_anon)


async def main():
    # fetch all the products from the db
    @tool(id="get_products_all")
    async def get_products_all(context: ToolContext) -> ToolResult:
        all_db = supabase.table("products").select("*").execute()
        return ToolResult(all_db.data)

    # verify if product category is in stock
    @tool(id="get_in_stock")
    async def get_in_stock(context: ToolContext, category: Categories) -> ToolResult:
        """Verifies if product type is in stock"""
        all_db = (
            supabase.table("products")
            .select("id, title, variant_inventory_qty")
            .eq("type", category.value)
            .execute()
        )

        in_stock_count = sum(
            1 for item in all_db.data if item["variant_inventory_qty"] > 2
        )
        return ToolResult(in_stock_count > 2)
    
    @tool(id="get_product_tags")
    async def get_product_tags(context: ToolContext, category: Categories, tags:Tags)-> ToolResult:
        """Get relevant tags of the product"""
        return ToolResult(TAG_VALUES[tags])
    
    # fetch products by tags
    @tool(id="get_products_by_tags")
    async def get_products_by_tags(
        context: ToolContext, category: Categories, tags: str
    ) -> ToolResult:
        """Gets list a products by tags"""
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
    

    async with PluginServer(
        tools=[get_products_all, get_in_stock, get_product_tags, get_products_by_tags]
    ):
        pass


asyncio.run(main())
