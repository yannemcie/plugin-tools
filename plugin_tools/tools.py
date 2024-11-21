[
  {
    "get_in_stock": {
      "name": "get_in_stock",
      "description": "Verifies if the product is in stock",
      "module_path": "tests.tool_utilities",
      "parameters": {
        "category": {
          "type": "string",
          "enum": ["Graphics Card","Processor","Storage","Power Supply","Motherboard","Memory","Case","CPU Cooler","Monitor","Keyboard","Mouse","Headset","Audio","Cooling","Accessories","Lighting","Networking","Laptop"],
          "description": "Product categories"
        }
      },
      "required": ["category"]
    },
    "get_products_by_tags": {
      "name": "get_products_by_tags",
      "description": "Gets products by tags given",
      "module_path": "tests.tool_utilities",
      "parameters": {
        "category": {
          "type": "string",
          "enum": ["Graphics Card","Processor","Storage","Power Supply","Motherboard","Memory","Case","CPU Cooler","Monitor","Keyboard","Mouse","Headset","Audio","Cooling","Accessories","Lighting","Networking","Laptop"],
          "description": "Product categories"
        },
        "tags": {
          "type": "string",
          "description": "Product tags"
        }
      },
      "required": ["category", "tags"]
    }
  }
]
