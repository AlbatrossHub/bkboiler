# BKB Customization

## Overview
This Odoo 18 addon extends the product.template model to support boiler manufacturing specifications. It adds custom fields for detailed product specifications that are commonly used in boiler manufacturing companies.

## Features

### Custom Fields Added to Product Template
The following fields are added to the product.template model:

- **SPECIFICATION**: Product specification details
- **MODEL NO.**: Model number of the product
- **SIZE**: Size specifications
- **SCH.**: Schedule information
- **CLASS**: Product class information
- **LONG**: Length specifications
- **RANGE**: Product range information
- **REF. NO.**: Reference number
- **MAKE**: Manufacturer information
- **PRESS.**: Pressure specifications
- **TEMP.**: Temperature specifications
- **HEAD**: Head specifications
- **FLOW**: Flow specifications
- **HP**: Horsepower specifications
- **KW**: Kilowatt specifications
- **RPM**: Revolutions per minute specifications

### User Interface Enhancements

1. **Form View**: A new "BKB Specs" section is added to the product form view in the General Information tab
2. **Tree View**: All BKB specification fields are available in the product tree view with optional show enabled by default

### Automatic Description Generation

The module automatically populates the `description_purchase` and `description_sale` fields based on the BKB specification fields. When you create or update a product with BKB specifications, the descriptions will be automatically generated in the following format:

```
MODEL NO.: A1B2C3
SIZE: 21mm
MAKE: bosch
PRESS.: 200
```

Only fields with values are included in the description, and each specification appears on a new line.

## Installation

1. Copy the `bk_customization` folder to your Odoo addons directory
2. Update the addon list in Odoo
3. Install the "BKB Customization" module

## Usage

1. Navigate to **Inventory > Products > Products**
2. Create or edit a product
3. In the product form, you'll see a new "BKB Specs" section in the General Information tab
4. Fill in the relevant boiler specification fields
5. Save the product
6. The `description_purchase` and `description_sale` fields will be automatically populated based on the BKB specifications you entered

### Example

If you enter:
- MODEL NO.: A1B2C3
- SIZE: 21mm
- MAKE: bosch
- PRESS.: 200

The description fields will automatically contain:
```
MODEL NO.: A1B2C3
SIZE: 21mm
MAKE: bosch
PRESS.: 200
```

## Technical Details

- **Dependencies**: product module
- **Odoo Version**: 18.0
- **License**: LGPL-3

## Files Structure

```
bk_customization/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   └── product_template.py
├── security/
│   └── ir.model.access.csv
├── views/
│   └── product_template_views.xml
└── README.md
```

## Support

For support and customization requests, please contact the development team.
