import pandas as pd

# Define all mappings
mappings = {
    "Customer Mapping": [
        ["KNA1", "Customer ID", "customers", "customer_id", "Direct mapping (P Key)"],
        ["KNA1", "Customer Name", "customers", "customer_name", "Direct mapping"],
        ["KNA1", "Country", "customers", "country", "Direct mapping"],
        ["KNA1", "Region", "customers", "region", "Direct mapping"],
        ["KNA1", "City", "customers", "city", "Direct mapping"],
        ["KNA1", "Postal Code", "customers", "postal_code", "Direct mapping"],
        ["KNA1", "Street Address", "customers", "street_address", "Direct mapping"],
        ["KNA1", "Phone Number", "customers", "phone_number", "Direct mapping"],
        ["KNA1", "Email Address", "customers", "email_address", "Direct mapping"],
        ["KNA1", "Language", "customers", "language", "Direct mapping"],
        ["KNA1", "Tax Number", "customers", "tax_number", "Direct mapping"],
        ["KNA1", "Customer Group", "customers", "customer_group", "Direct mapping"],
        ["KNA1", "Sales Organization", "customers", "sales_organization", "Direct mapping"],
        ["KNA1", "Distribution Channel", "customers", "distribution_channel", "Direct mapping"],
        ["KNA1", "Division", "customers", "division", "Direct mapping"],
        ["KNA1", "Street Address + Postal Code + City", "customers", "full_address", "Concatenation"]
    ],
    "Vendor/Carrier Mapping": [
        ["LFA1", "vendor_number", "carriers", "vendor_number", "Direct mapping (P Key)"],
        ["LFA1", "vendor_name", "carriers", "vendor_name", "Direct mapping"],
        ["LFA1", "country", "carriers", "country", "Direct mapping"],
        ["LFA1", "region", "carriers", "region", "Direct mapping"],
        ["LFA1", "city", "carriers", "city", "Direct mapping"],
        ["LFA1", "postal_code", "carriers", "postal_code", "Direct mapping"],
        ["LFA1", "street_address", "carriers", "street_address", "Direct mapping"],
        ["LFA1", "phone_number", "carriers", "phone_number", "Direct mapping"],
        ["LFA1", "email_address", "carriers", "email_address", "Direct mapping"],
        ["LFA1", "language", "carriers", "language", "Direct mapping"],
        ["LFA1", "tax_number", "carriers", "tax_number", "Direct mapping"],
        ["LFA1", "payment_terms", "carriers", "payment_terms", "Direct mapping"],
        ["LFA1", "street_address + postal_code + city", "carriers", "full_address", "Concatenation"]
    ],
    "Orders Mapping": [
        ["VBAK", "sales_document", "orders", "sales_document", "Direct mapping (P Key)"],
        ["VBAK", "order_date", "orders", "order_date", "Direct mapping"],
        ["VBAK", "customer_id", "orders", "customer_id", "Direct mapping (F Key from Customers)"],
        ["VBAK", "order_type", "orders", "order_type", "Direct mapping"],
        ["VBAK", "sales_organization", "orders", "sales_organization", "Direct mapping"],
        ["VBAK", "distribution_channel", "orders", "distribution_channel", "Direct mapping"],
        ["VBAK", "division", "orders", "division", "Direct mapping"],
        ["VBAK", "order_status", "orders", "order_status", "Direct mapping"],
        ["VBAK", "customer_name", "orders", "customer_name", "Lookup from KNA1 table"],
        ["VBAK", "full_address", "orders", "full_address", "Lookup from KNA1 table"]
    ],
    "Order Items Mapping": [
        ["VBAP", "sales_document", "order_items", "sales_document", "Direct mapping (F Key from orders)"],
        ["VBAP", "item_number", "order_items", "item_number", "Direct mapping"],
        ["VBAP", "material_number", "order_items", "material_number", "Direct mapping"],
        ["VBAP", "quantity", "order_items", "quantity", "Direct mapping"],
        ["VBAP", "net_price", "order_items", "net_price", "Direct mapping"],
        ["VBAP", "item_status", "order_items", "item_status", "Direct mapping"],
        ["VBAP", "delivery_date", "order_items", "delivery_date", "Direct mapping"],
        ["VBAP", "total_price", "order_items", "total_price", "quantity * net_price"]
    ],
    "Deliveries Mapping": [
        ["LIKP", "Delivery Number", "Deliveries", "delivery_number", "Direct Mapping (P Key)"],
        ["LIKP", "Delivery Date", "Deliveries", "delivery_date", "Convert SAP Date Format (YYYYMMDD) to E-com Date Format (YYYY-MM-DD)"],
        ["LIKP", "Sales Document", "Deliveries", "sales_document", "Direct Mapping"],
        ["LIKP", "Shipping Point", "Deliveries", "shipping_point", "Direct Mapping"],
        ["LIKP", "Shipping Type", "Deliveries", "shipping_type", "Direct Mapping"],
        ["LIKP", "Delivery Status", "Deliveries", "delivery_status", "Direct Mapping"],
        ["LIKP", "Shipping Status", "Deliveries", "shipping_status", "Direct Mapping"],
        ["LIKP", "Route", "Deliveries", "route", "Direct Mapping"],
        ["LIKP", "Delivery Priority", "Deliveries", "delivery_priority", "Direct Mapping"],
        ["LIKP", "Customer ID", "Deliveries", "customer_id", "Direct Mapping (F Key from customers)"]
    ],
    "Delivery Items Mapping": [
        ["LIPS", "Delivery Number", "Delivery_Items", "delivery_number", "Direct Mapping (F Key from deliveries)"],
        ["LIPS", "Item Number", "Delivery_Items", "item_number", "Direct Mapping"],
        ["LIPS", "Material Number", "Delivery_Items", "material_number", "Direct Mapping"],
        ["LIPS", "Delivered Quantity", "Delivery_Items", "delivered_quantity", "Direct Mapping"],
        ["LIPS", "Net Price", "Delivery_Items", "net_price", "Direct Mapping"],
        ["LIPS", "Delivery Status", "Delivery_Items", "delivery_status", "Direct Mapping"],
        ["LIPS", "Customer ID", "Delivery_Items", "customer_id", "Direct Mapping"],
        ["LIPS", "Sales Document", "Delivery_Items", "sales_document", "Direct Mapping"],
        ["LIPS", "Sales Item", "Delivery_Items", "sales_item", "Direct Mapping"],
        ["LIPS", "Delivery Date", "Delivery_Items", "delivery_date", "Convert SAP Date Format (YYYYMMDD) to E-com Date Format (YYYY-MM-DD)"],
        ["LIPS", "Total Price (Calculated)", "Delivery_Items", "total_price", "delivered_quantity * net_price"]
    ],
    "Shipments Mapping": [
        ["VTTK", "Shipment Number", "Shipments", "shipment_number", "Direct Mapping (P Key)"],
        ["VTTK", "Shipment Date", "Shipments", "shipment_date", "Convert SAP Date Format (YYYYMMDD) to E-com Date Format (YYYY-MM-DD)"],
        ["VTTK", "Sales Document", "Shipments", "sales_document", "Direct Mapping"],
        ["VTTK", "Delivery Number", "Shipments", "delivery_number", "Direct Mapping"],
        ["VTTK", "Shipping Point", "Shipments", "shipping_point", "Direct Mapping"],
        ["VTTK", "Carrier", "Shipments", "carrier", "Direct Mapping"],
        ["VTTK", "Shipment Status", "Shipments", "shipment_status", "Direct Mapping"],
        ["VTTK", "Route", "Shipments", "route", "Direct Mapping"],
        ["VTTK", "Shipping Type", "Shipments", "shipping_type", "Direct Mapping"],
        ["VTTK", "Customer ID", "Shipments", "customer_id", "Direct Mapping"],
        ["VTTK", "Total Shipped Quantity (Calculated)", "Shipments", "total_shipped_quantity", "Aggregated sum of shipped_quantity from VTTP table"]
    ],
    "Shipment Items Mapping": [
        ["VTTP", "Shipment Number", "Shipment_Items", "shipment_number", "Direct Mapping (F Key from shipments)"],
        ["VTTP", "Item Number", "Shipment_Items", "item_number", "Direct Mapping"],
        ["VTTP", "Material Number", "Shipment_Items", "material_number", "Direct Mapping"],
        ["VTTP", "Shipped Quantity", "Shipment_Items", "shipped_quantity", "Direct Mapping"],
        ["VTTP", "Item Status", "Shipment_Items", "item_status", "Direct Mapping"],
        ["VTTP", "Delivery Number", "Shipment_Items", "delivery_number", "Direct Mapping"],
        ["VTTP", "Customer ID", "Shipment_Items", "customer_id", "Direct Mapping"],
        ["VTTP", "Sales Document", "Shipment_Items", "sales_document", "Direct Mapping"],
        ["VTTP", "Sales Item", "Shipment_Items", "sales_item", "Direct Mapping"],
        ["VTTP", "Shipment Date", "Shipment_Items", "shipment_date", "Convert SAP Date Format (YYYYMMDD) to E-com Date Format (YYYY-MM-DD)"],
        ["VTTP", "Transformation Timestamp", "Shipment_Items", "transformation_timestamp", "Capture Load Timestamp"],
        ["VTTP", "Total Shipped Per Material (Calculated)", "Shipment_Items", "total_shipped_per_material", "Aggregated sum of shipped_quantity per material_number"]
    ]
}

# Create an Excel writer
with pd.ExcelWriter("SAP_to_Ecom_Mapping.xlsx", engine="openpyxl") as writer:
    for sheet_name, data in mappings.items():
        # Replace invalid characters in sheet names
        valid_sheet_name = sheet_name.replace("/", "_")
        df = pd.DataFrame(data, columns=["Source Table (SAP)", "Source Column", "Target Table (E-com)", "Target Column", "Transformation"])
        df.to_excel(writer, sheet_name=valid_sheet_name, index=False)

print("Excel file 'SAP_to_Ecom_Mapping.xlsx' created successfully!")